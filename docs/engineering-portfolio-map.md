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

| Repository | Role in the portfolio | Main proof |
|---|---|---|
| `zynq-sdr-course` | End-to-end SDR education and hardware experimentation | bilingual course, MkDocs, labs, HDL smoke tests |
| `cpp-dsp-showcase` | Production-style C++ DSP implementation | CMake, tests, benchmarks, installable package |
| `network-quality-assessment` | Hardware-assisted measurement and SLA analytics | FPGA/SFP timestamping concept, timing budget, demo reports |
| `optical-demodulator` | Research-grade optical DSP pipeline | MATLAB/C++/Verilog layers, BER/EVM/SNR methodology |
| `script-toolbox` | Engineering workstation automation | repeatable setup scripts and operational notes |

## What should be visible to a reviewer

A reviewer should quickly see that the projects share one method:

1. define the physical or signal-processing problem;
2. build a reference model;
3. validate implementation behavior with deterministic tests;
4. measure quality using explicit metrics;
5. document assumptions, limitations and reproducibility steps.

## Next portfolio improvements

- Keep README files short enough to scan in one minute.
- Put detailed methodology into `docs/` pages.
- Use generated figures and reports instead of static claims.
- Add CI checks for links, images, tests and documentation builds.
- Prefer small, reviewable commits for every documentation and engineering improvement.
