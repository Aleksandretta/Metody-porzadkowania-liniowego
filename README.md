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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Celem badania jest opracowanie rankingów krajów na świecie oraz jednostek terytorialnych (wysp, archipelagów itd.) oraz porównanie ich ze sobą na podstawie różnych wskaźników zdrowia, demografii i warunków sanitarnych, wykorzystując metody porządkowania liniowego, takie jak metoda Hellwiga i TOPSIS. Zakres badania obejmuje analizę danych z The World Bank, z bazy danych: Health Nutrition and Population, z 2016 roku, z uwzględnieniem cech diagnostycznych poddanych metodzie k-najbliższych sąsiadów oraz przybliżonych boxplotem. 
</br>

### 3.2 Przegląd literatury

### 3.3 Zmienne wybrane do analizy
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Wybierając cechy diagnostyczne do stworzenia rankingów państw na podstawie różnych wskaźników zdrowia, demografii i warunków sanitarnych, kierowano się analizą merytoryczną, statystyczną i dostępnością danych. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Analiza merytoryczna obejmowała ocenę znaczenia poszczególnych wskaźników w kontekście oceny stanu zdrowia, demografii i warunków sanitarnych w poszczególnych państwach. Wybierane były te cechy, które były istotne dla tego obszaru badawczego, takie jak wskaźniki dzietności, wskaźniki umieralności, czy wskaźniki dostępu do podstawowych usług sanitarnych. Dodatkowo, analizowano statystyczną zmienność cech, przyjmując minimalne kryteria współczynnika zmienności (co najmniej 0,1) oraz ilorazu skrajnych wartości (co najmniej 2), aby zapewnić reprezentatywność danych. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Podczas procesu tworzenia rankingów państw wykorzystano kryterium merytoryczne, wybierając wskaźniki, które adekwatnie charakteryzują stan zdrowia, demografii i warunków sanitarnych w poszczególnych państwach. Ponadto, zastosowano kryterium statystyczne, koncentrując się na cechach charakteryzujących się odpowiednią zmiennością w celu zapewnienia zróżnicowania analizy. Te działania miały na celu zapewnienie kompleksowej oceny i porównania państw pod kątem różnych aspektów zdrowia, demografii i warunków sanitarnych. 
</br>

| Zmienna                                                      | Uzasadnienie | Typ zmiennej     |
|--------------------------------------------------------------|--------------|------------------|
| Adolescent fertility rate (births per 1,000 women ages 15-19)| Dzietność ogólna ma kluczowe znaczenie dla kształtowania struktury populacji oraz zapewnienia równowagi demograficznej. | stymulanta (s)   |
| Fertility rate, total                                        | Dzietność ogólna ma kluczowe znaczenie dla kształtowania struktury populacji oraz zapewnienia równowagi demograficznej. | stymulanta (s)   |
| Birth rate, crude                                            | Wskaźnik urodzeń informuje o liczbie urodzeń w populacji i jest kluczowym miernikiem dynamiki demograficznej. | stymulanta (s)   |
| Life expectancy at birth total                               | Oczekiwana długość życia jest istotnym wskaźnikiem zdrowia i jakości życia w społeczeństwie. Wysoka oczekiwana długość życia świadczy o skuteczności systemu opieki zdrowotnej oraz poziomie rozwoju społecznego i ekonomicznego. | stymulanta (s)   |
| People using at least basic sanitation services              | Dostęp do podstawowych usług sanitarnych ma kluczowe znaczenie dla zapobiegania chorobom związanym z brakiem higieny. Poprawa tego wskaźnika może przyczynić się do poprawy zdrowia i jakości życia mieszkańców oraz zmniejszenia obciążenia systemu opieki zdrowotnej. | stymulanta (s)   |
| Population growth (annual)                                   | Tempo wzrostu populacji ma istotny wpływ na zrównoważony rozwój społeczno-gospodarczy oraz wykorzystanie zasobów naturalnych. | stymulanta (s)   |
| Population (total)                                           | Liczba ludności w danym kraju jest istotnym miernikiem dynamiki demograficznej oraz stanu gospodarki i społeczeństwa. | stymulanta (s)   |
| Death rate                                                   | Wskaźnik śmiertelności ogólnej informuje o liczbie zgonów w populacji i jest istotnym miernikiem stanu zdrowia i efektywności systemu opieki zdrowotnej. | destymulanta (d) |
| Number of deats ages 20-24                                   | Liczba zgonów w młodym wieku może świadczyć o istniejących zagrożeniach zdrowotnych oraz skuteczności działań prewencyjnych i leczniczych, a także o stabilności społecznej. | destymulanta (d) |
| Number of stillbirths                                        | Liczba martwych urodzeń jest istotnym miernikiem opieki zdrowotnej matki i dziecka podczas ciąży oraz porodu, a także jakości opieki prenatalnej. | destymulanta (d) |
| Prevalence of hypertension                                   | Rozpowszechnienie nadciśnienia tętniczego w populacji dorosłych jest istotnym wskaźnikiem zdrowia sercowo-naczyniowego oraz efektywności systemu opieki zdrowotnej w profilaktyce i leczeniu chorób układu sercowo-naczyniowego. | destymulanta (d) |

### 3.4 Wstępna analiza danych

#### 3.4.1 Braki danych
~14% oryginalnych danych (30 na 217 państw) stanowiły braki danych.
Metodą ich obsłużenia było usunięcie.
</br>

#### 3.4.2 Obserwacje odstające
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Winsoryzacja to metoda przetwarzania danych mająca na celu zmniejszenie wpływu wartości odstających na analizę statystyczną. Proces ten polega na zastępowaniu skrajnych wartości (najniższych i najwyższych) wartościami mniej ekstremalnymi. W typowym podejściu wykorzystuje się boxploty do identyfikacji wartości odstających, gdzie wąsy boxplota określają granice. Wartości leżące poza wąsami są uważane za odstające i są zastępowane wartościami na krańcach wąsów lub innymi wartościami bliskimi granicy rozkładu. Procedura ta pomaga w ograniczeniu wpływu ekstremalnych obserwacji na wyniki analizy, zachowując jednocześnie rozmiar próby.

[(Excel, arkusz "Dane po winsoryzacji")](https://sggwpl-my.sharepoint.com/:x:/g/personal/s217265_sggw_edu_pl/EZshiO4QAhtBlzm-VUYfEjIByj867XJWS55VH2JokrfT3A?e=gnTRJm&nav=MTVfezlBQUFBRkVFLUM2NDktNDE2QS05QTJCLTRGREUwNDk2RjQzMH0)

link do przykładowego wykresu: [boxplot_bar](Projekt/Porównania_analiz/Porównanie_rankingów_bar/boxplot_bar/porownanie_metod_bar_AFG-COD.jpg)

[Folder BOXPLOT](Projekt/Początkowa_obróbka_danych/Boxploty)


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Algorytm LOF (Local Outlier Factor) służy do wykrywania obserwacji odstających w danych. Działa poprzez porównanie lokalnej gęstości danej obserwacji z lokalną gęstością jej sąsiadów. Obserwacje o znacząco niższej gęstości niż ich sąsiedzi są uznawane za odstające. Wartość LOF bliska 1 oznacza obserwację typową, natomiast wartości znacząco większe od 1 wskazują na obserwacje odstające.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Algorytm imputacji k-sąsiadów (k-NN imputation) wykorzystuje informacje z k najbliższych sąsiadów obserwacji do uzupełnienia brakujących danych. Dla każdej obserwacji z brakującymi wartościami, algorytm znajduje k najbliższych sąsiadów (opartych na dostępnych cechach) i uzupełnia brakujące wartości na podstawie wartości tych sąsiadów. W tym przypadku, k=5 zostało wybrane jako optymalna liczba sąsiadów, zapewniająca dobry kompromis między dokładnością a złożonością obliczeniową.

[(Excel, arkusz "LOF outliers imputowane")](https://sggwpl-my.sharepoint.com/:x:/g/personal/s217265_sggw_edu_pl/EZshiO4QAhtBlzm-VUYfEjIByj867XJWS55VH2JokrfT3A?e=QdzOLB&nav=MTVfezJCOUIwRDhDLTZENTEtNEY3Ni1BQkMyLTUzN0NENDg0NkVEMX0)

[(Excel, arkusz "LOF outliers")](https://sggwpl-my.sharepoint.com/:x:/r/personal/s217265_sggw_edu_pl/_layouts/15/Doc.aspx?sourcedoc=%7BEE88219B-0210-411B-9739-BE55461F1232%7D&file=2_Poziom%20zdrowia%20na%20świecie.xlsx&action=default&mobileredirect=true&DefaultItemOpen=1)

link do przykładowego wykresu: [k_sasiadow_bar](Projekt/Porównania_analiz/Porównanie_rankingów_bar/k_sasiadow_bar/porownanie_metod_bar_k_sas_AFG-COD.jpg.jpg)

[Folder LOF](Projekt/Początkowa_obróbka_danych/Local_Outlier_Factor)


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

**Tabela 3.4.3.3** *Statystyki opisowe dla danych po przybliżeniu wartości odstających wykrytych przez algorytm LOF (Local Outlier Factor) za pomocą algorytmu imputacji danych k-sąsiadów (k=5) (2016 r.).* [(Excel, arkusz "LOF outliers imputowane")](https://sggwpl-my.sharepoint.com/:x:/g/personal/s217265_sggw_edu_pl/EZshiO4QAhtBlzm-VUYfEjIByj867XJWS55VH2JokrfT3A?e=QdzOLB&nav=MTVfezJCOUIwRDhDLTZENTEtNEY3Ni1BQkMyLTUzN0NENDg0NkVEMX0)
| Statystyka    | Adolescent fertility rate (births per 1,000 women ages 15-19) | Fertility rate, total (births per woman) | Birth rate, crude (per 1,000 people) | Life expectancy at birth, total (years) | People using at least basic sanitation services (% of population) | Population growth (annual %) | Population, total | Death rate, crude (per 1,000 people) | Number of deaths ages 20-24 years | Number of stillbirths | Prevalence of hypertension (% of adults ages 30-79) |
|---------------|---------------------------------------------------------------|------------------------------------------|--------------------------------------|-----------------------------------------|-------------------------------------------------------------------|------------------------------|-------------------|--------------------------------------|-----------------------------------|-----------------------|-----------------------------------------------------|
| min           | 2,068                                                         | 1,324                                    | 8,800                                | 56,659                                  | 7,744                                                             | -0,701                       | 10852,000         | 4,343                                | 1,000                             | 3,000                 | 24,900                                              |
| max           | 160,779                                                       | 5,587                                    | 43,411                               | 83,602                                  | 100,000                                                           | 3,586                        | 66724104,000      | 15,100                               | 12479,000                         | 28471,000             | 48,700                                              |
| rozstęp       | 158,711                                                       | 4,263                                    | 34,611                               | 26,943                                  | 92,256                                                            | 4,288                        | 66713252,000      | 10,757                               | 12478,000                         | 28468,000             | 23,800                                              |
| średnia       | 49,872                                                        | 2,728                                    | 21,428                               | 71,788                                  | 73,731                                                            | 1,351                        | 14323433,634      | 7,984                                | 2146,532                          | 4775,873              | 37,538                                              |
| odch. Stand.  | 39,090                                                        | 1,168                                    | 9,382                                | 7,107                                   | 28,081                                                            | 1,013                        | 15252778,700      | 2,378                                | 3118,742                          | 7066,944              | 5,762                                               |
| mediana       | 41,429                                                        | 2,354                                    | 19,592                               | 72,475                                  | 86,868                                                            | 1,346                        | 8730993,000       | 7,320                                | 596,000                           | 1198,500              | 37,650                                              |
| stara_mediana | 40,625                                                        | 2,261                                    | 18,972                               | 72,896                                  | 87,240                                                            | 1,227                        | 6974842,500       | 7,385                                | 518,000                           | 970,500               | 38,100                                              |
| kwartyl1      | 15,344                                                        | 1,740                                    | 12,900                               | 65,851                                  | 51,957                                                            | 0,641                        | 2330618,000       | 6,501                                | 149,750                           | 191,750               | 33,325                                              |
| kwartyl3      | 72,625                                                        | 3,692                                    | 30,016                               | 77,205                                  | 97,434                                                            | 2,161                        | 23646130,500      | 9,200                                | 2617,500                          | 6053,000              | 41,775                                              |
| IQR           | 57,282                                                        | 1,952                                    | 17,116                               | 11,354                                  | 45,476                                                            | 1,519                        | 21315512,500      | 2,699                                | 2467,750                          | 5861,250              | 8,450                                               |
| wąs dolny     | -70,579                                                       | -1,189                                   | -12,774                              | 48,819                                  | -16,257                                                           | -1,637                       | -29642650,750     | 2,453                                | -3551,875                         | -8600,125             | 20,650                                              |
| wąs górny     | 158,548                                                       | 6,621                                    | 55,689                               | 94,237                                  | 165,648                                                           | 4,439                        | 55619399,250      | 13,249                               | 6319,125                          | 14844,875             | 54,450                                              |
| skośność      | 0,863                                                         | 0,743                                    | 0,467                                | -0,219                                  | -0,889                                                            | 0,116                        | 1,204             | 0,980                                | 1,807                             | 1,710                 | -0,004                                              |

#### 3.4.4 Podstawowa wizualizacja
(opis+ histogramy dla każdej cechy na danych z arkusza "Dane bez braków", boxploty i wykresy LOF wszystko na bazie "Dane bez braków" + odnośniki do kodów i folderów ze zdjęciami: tu można poglądowo wstawić po 2-3)

## 4. Opis metod porządkowania liniowego

**Tabela 3.1** *Wybrane metody porządkowania liniowego obiektów*

| Metoda   | Cecha syntetyczna                                                | Pozostałe wzory                             |
|----------|------------------------------------------------------------------|---------------------------------------------|
| Hellwiga |![HellwigQi](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/0e3121f9-6f0e-4848-aa8d-ab3c9d8e7f2a) | ![zij](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/709bc53f-9e87-4e0f-95c7-843a7459b382) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![zijplus](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/7a4f6dbe-ff3b-4086-80f6-726f4dafd3c2) </br></br> ![diplus](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/ad37d73c-68a6-4939-9eeb-a48ad5e41034)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Sd](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/a6d93475-2bbb-477e-98b2-64bb5f363b89) </br></br> ![dzero](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/e9ce8628-51a4-43d6-8632-172fc81d90fe)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![ddaszek](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/33541fa4-1198-4f11-9e98-cd6e1863a90a) |
| TOPSIS | ![qi](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/ffdf3e2c-f2c3-4395-8920-f285b4357a73) | ![diplus](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/fd12f564-a88c-4b2d-902b-59c95a19b2b8)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![diminus](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/5d622451-d931-4761-9706-6585a4ae6691)</br></br>![zjplus](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/68e6b6f0-3b2e-4b38-9501-834b414c3c5c)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![zjminus](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/9cc4aa42-a363-413b-8e95-8ff90476a2e1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![zij](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/405027f0-e39e-4a45-80f1-1112749d70b8) |
| SSW |![qi](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/2877a860-ba7c-49b0-87a0-b8ba3f44fef5) |![zij](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/508398bc-1189-4348-a47f-82462c0adaed) |
| STRAHL | ![qi](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/fc12f896-23c5-40ab-9013-69bfe613d9a0)|![zij_strahl](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/02d6898f-ec40-4fbc-a418-4f5a9f6afa68)|
| NOWAK | ![qi](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/47fb3c06-7239-4a3b-8a04-9335c9dfa8b4) | ![zij_nowak](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/48699068/515fad88-73ab-4ace-ae7a-568b3e387917) |









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

</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Graficzne przedstawienie różnic w rankingach państw (zarówno na danych przybliżonych za pomocą metody winsoryzacji, jak również danych przybliżonych metodą k-sąsiadów) zostało sporządzone w postaci wykresów sieciowych (Obraz 5.1 oraz Obraz 5.2) oraz dla lepszego zilustrowania różnic w rankingach konkretnego kraju w postaci wykresów słupkowych (Wykres 5.1 oraz Wykres 5.2). </br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Wszystkie wykresy słupkowe są dostępne w folderze boxplot_bar: link do przykładowego wykresu: [boxplot_bar](Projekt/Porównania_analiz/Porównanie_rankingów_bar/boxplot_bar/porownanie_metod_bar_AFG-COD.jpg) oraz w folderze k_sasiadow_bar: link do przykładowego wykresu: [k_sasiadow_bar](Projekt/Porównania_analiz/Porównanie_rankingów_bar/k_sasiadow_bar/porownanie_metod_bar_k_sas_AFG-COD.jpg.jpg)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Wykresy sieciowe porównujące rankingi w zależności od użytej metody obsłużenia outlierów (winsoryzacja bądź metoda LOF i k-sąsiadów) w obrębie jednej metody porządkowania liniowego są dostępne w folderze Metody_porządkowania_liniowego w folderze dedykowanym danej metodzie: link do wykresu sieciowego porównującego wyniki analizy [Hellwig_radar](Projekt/Metody_porządkowania_liniowego/Hellwig)

**Obraz 5.1** *Graficzna reprezentacja różnic w przydzielanych państwom rankingach przez rożne metody porządkowania liniowego obiektów (na danych przybliżonych metodą winsoryzacji)* link do wykresu: [radar_boxplot](Projekt/Porównania_analiz/Porównanie_rankingów_radar/porownanie_metod_boxplot_radar.jpg)
![porownanie_metod_boxplot_radar](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/d5cd1473-f2f4-467c-a5a3-5275952eaf77)

**Obraz 5.2** *Graficzna reprezentacja różnic w przydzielanych państwom rankingach przez rożne metody porządkowania liniowego obiektów (na danych przybliżonych metodą k-sąsiadów)* link do wykresu: [radar k_sasiadow](Projekt/Porównania_analiz/Porównanie_rankingów_radar/porownanie_metod_k_sasiadow_radar.jpg)
![porownanie_metod_k_sasiadow_radar](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/780b34a3-48b0-43bd-84d1-8d780d02e89d)

**Wykres 5.1** *Porównanie rankingów państw AFG-COD wyliczone przez rożne metody porządkowania liniowego obiektów (na danych przybliżonych metodą winsoryzacji)* link do wykresu: [bar_boxplot_AFG-COD](Projekt/Porównania_analiz/Porównanie_rankingów_bar/boxplot_bar/porownanie_metod_bar_AFG-COD.jpg)
![porownanie_metod_bar_AFG-COD](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/706b9ebd-0512-4783-80dd-a526517cd749)

**Wykres 5.2** *Porównanie rankingów państw AFG-COD wyliczone przez rożne metody porządkowania liniowego obiektów (na danych przybliżonych metodą k-sąsiadów)* link do wykresu: [bar_boxplot_AFG-COD](Projekt/Porównania_analiz/Porównanie_rankingów_bar/k_sasiadow_bar/porownanie_metod_bar_k_sas_AFG-COD.jpg)
![porownanie_metod_bar_k_sas_AFG-COD](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/5103e225-2dd6-4113-887b-23a0d4a58d8e)

</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;W celu porównania rankingów obliczonych przy pomocy różnych metod porządkowania liniowego obiektów, przygotowano macierze korelacji metod porządkowania liniowego obiektów odpowiednio dla analiz przeprowadzonych na danych przybliżanych metodą winsoryzacji (Wykres 5.3) oraz metodą k-sąsiadów (k=5) (Wykres 5.4).

**Wykres 5.3** *Macierz korelacji metod porządkowania liniowego obiektów względem obliczonych rankingów (dla danych przybliżonych metodą winsoryzacji* link do wykresu: [Macierz korelacji boxplot](Projekt/Porównania_analiz/Macierze_korelacji_rankingów/macierz_korelacji_rankingow_boxplot.jpg)
![macierz_korelacji_rankingow_boxplot](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/9bb87299-17da-4ef2-b991-ee61f8a7dd63)


**Wykres 5.4** *Macierz korelacji metod porządkowania liniowego obiektów względem obliczonych rankingów (dla danych przybliżonych metodą winsoryzacji* link do wykresu: [Macierz korelacji k_sasiadow](Projekt/Porównania_analiz/Macierze_korelacji_rankingów/macierz_korelacji_rankingow_k_sasiadow.jpg)
![macierz_korelacji_rankingow_k_sasiadow](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/ce67ec0b-0309-48ad-99f5-5c1a1a675e06)

</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<<<Wnioski z macierzy&&&

</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;W celu zidentyfikowania metody porządowania liniowego obiektów najbardziej skorelowanej z pozostałymi metodami utworzono wektory z uśrednionym skorelowaniem danej metody względem pozostałych (u_winsor i u_k_sas) dla obu metod obsłużenia obserwacji odstających (link do programu: [wektor_korelacji](Projekt/Porównania_analiz/Macierze_korelacji_rankingów/wektor_korelacji.txt)). 
</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Współrzędne wektorów odpowiadają metodom porządkowania liniowego zgodnie z kolejnością w tabeli 4.1.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **u_winsor = [0.756, 0.742, 0.893, 0.905, 0.867, 0.891, 0.918]**

Dla danych, w których obserwacje odstające zostały obsłużone przy pomocy metody winsoryzacji, najbardziej skorelowana z pozostałymi metodami jest metoda STRAHL.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **u_k_sas = [0.518, 0.739, 0.807, 0.882, 0.767, 0.815, 0.878]**

Dla danych, w których obserwacje odstające zostały obsłużone przy pomocy metody k-sąsiadów (k=5), najbardziej skorelowana z pozostałymi metodami jest metoda NOWAK.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ostatecznie, kraje zostały podzielone na cztery grupy względem wysokości badanych wskaźników zdrowia, dla danych przybliżonych metodą winsoryzacji wartość miernika syntetycznego (qi) wzięto z obliczeń metodą STRAHL, zaś dla danych przybliżonych metodą k-sąsiadów z obliczeń metodą NOWAK, przy czym:

| Numer grupy | Opis                 | Wzór      |
|-------------|----------------------|-----------|
| 1           | bardzo wysoki poziom | ![CodeCogsEqn](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/729e36a4-a8e5-4418-a531-8cb4bcd6385b)          |
| 2           | wysoki poziom        | ![CodeCogsEqn](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/d6202f34-98ce-45c4-a398-43b826af69ba)          |
| 3           | średni poziom        | ![CodeCogsEqn3](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/04b40cc7-91f0-4d24-b5be-cdd5406944c4)          |
| 4           | niski poziom         | ![CodeCogsEqn4](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/7ee34c4c-2a94-45d8-a9fa-a4d91db66e0c)          |
|             | oraz:                | ![CodeCogsEqn5](https://github.com/Aleksandretta/Metody-porzadkowania-liniowego/assets/113725452/4d352c16-85f8-4ac5-aab0-cacc4e52a0d1)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Wykresy 5.5 i 5.6 ilustrują podział państw na grupy względem miernika syntetycznego (qi) dla obu metod obsłużenia obserwacji odstających.

**Wykres 5.5** *Podział państw na grupy względem miernika syntetycznego (qi) obliczonego metodą STRAHL dla danych przybliżonych metodą winsoryzacji*

**Wykres 5.6** *Podział państw na grupy względem miernika syntetycznego (qi) obliczonego metodą NOWAK dla danych przybliżonych metodą k-sąsiadów (k=5)*




## 6. Podsumowanie

## 7. Bibliografia
