# Bibliotheksverwaltungssystem (OOP mit Vererbung + Speicherung)

## Projektbeschreibung

Dieses Projekt ist ein objektorientiertes Bibliotheksverwaltungssystem, das in Python entwickelt wurde. Es ermöglicht die umfassende Verwaltung verschiedener Medientypen und Benutzer in mehreren Bibliotheken.

### Hauptfunktionen

- **Medienverwaltung**: Verwaltung von Büchern, Zeitschriften und digitalen Medien
- **Nutzerverwaltung**: Registrierung und Verwaltung von Bibliotheksbenutzern
- **Ausleihe und Rückgabe**: Vollständiges Ausleihsystem mit Verfügbarkeitsprüfung
- **Mehrere Bibliotheken**: Unterstützung für die Verwaltung verschiedener Bibliothekszweigstellen
- **Datenspeicherung**: Speicherung aller Daten in JSON-Dateien für dauerhafte Verfügbarkeit

### Technische Umsetzung

Das System nutzt objektorientierte Programmierung mit Vererbung:
- Basisklasse `Medium` mit spezialisierten Unterklassen für verschiedene Medientypen
- Klasse `Nutzer` für die Benutzerverwaltung
- Klasse `Verwaltung` als zentrale Administrationsstelle für die Benutzer- und Medienverwaltung
- Konsolenbasierte Benutzeroberfläche für eine einfache Bedienung

### Projektstruktur

- `classes/`: Kernklassen des Systems (Medium, Buch, Zeitschrift, DigitalesMedium, Nutzer, Verwaltung)
- `konsolenmenue/`: Konsolenmenülogik
- `verwaltungen/`: JSON-Dateien für verschiedene Bibliotheken
- `verwaltungen.json`: Zentrale JSON-Datei mit einer Liste aller registrierten Bibliotheksnamen als JSON-Array

### Genutzte Python Packages

- **typing**: Für Type Hints zur besseren Codequalität und Dokumentation
- **abc** (Abstract Base Classes): Zur Definition abstrakter Basisklassen und Interfaces
- **re**: Für reguläre Ausdrücke zur Validierung von Eingaben
- **os**: Für Dateisystem-Operationen und Pfadverwaltung
- **json**: Zur Serialisierung und Deserialisierung der Daten in JSON-Format
- **questionary**: Für interaktive Konsolen-Menüs mit verbesserter Benutzerfreundlichkeit
