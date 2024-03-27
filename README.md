# Analiza porównawcza metod porządkowania liniowego </br> (Hellwiga, TOPSIS, SSW, NOWAK, MUZ, STRAHL) </br> na przykładzie rankingu państw na świecie </br> względem wskaźników zdrowia

> [!IMPORTANT]
> Autorzy pracy: (dopisać numery indeksów) </br>
> Michał Adamiec, </br>
> Maciej Chaciński, 217421 </br> 
> Aleksandra Dowgwiłłowicz-Nowicka, 217265 </br>
> Krzysztof Federczyk, 217451

> [!TIP]
> Zestawienia rankingów państw według danej metody są zaprezentowane najczytelniej w odrębnych arkuszach pliku [Excel](https://sggwpl-my.sharepoint.com/:x:/g/personal/s217265_sggw_edu_pl/EZshiO4QAhtBlzm-VUYfEjIByj867XJWS55VH2JokrfT3A?e=Nk8kzL)

## 1. Streszczenie
(max. 150 słów)

### 1.1 Słowa kluczowe

## 2. Wprowadzenie

## 3. Przedmiot badania

### 3.1 Cel i zakres badania

### 3.2 Przegląd literatury

### 3.3 Zmienne wybrane do analizy

| Zmienna                                                      | Uzasadnienie | Typ zmiennej     |
|--------------------------------------------------------------|--------------|------------------|
| Adolescent fertility rate (births per 1000 women ages 15-19) | uzasadnienie | stymulanta (s)   |
| Fertility rate, total                                        | uzasadnienie | stymulanta (s)   |
| Birth rate, crude                                            | uzasadnienie | stymulanta (s)   |
| Life expectancy at birth total                               | uzasadnienie | stymulanta (s)   |
| People using at least basic sanitation services              | uzasadnienie | stymulanta (s)   |
| Population growth (annual)                                   | uzasadnienie | stymulanta (s)   |
| Population (total)                                           | uzasadnienie | stymulanta (s)   |
| Death rate                                                   | uzasadnienie | destymulanta (d) |
| Number of deats ages 20-24                                   | uzasadnienie | destymulanta (d) |
| Number of stillbirths                                        | uzasadnienie | destymulanta (d) |
| Prevalence of hypertension                                   | uzasadnienie | destymulanta (d) |

### 3.4 Wstępna analiza danych

#### 3.4.1 Statystyki opisowe
(opis)

**Tabela 3.4.1.1** *Statystyki opisowe dla danych oryginalnych (braki danych usunięte) (2016 r.).*
| Statystyka   | Adolescent fertility rate (births per 1,000 women ages 15-19) | Fertility rate, total (births per woman) | Birth rate, crude (per 1,000 people) | Life expectancy at birth, total (years) | People using at least basic sanitation services (% of population) | Population growth (annual %) | Population, total | Death rate, crude (per 1,000 people) | Number of deaths ages 20-24 years | Number of stillbirths | Prevalence of hypertension (% of adults ages 30-79) |
|--------------|---------------------------------------------------------------|------------------------------------------|--------------------------------------|-----------------------------------------|-------------------------------------------------------------------|------------------------------|-------------------|--------------------------------------|-----------------------------------|-----------------------|-----------------------------------------------------|
| min          | 2,068                                                         | 1,172                                    | 7,8                                  | 52,043                                  | 7,743550738                                                       | -2,21727979                  | 10852             | 0,991                                | 1                                 | 3                     | 20,1                                                |
| max          | 179,765                                                       | 7,141                                    | 46,52                                | 83,98487805                             | 100                                                               | 7,212802387                  | 1387790000        | 15,1                                 | 156890                            | 404242                | 56,5                                                |
| rozstęp      | 177,697                                                       | 5,969                                    | 38,72                                | 31,94187805                             | 92,25644926                                                       | 9,430082177                  | 1387779148        | 14,109                               | 156889                            | 404239                | 36,4                                                |
| średnia      | 50,98770968                                                   | 2,806572581                              | 21,31580498                          | 71,54811199                             | 74,84903874                                                       | 1,355429201                  | 39999575,22       | 7,721953574                          | 4082,564516                       | 11432,84409           | 37,72741935                                         |
| odch. Stand. | 41,16296971                                                   | 1,362969233                              | 10,12900459                          | 7,706538981                             | 28,046052                                                         | 1,334985504                  | 145827810,5       | 2,696201107                          | 13051,97551                       | 38588,95586           | 6,506383627                                         |
| mediana      | 41,429                                                        | 2,3075                                   | 18,942                               | 72,564                                  | 87,77381083                                                       | 1,226982794                  | 8946716           | 7,1865                               | 681                               | 1216                  | 38,15                                               |
| skośność     | 0,957144478                                                   | 1,043816803                              | 0,595751938                          | -0,42517569                             | -0,969103775                                                      | 0,447842372                  | 8,254867089       | 0,446480516                          | 9,210457463                       | 7,28667874            | -0,103417122                                        |

**Tabela 3.4.1.2** *Statystyki opisowe dla danych po przybliżeniu wartości odstających wykrytych na boxplotach metodą winsoryzacji (2016 r.).*

**Tabela 3.4.1.2** *Statystyki opisowe dla danych po przybliżeniu wartości odstających wykrytych przez algorytm LOF za pomocą algorytmu imputacji danych k-sąsiadów (k=5) (2016 r.).*

#### 3.4.2 Podstawowa wizualizacja

#### 3.4.3 Braki danych
jak je obsłużono

#### 3.4.5 Obserwacje odstające
jak je obsłużono

## 4. Opis metod porządkowania liniowego
| Metoda   | Cecha syntetyczna                                                | Pozostałe wzory                                                                   |
|----------|------------------------------------------------------------------|---------------------------------------------|
| Hellwiga | ![CodeCogsEqn](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/a6635f0b-60dd-4451-8b86-fd12a3a6339a) | ![CodeCogsEqn](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/e6326303-cf54-42c0-826c-e2f519385f41) ![CodeCogsEqn](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/e6128e4d-9421-4a90-8158-4cff8dffd18a) ![CodeCogsEqn](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/48e3a9c1-c3ca-4df7-8bb5-0e402760cf30) |






## 5. Rezultaty
wyniki: 
tabelarycznie + link do tabelki w Excelu
grafy porównawcze (tylko radar czy bar też?) + linki

| Jednostka terytorialna         | qi       | Rank |
|--------------------------------|----------|------|
| Equatorial Guinea              | 0,656257 | 1    |
| Jordan                         | 0,608104 | 2    |
| Gabon                          | 0,594027 | 3    |
| Oman                           | 0,593237 | 4    |
| Gambia, The                    | 0,59027  | 5    |
| Mauritania                     | 0,583321 | 6    |
| Congo, Rep.                    | 0,580974 | 7    |
| Zambia                         | 0,578213 | 8    |
| Solomon Islands                | 0,574824 | 9    |
| Mali                           | 0,574496 | 10   |
| ...                            | ...      | ...  |
| Moldova                        | 0,391241 | 180  |
| China                          | 0,387427 | 181  |
| Russian Federation             | 0,386575 | 182  |
| Bosnia and Herzegovina         | 0,386031 | 183  |
| Myanmar                        | 0,384622 | 184  |
| Lithuania                      | 0,381618 | 185  |
| Syrian Arab Republic           | 0,353429 | 186  |

## 6. Podsumowanie

## 7. Bibliografia
