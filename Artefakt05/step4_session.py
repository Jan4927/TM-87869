import json
import warnings
from urllib3.exceptions import NotOpenSSLWarning

warnings.filterwarnings("ignore", category=NotOpenSSLWarning)

def setup_integrated_session():
    print(">>> ZADANIE 5.4: INTEGRACJA ARTEFAKTÓW (STABLE BUILD) <<<")
    caps_path = "51_caps.json"
    selectors_path = "53_selectors.json"
    log_path = "54_session.log"

    try:
        with open(caps_path, 'r', encoding='utf-8') as f:
            caps_data = json.load(f)

        with open(selectors_path, 'r', encoding='utf-8') as f:
            ui_map = json.load(f)

        app_pkg = caps_data.get("appPackage") or caps_data.get("appium:appPackage")
        app_act = caps_data.get("appActivity") or caps_data.get("appium:appActivity")
        dev_name = caps_data.get("deviceName") or caps_data.get("appium:deviceName")

        if not app_pkg or not app_act:
            status_msg = "FAILED: Missing appPackage or appActivity in JSON!"
            color = "\033[91m"
        else:
            status_msg = "READY TO CONNECT"
            color = "\033[92m"

        session_info = (
            "=== ARTEFAKT 5.4: SESSION READINESS REPORT ===\n"
            f"Target App    : {app_pkg}\n"
            f"Main Activity : {app_act}\n"
            f"Device        : {dev_name}\n"
            f"UI Elements   : {len(ui_map['selectors'])} loaded\n"
            f"Status        : {status_msg}"
        )

        print(color + session_info + "\033[0m")

        with open(log_path, "w", encoding="utf-8") as f:
            f.write(session_info)

    except Exception as e:
        print(f"\033[91mBŁĄD KRYTYCZNY: {e}\033[0m")

if __name__ == "__main__":
    setup_integrated_session()