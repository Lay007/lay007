# Engineering Portfolio Map

This profile is organized as a connected engineering portfolio rather than a list of unrelated repositories.

## Core engineering chain

```text
mathematical model
-> reproducible software reference
-> fixed-point design
-> C++ implementation
-> Verilog / FPGA architecture
-> measurement and verification
-> engineering report
```

## Repository roles

| Repository | Role in the portfolio | Main proof | Best reviewer signal |
|---|---|---|---|
| `zynq-sdr-course` | End-to-end SDR education and hardware experimentation | bilingual course, MkDocs, labs, HDL smoke tests | theory-to-hardware learning path |
| `cpp-dsp-showcase` | Production-style C++ DSP implementation | CMake, tests, benchmarks, installable package | deterministic kernels and performance discipline |
| `network-quality-assessment` | Hardware-assisted measurement and SLA analytics | FPGA/SFP timestamping concept, timing budget, demo reports | measurement methodology and timing-error reasoning |
| `optical-demodulator` *(private)* | Research-grade optical DSP pipeline | MATLAB/C++/Verilog layers, BER/EVM/SNR methodology | publication-oriented coherent receiver workflow |
| `script-toolbox` | Engineering workstation automation | repeatable setup scripts and operational notes | practical deployment and environment reproducibility |
| `lay007.github.io` | Public portfolio landing page | structured project summaries and profile routing | fast navigation for recruiters and collaborators |

## What should be visible to a reviewer

A reviewer should quickly see that the projects share one method:

1. define the physical or signal-processing problem;
2. build a reference model;
3. validate implementation behavior with deterministic tests;
4. measure quality using explicit metrics;
5. document assumptions, limitations and reproducibility steps.

## Portfolio improvement checklist

Use this checklist when polishing any public repository:

- Add a one-screen problem statement: what is measured or implemented, and why it matters.
- Show one architecture or signal-flow diagram near the top of the README.
- Keep reproducibility visible: commands, test vectors, CI status, generated artifacts.
- Put detailed methodology into `docs/` pages instead of overloading the landing README.
- Use generated figures and reports instead of static claims.
- Add CI checks for links, images, tests and documentation builds.
- Prefer small, reviewable commits for every documentation and engineering improvement.

## Next high-impact moves

1. Add short demo screenshots or generated report previews to the three main public repositories.
2. Keep each README optimized for a one-minute scan before deeper technical sections.
3. Publish a sanitized public summary of the optical-demodulator methodology when private data can stay out of the repository.
4. Keep figures visually consistent across the profile, course, DSP showcase and network measurement projects.
