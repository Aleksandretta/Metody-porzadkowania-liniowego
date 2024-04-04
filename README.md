# Analiza porównawcza metod porządkowania liniowego </br> (Hellwiga, TOPSIS, SSW, NOWAK, MUZ, STRAHL) </br> na przykładzie rankingu państw na świecie </br> względem wskaźników zdrowia

> [!IMPORTANT]
> Autorzy pracy: </br>
> Michał Adamiec, 217633 </br>
> Maciej Chaciński, 217421 </br> 
> Aleksandra Dowgwiłłowicz-Nowicka, 217265 </br>
> Krzysztof Federczyk, 217451

> [!TIP]
> Zestawienia rankingów państw według danej metody są zaprezentowane najczytelniej w odrębnych arkuszach pliku [Excel](https://sggwpl-my.sharepoint.com/:x:/g/personal/s217265_sggw_edu_pl/EZshiO4QAhtBlzm-VUYfEjIByj867XJWS55VH2JokrfT3A?e=Nk8kzL)

## 1. Streszczenie
(max. 150 słów)

#### Słowa kluczowe: 

## 2. Wprowadzenie

## 3. Przedmiot badania

### 3.1 Cel i zakres badania
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Celem badania jest opracowanie rankingów krajów na świecie oraz jednostek terytorialnych (wysp, archipelagów itd.) oraz porównanie ich ze sobą na podstawie różnych wskaźników zdrowia, demografii i warunków sanitarnych, wykorzystując metody porządkowania liniowego, takie jak metoda Hellwiga, TOPSIS, STRAHL, SSW, Pozycyjna.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Zakres badania obejmuje analizę danych z <a href="https://data.worldbank.org/" target="_blank">The World Bank</a>, z bazy danych: <a href="https://databank.worldbank.org/source/health-nutrition-and-population-statistics" target="_blank">Health, Nutrition and Population</a>, z 2016 roku.
</br>

### 3.2 Przegląd literatury

### 3.3 Zmienne wybrane do analizy
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Analiza merytoryczna, kierowana ekonomicznością (koszt zebrania informacji) i interpretowalnością danych, obejmowała ocenę znaczenia poszczególnych wskaźników w kontekście oceny stanu zdrowia, demografii i warunków sanitarnych w poszczególnych państwach. Wybierane były te cechy, które były istotne dla tego obszaru badawczego, takie jak wskaźniki dzietności, wskaźniki umieralności, czy wskaźniki dostępu do podstawowych usług sanitarnych. Dodatkowo, analizowano statystyczną zmienność cech, przyjmując minimalne kryteria współczynnika zmienności (co najmniej 0,1) oraz ilorazu skrajnych wartości (co najmniej 2), aby zapewnić reprezentatywność danych. (do policzenia) 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Zastosowano kryterium statystyczne, koncentrując się na cechach charakteryzujących się odpowiednią zmiennością (do policzenia) w celu zapewnienia zróżnicowania analizy. Te działania miały na celu zapewnienie kompleksowej oceny i porównania państw pod kątem różnych aspektów. 
</br>

| Zmienna                                                      | Uzasadnienie | Typ zmiennej     |
|--------------------------------------------------------------|--------------|------------------|
| Birth rate, crude                                            | Liczba urodzeń informuje o liczbie urodzeń w populacji i jest kluczowym miernikiem dynamiki demograficznej. | stymulanta (s)   |
| Life expectancy at birth total                               | Przewidywana długość życia jest istotnym wskaźnikiem zdrowia i jakości życia w społeczeństwie. Wysoka przewidywana długość życia świadczy o skuteczności systemu opieki zdrowotnej oraz poziomie rozwoju społecznego i ekonomicznego. | stymulanta (s)   |
| People using at least basic sanitation services              | Dostęp do podstawowych usług sanitarnych ma kluczowe znaczenie dla zapobiegania chorobom związanym z brakiem higieny. Poprawa tego wskaźnika może przyczynić się do poprawy zdrowia i jakości życia mieszkańców oraz zmniejszenia obciążenia systemu opieki zdrowotnej. | stymulanta (s)   |
| Population growth (annual)                                   | Tempo wzrostu populacji ma istotny wpływ na zrównoważony rozwój społeczno-gospodarczy oraz wykorzystanie zasobów naturalnych. | stymulanta (s)   |
| Death rate                                                   | Śmiertelność ogólna informuje o liczbie zgonów w populacji i jest istotnym miernikiem stanu zdrowia i efektywności systemu opieki zdrowotnej. | destymulanta (d) |
| Number of deats ages 20-24                                   | Liczba zgonów w młodym wieku może świadczyć o istniejących zagrożeniach zdrowotnych oraz skuteczności działań prewencyjnych i leczniczych, a także o stabilności społecznej. | destymulanta (d) |
| Number of stillbirths                                        | Liczba martwych urodzeń jest istotnym miernikiem opieki zdrowotnej matki i dziecka podczas ciąży oraz porodu, a także jakości opieki prenatalnej. | destymulanta (d) |
| Prevalence of hypertension                                   | Intensywność występowania nadciśnienia tętniczego jest istotnym wskaźnikiem zdrowia oraz efektywności systemu opieki zdrowotnej w profilaktyce i leczeniu chorób układu sercowo-naczyniowego. | destymulanta (d) |

### 3.4 Wstępna analiza danych

#### 3.4.1 Braki danych
~14% oryginalnych danych (30 na 217 państw) stanowiły braki danych.
Metodą ich obsłużenia było usunięcie.
</br>

#### 3.4.2 Obserwacje odstające
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Winsoryzacja to metoda przetwarzania danych mająca na celu zmniejszenie wpływu wartości odstających na analizę statystyczną. Proces ten polega na zastępowaniu skrajnych wartości (najniższych i najwyższych) wartościami mniej ekstremalnymi. W typowym podejściu wykorzystuje się boxploty do identyfikacji wartości odstających, gdzie wąsy boxplota określają granice. Wartości leżące poza wąsami są uważane za odstające i są zastępowane wartościami na krańcach wąsów lub innymi wartościami bliskimi granicy rozkładu. Procedura ta pomaga w ograniczeniu wpływu ekstremalnych obserwacji na wyniki analizy, zachowując jednocześnie rozmiar próby. </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Wykres 3.4.2.1 ilustruje obserwacje odstające wykryte przy użyciu wykresów pudełkowych dla zmiennej Death rate, crude (per 1,000 people). Wszystkie wykresy są dostępne w folderze: [Boxploty](Projekt/Początkowa_obróbka_danych/Boxploty). Wyniki zastąpienia obserwacji odstających metodą winsoryzacji w postaci tabelarycznej są dostępne w arkuszu: [(Excel, arkusz "Dane po winsoryzacji")](https://sggwpl-my.sharepoint.com/:x:/g/personal/s217265_sggw_edu_pl/EZshiO4QAhtBlzm-VUYfEjIByj867XJWS55VH2JokrfT3A?e=gnTRJm&nav=MTVfezlBQUFBRkVFLUM2NDktNDE2QS05QTJCLTRGREUwNDk2RjQzMH0)

**Wykres 3.4.2.1** *Obserwacje odstające wykryte przy pomocy wykresu pudełkowego dla cechy Death rate, crude (per 1,000 people)*
![Death rate, crude (per 1,000 people)_boxplot](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/fdf61b6a-a171-4077-8720-7353db38ab43)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Algorytm LOF (Local Outlier Factor) służy do wykrywania obserwacji odstających w danych. Działa poprzez porównanie lokalnej gęstości danej obserwacji z lokalną gęstością jej sąsiadów. Obserwacje o znacząco niższej gęstości niż ich sąsiedzi są uznawane za odstające. Wartość LOF bliska 1 oznacza obserwację typową, natomiast wartości znacząco większe od 1 wskazują na obserwacje odstające. </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Wykres 3.4.2.2 ilustruje obserwacje odstające wykryte przez algorytm LOF dla zmiennej Population growth (annual %). Wszystkie wykresy są dostępne w folderze: [Local_Outlier_Factor](Projekt/Początkowa_obróbka_danych/Local_Outlier_Factor). Wyniki w postaci tabelarycznej są dostępne w arkuszu: [(Excel, arkusz "LOF outliers")](https://sggwpl-my.sharepoint.com/:x:/r/personal/s217265_sggw_edu_pl/_layouts/15/Doc.aspx?sourcedoc=%7BEE88219B-0210-411B-9739-BE55461F1232%7D&file=2_Poziom%20zdrowia%20na%20świecie.xlsx&action=default&mobileredirect=true&DefaultItemOpen=1)

**Wykres 3.4.2.2** *Obserwacje odstające wykryte przez algorytm LOF dla cechy Population growth (annual %).*
![Population growth (annual %)_outliers](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/6419b139-dd0b-49cd-a06f-920900ebbbb3)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Algorytm imputacji k-sąsiadów (k-NN imputation) wykorzystuje informacje z k najbliższych sąsiadów obserwacji do uzupełnienia brakujących danych. Dla każdej obserwacji z brakującymi wartościami, algorytm znajduje k najbliższych sąsiadów (opartych na dostępnych cechach) i uzupełnia brakujące wartości na podstawie wartości tych sąsiadów. W tym przypadku, k=5 zostało wybrane jako optymalna liczba sąsiadów, zapewniająca dobry kompromis między dokładnością a złożonością obliczeniową.

[(Excel, arkusz "LOF outliers imputowane")](https://sggwpl-my.sharepoint.com/:x:/g/personal/s217265_sggw_edu_pl/EZshiO4QAhtBlzm-VUYfEjIByj867XJWS55VH2JokrfT3A?e=QdzOLB&nav=MTVfezJCOUIwRDhDLTZENTEtNEY3Ni1BQkMyLTUzN0NENDg0NkVEMX0)




#### 3.4.3 Statystyki opisowe
(opis)

</br>

**Tabela 3.4.3.1** *Statystyki opisowe dla danych oryginalnych (braki danych usunięte) (2016 r.).* [(Excel, arkusz "Dane bez braków")](https://sggwpl-my.sharepoint.com/:x:/g/personal/s217265_sggw_edu_pl/EZshiO4QAhtBlzm-VUYfEjIByj867XJWS55VH2JokrfT3A?e=7NOE08&nav=MTVfezNFQzlCREU4LUQxMDUtNDQwRC1BQ0JELTE0RDE3N0ZEMkY0NX0)
| Statystyka   | Birth rate, crude (per 1,000 people) | Life expectancy at birth, total (years) | People using at least basic sanitation services (% of population) | Population growth (annual %) | Death rate, crude (per 1,000 people) | Number of deaths ages 20-24 years | Number of stillbirths | Prevalence of hypertension (% of adults ages 30-79) |
|--------------|--------------------------------------|-----------------------------------------|-------------------------------------------------------------------|------------------------------|--------------------------------------|-----------------------------------|-----------------------|-----------------------------------------------------|
| min          | 7,800                                | 52,043                                  | 7,744                                                             | -2,217                       | 0,991                                | 1,000                             | 3,000                 | 20,100                                              |
| max          | 46,520                               | 83,985                                  | 100,000                                                           | 7,213                        | 15,100                               | 156890,000                        | 404242,000            | 56,500                                              |
| rozstęp      | 38,720                               | 31,942                                  | 92,256                                                            | 9,430                        | 14,109                               | 156889,000                        | 404239,000            | 36,400                                              |
| średnia      | 21,316                               | 71,548                                  | 74,849                                                            | 1,355                        | 7,722                                | 4082,565                          | 11432,844             | 37,727                                              |
| odch. Stand. | 10,129                               | 7,707                                   | 28,046                                                            | 1,335                        | 2,696                                | 13051,976                         | 38588,956             | 6,506                                               |
| mediana      | 18,942                               | 72,564                                  | 87,774                                                            | 1,227                        | 7,187                                | 681,000                           | 1216,000              | 38,150                                              |
| skośność     | 0,596                                | -0,425                                  | -0,969                                                            | 0,448                        | 0,446                                | 9,210                             | 7,287                 | -0,103                                              |
</br>

**Tabela 3.4.3.2** *Statystyki opisowe dla danych po przybliżeniu wartości odstających wykrytych na boxplotach metodą winsoryzacji (2016 r.) oraz zamianie dwóch destymulant na stosunki względem populacji danego kraju.* [(Excel, arkusz "Dane po winsoryzacji")](https://sggwpl-my.sharepoint.com/:x:/g/personal/s217265_sggw_edu_pl/EZshiO4QAhtBlzm-VUYfEjIByj867XJWS55VH2JokrfT3A?e=gnTRJm&nav=MTVfezlBQUFBRkVFLUM2NDktNDE2QS05QTJCLTRGREUwNDk2RjQzMH0)

| Statystyka   | Birth rate, crude (per 1,000 people) | Life expectancy at birth, total (years) | People using at least basic sanitation services (% of population) | Population growth (annual %) | Death rate, crude (per 1,000 people) | Number of deaths ages 20-24 years | Number of stillbirths | Prevalence of hypertension (% of adults ages 30-79) |
|--------------|--------------------------------------|-----------------------------------------|-------------------------------------------------------------------|------------------------------|--------------------------------------|-----------------------------------|-----------------------|-----------------------------------------------------|
| min          | 7,800                                | 52,043                                  | 7,744                                                             | -2,217                       | 1,344                                | 0,000013                          | 0,000                 | 20,100                                              |
| max          | 46,520                               | 83,985                                  | 100,000                                                           | 4,936                        | 13,913                               | 0,000461                          | 0,001                 | 56,500                                              |
| rozstęp      | 38,720                               | 31,942                                  | 92,256                                                            | 7,154                        | 12,569                               | 0,000448                          | 0,001                 | 36,400                                              |
| średnia      | 21,316                               | 71,548                                  | 74,849                                                            | 1,343                        | 7,706                                | 0,000119                          | 0,000                 | 37,727                                              |
| odch. Stand. | 10,129                               | 7,707                                   | 28,046                                                            | 1,291                        | 2,640                                | 0,000096                          | 0,000                 | 6,506                                               |
| mediana      | 18,942                               | 72,564                                  | 87,774                                                            | 1,227                        | 7,187                                | 0,000095                          | 0,000                 | 38,150                                              |
| skośność     | 0,596                                | -0,425                                  | -0,969                                                            | 0,130                        | 0,376                                | 1,282976                          | 1,442                 | -0,103                                              |
| kwartyl1     | 12,20725                             | 65,698                                  | 52,5435275                                                        | 0,4450335                    | 6,05775                              | 4,19338E-05                       | 6,39548E-05           | 32,65                                               |
| kwartyl3     | 30,01575                             | 77,48275                                | 97,4499075                                                        | 2,241527                     | 9,2                                  | 0,00016107                        | 0,000401373           | 42,45                                               |
| IQR          | 17,8085                              | 11,78475                                | 44,90638                                                          | 1,7964935                    | 3,14225                              | 0,000119136                       | 0,000337418           | 9,8                                                 |
| wąs dolny    | -32,816375                           | -50,526125                              | -93,63133375                                                      | -2,917257                    | -7,74225                             | -0,000199671                      | -0,000538104          | -31,025                                             |
| wąs górny    | 48,326625                            | 176,02975                               | 176,2651988                                                       | 2,90907725                   | 18,286625                            | 0,000223971                       | 0,000497305           | 91,425                                              |

</br>

**Tabela 3.4.3.3** *Statystyki opisowe dla danych po przybliżeniu wartości odstających wykrytych przez algorytm LOF (Local Outlier Factor) za pomocą algorytmu imputacji danych k-sąsiadów (k=5) (2016 r.) oraz zamianie dwóch destymulant na stosunki względem populacji danego kraju.* [(Excel, arkusz "LOF outliers imputowane")](https://sggwpl-my.sharepoint.com/:x:/g/personal/s217265_sggw_edu_pl/EZshiO4QAhtBlzm-VUYfEjIByj867XJWS55VH2JokrfT3A?e=QdzOLB&nav=MTVfezJCOUIwRDhDLTZENTEtNEY3Ni1BQkMyLTUzN0NENDg0NkVEMX0)
| Statystyka   | Birth rate, crude (per 1,000 people) | Life expectancy at birth, total (years) | People using at least basic sanitation services (% of population) | Population growth (annual %) | Death rate, crude (per 1,000 people) | Number of deaths ages 20-24 years | Number of stillbirths | Prevalence of hypertension (% of adults ages 30-79) |
|--------------|--------------------------------------|-----------------------------------------|-------------------------------------------------------------------|------------------------------|--------------------------------------|-----------------------------------|-----------------------|-----------------------------------------------------|
| min          | 8,800                                | 56,659                                  | 7,744                                                             | -0,701                       | 4,343                                | 0,0000127                         | 0,000014              | 24,900                                              |
| max          | 43,411                               | 83,602                                  | 100,000                                                           | 3,586                        | 15,100                               | 0,0004606                         | 0,001413              | 48,700                                              |
| rozstęp      | 34,611                               | 26,943                                  | 92,256                                                            | 4,288                        | 10,757                               | 0,0004479                         | 0,001399              | 23,800                                              |
| średnia      | 21,428                               | 71,788                                  | 73,731                                                            | 1,351                        | 7,984                                | 0,0001343                         | 0,000313              | 37,538                                              |
| odch. Stand. | 9,382                                | 7,107                                   | 28,081                                                            | 1,013                        | 2,378                                | 0,0001069                         | 0,000302              | 5,762                                               |
| mediana      | 19,592                               | 72,475                                  | 86,868                                                            | 1,346                        | 7,320                                | 0,0000976                         | 0,000205              | 37,650                                              |
| skośność     | 0,467                                | -0,219                                  | -0,889                                                            | 0,116                        | 0,980                                | 0,9698453                         | 1,236373              | -0,004                                              |

#### 3.4.4 Podstawowa wizualizacja
(opis+ histogramy dla każdej cechy na danych z arkusza "Dane bez braków", boxploty i wykresy LOF wszystko na bazie "Dane bez braków" + odnośniki do kodów i folderów ze zdjęciami: tu można poglądowo wstawić po 2-3)

## 4. Opis metod porządkowania liniowego
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Celem metod porządkowania liniowego jest konstrukcja wskaźnika syntetycznego $Q_{i}$.</br> 
Im jego wartość jest wyższa, tym wyżej dany kraj uplasuje się w rankingu. </br></br>
**Tabela 3.1** *Wybrane metody porządkowania liniowego obiektów*

| Metoda   | Cecha syntetyczna                                                | Pozostałe wzory                             |
|----------|------------------------------------------------------------------|---------------------------------------------|
| Hellwiga |![HellwigQi](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/0e3121f9-6f0e-4848-aa8d-ab3c9d8e7f2a) | ![zij](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/709bc53f-9e87-4e0f-95c7-843a7459b382) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![zijplus](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/7a4f6dbe-ff3b-4086-80f6-726f4dafd3c2) </br></br> ![diplus](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/ad37d73c-68a6-4939-9eeb-a48ad5e41034)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Sd](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/a6d93475-2bbb-477e-98b2-64bb5f363b89) </br></br> ![dzero](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/e9ce8628-51a4-43d6-8632-172fc81d90fe)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![ddaszek](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/33541fa4-1198-4f11-9e98-cd6e1863a90a) |
| TOPSIS | ![qi](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/ffdf3e2c-f2c3-4395-8920-f285b4357a73) | ![diplus](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/fd12f564-a88c-4b2d-902b-59c95a19b2b8)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![diminus](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/5d622451-d931-4761-9706-6585a4ae6691)</br></br>![zjplus](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/68e6b6f0-3b2e-4b38-9501-834b414c3c5c)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![zjminus](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/9cc4aa42-a363-413b-8e95-8ff90476a2e1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![zij](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/405027f0-e39e-4a45-80f1-1112749d70b8) |
| TOPSIS z unitaryzacją | ![qi](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/ffdf3e2c-f2c3-4395-8920-f285b4357a73) | ![diplus](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/fd12f564-a88c-4b2d-902b-59c95a19b2b8)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![diminus](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/5d622451-d931-4761-9706-6585a4ae6691)</br></br>![zjplus](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/68e6b6f0-3b2e-4b38-9501-834b414c3c5c)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![zjminus](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/9cc4aa42-a363-413b-8e95-8ff90476a2e1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![zijmuz](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/a1c188f5-8fb5-4073-9375-7291c3ab4ba5)|
| SSW |![qi](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/2877a860-ba7c-49b0-87a0-b8ba3f44fef5) |![zij](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/508398bc-1189-4348-a47f-82462c0adaed) |
| MUZ |![qi](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/2877a860-ba7c-49b0-87a0-b8ba3f44fef5) | ![zijmuz](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/498fc788-201a-4f64-82ed-7df729fb8612)|
| STRAHL | ![qi](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/fc12f896-23c5-40ab-9013-69bfe613d9a0)|![zij_strahl](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/02d6898f-ec40-4fbc-a418-4f5a9f6afa68)|
| NOWAK | ![qi](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/47fb3c06-7239-4a3b-8a04-9335c9dfa8b4) | ![zij_nowak](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/515fad88-73ab-4ace-ae7a-568b3e387917) |

Oznaczenia: $x_{ij}$ - wartość j-tej cechy dla i-tego kraju; $z_{ij}$ - wartość unormowana j-tej cechy dla i-tego obiektu; $\overline{x_{j}}$ - średnia arytmetyczna j-tej cechy; $S_{j}$ - odchylenie standardowe j-tej cechy; $Q_{i}$ - wartość cechy syntetycznej dla i-tego obiektu

Żródło: [PRS, 2018](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/tree/main#7-bibliografia)






## 5. Rezultaty

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Wartości miernika syntetycznego (qi) oraz ranking (rank) przyporządkowane krajom (na danych przybliżanych metodą winsoryzacji) przez metody porządkowania liniowego (Hellwig, TOPSIS, TOPSIS_u, SWW, NOWAK, MUZ, STRAHL) zostały przedstawione w postaci tabelarycznej w tabeli 5.1. </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Wyświetlanie wyników ograniczono do krajów na pierwszych 10 pozcjach oraz 5 ostatnich pozycjach w danej metodzie. Pełne wyniki w postaci tabelarycznej znajdują się pod linkiem: [(Excel, arkusz "Porównanie państw")](https://sggwpl-my.sharepoint.com/:x:/g/personal/s217265_sggw_edu_pl/EZshiO4QAhtBlzm-VUYfEjIByj867XJWS55VH2JokrfT3A?e=aubdEd&nav=MTVfe0VEMUE0RDcyLUZGNDQtNDgxNi04QTQyLThFNTFFNzVBMEE4NX0) </br>

**Tabela 5.1** *Wartość miernika syntetycznego (qi) oraz ranking (rank) przyporządkowane krajom przez różne metody porządkowania liniowego (na danych przybliżanych metodą winsoryzacji)*
</br>
| Jednostka terytorialna   | qi     | Rank_Hellwig | Jednostka terytorialna   | qi    | Rank_TOPSIS | Jednostka terytorialna   | qi    | Rank_TOPSIS_u | Jednostka terytorialna   | qi     | Rank_SSW | Jednostka terytorialna   | qi     | Rank_NOWAK | Jednostka terytorialna   | qi    | Rank_MUZ | Jednostka terytorialna   | qi     | Rank_STRAHL |
|--------------------------|--------|--------------|--------------------------|-------|-------------|--------------------------|-------|---------------|--------------------------|--------|----------|--------------------------|--------|------------|--------------------------|-------|----------|--------------------------|--------|-------------|
| Maldives                 | 0,567  | 1            | Maldives                 | 0,547 | 1           | Maldives                 | 0,726 | 1             | Maldives                 | 0,944  | 1        | Qatar                    | 0,609  | 1          | Maldives                 | 0,791 | 1        | Qatar                    | 0,279  | 1           |
| Jordan                   | 0,543  | 2            | Jordan                   | 0,559 | 2           | Israel                   | 0,724 | 2             | Qatar                    | 0,909  | 2        | Oman                     | 0,574  | 2          | Qatar                    | 0,785 | 2        | Oman                     | 0,269  | 2           |
| Israel                   | 0,538  | 3            | Israel                   | 0,671 | 3           | Jordan                   | 0,722 | 3             | Israel                   | 0,845  | 3        | Maldives                 | 0,544  | 3          | Israel                   | 0,781 | 3        | Maldives                 | 0,269  | 3           |
| Saudi Arabia             | 0,498  | 4            | Bahrain                  | 0,539 | 4           | West Bank and Gaza       | 0,702 | 4             | Jordan                   | 0,815  | 4        | Jordan                   | 0,523  | 4          | Oman                     | 0,770 | 4        | Jordan                   | 0,263  | 4           |
| Iran, Islamic Rep.       | 0,494  | 5            | Kuwait                   | 0,560 | 5           | Bahrain                  | 0,698 | 5             | Kuwait                   | 0,805  | 5        | Kuwait                   | 0,489  | 5          | Kuwait                   | 0,769 | 5        | Kuwait                   | 0,250  | 5           |
| West Bank and Gaza       | 0,490  | 6            | Saudi Arabia             | 0,501 | 6           | Oman                     | 0,696 | 6             | Bahrain                  | 0,804  | 6        | Bahrain                  | 0,469  | 6          | Bahrain                  | 0,768 | 6        | Bahrain                  | 0,247  | 6           |
| Bahrain                  | 0,486  | 7            | Qatar                    | 0,672 | 7           | Saudi Arabia             | 0,695 | 7             | Oman                     | 0,798  | 7        | Israel                   | 0,383  | 7          | Jordan                   | 0,767 | 7        | Israel                   | 0,229  | 7           |
| Ecuador                  | 0,484  | 8            | Oman                     | 0,606 | 8           | Kuwait                   | 0,693 | 8             | Switzerland              | 0,669  | 8        | New Zealand              | 0,324  | 8          | Saudi Arabia             | 0,739 | 8        | Saudi Arabia             | 0,206  | 8           |
| Algeria                  | 0,483  | 9            | Iran, Islamic Rep.       | 0,593 | 9           | Algeria                  | 0,683 | 9             | Saudi Arabia             | 0,662  | 9        | Malta                    | 0,324  | 9          | Switzerland              | 0,737 | 9        | West Bank and Gaza       | 0,199  | 9           |
| Solomon Islands          | 0,475  | 10           | Ecuador                  | 0,535 | 10          | Qatar                    | 0,683 | 10            | Australia                | 0,652  | 10       | Luxembourg               | 0,317  | 10         | Australia                | 0,736 | 10       | New Zealand              | 0,194  | 10          |
| …                        | …      | …            | …                        | …     | …           | …                        | …     | …             | …                        | …      | …        | …                        | …      | …          | …                        | …     | …        | …                        | …      | …           |
| Lithuania                | -0,033 | 182          | Chad                     | 0,628 | 182         | Guinea                   | 0,389 | 182           | Somalia                  | -0,972 | 182      | Sierra Leone             | -0,532 | 182        | Somalia                  | 0,363 | 182      | Guinea                   | -0,099 | 182         |
| Somalia                  | -0,065 | 183          | Eswatini                 | 0,676 | 183         | Chad                     | 0,385 | 183           | Sierra Leone             | -1,003 | 183      | Somalia                  | -0,568 | 183        | Sierra Leone             | 0,353 | 183      | Sierra Leone             | -0,112 | 183         |
| Chad                     | -0,086 | 184          | Sierra Leone             | 0,599 | 184         | Sierra Leone             | 0,375 | 184           | Chad                     | -1,118 | 184      | Chad                     | -0,571 | 184        | Chad                     | 0,324 | 184      | Chad                     | -0,126 | 184         |
| Lesotho                  | -0,093 | 185          | Central African Republic | 0,551 | 185         | Central African Republic | 0,337 | 185           | Lesotho                  | -1,330 | 185      | Lesotho                  | -0,696 | 185        | Lesotho                  | 0,291 | 185      | Lesotho                  | -0,166 | 185         |
| Central African Republic | -0,140 | 186          | Lesotho                  | 0,458 | 186         | Lesotho                  | 0,323 | 186           | Central African Republic | -1,388 | 186      | Central African Republic | -0,811 | 186        | Central African Republic | 0,273 | 186      | Central African Republic | -0,187 | 186         |

</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Wartości miernika syntetycznego (qi) oraz ranking (rank) przyporządkowane krajom (na danych przybliżanych metodą k-sąsiadów) przez metody porządkowania liniowego (Hellwig, TOPSIS, SWW, NOWAK, STRAHL) zostały przedstawione w postaci tabelarycznej w tabeli 5.2. </br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Wyświetlanie wyników ograniczono do krajów na pierwszych 10 pozcjach oraz 5 ostatnich pozycjach w danej metodzie. Pełne wyniki w postaci tabelarycznej znajdują się pod linkiem: [(Excel, arkusz "Porównanie państw")](https://sggwpl-my.sharepoint.com/:x:/g/personal/s217265_sggw_edu_pl/EZshiO4QAhtBlzm-VUYfEjIByj867XJWS55VH2JokrfT3A?e=aubdEd&nav=MTVfe0VEMUE0RDcyLUZGNDQtNDgxNi04QTQyLThFNTFFNzVBMEE4NX0) </br>

**Tabela 5.2** *Wartość miernika syntetycznego (qi) oraz ranking (rank) przyporządkowane krajom przez różne metody porządkowania liniowego (na danych przybliżanych metodą k-sąsiadów (k=5)*
</br>

| Jednostka terytorialna   | qi     | Hellwig_Rank | Jednostka terytorialna   | qi    | Rank_TOPSIS | Jednostka terytorialna   | qi    | Rank_TOPSIS_u | Jednostka terytorialna   | qi     | Rank_SSW | Jednostka terytorialna   | qi     | Rank_NOWAK | Jednostka terytorialna   | qi    | Rank_MUZ | Jednostka terytorialna   | qi     | Rank_STRAHL |
|--------------------------|--------|--------------|--------------------------|-------|-------------|--------------------------|-------|---------------|--------------------------|--------|----------|--------------------------|--------|------------|--------------------------|-------|----------|--------------------------|--------|-------------|
| Israel                   | 0,609  | 1            | Israel                   | 0,767 | 1           | Israel                   | 0,756 | 1             | Israel                   | 0,927  | 1        | Kuwait                   | 0,415  | 1          | Israel                   | 0,825 | 1        | Israel                   | 0,247  | 1           |
| Algeria                  | 0,535  | 2            | Korea, Rep.              | 0,715 | 2           | Korea, Rep.              | 0,711 | 2             | Korea, Rep.              | 0,810  | 2        | Bahrain                  | 0,402  | 2          | Korea, Rep.              | 0,798 | 2        | Kuwait                   | 0,232  | 2           |
| Ecuador                  | 0,519  | 3            | Algeria                  | 0,712 | 3           | Algeria                  | 0,704 | 3             | New Zealand              | 0,715  | 3        | Israel                   | 0,391  | 3          | New Zealand              | 0,771 | 3        | Bahrain                  | 0,231  | 3           |
| Solomon Islands          | 0,507  | 4            | Ecuador                  | 0,712 | 4           | Ecuador                  | 0,698 | 4             | Australia                | 0,709  | 4        | New Zealand              | 0,335  | 4          | Australia                | 0,770 | 4        | New Zealand              | 0,213  | 4           |
| Saudi Arabia             | 0,506  | 5            | New Zealand              | 0,711 | 5           | New Zealand              | 0,696 | 5             | Malta                    | 0,701  | 5        | Malta                    | 0,332  | 5          | Malta                    | 0,767 | 5        | Malta                    | 0,209  | 5           |
| New Zealand              | 0,498  | 6            | Australia                | 0,703 | 6           | Australia                | 0,691 | 6             | Singapore                | 0,680  | 6        | Luxembourg               | 0,325  | 6          | Singapore                | 0,760 | 6        | Korea, Rep.              | 0,204  | 6           |
| Korea, Rep.              | 0,491  | 7            | Malta                    | 0,698 | 7           | Saudi Arabia             | 0,687 | 7             | Luxembourg               | 0,669  | 7        | Australia                | 0,293  | 7          | Iceland                  | 0,760 | 7        | Luxembourg               | 0,203  | 7           |
| Panama                   | 0,482  | 8            | Saudi Arabia             | 0,697 | 8           | Bahrain                  | 0,685 | 8             | Iceland                  | 0,667  | 8        | Singapore                | 0,280  | 8          | Luxembourg               | 0,759 | 8        | Australia                | 0,200  | 8           |
| West Bank and Gaza       | 0,481  | 9            | Bahrain                  | 0,696 | 9           | Malta                    | 0,683 | 9             | Bahrain                  | 0,652  | 9        | Korea, Rep.              | 0,278  | 9          | Bahrain                  | 0,756 | 9        | Algeria                  | 0,193  | 9           |
| Australia                | 0,478  | 10           | Solomon Islands          | 0,695 | 10          | Iceland                  | 0,680 | 10            | Kuwait                   | 0,636  | 10       | Tajikistan               | 0,273  | 10         | Kuwait                   | 0,752 | 10       | Singapore                | 0,191  | 10          |
| …                        | …      | …            | …                        | …     | …           | …                        | …     | …             | …                        | …      | …        | …                        | …      | …          | …                        | …     | …        | …                        | …      | …           |
| Lesotho                  | -0,026 | 182          | Sierra Leone             | 0,406 | 182         | Chad                     | 0,400 | 182           | Sierra Leone             | -0,897 | 182      | Sierra Leone             | -0,439 | 182        | Sierra Leone             | 0,371 | 182      | Sierra Leone             | -0,078 | 182         |
| Chad                     | -0,036 | 183          | Chad                     | 0,398 | 183         | Sierra Leone             | 0,397 | 183           | Chad                     | -0,938 | 183      | Chad                     | -0,534 | 183        | Chad                     | 0,369 | 183      | Chad                     | -0,095 | 183         |
| Bulgaria                 | -0,058 | 184          | Central African Republic | 0,371 | 184         | Central African Republic | 0,381 | 184           | Lesotho                  | -1,062 | 184      | Lesotho                  | -0,581 | 184        | Somalia                  | 0,345 | 184      | Lesotho                  | -0,124 | 184         |
| Central African Republic | -0,078 | 185          | Somalia                  | 0,364 | 185         | Somalia                  | 0,377 | 185           | Central African Republic | -1,066 | 185      | Central African Republic | -0,670 | 185        | Lesotho                  | 0,344 | 185      | Somalia                  | -0,133 | 185         |
| Somalia                  | -0,083 | 186          | Lesotho                  | 0,347 | 186         | Lesotho                  | 0,356 | 186           | Somalia                  | -1,072 | 186      | Somalia                  | -0,740 | 186        | Central African Republic | 0,341 | 186      | Central African Republic | -0,134 | 186         |

</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Graficzne przedstawienie różnic w rankingach państw (zarówno na danych przybliżonych za pomocą metody winsoryzacji, jak również danych przybliżonych metodą k-sąsiadów) zostało sporządzone w postaci wykresów sieciowych (Obraz 5.1 oraz Obraz 5.2) oraz dla lepszego zilustrowania różnic w rankingach konkretnego kraju w postaci wykresów słupkowych (Wykres 5.1 oraz Wykres 5.2). </br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Wszystkie wykresy słupkowe są dostępne w folderze boxplot_bar: link do przykładowego wykresu: [boxplot_bar](Projekt/Porównania_analiz/Porównanie_rankingów_bar/boxplot_bar/porownanie_metod_bar_AFG-COD.jpg) oraz w folderze k_sasiadow_bar: link do przykładowego wykresu: [k_sasiadow_bar](Projekt/Porównania_analiz/Porównanie_rankingów_bar/k_sasiadow_bar/porownanie_metod_bar_k_sas_AFG-COD.jpg.jpg)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Wykresy sieciowe porównujące rankingi w zależności od użytej metody obsłużenia outlierów (winsoryzacja bądź metoda LOF i k-sąsiadów) w obrębie jednej metody porządkowania liniowego są dostępne w folderze Metody_porządkowania_liniowego w folderze dedykowanym danej metodzie: link do wykresu sieciowego porównującego wyniki analizy: [Hellwig_radar](Projekt/Metody_porządkowania_liniowego/Hellwig)

**Wykres 5.1** *Graficzna reprezentacja różnic w przydzielanych państwom rankingach przez rożne metody porządkowania liniowego obiektów (na danych przybliżonych metodą winsoryzacji)* link do wykresu: [radar_boxplot](Projekt/Porównania_analiz/Porównanie_rankingów_radar/porownanie_metod_boxplot_radar.jpg)
![porownanie_metod_boxplot_radar](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/9efd6786-6254-4552-9fe5-6a5e307685e0)

**Wykres 5.2** *Graficzna reprezentacja różnic w przydzielanych państwom rankingach przez rożne metody porządkowania liniowego obiektów (na danych przybliżonych metodą k-sąsiadów)* link do wykresu: [radar k_sasiadow](Projekt/Porównania_analiz/Porównanie_rankingów_radar/porownanie_metod_k_sasiadow_radar.jpg)
![porownanie_metod_k_sasiadow_radar](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/d542d0e2-7b00-4043-9243-ea66eef89d91)

**Wykres 5.3** *Porównanie rankingów państw AFG-COD przyporządkowanym państwom przez różne metody porządkowania liniowego obiektów (na danych przybliżonych metodą winsoryzacji)* link do wykresu: [bar_boxplot_AFG-COD](Projekt/Porównania_analiz/Porównanie_rankingów_bar/boxplot_bar/porownanie_metod_bar_boxplot_AFG-COD.jpg)
![porownanie_metod_bar_boxplot_AFG-COD](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/b0ece9ec-b0bb-4a81-b2bd-d28416511a2d)

**Wykres 5.4** *Porównanie rankingów państw AFG-COD przyporządkowanym państwom przez różne metody porządkowania liniowego obiektów (na danych przybliżonych metodą k-sąsiadów)* link do wykresu: [bar_k_sasiadow_AFG-COD](Projekt/Porównania_analiz/Porównanie_rankingów_bar/k_sasiadow_bar/porownanie_metod_bar_k_sasiadow_AFG_COD.jpg)
![porownanie_metod_bar_k_sasiadow_AFG_COD](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/6150820e-04b7-478e-8c1e-d978a5a7c532)

</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;W celu porównania rankingów obliczonych przy pomocy różnych metod porządkowania liniowego obiektów, przygotowano macierze korelacji metod porządkowania liniowego obiektów odpowiednio dla analiz przeprowadzonych na danych przybliżanych metodą winsoryzacji (Wykres 5.3) oraz metodą k-sąsiadów (k=5) (Wykres 5.4).

**Wykres 5.5** *Macierz korelacji metod porządkowania liniowego obiektów względem obliczonych rankingów (dla danych przybliżonych metodą winsoryzacji* link do wykresu: [Macierz korelacji boxplot](Projekt/Porównania_analiz/Macierze_korelacji_rankingów/macierz_korelacji_rankingow_boxplot.jpg)
![macierz_korelacji_rankingow_boxplot](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/b9dd2f84-68a1-4245-bccf-a9c01c7fa74a)


**Wykres 5.6** *Macierz korelacji metod porządkowania liniowego obiektów względem obliczonych rankingów (dla danych przybliżonych metodą winsoryzacji* link do wykresu: [Macierz korelacji k_sasiadow](Projekt/Porównania_analiz/Macierze_korelacji_rankingów/macierz_korelacji_rankingow_k_sasiadow.jpg)
![macierz_korelacji_rankingow_k_sasiadow](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/c597a2d8-7bf7-4417-b48b-d45c9af0a6d1)

</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<<<Wnioski z macierzy&&&

</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;W celu zidentyfikowania metody porządowania liniowego obiektów najbardziej skorelowanej z pozostałymi metodami utworzono wektory z uśrednionym skorelowaniem danej metody względem pozostałych (u_winsor i u_k_sas) dla obu metod obsłużenia obserwacji odstających (link do programu: [wektor_korelacji](Projekt/Porównania_analiz/Macierze_korelacji_rankingów/wektor_korelacji.txt)). 
</br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Współrzędne wektorów odpowiadają metodom porządkowania liniowego zgodnie z kolejnością w tabeli 4.1.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **u_winsor = [0.863, 0.958, 0.975, 0.979, 0.951, 0.971, 0.979]**

Dla danych, w których obserwacje odstające zostały obsłużone przy pomocy metody winsoryzacji, najbardziej skorelowana z pozostałymi metodami jest metoda STRAHL.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **u_k_sas = [0.898, 0.969, 0.974, 0.978, 0.938, 0.977, 0.974]**

Dla danych, w których obserwacje odstające zostały obsłużone przy pomocy metody k-sąsiadów (k=5), najbardziej skorelowana z pozostałymi metodami jest metoda SSW.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ostatecznie, kraje zostały podzielone na cztery grupy względem wysokości badanych wskaźników zdrowia. Dla danych przybliżonych metodą winsoryzacji ostała wykorzystana wartość miernika syntetycznego (qi) obliczona metodą STRAHL, zaś dla danych przybliżonych metodą k-sąsiadów została wykorzystana wartość miernika syntetycznego (qi) obliczona metodą SSW, przy czym:

| Numer grupy | Opis                 | Wzór      |
|-------------|----------------------|-----------|
| 1           | bardzo wysoki poziom | ![CodeCogsEqn](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/729e36a4-a8e5-4418-a531-8cb4bcd6385b)          |
| 2           | wysoki poziom        | ![CodeCogsEqn](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/d6202f34-98ce-45c4-a398-43b826af69ba)          |
| 3           | średni poziom        | ![CodeCogsEqn3](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/04b40cc7-91f0-4d24-b5be-cdd5406944c4)          |
| 4           | niski poziom         | ![CodeCogsEqn4](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/7ee34c4c-2a94-45d8-a9fa-a4d91db66e0c)          |
|             | oraz:                | ![CodeCogsEqn5](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/4d352c16-85f8-4ac5-aab0-cacc4e52a0d1)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Wykresy 5.5 i 5.6 ilustrują podział państw na grupy względem miernika syntetycznego (qi) dla obu metod obsłużenia obserwacji odstających.

**Wykres 5.7** *Podział państw na grupy względem poziomu miernika syntetycznego (qi) obliczonego metodą STRAHL dla danych przybliżonych metodą winsoryzacji*
![boxplotsuper](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/ba1a6188-14d9-4cd2-9a79-e9bb5b8f90a8)

**Wykres 5.8** *Podział państw na grupy względem poziomu miernika syntetycznego (qi) obliczonego metodą SSW dla danych przybliżonych metodą k-sąsiadów (k=5)*
![knajblizszych](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/400ed477-9e93-4c0d-a843-74168401b084)




## 6. Podsumowanie

## 7. Bibliografia
1. PRS Zeszyty Naukowe Szkoły Głównej Gospodarstwa Wiejskiego w Warszawie Problemy Rolnictwa ĝwiatowego tom 18 (XXXIII), zeszyt 2, 2018: 183–192 DOI: 10.22630/PRS.2018.18.2.46 Karol Kukuła, Lidia Luty Uniwersytet Rolniczy im. Hugona Kołłątaja w Krakowie 
