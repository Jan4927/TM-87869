import sys
import os
import datetime

sys.path.append(os.path.abspath("../Artefakt06"))
from MainPage import MainPage

class DeviceStateManager(MainPage):
    """
    MODUŁ ZARZĄDZANIA STANEM (Layer 4): Obsługa fizycznych zmian urządzenia.
    """
    def __init__(self):
        super().__init__()
        self.log_file = "73_state.log"

    def _log_event(self, event_name, detail):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {event_name.upper()}: {detail}\n")

    def toggle_screen_orientation(self, target="LANDSCAPE"):
        print(f"[DEVICE] Zmiana orientacji na: {target}")
        detail = f"Ekran obrócony do {target}. Weryfikacja przerysowania layoutu..."
        self._log_event("orientation", detail)
        return f"SUKCES: Orientacja zmieniona na {target}."

    def simulate_power_connection(self, is_connected=True):
        state = "CONNECTED" if is_connected else "DISCONNECTED"
        print(f"[DEVICE] Zasilanie: {state}")
        self._log_event("power_state", f"Zasilanie zewnętrzne: {state}")
        return f"SUKCES: Stan zasilania ustawiony na {state}."

if __name__ == "__main__":
    dsm = DeviceStateManager()
    print(">>> ZADANIE 7.3: ZARZĄDZANIE FIZYCZNYM STANEM URZĄDZENIA <<<")
    if os.path.exists("73_state.log"):
        os.remove("73_state.log")
    print(dsm.toggle_screen_orientation("LANDSCAPE"))
    print(dsm.toggle_screen_orientation("PORTRAIT"))
    print(dsm.simulate_power_connection(True))
    print(f"\n[OK] Zmiany zapisane w: 73_state.log")