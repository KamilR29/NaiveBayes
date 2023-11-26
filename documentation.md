# Dokumentacja algorytmu Naive Bayes

## Opis algorytmu
Algorytm Naive Bayes jest modelem statystycznym wykorzystywanym w dziedzinie uczenia maszynowego i klasyfikacji. Jego działanie opiera się na regule Bayesa, która wykorzystuje prawdopodobieństwo warunkowe do przewidywania klasy danej próbki na podstawie cech tej próbki.

## Krok 1: Odczytanie danych
Funkcja `read_data()` wczytuje dane z pliku `car_evaluation.data` do pamięci.

## Krok 2: Podział danych na zbiór treningowy i testowy
Funkcja `split_data(lines, number)` dzieli odczytane dane na zbiory treningowy i testowy w stosunku 70% do 30%. Zmienna  `number`, pozwal an tworzenie kolejnych plikóe zawierających odpowiednio dane treningowe (`cars_evaluation_trn[number].data`) i dane testowe (`cars_evaluation_tst[number].data`).

## Krok 3: Implementacja algorytmu Naive Bayes
Funkcja `naive_bayes(trening_file, test_file)` implementuje algorytm Naive Bayes. Wczytuje dane z plików treningowych, oblicza odpowiednie prawdopodobieństwa dla każdej cechy w zależności od klasy, a następnie dokonuje klasyfikacji dla danych testowych na podstawie obliczonych prawdopodobieństw. W algorytmie występują 3 główne fragmenty: frgment odpowiedzialny zaznalezienie wszytkich klas wynikowych, zliczenie wystópień poszcególnych cech należacyh do danej klasy i fragment klasyfikujacy do danej klasy

## Krok 4: Obliczenie dokładności klasyfikacji
Po wykonaniu klasyfikacji dla 10 różnych podziałów danych, algorytm oblicza dokładność (accuracy) klasyfikacji dla każdego z podziałów. Na końcu oblicza średnią dokładność oraz odchylenie standardowe dla 10 prób klasyfikacji.

### Funkcje pomocnicze
- `write_result(result)`: Funkcja zapisuje wyniki do pliku o nazwie "result_file".

## Uruchomienie algorytmu
Główna część kodu wywołuje opisane funkcje dla 10 różnych podziałów danych, oblicza dokładność oraz prezentuje średnią dokładność i odchylenie standardowe wyników.

### Uwagi
1. Algorytm zakłada, że dane są zapisane w pliku 'car_evaluation.data' w określonym formacie.
2. Implementacja ma za zadanie klasyfikować dane dotyczące oceny samochodów do odpowiednich klas na podstawie cech.
3. Dokładność klasyfikacji oraz inne wyniki są zapisywane do pliku "result_file".
