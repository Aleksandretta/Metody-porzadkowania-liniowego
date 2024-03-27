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
/**Tabela 3.4.1.2** *Statystyki opisowe dla danych po przybliżeniu wartości odstających wykrytych na boxplotach metodą winsoryzacji (2016 r.).*
| Statystyka   | Adolescent fertility rate (births per 1,000 women ages 15-19) | Fertility rate, total (births per woman) | Birth rate, crude (per 1,000 people) | Life expectancy at birth, total (years) | People using at least basic sanitation services (% of population) | Population growth (annual %) | Population, total | Death rate, crude (per 1,000 people) | Number of deaths ages 20-24 years | Number of stillbirths | Prevalence of hypertension (% of adults ages 30-79) |
|--------------|---------------------------------------------------------------|------------------------------------------|--------------------------------------|-----------------------------------------|-------------------------------------------------------------------|------------------------------|-------------------|--------------------------------------|-----------------------------------|-----------------------|-----------------------------------------------------|
| min          | 2,068                                                         | 1,172                                    | 7,8                                  | 52,043                                  | 7,743550738                                                       | -2,21727979                  | 10852             | 0,991                                | 1                                 | 3                     | 20,1                                                |
| max          | 179,765                                                       | 7,141                                    | 46,52                                | 83,98487805                             | 100                                                               | 7,212802387                  | 1387790000        | 15,1                                 | 156890                            | 404242                | 56,5                                                |
| rozstęp      | 177,697                                                       | 5,969                                    | 38,72                                | 31,94187805                             | 92,25644926                                                       | 9,430082177                  | 1387779148        | 14,109                               | 156889                            | 404239                | 36,4                                                |
| średnia      | 50,98770968                                                   | 2,806572581                              | 21,31580498                          | 71,54811199                             | 74,84903874                                                       | 1,355429201                  | 39999575,22       | 7,721953574                          | 4082,564516                       | 11432,84409           | 37,72741935                                         |
| odch. Stand. | 41,16296971                                                   | 1,362969233                              | 10,12900459                          | 7,706538981                             | 28,046052                                                         | 1,334985504                  | 145827810,5       | 2,696201107                          | 13051,97551                       | 38588,95586           | 6,506383627                                         |
| kwartyl1     | 15,34375                                                      | 1,71575                                  | 12,20725                             | 65,698                                  | 52,54352814                                                       | 0,445033576                  | 2330618           | 6,05775                              | 149,75                            | 191,75                | 32,65                                               |
| kwartyl3     | 73,96525                                                      | 3,7625                                   | 30,01575                             | 77,48275                                | 97,44990752                                                       | 2,241527047                  | 29244188          | 9,2                                  | 3185                              | 6948,25               | 42,45                                               |
| IQR          | 58,6215                                                       | 2,04675                                  | 17,8085                              | 11,78475                                | 44,90637938                                                       | 1,79649347                   | 26913570          | 3,14225                              | 3035,25                           | 6756,5                | 9,8                                                 |
| wąs dolny    | -72,5885                                                      | -1,354375                                | -14,5055                             | 48,020875                               | -14,81604094                                                      | -2,249706629                 | -38039737         | 1,344375                             | -4403,125                         | -9943                 | 17,95                                               |
| wąs górny    | 161,8975                                                      | 6,832625                                 | 56,7285                              | 95,159875                               | 164,8094766                                                       | 4,936267252                  | 69614543          | 13,913375                            | 7737,875                          | 17083                 | 57,15                                               |
| skośność     | 0,976233558                                                   | 1,054962332                              | 0,611243063                          | -0,438287868                            | -0,989491871                                                      | 0,455759597                  | 8,232235261       | 0,449814176                          | 9,186130734                       | 7,266411803           | -0,093484399                                        | \

**Tabela 3.4.1.2** *Statystyki opisowe dla danych po przybliżeniu wartości odstających wykrytych przez algorytm LOF za pomocą algorytmu imputacji danych k-sąsiadów (k=5) (2016 r.).*
| Statystyka    | Adolescent fertility rate (births per 1,000 women ages 15-19) | Fertility rate, total (births per woman) | Birth rate, crude (per 1,000 people) | Life expectancy at birth, total (years) | People using at least basic sanitation services (% of population) | Population growth (annual %) | Population, total | Death rate, crude (per 1,000 people) | Number of deaths ages 20-24 years | Number of stillbirths | Prevalence of hypertension (% of adults ages 30-79) |
|---------------|---------------------------------------------------------------|------------------------------------------|--------------------------------------|-----------------------------------------|-------------------------------------------------------------------|------------------------------|-------------------|--------------------------------------|-----------------------------------|-----------------------|-----------------------------------------------------|
| min           | 2,068                                                         | 1,324                                    | 8,8                                  | 56,659                                  | 7,743551                                                          | -0,70138                     | 10852             | 4,343                                | -19311                            | -85633                | 24,9                                                |
| max           | 160,779                                                       | 5,587                                    | 43,411                               | 83,60244                                | 100                                                               | 3,586211                     | 105000000         | 15,1                                 | 12479                             | 28471                 | 48,7                                                |
| rozstęp       | 158,711                                                       | 4,263                                    | 34,611                               | 26,94344                                | 92,256449                                                         | 4,287591                     | 104989148         | 10,757                               | 31790                             | 114104                | 23,8                                                |
| średnia       | 49,79105269                                                   | 2,713312366                              | 21,39529855                          | 71,83783204                             | 73,96280898                                                       | 1,343703177                  | 15466464,17       | 8,042200887                          | 2026,996774                       | 4271,608602           | 37,59376344                                         |
| odch. Stand.  | 39,05085256                                                   | 1,158198397                              | 9,32073982                           | 7,072299561                             | 27,94420652                                                       | 1,009831637                  | 18380909,76       | 2,370031534                          | 3491,696278                       | 9694,38497            | 5,733529626                                         |
| mediana       | 41,429                                                        | 2,3535                                   | 19,592                               | 72,475                                  | 86,867615                                                         | 1,305626                     | 8730993           | 7,535                                | 583,5                             | 1150,5                | 37,65                                               |
| stara_mediana | 40,625                                                        | 2,261                                    | 18,972                               | 72,896                                  | 87,24000056                                                       | 1,226982794                  | 6974842,5         | 7,385                                | 518                               | 970,5                 | 38,1                                                |
| kwartyl1      | 15,34375                                                      | 1,74                                     | 12,9                                 | 66,01075                                | 51,9574925                                                        | 0,64146025                   | 2330618           | 6,501                                | 146,75                            | 187,75                | 33,325                                              |
| kwartyl3      | 71,994                                                        | 3,44925                                  | 29,6752                              | 77,2049625                              | 97,4335425                                                        | 2,07307225                   | 24071087,75       | 9,2                                  | 2469,85                           | 5906,25               | 41,775                                              |
| IQR           | 56,65025                                                      | 1,70925                                  | 16,7752                              | 11,1942125                              | 45,47605                                                          | 1,431612                     | 21740469,75       | 2,699                                | 2323,1                            | 5718,5                | 8,45                                                |
| wąs dolny     | -69,631625                                                    | -0,823875                                | -12,2628                             | 49,21943125                             | -16,2565825                                                       | -1,50595775                  | -30280086,63      | 2,4525                               | -3337,9                           | -8390                 | 20,65                                               |
| wąs górny     | 156,969375                                                    | 6,013125                                 | 54,838                               | 93,99628125                             | 165,6476175                                                       | 4,22049025                   | 56681792,38       | 13,2485                              | 5954,5                            | 14484                 | 54,45                                               |
| skośność      | 0,870638397                                                   | 0,784660455                              | 0,463994965                          | -0,233208993                            | -0,91731686                                                       | 0,13141879                   | 1,979169652       | 0,91879235                           | 0,123474901                       | -3,598365926          | -0,026218105                                        |

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
