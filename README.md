# Alexander | Lay007

**DSP / FPGA / Communications Engineer**  
Candidate of Technical Sciences  
C++ • Verilog • MATLAB/Simulink • Fixed-Point DSP • Circuit Design • Information Security

I build reproducible DSP and communication-system pipelines: from MATLAB/Simulink reference models to C++ implementations, Verilog/FPGA architecture, measurements, BER/EVM/SNR analysis, and engineering documentation.

---

## 60-second reviewer snapshot

| Signal I want to show | Evidence in the portfolio |
|---|---|
| **I can connect theory to hardware** | SDR course path from signal theory to Zynq/AD9363 experiments and RTL flow |
| **I can implement DSP, not only describe it** | C++ DSP kernels with tests, benchmark tooling, and generated reports |
| **I can verify engineering systems** | MATLAB/C++/RTL alignment, deterministic vectors, CI checks, and metric-driven validation |
| **I can work with real measurements** | BER, EVM, SNR, jitter, latency, timestamp accuracy, and error-budget reporting |
| **I can turn R&D into documentation** | MkDocs sites, IEEE-style figures, experiment manifests, and publication-oriented reports |

---

## Engineering Pipeline

![Engineering Pipeline](assets/engineering_pipeline.svg)

| Stage | Engineering result |
|---|---|
| **Signal / RF problem** | define channel, impairments, constraints, and measurable goals |
| **MATLAB / Simulink model** | build readable golden reference, diagnostic plots, and test vectors |
| **C++ implementation** | create deterministic, testable, reproducible software processing |
| **Fixed-point design** | define Q-format, rounding, saturation, and error budget |
| **Verilog / FPGA architecture** | map stable DSP blocks to streaming RTL and testbenches |
| **Measurement and verification** | compare model, software, RTL, and real/synthetic signals |
| **BER / EVM / SNR reports** | turn experiments into engineering conclusions and publication-ready artifacts |

Additional portfolio structure notes are available in [docs/engineering-portfolio-map.md](docs/engineering-portfolio-map.md).

---

## Engineering Proof

| Proof artifact | Repository | What it demonstrates |
|---|---|---|
| Experiment manifests + CI checks | [zynq-sdr-course](https://github.com/Lay007/zynq-sdr-course) | reproducible SDR labs and acceptance criteria |
| DSP test-vector strategy + benchmark schema | [cpp-dsp-showcase](https://github.com/Lay007/cpp-dsp-showcase) | deterministic C++ DSP validation and performance reporting |
| Synthetic SLA demo + timestamp methodology | [network-quality-assessment](https://github.com/Lay007/network-quality-assessment) | measurement credibility, trace schema and hardware/software timestamp analysis |
| CDC comparison flow + IEEE experiment plan | private research workspace | coherent optical DSP research workflow and MATLAB/C++/RTL evidence path |
| PowerShell CI + security policy | [script-toolbox](https://github.com/Lay007/script-toolbox) | repeatable engineering workstation automation with safety checks |

---

## Repository Maturity Matrix

| Repository | Role | Status | Best reviewer signal | Next milestone |
|---|---|---|---|---|
| [zynq-sdr-course](https://github.com/Lay007/zynq-sdr-course) | SDR / FPGA education | active public | bilingual course, MkDocs, CI-checked labs and generated plots | board-level verification demos |
| [cpp-dsp-showcase](https://github.com/Lay007/cpp-dsp-showcase) | C++ DSP kernels | active public | tests, benchmarks, algorithm evidence matrix and CMake package structure | downstream CMake consumer smoke test |
| [network-quality-assessment](https://github.com/Lay007/network-quality-assessment) | SLA / timestamping | active public | synthetic SLA CI demo, trace schema, CSV/SVG/Markdown report pipeline | real or sanitized trace adapter |
| optical-demodulator | coherent optical DSP research | active private | IEEE experiment plan, implementation matrix and canonical MATLAB CDC summary | C++ canonical CSV and MATLAB/C++ agreement |
| [script-toolbox](https://github.com/Lay007/script-toolbox) | Windows automation | active public | PowerShell CI, PSScriptAnalyzer, CONTRIBUTING and SECURITY policy | Pester tests and toolkit template validation |

Full maturity notes are available in [docs/repository-maturity-matrix.md](docs/repository-maturity-matrix.md).

---

## Featured Engineering Projects

### [zynq-sdr-course](https://github.com/Lay007/zynq-sdr-course)
Bilingual SDR course connecting signal theory, DSP, fixed-point modeling, HDL flow, RF front-end understanding, and board-level experiments.

**Focus:** Zynq-7020, AD9363, RTL-SDR, HDSDR, experiment manifests, CI-checked assets, reproducible IEEE-style plots.  
**Best reviewer signal:** reproducible learning path from DSP theory to HDL/FPGA-oriented experiments.

### [cpp-dsp-showcase](https://github.com/Lay007/cpp-dsp-showcase)
Modern C++ DSP showcase with deterministic kernels, tests, benchmark tooling, CI, and generated engineering plots.

**Focus:** FIR filtering, FFT overlap-save, Goertzel detector, GCC-PHAT delay estimation, rational resampling, golden vectors, benchmark methodology.  
**Best reviewer signal:** algorithm evidence matrix with tests, benchmarks, generated reports and CMake packaging.

### [network-quality-assessment](https://github.com/Lay007/network-quality-assessment)
Hardware-assisted network measurement concept based on FPGA/SFP datapath timestamping and SLA-oriented metrics.

**Focus:** one-way delay, jitter, packet loss, timestamp accuracy, timing error budget, SLA reports, software vs hardware timestamps.  
**Best reviewer signal:** hardware-free synthetic SLA demo that generates trace CSV, SLA summary, SVG plots and Markdown report in CI.

### optical-demodulator *(private research workspace)*
Private coherent optical DSP research workspace used to build a MATLAB → C++ → fixed-point → Verilog evidence chain for receiver studies.

**Focus:** chromatic-dispersion compensation, DP-QPSK processing, CDC comparison reports, BER/EVM/SNR metrics, fixed-point and RTL mapping.  
**Best reviewer signal:** IEEE experiment plan, implementation matrix and canonical MATLAB CDC summary for future MATLAB/C++ agreement.

### [script-toolbox](https://github.com/Lay007/script-toolbox)
Practical automation toolbox for repeatable Windows engineering workstation setup.

**Focus:** SSH, Git, CMake, Visual Studio Build Tools, deployment helpers, repeatable developer environments.  
**Best reviewer signal:** PowerShell syntax CI, PSScriptAnalyzer gate, contribution guide and security policy for setup scripts.

### [lay007.github.io](https://github.com/Lay007/lay007.github.io)
Personal engineering website and portfolio landing page.

**Best reviewer signal:** public landing page that can route readers to the strongest engineering evidence.

---

## What I Do Best

- Design DSP chains for communication and measurement systems.
- Convert algorithms into hardware-aware C++ and Verilog implementations.
- Build verification flows across MATLAB, C++, RTL simulation, and real signals.
- Analyze receiver quality using BER, EVM, SNR, jitter, latency, and error-budget metrics.
- Document engineering systems so that results are reproducible, reviewable, and useful.

---

## Currently Building

- reproducible SDR course with hardware labs and manifest-driven experiments;
- C++ DSP benchmark and verification framework;
- optical coherent receiver research platform for CDC and BER/EVM/SNR studies;
- hardware-assisted network measurement methodology with SLA reports;
- portfolio site that connects these repositories into one engineering story.

---

## Technical Stack

| Area | Tools and technologies |
|---|---|
| DSP / modeling | MATLAB, Simulink, fixed-point modeling, Python |
| Software | C++, CMake, tests, CI, benchmark tooling |
| FPGA / HDL | Verilog, streaming RTL, testbenches, Xilinx-oriented flows |
| Measurement | BER, EVM, SNR, constellation analysis, jitter, latency, error budget |
| Hardware | Zynq, AD9363, RTL-SDR, optical/communication signal chains, applied electronics |
| Engineering tooling | GitHub Actions, MkDocs, documentation automation, PowerShell scripts |

---

## Research and Engineering Interests

- Coherent optical demodulation and chromatic-dispersion compensation.
- SDR systems from signal model to RF experiment.
- Fixed-point DSP and FPGA-ready receiver architectures.
- Hardware-assisted network and communication measurements.
- Reproducible engineering documentation and CI-generated plots.

---

## Background

- **Candidate of Technical Sciences**
- **10 years** of teaching experience in higher education
- **Author of 3 textbooks**
- Publications, inventions, and patents in technical fields
- Strong background in **circuit design** and **information security**

---

## Engineering Principles

- Start with a clear mathematical model.
- Keep MATLAB, C++, and RTL behavior aligned with shared vectors and metrics.
- Treat measurements, plots, and reports as part of the engineering system.
- Prefer reproducible validation over one-off demos.
- Document assumptions, limitations, and error sources explicitly.

---

## Open to

- DSP / FPGA / SDR / optical communication discussions;
- engineering collaboration and R&D initiatives;
- communication-system and telemetry-related development;
- educational engineering content and technical documentation;
- specialized software and tooling projects.

---

## Contact

- GitHub Pages: [lay007.github.io](https://lay007.github.io/)
- Telegram: [@laymob](https://t.me/laymob)
