# ClipFileNamesUpdater

Ein Python-Tool zum automatischen Umbenennen von Spielaufnahmen (Clips) von GeForce Experience in ein einheitliches und strukturiertes Dateinamensformat.

## 📝 Über das Projekt

GeForce Experience erstellt beim Aufnehmen von Spielhighlights Dateien mit inkonsistenten Namensformaten wie:
- `Cool Game 2023.08.15.mp4`
- `Cool Game Screenshot 2023.08.15.png`

Dieses Tool benennt sie automatisch in ein strukturiertes Format um:
- `Cool_Game_2023-08-15.mp4`
- `Cool_Game_Screenshot_2023-08-15.png`

## ✨ Features

- 🎮 **Automatische Erkennung**: Erkennt MP4-Videos und PNG-Screenshots
- 📁 **Sichere Verarbeitung**: Verarbeitet **nur** Dateien in "Cutted"-Ordnern (schützt ungeschnittene Original-Clips)
- 🔄 **Rekursive Suche**: Durchsucht alle Unterordner nach "Cutted"-Verzeichnissen
- 🎯 **Spiel-Aliases**: Optionale Unterstützung für benutzerdefinierte Spielnamen (z.B. "Counter-strike 2" → "CS2")
- 🛡️ **Intelligente Filterung**: Überspringt bereits korrekt benannte Dateien
- 📊 **Detaillierte Ausgabe**: Zeigt alle Änderungen und Statistiken an

## 🚀 Installation

### Voraussetzungen

- Python 3.8 oder höher
- pip (Python Package Manager)

### Setup

1. **Repository klonen:**
   ```bash
   git clone https://github.com/yourusername/ClipFileNamesUpdater.git
   cd ClipFileNamesUpdater
   ```

2. **Dependencies installieren:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Umgebungskonfiguration erstellen:**
   ```bash
   cp .env.example .env
   ```

## ⚙️ Konfiguration

### 1. Umgebungsvariablen (.env)

Bearbeite die `.env` Datei mit deinen Einstellungen:

```env
# Absoluter Pfad zu deinem GeForce Experience Clips Ordner
GAME_CLIPS_PATH=/path/to/your/GeForce Experience/game/clips

# Aktiviere Spielnamen-Ersetzungen (optional)
ENABLE_REPLACEMENT_NAMES=true
```

**Beispiel für Windows:**
```env
GAME_CLIPS_PATH=C:\Users\Username\Videos\GeForce Experience
ENABLE_REPLACEMENT_NAMES=false
```

**Beispiel für macOS/Linux:**
```env
GAME_CLIPS_PATH=/Users/username/Videos/GeForce Experience
ENABLE_REPLACEMENT_NAMES=false
```

### 2. Spielnamen-Ersetzungen (Optional)

Bearbeite `src/replacement_dict.py` um benutzerdefinierte Spielnamen hinzuzufügen:

```python
known_games = {
    "Ark Survival Evolved": "ARK",
    "Counter-strike  Global Offensive": "CSGO",
    "Counter-strike 2": "CS2",
    "Escape from Tarkov": "EFT",
    "Escape from Tarkov Arena": "EFT Arena",
    "League of Legends": "LoL",
    "Mount & Blade II Bannerlord": "Bannerlord",
    "Tom Clancy's Ghost Recon Wildlands": "Wildlands",
    "Tom Clancy's Rainbow Six Siege": "R6",
}
```

## 🎯 Verwendung

### ⚠️ Wichtig: Datei-Organisation

**Das Tool verarbeitet NUR Dateien in "Cutted"-Ordnern!** Dies ist eine bewusste Sicherheitsmaßnahme, um zu verhindern, dass ungeschnittene Original-Clips versehentlich umbenannt werden.

**Typische Ordnerstruktur:**
```
GeForce Experience/
├── Game Name 1/
│   ├── Game Name 1 2024.08.15.mp4               # ❌ Diese werden NICHT verarbeitet
│   ├── Game Name 1 Screenshot 2024.08.15.png    # ❌ Diese werden NICHT verarbeitet
│   └── Cutted/                                  # ✅ Nur diese werden umbenannt
│       ├── Game Name 1 2023.08.15.mp4
│       └── Game Name 1 Screenshot 2023.08.15.png
└── Game Name 2/
    ├── Game Name 2 2024.08.15.mp4               # ❌ Diese werden NICHT verarbeitet
    ├── Game Name 2 Screenshot 2024.08.15.png    # ❌ Diese werden NICHT verarbeitet
    └── Cutted/                                  # ✅ Nur diese werden umbenannt
        └── Game Name 2 2023.08.16.mp4
```

### Grundlegende Ausführung

```bash
python main.py
```

### Beispiel-Ausgabe

```
Checking game clips inside: /path/to/clips/Cool Game/Cutted
	Renamed: Cool Game 2023.08.15.mp4 → Cool_Game_2023-08-15.mp4
	Renamed: Cool Game Screenshot 2023.08.15.png → Cool_Game_Screenshot_2023-08-15.png

Checking game clips inside: /path/to/clips/Another Game/Cutted
	Renamed: Another Game 2022.12.01_extra_info.mp4 → Another_Game_2022-12-01_extra_info.mp4
	No filename updates made.

4 files were updated.
```

## 📋 Unterstützte Dateiformate und Namensmuster

### 🎬 Video-Dateien (.mp4)

Das Tool erkennt und konvertiert folgende MP4-Dateienamensmuster:

**Basis-Format (GeForce Experience Standard):**
```
Eingabe:  Game Name 2023.08.15.mp4
Ausgabe:  Game_Name_2023-08-15.mp4
```

**Mit zusätzlichen Informationen:**
```
Eingabe:  Game Name 2023.08.15_extra_info.mp4
Ausgabe:  Game_Name_2023-08-15_extra_info.mp4
```

**Mit GeForce Experience Zusatztext (wird entfernt):**
```
Eingabe:  Game Name 2023.08.15 - 00.23.54.12.DVR.mp4
Ausgabe:  Game_Name_2023-08-15.mp4

Eingabe:  Game Name 2023.08.15_custom_info - 00.23.54.12.DVR.mp4
Ausgabe:  Game_Name_2023-08-15_custom_info.mp4
```

### 🖼️ Screenshot-Dateien (.png)

Das Tool erkennt und konvertiert folgende PNG-Dateienamensmuster:

**Basis-Format (GeForce Experience Standard):**
```
Eingabe:  Game Name Screenshot 2023.08.15.png
Ausgabe:  Game_Name_Screenshot_2023-08-15.png
```

**Mit zusätzlichen Informationen:**
```
Eingabe:  Game Name Screenshot 2023.08.15_boss_fight.png
Ausgabe:  Game_Name_Screenshot_2023-08-15_boss_fight.png
```

**Mit GeForce Experience Zusatztext (wird entfernt):**
```
Eingabe:  Game Name Screenshot 2023.08.15 - Kopie.png
Ausgabe:  Game_Name_Screenshot_2023-08-15.png
```

### 🚫 Nicht unterstützte Formate

Diese Dateien werden **übersprungen** und nicht umbenannt:

```
❌ Game Name 22.12.01.mp4          # Falsches Datumsformat (YY statt YYYY)
❌ InvalidFileName.mp4             # Kein erkanntes Muster
❌ Game_Name_2023-08-15.mp4        # Bereits korrekt formatiert
❌ Game Name 2023.08.15.avi        # Nicht unterstütztes Format
❌ Screenshot 2023.08.15.png       # Kein Spielname vorhanden
```

## 🧪 Tests ausführen

```bash
# Alle Tests
python -m unittest discover -s tests -p "test_*.py" -v

# Spezifische Testdatei
python -m unittest tests.test_adapt_file_names -v
```

## ⚠️ Wichtige Hinweise

- **🔒 Sicherheit durch "Cutted"-Ordner**: Das Tool verarbeitet ausschließlich Dateien in Ordnern namens "Cutted". Dies schützt Ihre ungeschnittenen Original-Clips vor versehentlichen Umbenennungen
- **Backup empfohlen**: Erstellen Sie eine Sicherungskopie Ihrer Clips vor der ersten Ausführung
- **Ordner-Struktur beachten**: Stellen Sie sicher, dass Ihre bearbeiteten Clips in "Cutted"-Ordnern liegen
- **Bereits umbenannte Dateien**: Werden automatisch übersprungen
- **Ungültige Formate**: Dateien mit unerkannten Namensmustern werden übersprungen

## 📄 Lizenz

Dieses Projekt steht unter der [MIT Lizenz](LICENSE).

## 🐛 Fehlerbehebung

### Häufige Probleme

**Problem**: "No filename updates made" für alle Dateien
- **Lösung**: Überprüfen Sie den `GAME_CLIPS_PATH` in der `.env` Datei
- **Lösung**: Stellen Sie sicher, dass Ihre geschnittenen Clips in "Cutted"-Ordnern liegen
- **Lösung**: Prüfen Sie, ob die Ordnerstruktur korrekt ist (Dateien müssen in einem Unterordner namens "Cutted" liegen)

**Problem**: Bestimmte Dateien werden nicht umbenannt
- **Lösung**: Überprüfen Sie das Dateinamenformat - es muss dem GeForce Experience Schema entsprechen
- **Lösung**: Stellen Sie sicher, dass sich die Dateien in einem "Cutted"-Ordner befinden

**Problem**: Tool findet keine Dateien
- **Lösung**: Überprüfen Sie, ob Ihre Clips in Ordnern namens "Cutted" organisiert sind
- **Lösung**: Das Tool ignoriert bewusst alle anderen Ordner zum Schutz unbearbeiteter Clips

**Problem**: ModuleNotFoundError
- **Lösung**: Führen Sie `pip install -r requirements.txt` aus

### Debug-Modus

Für detaillierte Informationen können Sie das Logging aktivieren oder die Tests als Referenz verwenden:

```bash
python -m unittest tests.test_adapt_file_names.TestAdaptMP4FileNames.test__should_adapt_mp4_file_name -v
```


