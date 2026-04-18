# 📱 Mobile Automation & Cloud-Ready Testing Suite

**Prowadzący:** mgr Mariusz Dworniczak  
**Student:** Jan Kurczab  
**Numer Albumu:** 87869  

---

## 🏗️ Architektura Projektu
Projekt przedstawia pełny proces testowania aplikacji mobilnych: od przygotowania środowiska, przez analizę statyczną APK,
automatyzację w Pythonie, testy API, Appium, aż po raportowanie Allure i pipeline CI/CD.

**Główne technologie:**
- Python
- Appium
- Docker / Docker Compose
- Requests
- Pytest
- Allure
- MobSF
- ADB

---

## 📅 Przebieg laboratoriów

### 🔹 Blok 1: Środowisko i repozytorium
Przygotowanie środowiska pracy, struktury katalogów i pierwszego repozytorium Git.

### 🔹 Blok 2: ADB i analiza APK
Dekompilacja aplikacji, analiza zasobów i manifestu oraz przygotowanie danych wejściowych do dalszych testów.

### 🔹 Blok 3: Docker Compose i serwer Appium
Uruchomienie Appium w kontenerze i weryfikacja działania portu 4723.

### 🔹 Blok 4: Selektory i lokalizatory
Automatyczne wydobywanie ID z layoutów i tworzenie mapy elementów UI.

### 🔹 Blok 5: Pierwszy skrypt automatyczny
Budowa capabilities, analiza manifestu, mapa selektorów i pierwszy raport testowy.

### 🔹 Blok 6: Page Object Model
Rozdzielenie logiki testowej i warstwy dostępu do danych UI przez klasy BasePage i MainPage.

### 🔹 Blok 7: Gesty i przerwania
Symulacja gestów, połączeń przychodzących, zmian stanu urządzenia oraz synchronizacji.

### 🔹 Blok 8: Statyczna analiza bezpieczeństwa
Audyt manifestu, wykrywanie hardcoded secrets, analiza bibliotek i scoring ryzyka.

### 🔹 Blok 9: Testowanie API dla Mobile
Testy endpointów REST, operacje CRUD, walidacja kontraktu JSON, testy negatywne oraz integracja API + Appium.

### 🔹 Blok 10: Raportowanie i automatyzacja
Tworzenie raportów Allure, załączników, metadanych oraz pipeline uruchamianego jednym kliknięciem.

---

## 📊 Raportowanie Wyników
W projekcie wykorzystano Allure Report do prezentowania:
- kroków testowych,
- statusów Passed / Failed,
- załączników,
- metadanych środowiska,
- hierarchii Epic / Feature / Story.

---

## 🚀 Jak uruchomić projekt?
```bash
cd Artefakt10
python pipeline.py