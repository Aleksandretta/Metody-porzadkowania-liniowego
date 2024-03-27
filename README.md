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
| min          | 2,068                                                         | 1,172                                    | 7,800                                | 52,043                                  | 7,744                                                             | -2,217                       | 10852,000         | 0,991                                | 1,000                             | 3,000                 | 20,100                                              |
| max          | 179,765                                                       | 7,141                                    | 46,520                               | 83,985                                  | 100,000                                                           | 7,213                        | 1387790000,000    | 15,100                               | 156890,000                        | 404242,000            | 56,500                                              |
| rozstęp      | 177,697                                                       | 5,969                                    | 38,720                               | 31,942                                  | 92,256                                                            | 9,430                        | 1387779148,000    | 14,109                               | 156889,000                        | 404239,000            | 36,400                                              |
| średnia      | 50,988                                                        | 2,807                                    | 21,316                               | 71,548                                  | 74,849                                                            | 1,355                        | 39999575,215      | 7,722                                | 4082,565                          | 11432,844             | 37,727                                              |
| odch. Stand. | 41,163                                                        | 1,363                                    | 10,129                               | 7,707                                   | 28,046                                                            | 1,335                        | 145827810,477     | 2,696                                | 13051,976                         | 38588,956             | 6,506                                               |
| mediana      | 41,429                                                        | 2,308                                    | 18,942                               | 72,564                                  | 87,774                                                            | 1,227                        | 8946716,000       | 7,187                                | 681,000                           | 1216,000              | 38,150                                              |
| skośność     | 0,957                                                         | 1,044                                    | 0,596                                | -0,425                                  | -0,969                                                            | 0,448                        | 8,255             | 0,446                                | 9,210                             | 7,287                 | -0,103                                              |
</br>

**Tabela 3.4.1.2** *Statystyki opisowe dla danych po przybliżeniu wartości odstających wykrytych na boxplotach metodą winsoryzacji (2016 r.).*

| Statystyka   | Adolescent fertility rate (births per 1,000 women ages 15-19) | Fertility rate, total (births per woman) | Birth rate, crude (per 1,000 people) | Life expectancy at birth, total (years) | People using at least basic sanitation services (% of population) | Population growth (annual %) | Population, total | Death rate, crude (per 1,000 people) | Number of deaths ages 20-24 years | Number of stillbirths | Prevalence of hypertension (% of adults ages 30-79) |
|--------------|---------------------------------------------------------------|------------------------------------------|--------------------------------------|-----------------------------------------|-------------------------------------------------------------------|------------------------------|-------------------|--------------------------------------|-----------------------------------|-----------------------|-----------------------------------------------------|
| min          | 2,068                                                         | 1,172                                    | 7,800                                | 52,043                                  | 7,744                                                             | -2,217                       | 10852,000         | 0,991                                | 1,000                             | 3,000                 | 20,100                                              |
| max          | 179,765                                                       | 7,141                                    | 46,520                               | 83,985                                  | 100,000                                                           | 7,213                        | 1387790000,000    | 15,100                               | 156890,000                        | 404242,000            | 56,500                                              |
| rozstęp      | 177,697                                                       | 5,969                                    | 38,720                               | 31,942                                  | 92,256                                                            | 9,430                        | 1387779148,000    | 14,109                               | 156889,000                        | 404239,000            | 36,400                                              |
| średnia      | 50,988                                                        | 2,807                                    | 21,316                               | 71,548                                  | 74,849                                                            | 1,355                        | 39999575,215      | 7,722                                | 4082,565                          | 11432,844             | 37,727                                              |
| odch. Stand. | 41,163                                                        | 1,363                                    | 10,129                               | 7,707                                   | 28,046                                                            | 1,335                        | 145827810,477     | 2,696                                | 13051,976                         | 38588,956             | 6,506                                               |
| kwartyl1     | 15,344                                                        | 1,716                                    | 12,207                               | 65,698                                  | 52,544                                                            | 0,445                        | 2330618,000       | 6,058                                | 149,750                           | 191,750               | 32,650                                              |
| kwartyl3     | 73,965                                                        | 3,763                                    | 30,016                               | 77,483                                  | 97,450                                                            | 2,242                        | 29244188,000      | 9,200                                | 3185,000                          | 6948,250              | 42,450                                              |
| IQR          | 58,622                                                        | 2,047                                    | 17,809                               | 11,785                                  | 44,906                                                            | 1,796                        | 26913570,000      | 3,142                                | 3035,250                          | 6756,500              | 9,800                                               |
| wąs dolny    | -72,589                                                       | -1,354                                   | -14,506                              | 48,021                                  | -14,816                                                           | -2,250                       | -38039737,000     | 1,344                                | -4403,125                         | -9943,000             | 17,950                                              |
| wąs górny    | 161,898                                                       | 6,833                                    | 56,729                               | 95,160                                  | 164,809                                                           | 4,936                        | 69614543,000      | 13,913                               | 7737,875                          | 17083,000             | 57,150                                              |
| skośność     | 0,976                                                         | 1,055                                    | 0,611                                | -0,438                                  | -0,989                                                            | 0,456                        | 8,232             | 0,450                                | 9,186                             | 7,266                 | -0,093                                              |
</br>

**Tabela 3.4.1.2** *Statystyki opisowe dla danych po przybliżeniu wartości odstających wykrytych przez algorytm LOF za pomocą algorytmu imputacji danych k-sąsiadów (k=5) (2016 r.).*
| Statystyka    | Adolescent fertility rate (births per 1,000 women ages 15-19) | Fertility rate, total (births per woman) | Birth rate, crude (per 1,000 people) | Life expectancy at birth, total (years) | People using at least basic sanitation services (% of population) | Population growth (annual %) | Population, total | Death rate, crude (per 1,000 people) | Number of deaths ages 20-24 years | Number of stillbirths | Prevalence of hypertension (% of adults ages 30-79) |
|---------------|---------------------------------------------------------------|------------------------------------------|--------------------------------------|-----------------------------------------|-------------------------------------------------------------------|------------------------------|-------------------|--------------------------------------|-----------------------------------|-----------------------|-----------------------------------------------------|
| min           | 2,068                                                         | 1,324                                    | 8,800                                | 56,659                                  | 7,744                                                             | -0,701                       | 10852,000         | 4,343                                | -19311,000                        | -85633,000            | 24,900                                              |
| max           | 160,779                                                       | 5,587                                    | 43,411                               | 83,602                                  | 100,000                                                           | 3,586                        | 105000000,000     | 15,100                               | 12479,000                         | 28471,000             | 48,700                                              |
| rozstęp       | 158,711                                                       | 4,263                                    | 34,611                               | 26,943                                  | 92,256                                                            | 4,288                        | 104989148,000     | 10,757                               | 31790,000                         | 114104,000            | 23,800                                              |
| średnia       | 49,791                                                        | 2,713                                    | 21,395                               | 71,838                                  | 73,963                                                            | 1,344                        | 15466464,172      | 8,042                                | 2026,997                          | 4271,609              | 37,594                                              |
| odch. Stand.  | 39,051                                                        | 1,158                                    | 9,321                                | 7,072                                   | 27,944                                                            | 1,010                        | 18380909,759      | 2,370                                | 3491,696                          | 9694,385              | 5,734                                               |
| mediana       | 41,429                                                        | 2,354                                    | 19,592                               | 72,475                                  | 86,868                                                            | 1,306                        | 8730993,000       | 7,535                                | 583,500                           | 1150,500              | 37,650                                              |
| stara_mediana | 40,625                                                        | 2,261                                    | 18,972                               | 72,896                                  | 87,240                                                            | 1,227                        | 6974842,500       | 7,385                                | 518,000                           | 970,500               | 38,100                                              |
| kwartyl1      | 15,344                                                        | 1,740                                    | 12,900                               | 66,011                                  | 51,957                                                            | 0,641                        | 2330618,000       | 6,501                                | 146,750                           | 187,750               | 33,325                                              |
| kwartyl3      | 71,994                                                        | 3,449                                    | 29,675                               | 77,205                                  | 97,434                                                            | 2,073                        | 24071087,750      | 9,200                                | 2469,850                          | 5906,250              | 41,775                                              |
| IQR           | 56,650                                                        | 1,709                                    | 16,775                               | 11,194                                  | 45,476                                                            | 1,432                        | 21740469,750      | 2,699                                | 2323,100                          | 5718,500              | 8,450                                               |
| wąs dolny     | -69,632                                                       | -0,824                                   | -12,263                              | 49,219                                  | -16,257                                                           | -1,506                       | -30280086,625     | 2,453                                | -3337,900                         | -8390,000             | 20,650                                              |
| wąs górny     | 156,969                                                       | 6,013                                    | 54,838                               | 93,996                                  | 165,648                                                           | 4,220                        | 56681792,375      | 13,249                               | 5954,500                          | 14484,000             | 54,450                                              |
| skośność      | 0,871                                                         | 0,785                                    | 0,464                                | -0,233                                  | -0,917                                                            | 0,131                        | 1,979             | 0,919                                | 0,123                             | -3,598                | -0,026                                              |

</br>

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
