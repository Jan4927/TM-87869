# 🛡️ AUDYT BEZPIECZEŃSTWA: MANIFEST SCANNER
**Status:** Wykonano automatyczną ekstrakcję ryzyka.

### 📝 1. Zawartość RiskyPermission.xml
Zidentyfikowano następujące wpisy krytyczne:
- **Debuggable:** `true` lub `false` — sprawdź wartość z wygenerowanego XML.
- **Permissions:** Wykryto uprawnienia dające dostęp do sieci (`INTERNET`) oraz inne wskazane przez parser.

### 🧠 2. Interpretacja Inżynierska
Z punktu widzenia bezpieczeństwa, najpoważniejszym problemem jest flaga `debuggable`, jeśli jest aktywna. Pozwala ona na użycie narzędzi debugujących do śledzenia procesów aplikacji przez osoby niepowołane.

### 🛠️ 3. Akcja korygująca
Zaleca się wdrożenie skryptu do procesu CI/CD, który będzie automatycznie blokował buildy, jeśli raport wykaże aktywną flagę debugowania lub obecność zbędnych ryzykownych uprawnień.

#### Raport wykonany przez:
**Podpis:** Jan Kurczab, 87869  
**Data:** 2026-04-18