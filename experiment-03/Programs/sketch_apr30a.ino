#include <avr/io.h>
#include <avr/interrupt.h>

// Definicja częstotliwości próbkowania: 8000 Hz
// Wzór: 16MHz / (prescaler * Fs) - 1
// Dla 8000Hz i prescalera 8: (16000000 / (8 * 8000)) - 1 = 249
const uint16_t timer_compare = 152;

volatile bool sample_ready = false;
volatile uint16_t adc_value = 0;

void setup() {
  // 1. Inicjalizacja Seriala na wysokiej prędkości
  Serial.begin(500000);

  // 2. Konfiguracja ADC (Przetwornik Analogowo-Cyfrowy)
  ADMUX = (1 << REFS0); // Napięcie odniesienia AVCC (5V), wejście A0 (MUX 0000)
  
  // ADCSRA: Włącz ADC, ustaw Prescaler na 64 (1MHz taktowanie ADC)
  ADCSRA = (1 << ADEN) | (1 << ADPS2) | (1 << ADPS1);

  // 3. Konfiguracja Timera 1 (Tryb CTC - Clear Timer on Compare Match)
  TCCR1A = 0;             // Tryb normalny pinów
  TCCR1B = (1 << WGM12) | (1 << CS11); // Tryb CTC, Prescaler 8
  OCR1A = timer_compare;  // Ustawienie progu dla 8kHz
  TIMSK1 = (1 << OCIE1A); // Włącz przerwanie Timer Compare Match A

  sei(); // Włącz globalne przerwania
}

// Przerwanie Timera 1 - wywoływane dokładnie co 125 mikrosekund
ISR(TIMER1_COMPA_vect) {
  // Rozpocznij konwersję ADC
  ADCSRA |= (1 << ADSC);
  
  // Czekaj na zakończenie (zajmie to ok 13-16us)
  while (ADCSRA & (1 << ADSC));
  
  // Pobierz wartość
  adc_value = ADC;
  sample_ready = true;
}

void loop() {
  // Jeśli przerwanie przygotowało nową próbkę
  if (sample_ready) {
    // Wyślij binarnie 2 bajty
    Serial.write(adc_value & 0xFF);         // Młodszy bajt
    Serial.write((adc_value >> 8) & 0xFF);  // Starszy bajt
    
    sample_ready = false;
  }
}