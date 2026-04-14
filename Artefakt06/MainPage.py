from BasePage import BasePage

class MainPage(BasePage):
    """
    PAGE OBJECT (Layer 2): Reprezentuje konkretny ekran aplikacji.
    """
    def __init__(self):
        super().__init__()
        print("[MAIN_PAGE] Ekran główny zainicjalizowany.")

    def navigate_to_add_content(self):
        selector = self.find_id("ADD")
        if selector:
            return f"SUKCES: Wykonano kliknięcie w element UI o ID: '{selector}'"
        return "BŁĄD: Nie można nawigować - brak selektora 'ADD' w mapie!"

    def get_main_title_status(self):
        selector = self.find_id("TITLE")
        if selector:
            return f"SUKCES: Odnaleziono nagłówek strony (ID: {selector}). Status: Widoczny."
        return "INFORMACJA: Element 'TITLE' nie jest zdefiniowany dla tego ekranu."

    def perform_search_action(self, query):
        selector = self.find_id("SEARCH_BUTTON")
        if selector:
            return f"SUKCES: Wpisano '{query}' do pola {selector} i zatwierdzono."
        return "BŁĄD: Przycisk wyszukiwania nie został zmapowany."

if __name__ == "__main__":
    main_page = MainPage()
    print("-" * 30)
    print(main_page.navigate_to_add_content())
    print(main_page.get_main_title_status())
    print("-" * 30)