# unconventional-cybersecurity-vulnerabilities
Research data, scripts (Python, MATLAB), and Arduino firmware evaluating budget DIY side-channel attacks: bioacoustic, optical, and electrodynamic audio signal reconstruction.

## Project Overview
The thesis analyzes three unconventional side-channel attacks that enable the interception of audio signals without traditional surveillance. The aim is to empirically assess the feasibility of these attack vectors in domestic settings using budget DIY (Do It Yourself) tools and to provide the first systematic comparative characterization in terms of the quality of reconstructed audio signals, their intelligibility, and practical feasibility.

## Evaluated Attack Vectors
The research aspect focuses on the physical reproduction of three distinct methods:
* **Bioacoustic Exploit:** A biohybrid injection device for collecting data from a simulated implant in ballistic gel, including an analysis of external factors.
* **Optical Exploit:** Optical sound reproduction through the reconstruction of surface micro-vibrations from high-frequency video recordings and audio signal extraction.
* **Electrodynamic Exploit:** Retasking audio connectors to convert a standard speaker into a microphone capable of capturing sound.

## Engineering & Repository Contents
This repository contains the full DIY engineering implementation optimized for low cost, demonstrating the feasibility of mass attacks:
* **`/arduino`** – Firmware code for electrodynamic audio connector retasking.
* **`/python` & `/matlab`** – Scripts used for signal analysis, noise cleaning, and data visualization.
* **`/experiment-01`, `/experiment-02`, `/experiment-03`** – Audio recordings and datasets generated during the experiments to allow full reproducibility of the results.
