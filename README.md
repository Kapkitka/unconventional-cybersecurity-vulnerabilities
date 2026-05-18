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


# Experiment 01: Bioacoustic Exploit (Biohybrid Injection Device)

This folder contains the dataset, reconstructed audio recordings, and visual spectrograms for **Experiment 01**, which evaluates the unauthorized recovery of audio signals via a biohybrid injection device simulating an implant in ballistic gel.

## Directory Structure & Dataset Nomenclature

The dataset is strictly organized into three main categories: `Sample`, `Inside` (controlled indoor environment), and `Outside` (outdoor environmental conditions).

### 1. /Sample
Contains the original source signals played during the experiment to be captured by the simulated audio implant inside the phantom setup.
* **`/Records`**: 3 reference audio files (`chirp.wav`, `conversation.wav`, `tone.wav`).
* **`/Spectrograms`**: Visual frequency analysis representations (`.png`) corresponding to each audio file.

### 2. /Inside (Indoor Environment)
Data collected under controlled indoor conditions, split into two experimental variables:

* **`/Depth`**: Analyzes the impact of the implant’s physical depth within the ballistic gel.
  * **`/Records`**: Audio recordings (`.wav`) of 4 signal types (*chirp, tone, ref (reference), conversation*) across 3 implantation depths:
    * `_deep` (Deep deployment)
    * `_medium` (Medium deployment)
    * `_shallow` (Shallow deployment)
    * *Example filename:* `chirp_deep.wav`
  * **`/Spectrograms`**: Corresponding spectrograms (`.png`) for each depth variation (e.g., `chirp_deep.png`).

* **`/Distance`**: Analyzes the impact of the audio source distance measured in centimeters along the floor.
  * **`/Records`**: Audio recordings (`.wav`) of 4 signal types across 5 distinct distances: `_10`, `_50`, `_150`, `_300`, and `_600` cm.
    * *Example filename:* `chirp_10.wav`
  * **`/Spectrograms`**: Corresponding spectrograms (`.png`) for each distance variation (e.g., `chirp_10.png`).

### 3. /Outside (Outdoor Environment)
* Contains the **exact same directory structure, signal types, and file naming conventions** as the `/Inside` directory. This subfolder represents the replication of the entire experiment exposed to real-world outdoor environmental noise and external factors.

## Technical Details
* **Audio Format:** Lossless Waveform Audio file format (`.wav`)
* **Visualization Format:** Portable Network Graphics (`.png`) spectrograms for acoustic signature verification.
