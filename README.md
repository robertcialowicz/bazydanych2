# bazydanych2
## Projekt:
Python + Django + MSSQL + Northwind
## Authors:
Chwała Paweł <pchwala@student.agh.edu.pl>
Ciałowicz Robert <robcial@student.agh.edu.pl>
Kozaczkiewicz Łukasz <kozaczki@student.agh.edu.pl>
Szpila Magdalena <mszpila@student.agh.edu.pl>
## Struktura projektu:
 -> `./docu` dokumentacja projektu, przewodnik po projekcie
 -> `./meeting_minutes` notatki ze spotkań
 -> `./presentations` prezentacje pokazywane podczas zajęć
 -> `./src` pliki źródłowe projektu
 ## Opis
Aplikacja napisana w języku Python z wykorzystaniem Django Rest Framework.
W projekcie wykorzystano serwer bazy danych MSSql.
Przykładową bazą, na której wykonywane będą operacje jest baza Northwind.
Celem projektu jest zaimplementowanie operacji CRUD na dowolnej tabeli, operacji składania zamówienia oraz możliwość tworzenia raportów (do zdefiniowania).
 ## Uruchamianie
 W lokalizacji `./src` przygotowany jest plik docker-compose.yml uruchamiający niezbędne środowisko. Aby uruchomić należy w lokalizacji `./src` wywołać następującą komendę:
```
docker-compose up --build -d
```
