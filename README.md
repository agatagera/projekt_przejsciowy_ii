# Steam Games - analiza danych
Repozytorium zawiera projekt zaliczeniowy realizowany w ramach zajęć.

## Wykorzystany zbiór danych 

https://www.kaggle.com/datasets/nikdavis/steam-store-games/data

Zbiór zawiera informacje o kilku tysiącach gier dostępnych na Steam, m.in.:
- nazwa gry
- data wydania
- gatunki
- cena
- developer
- publisher
- liczba pozytywnych i negatywnych recenzji
- średni czas gry

---

## Przygotowanie danych

Na potrzeby projektu wykonano proces **oczyszczania danych**, który obejmował:
- usunięcie brakujących lub niepoprawnych dat wydania
- uzupełnienie braków w kolumnach `developer` i `publisher`
- wybór kluczowych kolumn do dalszej analizy
- konwersję dat do formatu `datetime`
- utworzenie dodatkowych zmiennych:
  - `release_year`
  - `total_reviews`
  - `user_score`

## Wykorzystane technologie

- **pandas** – wczytywanie, czyszczenie oraz analiza danych tabelarycznych  
- **Path (pathlib)** – obsługa ścieżek do plików w sposób niezależny od systemu  
- **kagglehub** – pobieranie zbioru danych bezpośrednio z platformy Kaggle  
- **os** – operacje na plikach i katalogach (tworzenie folderów, ścieżki)  
- **matplotlib** – tworzenie wykresów i wizualizacji danych  
- **streamlit** – budowa interaktywnego dashboardu analitycznego

##Uruchomienie projektu

1. Zainstaluj wymagane biblioteki:
```bash
pip install -r requirements.txt
```
2. Uruchom aplikację Streamlit:
```
python -m streamlit run "https://github.com/agatagera/projekt_przejsciowy_ii/blob/main/app.py"
```
3. Dashboard będzie dostępny w przeglądarce pod adresem:
```
http://localhost:8501
```

