# Niekonwencjonalne luki cyberbezpieczeństwa - nieautoryzowana rekonstrukcja sygnałów poprzez exploity bioakustyczne, optyczne i elektrodynamiczne
--- 🇬🇧 For English version scroll down ---

## Omówienie projektu
W niniejszej pracy przeanalizowano trzy niekonwencjonalne ataki typu side-channel, które umożliwiają przechwytywanie sygnałów audio bez konieczności stosowania tradycyjnych metod inwigilacji. Celem jest empiryczna ocena wykonalności tych wektorów ataku w warunkach domowych przy użyciu niedrogich narzędzi typu „zrób to sam” (DIY) oraz przedstawienie pierwszej systematycznej charakterystyki porównawczej pod kątem jakości odtworzonych sygnałów audio, ich zrozumiałości oraz praktycznej wykonalności.

## Wektory ataku
Aspekt badawczy koncentruje się na fizycznej reprodukcji trzech różnych metod:
* **Exploit bioakustyczny:** Biohybrydowe urządzenie iniekcyjne do gromadzenia danych z symulowanego implantu w żelu balistycznym, w tym analiza czynników zewnętrznych.
* **Exploit optyczny:** Optyczna reprodukcja dźwięku poprzez rekonstrukcję mikrowibracji powierzchniowych na podstawie nagrań wideo o wysokiej częstotliwości i ekstrakcji sygnału audio.
* **Exploit elektrodynamiczny:** Zmiana przeznaczenia złączy audio w celu przekształcenia standardowego głośnika w mikrofon zdolny do przechwytywania dźwięku.

## Inżynieria i zawartość repozytorium
To repozytorium zawiera pełną implementację inżynieryjną typu „zrób to sam”, zoptymalizowaną pod kątem niskich kosztów, demonstrującą wykonalność ataków masowych:
* **`/experiment-01`, `/experiment-02`, `/experiment-03`** – Nagrania audio i zbiory danych wygenerowane podczas eksperymentów, umożliwiające pełną odtwarzalność wyników.

# Eksperyment 01: Implantowe urządzenie wywiadowcze

Ten folder zawiera zbiór danych, zrekonstruowane nagrania audio oraz spektrogramy wizualne dotyczące **Eksperymentu 01**, w ramach którego oceniano nieuprawnione odzyskiwanie sygnałów audio za pomocą biohybrydowego urządzenia wstrzykującego symulującego implant umieszczony w żelu balistycznym.

## Struktura katalogów i nazewnictwo zbioru danych

Zbiór danych jest ściśle podzielony na trzy główne kategorie: `Sample`, `Inside` (kontrolowane środowisko wewnętrzne) oraz `Outside` (warunki środowiskowe na zewnątrz).

### 1. /Sample
Zawiera oryginalne sygnały źródłowe odtwarzane podczas eksperymentu, które mają zostać przechwycone przez symulowany implant audio wewnątrz konfiguracji fantomowej.
* **`/Records`**: 3 referencyjne pliki audio (`chirp.wav`, `conversation.wav`, `tone.wav`).
* **`/Spectrograms`**: Wizualne przedstawienia analizy częstotliwości (`.png`) odpowiadające każdemu plikowi audio.

### 2. /Inside (Środowisko wewnętrzne)
Dane zebrane w kontrolowanych warunkach wewnętrznych, podzielone na dwie zmienne eksperymentalne:
* **`/Depth`**: Analiza wpływu fizycznej głębokości umieszczenia implantu w żelu balistycznym.
  * **`/Records`**: Nagrania audio (`.wav`) zawierające 4 rodzaje sygnałów (*chirp, ton, ref (odniesienie), rozmowa*) dla 3 głębokości umieszczenia:
    * `_deep` (Głęboka implementacja)
    * `_medium` (Średnia implementacja)
    * `_shallow` (Implementacja płytka)
    * *Przykładowa nazwa pliku:* `chirp_deep.wav`
  * **`/Spectrograms`**: Odpowiednie spektrogramy (`.png`) dla każdej odmiany głębokości (np. `chirp_deep.png`).

* **`/Distance`**: Analizuje wpływ odległości źródła dźwięku mierzonej w centymetrach wzdłuż podłoża.
  * **`/Records`**: Nagrania audio (`.wav`) 4 typów sygnałów dla 5 różnych odległości: `_10`, `_50`, `_150`, `_300` i `_600` cm.
    * *Przykładowa nazwa pliku:* `chirp_10.wav`
  * **`/Spectrograms`**: Odpowiednie spektrogramy (`.png`) dla każdej zmiany odległości (np. `chirp_10.png`).

### 3. /Outside (Środowisko zewnętrzne)
* Zawiera **dokładnie taką samą strukturę katalogów, typy sygnałów i konwencje nazewnictwa plików** jak katalog `/Inside`. Ten podfolder stanowi replikację całego eksperymentu w warunkach rzeczywistego hałasu środowiskowego na zewnątrz i czynników zewnętrznych.

## Szczegóły techniczne
* **Format audio:** Bezstratny format pliku audio Waveform (`.wav`)
* **Format wizualizacji:** Spektrogramy w formacie Portable Network Graphics (`.png`) do weryfikacji sygnatury akustycznej.

# Eksperyment 02: Mikrofon wizualny

# Eksperyment 03: Konwersja głośnika w mikrofon

Ten folder zawiera prototypy inżynieryjne, kod źródłowy oraz dane eksperymentalne dotyczące **Eksperymentu 03**. Badania pokazują, w jaki sposób standardowe głośniki można przekształcić w mikrofony przy użyciu niedrogich mikrokontrolerów (Arduino Uno) i podstawowych wzmacniaczy operacyjnych.

## Przegląd projektu
Eksperyment bada możliwość przechwytywania sygnałów akustycznych poprzez wykorzystanie właściwości elektrodynamicznych głośników. Wykorzystując specjalnie skonstruowany obwód kondycjonujący sygnał oraz zoptymalizowane ustawienia przetwornika analogowo-cyfrowego (ADC) w Arduino Uno, pokazujemy, że głośniki mogą rejestrować zrozumiały dźwięk.

## Zawartość repozytorium

### 1. /Programy
Implementacja sprzętowa i programowa:
* `sketch_apr30a.ino`: Oprogramowanie układowe Arduino skonfigurowane z niestandardowym preskalerem ADC i ustawieniami szybkiego próbkowania niezbędnymi do rekonstrukcji dźwięku o wysokiej częstotliwości.
* `main.py`: aplikacja terminalowa oparta na języku Python, służąca do komunikacji ze sprzętem, przetwarzania przychodzącego strumienia bitów i zapisywania zrekonstruowanego dźwięku.

### 2. /Records & /Spectrograms
Dane są podzielone na dwie fazy badań:
#### Faza 1: Analiza porównawcza przetworników i wzmacniaczy operacyjnych
Znajduje się w katalogach `/Speaker_1`, `/Speaker_2` i `/Speaker_3`. W tej fazie oceniana jest wydajność trzech różnych głośników pełniących rolę mikrofonów.
* **Zmienne sprzętowe:** * **Wzmacniacze operacyjne:** LM358 (ogólnego przeznaczenia) vs. MCP6002 (nowoczesny rail-to-rail).
    * **Konfiguracje:** odwracająca vs. nieodwracająca.
* **Konwencja nazewnictwa:** `[OpAmp]_[Config]_[Signal].wav`
    * *Przykład:* `LM_invert_conversation.wav` (LM358, konfiguracja odwracająca, sygnał mowy).

#### Faza 2: Efektywny zasięg i wykonalność odległości
Znajduje się w katalogu `/Distance`. Ta faza skupia się na najbardziej stabilnym przetworniku (głośnik 2) w celu określenia maksymalnej odległości, przy której możliwe jest odzyskanie zrozumiałego sygnału.
* **Parametry testowe:** Odległości 5, 150, 300 i 600 cm.
* **Konfiguracja:** Wyłącznie nieodwracająca (na podstawie optymalizacji z etapu 1).
* **Konwencja nazewnictwa:** `[OpAmp]_noninvert_[Signal]_[Distance].wav`
    * *Przykład:* `MCP_noninvert_chirp_300.wav` (MCP6002 w odległości 3 metrów).

### 3. /Sample
Zawiera oryginalne sygnały referencyjne użyte jako źródło audio podczas eksperymentów (`chirp`, `tone`, `conversation`), zapewniając spójność między eksperymentami 01 i 03.

## Główne cele badań
* **Analiza pasma:** Wykorzystanie sygnałów typu chirp o częstotliwościach od 50 Hz do 10 kHz w celu określenia granic pasma przenoszenia.
* **Ocena zrozumiałości:** Ocena czystości mowy ludzkiej zarejestrowanej za pomocą elektrodynamicznego urządzenia podsłuchowego.
* **Optymalizacja sprzętu:** Określenie, w jaki sposób wybór wzmacniacza operacyjnego i topologii obwodu wpływa na zasięg nieuprawnionego podsłuchu.

---

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

# Experiment 02: 

# Experiment 03: Electrodynamic Retasking (Speaker-to-Microphone Exploit)

This folder contains the engineering prototypes, source code, and experimental data for **Experiment 03**. The research demonstrates how standard loudspeakers can be surreptitiously repurposed as microphones using budget microcontrollers (Arduino Uno) and basic operational amplifiers.

## Project Overview
The experiment investigates the feasibility of intercepting acoustic signals by exploiting the electrodynamic properties of speakers. By utilizing a custom-built signal conditioning circuit and optimized ADC (Analog-to-Digital Converter) settings on an Arduino Uno, we demonstrate that speakers can capture intelligible audio.

## Repository Contents

### 1. /Programs
Hardware and software implementation:
* `sketch_apr30a.ino`: Arduino firmware configured with a custom ADC prescaler and high-speed sampling settings necessary for high-frequency audio reconstruction.
* `main.py`: A Python-based terminal application used to interface with the hardware, process the incoming bitstream, and save the reconstructed audio.

### 2. /Records & /Spectrograms
The data is divided into two research phases:

#### Phase 1: Transducer and Op-Amp Comparative Analysis
Located in `/Speaker_1`, `/Speaker_2`, and `/Speaker_3`. This phase evaluates the efficiency of three different loudspeakers acting as microphones.
* **Hardware Variables:** * **Op-Amps:** LM358 (General purpose) vs. MCP6002 (Modern Rail-to-Rail).
    * **Configurations:** Inverting vs. Non-inverting.
* **Naming Convention:** `[OpAmp]_[Config]_[Signal].wav`
    * *Example:* `LM_invert_conversation.wav` (LM358, Inverting config, Speech signal).

#### Phase 2: Effective Range and Distance Feasibility
Located in `/Distance`. This phase focuses on the most stable transducer (Speaker 2) to determine the maximum distance for intelligible signal recovery.
* **Testing Parameters:** Distances of 5, 150, 300, and 600 cm.
* **Configuration:** Exclusively non-inverting (based on Phase 1 optimization).
* **Naming Convention:** `[OpAmp]_noninvert_[Signal]_[Distance].wav`
    * *Example:* `MCP_noninvert_chirp_300.wav` (MCP6002 at 3 meters).

### 3. /Sample
Contains the original reference signals used as the audio source during experiments (`chirp`, `tone`, `conversation`), ensuring consistency across Experiment 01 and 03.

## Key Research Goals
* **Bandwidth Analysis:** Using 50 Hz – 10 kHz chirps to identify frequency response limits.
* **Intelligibility Assessment:** Evaluating the clarity of human speech captured via the electrodynamic exploit.
* **Hardware Optimization:** Quantifying how the choice of operational amplifier and circuit topology affects the range of unauthorized eavesdropping.
