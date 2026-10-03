# Timetracking

Ein einfaches Python-Kommandozeilenprogramm zur lokalen Zeiterfassung in Markdown-Dateien. Pro Arbeitswoche entsteht ein Bericht mit Tabellen für Montag bis Freitag. Einträge enthalten einen Zeitraum, eine optionale Aktivitätskennung und eine Tätigkeitsbeschreibung („Doing“).

## Funktionen

- Wochenberichte automatisch anlegen.
- Einträge für den aktuellen Tag erfassen, interaktiv oder über Argumente.
- Einträge innerhalb eines Tages nach Startzeit sortieren.
- Vorhandene Markdown-Dateien auswählen und im Terminal anzeigen.
- Datenverzeichnis lokal konfigurieren; kein Cloud-Dienst erforderlich.

## Voraussetzungen

Python 3; für neue Installationen wird Python 3.11 oder neuer empfohlen. Die grundlegenden Abläufe wurden unter Python 3.14.7 geprüft. Weitere Python-Versionen und Betriebssysteme wurden nicht getestet.

Das Programm verwendet ausschließlich die Python-Standardbibliothek. Eine Installation zusätzlicher Pakete ist nicht erforderlich. Git wird nur zum Klonen benötigt.

## Einrichtung

```sh
git clone https://github.com/Glaeser/Timetracking.git
cd Timetracking
mkdir -p "$HOME/Timetracking-Daten"
python3 main.py --config "$HOME/Timetracking-Daten"
```

Unter Windows kann anstelle von `python3` der Python-Launcher `py` verwendet werden. Das Datenverzeichnis muss vorher angelegt werden, beispielsweise mit PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME/Timetracking-Daten"
py main.py --config "$HOME/Timetracking-Daten"
```

Verwende einen absoluten Pfad: Relative Pfade werden beim späteren Aufruf gegenüber dem aktuellen Arbeitsverzeichnis ausgewertet. Die Konfiguration liegt in `~/.timetracker_config.json` und wird bei erneuter Konfiguration überschrieben. Zeitberichte sollten außerhalb dieses Quellcode-Repositories gespeichert werden.

## Verwendung

### Eintrag mit Argumenten erfassen

```sh
python3 main.py --add 9 11 "123" "Coding"
python3 main.py --add 11.30 12.15 "" "Besprechung"
```

Die Reihenfolge lautet `Von Bis Aktivität Doing`. Aktivität und Doing sind in diesem Modus optional. Leerzeichen in einer Beschreibung erfordern Anführungszeichen. Für eine Beschreibung ohne Aktivitätskennung muss eine leere Zeichenfolge als drittes Argument angegeben werden.

Unterstützte Zeitformate sind `9`, `09:30` und `9.30`. Die Zeitangaben werden als `HH:MM` gespeichert. Einträge beziehen sich immer auf das aktuelle lokale Datum des Computers.

### Interaktiv erfassen

```sh
python3 main.py --add
```

Das Programm fragt nach Von, Bis, Aktivität und Doing.

### Bericht anzeigen

```sh
python3 main.py --list
```

Das Programm listet die `.md`-Dateien im Datenverzeichnis. Gib die angezeigte Nummer einer Datei ein, um deren Inhalt zu lesen.

### Hilfe anzeigen

```sh
python3 main.py --help
```

Verwende jeweils nur eine Aktion pro Aufruf. Bei mehreren Aktionen hat `--config` Vorrang vor `--list` und `--add`.

## Datenformat

Der Dateiname enthält Montag und Freitag der jeweiligen Woche, beispielsweise `2026-10-05 bis 2026-10-09.md`. Ein Tagesabschnitt sieht so aus:

```markdown
## Reporting 05. Oktober

Zeit            | Aktivität     | Doing
--------------- | ------------- | ------------------
09:00 - 11:00   | 123           | Coding
```

Deutsche Monatsnamen werden verwendet, sofern die deutsche System-Locale verfügbar ist. Andernfalls stammen die Monatsnamen aus der aktiven System-Locale. Die Berichte können in einem Markdown-Editor gelesen und bearbeitet werden. Überschriften und Tabellenstruktur sollten dabei erhalten bleiben, damit weitere Einträge korrekt zugeordnet werden.

## Bekannte Einschränkungen

- Die Wochenvorlage enthält nur Montag bis Freitag. Wochenend-Einträge werden derzeit am Dateiende angehängt, ohne eigenen Tagesabschnitt.
- Leere oder fehlende Datenverzeichnisse und ungültige Dateiauswahlen können beim Auflisten zu Fehlern führen.
- Die Zeitprüfung ist unvollständig: Negative Werte, falsche Formate, Endzeiten vor Startzeiten und Überschneidungen werden nicht zuverlässig abgefangen.
- Senkrechte Striche (`|`) und Zeilenumbrüche in Beschreibungen werden nicht für Markdown maskiert.
- Gleichzeitige Schreibzugriffe werden nicht abgesichert. Es gibt keine automatische Sicherung, keine Dauerberechnung und keine nachträgliche Datumswahl.
- Das Projekt besitzt derzeit keine automatisierten Tests oder CI-Konfiguration.

## Projektstruktur

| Datei | Aufgabe |
| --- | --- |
| `main.py` | Argumente auswerten und Aktionen starten |
| `cli.py` | Benutzereingaben und CLI-Aktionen |
| `config.py` | Datenverzeichnis laden und speichern |
| `storage.py` | Wochenberichte lesen, erstellen und aktualisieren |
| `utils.py` | Datums-, Zeit- und Tabellenformatierung |

## Mitwirken

Fehlerberichte und Pull Requests sind willkommen. Beschreibe bei Fehlern den verwendeten Aufruf, die Python-Version und das Betriebssystem. Nutze anonymisierte Beispieldaten, keine echten Arbeitsberichte oder Zugangsdaten.

## Lizenz

Copyright © 2026 Sebastian Gläser. Das Projekt steht unter der [MIT-Lizenz](LICENSE). Sie erlaubt auch kommerzielle Nutzung und Änderungen, sofern der Copyright- und Lizenzhinweis erhalten bleibt.
