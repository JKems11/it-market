import os
import requests

def wczytaj_technologie(sciezka_pliku):
    if os.path.exists(sciezka_pliku):
        with open(sciezka_pliku, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    return []

def analizuj_ogloszenie(tekst, technologie):
    print(f"\n--- Analiza ofert pod kątem {len(technologie)} technologii ---")
    znalezione = [tech for tech in technologie if tech.lower() in tekst.lower()]
    return znalezione

def pobierz_strone(url):
    try:
        odpowiedz = requests.get(url)
        
        if odpowiedz.status_code == 200:
            return odpowiedz.text
        else:
            print(f"Błąd: Serwer zwrócił kod {odpowiedz.status_code}")
            return None
    except Exception as e:
        print(f"Wystąpił problem z połączeniem: {e}")
        return None

def start_scraper():
    sciezka = os.path.join(os.getcwd(), 'keywords.txt')
    technologie = wczytaj_technologie(sciezka)
    
    
    url = "https://justjoin.it/"
    
    print(f"Łączę się z: {url}...")
    tresc_strony = pobierz_strone(url)
    
    if tresc_strony:
        print("Sukces! Pobrałem kod strony.")
    else:
        print("Nie udało się pobrać danych.")

if __name__ == "__main__":
    start_scraper()