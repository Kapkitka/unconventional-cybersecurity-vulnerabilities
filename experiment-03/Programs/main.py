import serial
import numpy as np
import wave
import time
import sys
import re
import keyboard  # <-- Nowa biblioteka do obsługi klawiszy

# --- KONFIGURACJA ---
PORT = 'COM6'          # <-- Zmień na swój port (np. 'COM4' lub '/dev/ttyUSB0')
BAUD_RATE = 500000     # Musi być taki sam jak w Arduino
DURATION = 60          # Maksymalny czas nagrania w sek (spacja zakończy je wcześniej)
DEFAULT_OUTPUT = "nagranie_arduino.wav"
# --------------------

def slugify(text):
    """Funkcja oczyszczająca nazwę pliku z niedozwolonych znaków systemowych"""
    text = text.strip()
    # Usuwamy znaki niedozwolone w nazwach plików Windows/Linux
    text = re.sub(r'[\\/*?:"<>|]', "", text)
    return text

def record_audio():
    try:
        # Inicjalizacja połączenia
        ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
        print(f"Łączenie z {PORT}...")
        time.sleep(2)  # Czekamy na restart Arduino
        ser.reset_input_buffer()

        samples = []
        
        print(f"\n[URUCHOMIONO] Rozpoczynam nasłuchiwanie (max {DURATION} sekund)...")
        print("--> Mów do głośnika now!")
        print("--> NACIŚNIJ SPACJĘ na klawiaturze, aby zakończyć nagrywanie w dowolnym momencie!")
        
        # Czekamy chwilę, aby upewnić się, że użytkownik puścił spację, 
        # jeśli uruchamiał program skrótem klawiszowym
        time.sleep(0.2) 
        
        start_time = time.time()
        
        # Pętla zbierania danych
        while True:
            # 1. SPRAWDZENIE SPACJI: Jeśli wciśnięto spację, przerywamy pętlę
            if keyboard.is_pressed('space'):
                print("\n[INFO] Wykryto wciśnięcie SPACJI. Zatrzymuję nagrywanie...")
                break

            # 2. Awaryjne sprawdzenie maksymalnego czasu trwania nagrania
            current_elapsed = time.time() - start_time
            if current_elapsed >= DURATION:
                print("\n[INFO] Osiągnięto maksymalny czas nagrania.")
                break
                
            # Czytamy 2 bajty (surowy int z Arduino)
            raw_data = ser.read(2)
            if len(raw_data) == 2:
                # Konwersja z bajtów (Little Endian) na liczbę
                val = int.from_bytes(raw_data, byteorder='little')
                
                # --- AUTO-SYNCHRONIZACJA ---
                if val > 1023:
                    # Jeśli wartość przekracza 1023, straciliśmy synchronizację bajtów!
                    # Odczytujemy 'w ciemno' jeden nadmiarowy bajt, aby wskoczyć na właściwy tor
                    ser.read(1)
                    continue # Pomijamy tę jedną zepsutą próbkę
                # ---------------------------
                
                # Normalizacja sygnału:
                # 1. Przesuwamy o 512 (środek ADC) w dół
                # 2. Mnożymy x10 (wzmocnienie cyfrowe)
                sample = (val - 512) * 10
                
                # Zabezpieczenie przed przesterowaniem (clipping)
                sample = max(-32768, min(32767, sample))
                samples.append(sample)
                
        end_time = time.time()
        ser.close()

        # --- KALIBRACJA TEMPA ---
        actual_duration = end_time - start_time
        actual_fs = int(len(samples) / actual_duration)
        
        print(f"\nKoniec przechwytywania danych!")
        print(f"Rzeczywisty czas trwania: {actual_duration:.2f} s")
        print(f"Wykryte próbkowanie (Fs): {actual_fs} Hz")

        # --- INFORMACJA O MOŻLIWOŚCI ZAPISU I PROŚBA O NAZWĘ ---
        print("\n=========================================================")
        print(" STATUS: Dźwięk znajduje się bezpiecznie w pamięci bufora.")
        print(" Możesz teraz zapisać swoje nagranie jako plik audio .WAV")
        print("=========================================================")
        
        user_title = input("Wpisz własną nazwę nagrania (lub wciśnij Enter dla nazwy domyślnej): ")
        user_title = slugify(user_title) # Czyszczenie z zakazanych znaków systemowych
        
        if user_title == "":
            filename = DEFAULT_OUTPUT
        else:
            # Jeśli użytkownik zapomniał dopisać .wav, robimy to za niego
            if not user_title.lower().endswith(".wav"):
                filename = f"{user_title}.wav"
            else:
                filename = user_title

        # Zapis do pliku WAV
        save_wav(samples, actual_fs, filename)

    except serial.SerialException as e:
        print(f"\nBłąd portu szeregowego: {e}")
    except Exception as e:
        print(f"\nWystąpił błąd: {e}")

def save_wav(data, fs, filename):
    print(f"\nZapisywanie do pliku: {filename}...")
    audio_array = np.array(data, dtype=np.int16)
    
    with wave.open(filename, 'w') as f:
        f.setnchannels(1)      # Mono
        f.setsampwidth(2)      # 16-bit (2 bajty)
        f.setframerate(fs)     # Używamy zmierzonego Fs
        f.writeframes(audio_array.tobytes())
    
    print(f"Sukces! Plik '{filename}' został pomyślnie utworzony i zamknięty.")

if __name__ == "__main__":
    record_audio()