# Repository Maturity Matrix

This matrix summarizes the role, current maturity and best review signal for the main engineering repositories in this portfolio.

## Portfolio structure

| Repository | Role in portfolio | Maturity | Best evidence | Next milestone |
|---|---|---|---|---|
| [`zynq-sdr-course`](https://github.com/Lay007/zynq-sdr-course) | SDR, DSP and FPGA education path | active / public | bilingual course structure, MkDocs site, CI-checked assets, reproducible plots and HDL flow notes | expand hardware bring-up and board-level verification demos |
| [`cpp-dsp-showcase`](https://github.com/Lay007/cpp-dsp-showcase) | production-style C++ DSP kernels | active / public | unit tests, benchmarks, algorithm evidence matrix, generated reports and CMake package structure | downstream CMake consumer smoke test and fixed-point notes |
| [`network-quality-assessment`](https://github.com/Lay007/network-quality-assessment) | SLA, timestamping and measurement credibility | active / public | synthetic SLA demo workflow, trace schema, generated CSV/SVG/Markdown report pipeline | real/sanitized trace adapter and hardware timestamp evidence dashboard |
| `optical-demodulator` | coherent optical DSP research workflow | active / private research | IEEE experiment plan, implementation matrix, canonical MATLAB CDC summary, BER/EVM/SNR methodology | C++ canonical CSV and MATLAB/C++ agreement report |
| [`script-toolbox`](https://github.com/Lay007/script-toolbox) | repeatable Windows engineering workstation automation | active / public | PowerShell syntax CI, PSScriptAnalyzer gate, CONTRIBUTING and SECURITY policy | Pester tests and toolkit template validation |
| [`lay007.github.io`](https://github.com/Lay007/lay007.github.io) | personal engineering website | supporting / public | portfolio landing page | synchronize with profile README and project evidence pages |

## Evidence types used across the portfolio

| Evidence type | Why it matters | Repositories |
|---|---|---|
| CI checks | proves that code, scripts or generated assets are not only documented but checked | `zynq-sdr-course`, `cpp-dsp-showcase`, `network-quality-assessment`, `script-toolbox` |
| Generated reports | makes engineering results reproducible and reviewable | `cpp-dsp-showcase`, `network-quality-assessment`, `optical-demodulator` |
| Shared metrics | keeps experiments comparable across tools and layers | `optical-demodulator`, `zynq-sdr-course`, `network-quality-assessment` |
| Test vectors | connects reference models, C++ and RTL-oriented verification | `cpp-dsp-showcase`, `optical-demodulator`, `zynq-sdr-course` |
| Documentation sites and reviewer guides | make complex engineering work understandable to a reviewer | `zynq-sdr-course`, `optical-demodulator`, `script-toolbox` |

## Maturity levels

| Level | Meaning |
|---|---|
| `supporting` | Useful as a portfolio or documentation support project. |
| `active` | Core project with ongoing implementation or documentation work. |
| `public` | Safe for external review. |
| `private research` | Active work that may contain private data, unpublished experiments or restricted artifacts. |

## Current focus

The current portfolio direction is to make each major repository evidence-driven:

```text
claim -> implementation -> test or experiment -> generated artifact -> reviewer documentation
```

The strongest next improvements are:

1. `optical-demodulator`: MATLAB/C++ agreement artifacts.
2. `network-quality-assessment`: real/sanitized trace adapter.
3. `cpp-dsp-showcase`: downstream CMake consumer test.
4. `zynq-sdr-course`: tighter bridge to C++ DSP implementation evidence.
5. `script-toolbox`: Pester tests and toolkit template checks.
