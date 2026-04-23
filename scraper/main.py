import requests

def sprawdz_polaczenie():
    print("Próbuję połączyć się z serwerem...")
    # Używamy prostego API GitHub, które zwraca losowe cytaty
    url = "https://api.github.com/zen"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("--- SUKCES ---")
            print(f"Cytat od GitHub: {response.text}")
        else:
            print(f"Błąd! Kod statusu: {response.status_code}")
    except Exception as e:
        print(f"Błąd połączenia: {e}")

if __name__ == "__main__":
    sprawdz_polaczenie()