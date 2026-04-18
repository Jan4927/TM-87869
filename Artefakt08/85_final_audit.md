# 🏦 RAPORT Z AUDYTU BEZPIECZEŃSTWA: APIDEMOS
**Data:** 2026-04-18  
**Audytor:** Jan Kurczab, 87869  
**Projekt:** Mobilny System Demonstracyjny (Android)

---

## 📊 1. OCENA KOŃCOWA (SECURITY SCORE)
**WYNIK:** 0/100  
**STATUS:** 🔴 REJECTED / NEEDS FIX

---

## 🛡️ 2. KLUCZOWE OBSZARY RYZYKA

### A. Konfiguracja Systemowa (Zadanie 8.1)
* **Problem:** Flaga `debuggable="true"` w Manifest.
* **Wpływ:** Umożliwia podpięcie debuggera i analizę działania aplikacji w czasie rzeczywistym.

### B. Wycieki Danych (Zadanie 8.2)
* **Problem:** Wykryto twardo zakodowane słowa kluczowe i potencjalne endpointy w zasobach.
* **Wpływ:** Ryzyko przejęcia danych testowych lub ujawnienia niepublicznych adresów.

### C. Biblioteki Zewnętrzne (Zadanie 8.3)
* **Problem:** Użycie `org.apache.commons` w wersji 1.0.0.
* **Wpływ:** Podatność krytyczna pozwalająca na zdalne wykonanie kodu.

---

## 📝 3. MAPA DROGOWA NAPRAWCZA (REMEDIATION)
1. **[PRIORYTET 1]:** Aktualizacja biblioteki `org.apache.commons` do bezpiecznej wersji.
2. **[PRIORYTET 1]:** Wyłączenie trybu debugowania w buildzie release.
3. **[PRIORYTET 2]:** Przeniesienie wrażliwych danych ze `strings.xml` do bezpiecznego magazynu.

---

## 🎓 WNIOSKI KOŃCOWE
Aplikacja w obecnym stanie nie powinna zostać opublikowana. Główne ryzyka wynikają z kombinacji błędnej konfiguracji manifestu, potencjalnych wycieków danych oraz nieaktualnych bibliotek zewnętrznych.