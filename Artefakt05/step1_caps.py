import os
import json
import xml.etree.ElementTree as ET

ANDROID_NS = "{http://schemas.android.com/apk/res/android}"

def discover_caps():
    print(">>> ZADANIE 5.1: CAPABILITIES DISCOVERY <<<")

    manifest_path = "../Artefakt02/decompiled_apk/AndroidManifest.xml"
    output_path = "51_caps.json"

    if not os.path.exists(manifest_path):
        print(f"BŁĄD: Nie znaleziono manifestu: {manifest_path}")
        return

    tree = ET.parse(manifest_path)
    root = tree.getroot()

    package_name = root.attrib.get("package")
    launchable_activity = None

    app_node = root.find("application")
    if app_node is not None:
        for activity in app_node.findall("activity"):
            has_main = False
            has_launcher = False

            for intent_filter in activity.findall("intent-filter"):
                actions = [
                    a.attrib.get(ANDROID_NS + "name")
                    for a in intent_filter.findall("action")
                ]
                categories = [
                    c.attrib.get(ANDROID_NS + "name")
                    for c in intent_filter.findall("category")
                ]

                if "android.intent.action.MAIN" in actions:
                    has_main = True
                if "android.intent.category.LAUNCHER" in categories:
                    has_launcher = True

            if has_main and has_launcher:
                launchable_activity = activity.attrib.get(ANDROID_NS + "name")
                break

    caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "emulator-5554",
        "appPackage": package_name,
        "appActivity": launchable_activity
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(caps, f, indent=4, ensure_ascii=False)

    print(f"Sukces! Wykryto: {package_name} / {launchable_activity}")
    print(f"[OK] Zapisano plik: {output_path}")

if __name__ == "__main__":
    discover_caps()