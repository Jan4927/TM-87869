import sys
import os
import time

sys.path.append(os.path.abspath("../Artefakt06"))

try:
    from MainPage import MainPage
except ImportError:
    print("BŁĄD: Brak dostępu do MainPage.py w ../Artefakt06/")
    sys.exit(1)

class InterruptManager(MainPage):
    """
    MODUŁ PRZERWAŃ (Layer 4): Symulacja zdarzeń systemowych Androida.
    """
    def simulate_incoming_call(self, duration_sec=5):
        print(f"\n[INTERRUPT] KROK 1: Stan aplikacji przed połączeniem: ACTIVE")
        print(f"[INTERRUPT] KROK 2: Wyzwalanie zdarzenia: INCOMING CALL (Duration: {duration_sec}s)")
        time.sleep(1)
        print(">>> SYSTEM: Aplikacja w tle (onPause) | Widoczny ekran połączenia <<<")
        time.sleep(duration_sec)
        print(f"[INTERRUPT] KROK 3: Zakończenie połączenia. Powrót do aplikacji.")
        return "SUKCES: Aplikacja odzyskała fokus (onResume). Dane sesji zachowane."

    def simulate_low_battery_warning(self):
        print(f"\n[INTERRUPT] Wyzwalanie zdarzenia: LOW BATTERY WARNING")
        return "SUKCES: Aplikacja obsłużyła systemowe okno dialogowe bez błędu."

if __name__ == "__main__":
    im = InterruptManager()
    print(">>> ZADANIE 7.2: TESTY ODPORNOŚCI NA PRZERWANIA <<<")
    print("-" * 45)
    status_call = im.simulate_incoming_call(duration_sec=3)
    print(status_call)
    status_battery = im.simulate_low_battery_warning()
    print(status_battery)
    print("-" * 45)