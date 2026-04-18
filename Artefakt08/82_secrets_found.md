# 🛡️ RAPORT ANALIZY WYCIEKÓW (SECRETS)
**Student:** Jan Kurczab  
**Indeks:** 87869  
**Data raportu:** 18-04-2026  

---

## 🛑 1. Trzy najbardziej groźne znaleziska (High Risk)
*Poniższe elementy wymagają natychmiastowej zmiany w kodzie źródłowym:*

1. **[URL_Endpoint]**  
   - *Uzasadnienie:* Wskazuje na jawny endpoint obecny w zasobach aplikacji.

2. **[Potential_Secret] -> `password`**  
   - *Uzasadnienie:* Sugeruje możliwość przechowywania hasła lub mechanizmu logowania w zasobach.

3. **[Potential_Secret] -> `token` / `secret` / podobne znalezione słowo**  
   - *Uzasadnienie:* Może wskazywać na twardo zakodowane dane autoryzacyjne.

## 🟢 2. Trzy znaleziska typu "False Positive" (Low/No Risk)
*Poniższe elementy zostały błędnie sklasyfikowane jako zagrożenie:*

1. **Standardowy URL testowy**
   - *Uzasadnienie:* Nie musi oznaczać wycieku, może być zwykłym adresem demonstracyjnym.

2. **Długi identyfikator zasobu UI**
   - *Uzasadnienie:* Pasuje do wzorca, ale nie jest sekretem.

3. **Nazwa systemowego zasobu**
   - *Uzasadnienie:* To element biblioteki lub interfejsu, a nie klucz bezpieczeństwa.

---

## 🎓 Wnioski końcowe
Automatyczne skanowanie RegEx jest skuteczne, ale wymaga manualnej weryfikacji inżyniera, ponieważ sam skrypt nie rozumie kontekstu biznesowego aplikacji.