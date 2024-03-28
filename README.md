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

#### 3.4.1 Braki danych
jak je obsłużono
</br>

#### 3.4.2 Obserwacje odstające
jak je obsłużono (opis metod)
</br>

#### 3.4.3 Statystyki opisowe
(opis)

</br>

**Tabela 3.4.3.1** *Statystyki opisowe dla danych oryginalnych (braki danych usunięte) (2016 r.).* [(Excel, arkusz "Dane bez braków")](https://sggwpl-my.sharepoint.com/:x:/g/personal/s217265_sggw_edu_pl/EZshiO4QAhtBlzm-VUYfEjIByj867XJWS55VH2JokrfT3A?e=7NOE08&nav=MTVfezNFQzlCREU4LUQxMDUtNDQwRC1BQ0JELTE0RDE3N0ZEMkY0NX0)
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

**Tabela 3.4.3.2** *Statystyki opisowe dla danych po przybliżeniu wartości odstających wykrytych na boxplotach metodą winsoryzacji (2016 r.).* [(Excel, arkusz "Dane po winsoryzacji")](https://sggwpl-my.sharepoint.com/:x:/g/personal/s217265_sggw_edu_pl/EZshiO4QAhtBlzm-VUYfEjIByj867XJWS55VH2JokrfT3A?e=gnTRJm&nav=MTVfezlBQUFBRkVFLUM2NDktNDE2QS05QTJCLTRGREUwNDk2RjQzMH0)

| Statystyka   | Adolescent fertility rate (births per 1,000 women ages 15-19) | Fertility rate, total (births per woman) | Birth rate, crude (per 1,000 people) | Life expectancy at birth, total (years) | People using at least basic sanitation services (% of population) | Population growth (annual %) | Population, total | Death rate, crude (per 1,000 people) | Number of deaths ages 20-24 years | Number of stillbirths | Prevalence of hypertension (% of adults ages 30-79) |
|--------------|---------------------------------------------------------------|------------------------------------------|--------------------------------------|-----------------------------------------|-------------------------------------------------------------------|------------------------------|-------------------|--------------------------------------|-----------------------------------|-----------------------|-----------------------------------------------------|
| min          | 2,068                                                         | 1,172                                    | 7,800                                | 52,043                                  | 7,744                                                             | -2,217                       | 10852,000         | 1,344                                | 1,000                             | 3,000                 | 20,100                                              |
| max          | 161,898                                                       | 6,833                                    | 46,520                               | 83,985                                  | 100,000                                                           | 4,936                        | 69614543,000      | 13,913                               | 7737,875                          | 17083,000             | 56,500                                              |
| rozstęp      | 159,830                                                       | 5,661                                    | 38,720                               | 31,942                                  | 92,256                                                            | 7,154                        | 69603691,000      | 12,569                               | 7736,875                          | 17080,000             | 36,400                                              |
| średnia      | 50,832                                                        | 2,805                                    | 21,316                               | 71,548                                  | 74,849                                                            | 1,343                        | 19134624,242      | 7,706                                | 2114,667                          | 4684,656              | 37,727                                              |
| odch. Stand. | 40,709                                                        | 1,357                                    | 10,129                               | 7,707                                   | 28,046                                                            | 1,291                        | 22795634,848      | 2,640                                | 2730,801                          | 6242,382              | 6,506                                               |
| mediana      | 41,429                                                        | 2,308                                    | 18,942                               | 72,564                                  | 87,774                                                            | 1,227                        | 8946716,000       | 7,187                                | 681,000                           | 1216,000              | 38,150                                              |
| skośność     | 0,902                                                         | 1,021                                    | 0,596                                | -0,425                                  | -0,969                                                            | 0,130                        | 1,268             | 0,376                                | 1,206                             | 1,175                 | -0,103                                              |

</br>

**Tabela 3.4.3.2** *Statystyki opisowe dla danych po przybliżeniu wartości odstających wykrytych przez algorytm LOF (Local Outlier Factor) za pomocą algorytmu imputacji danych k-sąsiadów (k=5) (2016 r.).* [(Excel, arkusz "LOF outliers imputowane")](https://sggwpl-my.sharepoint.com/:x:/g/personal/s217265_sggw_edu_pl/EZshiO4QAhtBlzm-VUYfEjIByj867XJWS55VH2JokrfT3A?e=QdzOLB&nav=MTVfezJCOUIwRDhDLTZENTEtNEY3Ni1BQkMyLTUzN0NENDg0NkVEMX0)
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

#### 3.4.4 Podstawowa wizualizacja
(opis+ histogramy dla każdej cechy na danych z arkusza "Dane bez braków", boxploty i wykresy LOF wszystko na bazie "Dane bez braków" + odnośniki do kodów i folderów ze zdjęciami: tu można poglądowo wstawić po 2-3)

## 4. Opis metod porządkowania liniowego
| Metoda   | Cecha syntetyczna                                                | Pozostałe wzory                                                                   |
|----------|------------------------------------------------------------------|---------------------------------------------|
| Hellwiga | ![CodeCogsEqn](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/a6635f0b-60dd-4451-8b86-fd12a3a6339a) | ![CodeCogsEqn](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/e6326303-cf54-42c0-826c-e2f519385f41) ![CodeCogsEqn](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/e6128e4d-9421-4a90-8158-4cff8dffd18a) ![CodeCogsEqn](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/48e3a9c1-c3ca-4df7-8bb5-0e402760cf30) |






## 5. Rezultaty
wyniki: 
tabelarycznie + link do tabelki w Excelu
grafy porównawcze (tylko radar czy bar też?) + linki

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Wartości miernika syntetycznego (qi) oraz ranking (rank) przyporządkowane krajom (na danych przybliżanych metodą winsoryzacji) przez metody porządkowania liniowego (Hellwig, TOPSIS, TOPSIS (unitaryzacja), SWW, NOWAK, MUZ, STRAHL) zostały przedstawione w postaci tabelarycznej w tabeli 5.1. </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Wyświetlanie wyników ograniczono do krajów na pierwszych 10 pozcjach oraz 5 ostatnich pozycjach w danej metodzie. Pełne wyniki w postaci tabelarycznej znajdują się pod linkiem: [(Excel, arkusz "Porównanie państw")](https://sggwpl-my.sharepoint.com/:x:/g/personal/s217265_sggw_edu_pl/EZshiO4QAhtBlzm-VUYfEjIByj867XJWS55VH2JokrfT3A?e=aubdEd&nav=MTVfe0VEMUE0RDcyLUZGNDQtNDgxNi04QTQyLThFNTFFNzVBMEE4NX0) </br>

**Tabela 5.1** *Wartość miernika syntetycznego (qi) oraz ranking (rank) przyporządkowane krajom przez różne metody porządkowania liniowego (na danych przybliżanych metodą winsoryzacji*
</br>
| Jednostka terytorialna | qi     | Hellwig_rank | Jednostka terytorialna | qi    | TOPSIS_rank | Jednostka terytorialna | qi    | TOPSIS_uni_rank | Jednostka terytorialna | qi     | SSW_rank | Jednostka terytorialna | qi     | NOWAK_rank | Jednostka terytorialna | qi    | MUZ_rank | Jednostka terytorialna | qi    | STRAHL_rank |
|------------------------|--------|--------------|------------------------|-------|-------------|------------------------|-------|-----------------|------------------------|--------|----------|------------------------|--------|------------|------------------------|-------|----------|------------------------|-------|-------------|
| Solomon Islands        | 0,392  | 1            | Equatorial Guinea      | 0,656 | 1           | West Bank and Gaza     | 0,600 | 1               | Jordan                 | 0,548  | 1        | Equatorial Guinea      | 0,769  | 1          | West Bank and Gaza     | 0,268 | 1        | Equatorial Guinea      | 0,285 | 1           |
| West Bank and Gaza     | 0,384  | 2            | Jordan                 | 0,608 | 2           | Jordan                 | 0,590 | 2               | West Bank and Gaza     | 0,512  | 2        | Jordan                 | 0,635  | 2          | Jordan                 | 0,261 | 2        | Jordan                 | 0,273 | 2           |
| Zambia                 | 0,370  | 3            | Gabon                  | 0,594 | 3           | Equatorial Guinea      | 0,587 | 3               | Equatorial Guinea      | 0,476  | 3        | Oman                   | 0,622  | 3          | Equatorial Guinea      | 0,256 | 3        | Oman                   | 0,264 | 3           |
| Guatemala              | 0,369  | 4            | Oman                   | 0,593 | 4           | Israel                 | 0,578 | 4               | Maldives               | 0,468  | 4        | Gabon                  | 0,568  | 4          | Israel                 | 0,252 | 4        | West Bank and Gaza     | 0,261 | 4           |
| Jordan                 | 0,366  | 5            | Gambia, The            | 0,590 | 5           | Samoa                  | 0,575 | 5               | Oman                   | 0,462  | 5        | Qatar                  | 0,567  | 5          | Oman                   | 0,249 | 5        | Qatar                  | 0,244 | 5           |
| Malawi                 | 0,359  | 6            | Mauritania             | 0,583 | 6           | Oman                   | 0,572 | 6               | Israel                 | 0,462  | 6        | West Bank and Gaza     | 0,559  | 6          | Maldives               | 0,241 | 6        | Maldives               | 0,243 | 6           |
| Senegal                | 0,358  | 7            | Congo, Rep.            | 0,581 | 7           | Solomon Islands        | 0,570 | 7               | Solomon Islands        | 0,432  | 7        | Gambia, The            | 0,556  | 7          | Samoa                  | 0,238 | 7        | Bahrain                | 0,230 | 7           |
| Ecuador                | 0,358  | 8            | Zambia                 | 0,578 | 8           | Ecuador                | 0,570 | 8               | Qatar                  | 0,414  | 8        | Solomon Islands        | 0,556  | 8          | Qatar                  | 0,231 | 8        | Israel                 | 0,229 | 8           |
| Rwanda                 | 0,357  | 9            | Solomon Islands        | 0,575 | 9           | Maldives               | 0,564 | 9               | Ecuador                | 0,385  | 9        | Maldives               | 0,542  | 9          | Solomon Islands        | 0,229 | 9        | Samoa                  | 0,228 | 9           |
| Equatorial Guinea      | 0,353  | 10           | Mali                   | 0,574 | 10          | Panama                 | 0,563 | 10              | Bahrain                | 0,380  | 10       | Vanuatu                | 0,538  | 10         | Bahrain                | 0,228 | 10       | Kuwait                 | 0,228 | 10          |
| ...                    | ...    | ...          | ...                    | ...   | ...         | ...                    | ...   | ...             | ...                    | ...    | ...      | ...                    | ...    | ...        | ...                    | ...   | ...      | ...                    | ...   | ...         |
| Latvia                 | -0,038 | 182          | Russian Federation     | 0,387 | 182         | Moldova                | 0,425 | 182             | Serbia                 | -0,538 | 182      | Myanmar                | -0,047 | 182        | Myanmar                | 0,025 | 182      | Myanmar                | 0,040 | 182         |
| Croatia                | -0,038 | 183          | Bosnia and Herzegovina | 0,386 | 183         | Cote d'Ivoire          | 0,423 | 183             | Latvia                 | -0,553 | 183      | India                  | -0,055 | 183        | Moldova                | 0,023 | 183      | Moldova                | 0,034 | 183         |
| Serbia                 | -0,039 | 184          | Myanmar                | 0,385 | 184         | Russian Federation     | 0,409 | 184             | Russian Federation     | -0,579 | 184      | Russian Federation     | -0,065 | 184        | Lithuania              | 0,020 | 184      | South Africa           | 0,025 | 184         |
| Moldova                | -0,045 | 185          | Lithuania              | 0,382 | 185         | Myanmar                | 0,404 | 185             | Moldova                | -0,626 | 185      | South Africa           | -0,086 | 185        | Russian Federation     | 0,006 | 185      | Lithuania              | 0,024 | 185         |
| Lithuania              | -0,079 | 186          | Syrian Arab Republic   | 0,353 | 186         | South Africa           | 0,392 | 186             | Lithuania              | -0,648 | 186      | China                  | -0,099 | 186        | South Africa           | 0,002 | 186      | Russian Federation     | 0,019 | 186         |

</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Wartości miernika syntetycznego (qi) oraz ranking (rank) przyporządkowane krajom (na danych przybliżanych metodą k-sąsiadów) przez metody porządkowania liniowego (Hellwig, TOPSIS, TOPSIS (unitaryzacja), SWW, NOWAK, MUZ, STRAHL) zostały przedstawione w postaci tabelarycznej w tabeli 5.2. </br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Wyświetlanie wyników ograniczono do krajów na pierwszych 10 pozcjach oraz 5 ostatnich pozycjach w danej metodzie. Pełne wyniki w postaci tabelarycznej znajdują się pod linkiem: [(Excel, arkusz "Porównanie państw")](https://sggwpl-my.sharepoint.com/:x:/g/personal/s217265_sggw_edu_pl/EZshiO4QAhtBlzm-VUYfEjIByj867XJWS55VH2JokrfT3A?e=aubdEd&nav=MTVfe0VEMUE0RDcyLUZGNDQtNDgxNi04QTQyLThFNTFFNzVBMEE4NX0) </br>

**Tabela 5.2** *Wartość miernika syntetycznego (qi) oraz ranking (rank) przyporządkowane krajom przez różne metody porządkowania liniowego (na danych przybliżanych metodą k-sąsiadów (k=5)*
</br>

| Jednostka terytorialna | qi     | Hellwig_rank | Jednostka terytorialna | qi    | TOPSIS_rank | Jednostka terytorialna | qi    | TOPSIS_uni_rank | Jednostka terytorialna | qi     | SSW_rank | Jednostka terytorialna | qi     | NOWAK_rank | Jednostka terytorialna | qi     | MUZ_rank | Jednostka terytorialna | qi    | STRAHL_rank |
|------------------------|--------|--------------|------------------------|-------|-------------|------------------------|-------|-----------------|------------------------|--------|----------|------------------------|--------|------------|------------------------|--------|----------|------------------------|-------|-------------|
| Ethiopia               | 0,668  | 1            | Ethiopia               | 0,878 | 1           | Ethiopia               | 0,636 | 1               | Ethiopia               | 2,163  | 1        | Ethiopia               | 3,8617 | 1          | Ethiopia               | 0,329  | 1        | Ethiopia               | 0,742 | 1           |
| Korea, Rep.            | 0,206  | 2            | Equatorial Guinea      | 0,333 | 2           | Tanzania               | 0,540 | 2               | Korea, Rep.            | 0,578  | 2        | Equatorial Guinea      | 0,6359 | 2          | Tanzania               | 0,192  | 2        | Equatorial Guinea      | 0,266 | 2           |
| Solomon Islands        | 0,196  | 3            | Gabon                  | 0,323 | 3           | Korea, Rep.            | 0,529 | 3               | Israel                 | 0,496  | 3        | Gabon                  | 0,5792 | 3          | Korea, Rep.            | 0,178  | 3        | Gambia, The            | 0,261 | 3           |
| Vanuatu                | 0,188  | 4            | Solomon Islands        | 0,321 | 4           | Egypt, Arab Rep.       | 0,524 | 4               | Solomon Islands        | 0,481  | 4        | Korea, Rep.            | 0,5728 | 4          | Egypt, Arab Rep.       | 0,169  | 4        | Solomon Islands        | 0,258 | 4           |
| Gabon                  | 0,185  | 5            | Vanuatu                | 0,320 | 5           | Israel                 | 0,521 | 5               | Tanzania               | 0,472  | 5        | Gambia, The            | 0,5656 | 5          | Israel                 | 0,167  | 5        | West Bank and Gaza     | 0,257 | 5           |
| Israel                 | 0,184  | 6            | Nauru                  | 0,320 | 6           | Iran, Islamic Rep.     | 0,518 | 6               | Ecuador                | 0,434  | 6        | Solomon Islands        | 0,5647 | 6          | Iran, Islamic Rep.     | 0,161  | 6        | Gabon                  | 0,253 | 6           |
| West Bank and Gaza     | 0,183  | 7            | Gambia, The            | 0,319 | 7           | Zambia                 | 0,515 | 7               | Iran, Islamic Rep.     | 0,426  | 7        | Vanuatu                | 0,5478 | 7          | Zambia                 | 0,157  | 7        | Zambia                 | 0,249 | 7           |
| Panama                 | 0,182  | 8            | Korea, Rep.            | 0,318 | 8           | Solomon Islands        | 0,514 | 8               | Egypt, Arab Rep.       | 0,386  | 8        | Nauru                  | 0,5407 | 8          | Solomon Islands        | 0,154  | 8        | Israel                 | 0,248 | 8           |
| Samoa                  | 0,181  | 9            | France                 | 0,317 | 9           | Ecuador                | 0,511 | 9               | Zambia                 | 0,384  | 9        | Mauritania             | 0,5357 | 9          | Ecuador                | 0,151  | 9        | Mauritania             | 0,247 | 9           |
| Ecuador                | 0,179  | 10           | Sao Tome and Principe  | 0,317 | 10          | Uganda                 | 0,507 | 10              | West Bank and Gaza     | 0,362  | 10       | Sao Tome and Principe  | 0,5146 | 10         | Uganda                 | 0,147  | 10       | Vanuatu                | 0,245 | 10          |
| ...                    | ...    | ...          | ...                    | ...   | ...         | ...                    | ...   | ...             | ...                    | ...    | ...      | ...                    | ...    | ...        | ...                    | ...    | ...      | ...                    | ...   | ...         |
| Russian Federation     | 0,005  | 182          | Niger                  | 0,190 | 182         | Romania                | 0,321 | 182             | Latvia                 | -0,595 | 182      | Kenya                  | -0,241 | 182        | Romania                | -0,098 | 182      | Serbia                 | 0,041 | 182         |
| Mozambique             | 0,001  | 183          | United States          | 0,185 | 183         | Russian Federation     | 0,318 | 183             | Croatia                | -0,644 | 183      | United States          | -0,241 | 183        | Latvia                 | -0,102 | 183      | Croatia                | 0,041 | 183         |
| Uganda                 | -0,001 | 184          | Bangladesh             | 0,183 | 184         | Dominica               | 0,317 | 184             | Serbia                 | -0,670 | 184      | Bangladesh             | -0,318 | 184        | Croatia                | -0,110 | 184      | Bulgaria               | 0,035 | 184         |
| Philippines            | -0,002 | 185          | Philippines            | 0,181 | 185         | Bulgaria               | 0,311 | 185             | Bulgaria               | -0,696 | 185      | Philippines            | -0,384 | 185        | Serbia                 | -0,115 | 185      | Brazil                 | 0,027 | 185         |
| Brazil                 | -0,028 | 186          | Brazil                 | 0,162 | 186         | Latvia                 | 0,309 | 186             | Russian Federation     | -0,699 | 186      | Brazil                 | -0,455 | 186        | Bulgaria               | -0,122 | 186      | Russian Federation     | 0,009 | 186         |

</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Graficzne przedstawienie różnic w rankingach państw (zarówno na danych przybliżonych za pomocą metody winsoryzacji, jak również danych przybliżonych metodą k-sąsiadów) w postaci wykresów sieciowych (Obraz 5.1 oraz Obraz 5.2) oraz dla lepszego zilustrowania różnic w rankingach konkretnego kraju w postaci wykresów słupkowych (Wykres 5.1 oraz Wykres 5.2). </br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Wszystkie wykresy słupkowe są dostępne w folderze boxplot_bar: przykładowy link do wykresu: [boxplot_bar](Projekt/Porównania_analiz/Porównanie_rankingów_bar/boxplot_bar/porownanie_metod_bar_AFG-COD.jpg) oraz w folderze k_sasiadow_bar: przykładowy link do wykresu: [k_sasiadow_bar](Projekt/Porównania_analiz/Porównanie_rankingów_bar/k_sasiadow_bar/porownanie_metod_bar_k_sas_AFG-COD.jpg.jpg)</br>

## 6. Podsumowanie

## 7. Bibliografia
