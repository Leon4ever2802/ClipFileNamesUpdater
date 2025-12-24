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
- 📁 **Rekursive Verarbeitung**: Durchsucht alle Unterordner nach "Cutted"-Verzeichnissen
- 🎯 **Spiel-Aliases**: Optionale Unterstützung für benutzerdefinierte Spielnamen (z.B. "Counter-strike 2" → "CS2")

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
    "Counter-strike  Global Offensive": "CSGO",
    "Counter-strike 2": "CS2",
    "Grand Theft Auto V": "GTA5",
    "Red Dead Redemption 2": "RDR2"
}
```

## 🎯 Verwendung

### Grundlegende Ausführung

```bash
python main.py
```

## 🧪 Tests ausführen

```bash
# Alle Tests
python -m unittest discover -s tests -p "test_*.py" -v

# Spezifische Testdatei
python -m unittest tests.test_adapt_file_names -v
```

## ⚠️ Wichtige Hinweise

- **Backup empfohlen**: Erstellen Sie eine Sicherungskopie Ihrer Clips vor der ersten Ausführung
- **Pfad-Anforderungen**: Das Tool sucht nur in Ordnern namens "Cutted"
- **Bereits umbenannte Dateien**: Werden automatisch übersprungen
- **Ungültige Formate**: Dateien mit unerkannten Namensmustern werden übersprungen

## 📄 Lizenz

Dieses Projekt steht unter der [MIT Lizenz](LICENSE).

## 🐛 Fehlerbehebung

### Häufige Probleme

**Problem**: "No filename updates made" für alle Dateien
- **Lösung**: Überprüfen Sie den `GAME_CLIPS_PATH` in der `.env` Datei
- **Lösung**: Stellen Sie sicher, dass Ihre geschnittenen Clips in "Cutted"-Ordnern liegen

**Problem**: Bestimmte Dateien werden nicht umbenannt
- **Lösung**: Überprüfen Sie das Dateinamenformat - es muss dem GeForce Experience Schema entsprechen

**Problem**: ModuleNotFoundError
- **Lösung**: Führen Sie `pip install -r requirements.txt` aus

### Debug-Modus

Für detaillierte Informationen können Sie das Logging aktivieren oder die Tests als Referenz verwenden:

```bash
python -m unittest tests.test_adapt_file_names.TestAdaptMP4FileNames.test__should_adapt_mp4_file_name -v
```


