# Alexander | Lay007

**DSP / FPGA / Communications Engineer**  
Candidate of Technical Sciences  
C++ • Verilog • MATLAB/Simulink • Fixed-Point DSP • SDR • Measurement Systems

[LinkedIn](https://ru.linkedin.com/in/alexander-lyubko-dsp) · [Engineering portfolio](https://lay007.github.io) · [laymob@gmail.com](mailto:laymob@gmail.com)

I build reproducible communication-system pipelines: from MATLAB/Simulink reference models to C++ and RTL implementations, FPGA/SDR integration, measurements, and engineering reports.

## Current flagship work

### [zynq-sdr-course](https://github.com/Lay007/zynq-sdr-course)

An end-to-end SDR engineering course and evidence base. Its in-fabric QPSK modem is validated on two independent Zynq-7020 + AD936x boards over a 915 MHz cabled RF link.

- 5.6 million fabric-loopback bits with zero errors; reported BER upper bound below `5.34e-7`.
- Two-board differential QPSK with whole-burst rotation failures eliminated and payload BER around `4e-4`.
- Reproducible RTL tests, IQ captures, machine-readable results, timing/resource reports, and measurement documentation.

### [zynq-lora-phy-positioning](https://github.com/Lay007/zynq-lora-phy-positioning)

A LoRa PHY and ToA/TDoA positioning platform with a traceable MATLAB → Simulink → generated Verilog → ZynqSDR path.

- Complete MATLAB floating-point M1: continuous-IQ packet acquisition, hard/soft LoRa decoding, BER/PER, fractional ToA, and calibrated 2D TDoA.
- Streaming fixed-point Simulink front end with blind acquisition, grid realignment, SFD/framing, coarse timestamps, and packet-rate fractional ToA regression against MATLAB.
- Generated HDL for eight hardware-bound blocks, including the packet-rate ToA interpolator and dedicated carrier-frequency estimator; all eight have out-of-context synthesis evidence, while the correlator and ToA block also have post-route timing and vectorless core-power estimates.

## 10-minute review path

| Step | Repository | What to review |
|---:|---|---|
| 1 | [zynq-sdr-course](https://github.com/Lay007/zynq-sdr-course) | DSP model → fixed-point RTL → Zynq/AD936x RF measurements |
| 2 | [zynq-lora-phy-positioning](https://github.com/Lay007/zynq-lora-phy-positioning) | LoRa PHY, real IQ, Simulink/HDL path, ToA/TDoA methodology |
| 3 | [cpp-dsp-showcase](https://github.com/Lay007/cpp-dsp-showcase) | Modern C++ DSP kernels, deterministic tests, benchmarks, and CMake packaging |
| 4 | [network-quality-assessment](https://github.com/Lay007/network-quality-assessment) | Latency/jitter methodology, timestamp credibility, and reproducible reports |
| 5 | [script-toolbox](https://github.com/Lay007/script-toolbox) | Repeatable Windows, SSH, Git, and workstation automation |

## Engineering evidence

| Capability | Evidence |
|---|---|
| Theory to hardware | Reference models, fixed-point design, generated/manual RTL, FPGA integration, and RF/IQ measurements |
| DSP implementation | MATLAB, Simulink, C++, Python, and Verilog components with deterministic vectors |
| Verification | Cross-model regressions, CI, BER/PER/EVM/SNR metrics, timing/resource reports, and acceptance gates |
| Real measurements | IQ captures, manifests, calibration, latency/jitter analysis, and uncertainty-aware reporting |
| Technical communication | Bilingual documentation, reviewer paths, experiment guides, and publication-oriented figures |

## Selected repositories

| Repository | Focus | Status |
|---|---|---|
| [zynq-sdr-course](https://github.com/Lay007/zynq-sdr-course) | SDR education, Zynq/AD936x, FPGA, RF measurement | Flagship / active |
| [zynq-lora-phy-positioning](https://github.com/Lay007/zynq-lora-phy-positioning) | LoRa PHY, generated HDL, ToA/TDoA positioning | Research / active |
| [cpp-dsp-showcase](https://github.com/Lay007/cpp-dsp-showcase) | Reusable C++ DSP kernels and validation | Active showcase |
| [network-quality-assessment](https://github.com/Lay007/network-quality-assessment) | Network measurement and timestamp methodology | Engineering demo |
| [script-toolbox](https://github.com/Lay007/script-toolbox) | Windows/SSH/Git automation with quality gates | Infrastructure toolkit |

## Working principles

1. Define measurable acceptance criteria before implementation.
2. Keep the reference model, software, RTL, and hardware on shared test vectors.
3. Record configurations, provenance, raw counts, and known limitations.
4. Treat reproducibility and documentation as engineering deliverables.

![Engineering pipeline](assets/engineering_pipeline.svg)
