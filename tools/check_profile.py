#!/usr/bin/env python3
"""Validate the GitHub profile README without third-party Python dependencies."""

from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
REQUIRED_LINK_FRAGMENTS = (
    "github.com/Lay007/zynq-sdr-course",
    "github.com/Lay007/zynq-lora-phy-positioning",
    "github.com/Lay007/cpp-dsp-showcase",
    "lay007.github.io",
    "linkedin.com/in/alexander-lyubko-dsp",
)
SKIP_EXTERNAL_HOSTS = {
    "linkedin.com",
    "www.linkedin.com",
    "ru.linkedin.com",
}


def extract_targets(markdown: str) -> list[str]:
    targets: list[str] = []
    for raw in LINK_RE.findall(markdown):
        target = raw.strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1].strip()
        if target:
            targets.append(target)
    return targets


def local_path_from_target(target: str) -> Path | None:
    if target.startswith(("#", "mailto:", "http://", "https://")):
        return None

    parsed = urllib.parse.urlsplit(target)
    path = urllib.parse.unquote(parsed.path)
    if not path:
        return None

    return (README.parent / path).resolve()


def check_static(markdown: str, targets: list[str]) -> list[str]:
    errors: list[str] = []

    if not markdown.startswith("# "):
        errors.append("README.md must start with a level-1 heading")

    if not targets:
        errors.append("README.md contains no Markdown links")

    for fragment in REQUIRED_LINK_FRAGMENTS:
        if not any(fragment in target for target in targets):
            errors.append(f"required profile link is missing: {fragment}")

    for target in targets:
        local = local_path_from_target(target)
        if local is None:
            continue

        try:
            local.relative_to(ROOT)
        except ValueError:
            errors.append(f"local link escapes repository root: {target}")
            continue

        if not local.exists():
            errors.append(f"broken local link: {target}")

    return errors


def request_url(url: str, timeout: float = 12.0) -> tuple[str, str | None]:
    headers = {
        "User-Agent": "Lay007-profile-check/1.0 (+https://github.com/Lay007/lay007)",
        "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
    }

    for attempt in range(2):
        try:
            request = urllib.request.Request(url, headers=headers, method="HEAD")
            with urllib.request.urlopen(request, timeout=timeout) as response:
                code = response.getcode()
                if 200 <= code < 400:
                    return "ok", None
                return "error", f"HTTP {code}"
        except urllib.error.HTTPError as exc:
            if exc.code in (405, 501):
                try:
                    request = urllib.request.Request(url, headers=headers, method="GET")
                    with urllib.request.urlopen(request, timeout=timeout) as response:
                        code = response.getcode()
                        if 200 <= code < 400:
                            return "ok", None
                        return "error", f"HTTP {code}"
                except urllib.error.HTTPError as get_exc:
                    if get_exc.code in (401, 403, 429):
                        return "warning", f"HTTP {get_exc.code} (access/rate limited)"
                    return "error", f"HTTP {get_exc.code}"
                except urllib.error.URLError as get_exc:
                    if attempt == 0:
                        time.sleep(1.0)
                        continue
                    return "error", str(get_exc.reason)

            if exc.code in (401, 403, 429):
                return "warning", f"HTTP {exc.code} (access/rate limited)"
            return "error", f"HTTP {exc.code}"
        except urllib.error.URLError as exc:
            if attempt == 0:
                time.sleep(1.0)
                continue
            return "error", str(exc.reason)
        except TimeoutError:
            if attempt == 0:
                time.sleep(1.0)
                continue
            return "error", "timeout"

    return "error", "unknown network error"


def check_external(targets: list[str]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    urls = sorted(
        {
            target
            for target in targets
            if target.startswith(("http://", "https://"))
        }
    )

    for url in urls:
        host = (urllib.parse.urlsplit(url).hostname or "").lower()
        if host in SKIP_EXTERNAL_HOSTS:
            warnings.append(f"skipped bot-protected host: {url}")
            continue

        status, detail = request_url(url)
        if status == "ok":
            print(f"OK external: {url}")
        elif status == "warning":
            warnings.append(f"{url}: {detail}")
        else:
            errors.append(f"broken external link: {url}: {detail}")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check-external",
        action="store_true",
        help="also validate external HTTP(S) links",
    )
    args = parser.parse_args()

    if not README.exists():
        print("ERROR: README.md is missing", file=sys.stderr)
        return 1

    markdown = README.read_text(encoding="utf-8")
    targets = extract_targets(markdown)

    errors = check_static(markdown, targets)
    warnings: list[str] = []

    if args.check_external:
        external_errors, external_warnings = check_external(targets)
        errors.extend(external_errors)
        warnings.extend(external_warnings)

    for warning in warnings:
        print(f"WARNING: {warning}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    mode = "static + external" if args.check_external else "static"
    print(f"Profile check passed ({mode}); {len(targets)} Markdown targets inspected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
