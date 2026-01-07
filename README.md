# ClipFileNamesUpdater

A Python tool for automatically renaming game recordings (clips) from GeForce Experience to a consistent and structured filename format.

## 📝 About the Project

GeForce Experience creates files with inconsistent naming formats when recording game highlights, such as:
- `Cool Game 2023.08.15 - 12.64.12.75.DVR.mp4`
- `Cool Game Screenshot 2023.08.15 - 12.64.12.75.DVR.png`

This tool automatically renames them to a structured format and removes the GeForce Experience timestamps and DVR suffixes:
- `Cool_Game_2023-08-15.mp4`
- `Cool_Game_Screenshot_2023-08-15.png`

## ✨ Features

- 🎮 **Automatic Detection**: Recognizes MP4 videos and PNG screenshots
- 🧹 **Clean Filenames**: Removes GeForce Experience metadata (timestamps, DVR suffixes)
- 📁 **Safe Processing**: Processes **only** files in "Cutted" folders (protects unedited original clips)
- 🔄 **Recursive Search**: Searches all subfolders for "Cutted" directories
- 🎯 **Game Aliases**: Optional support for custom game names (e.g., "Counter-strike 2" → "CS2")
- 🛡️ **Smart Filtering**: Skips already correctly named files
- 📊 **Detailed Output**: Shows all changes and statistics

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python Package Manager)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ClipFileNamesUpdater.git
   cd ClipFileNamesUpdater
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create environment configuration:**
   ```bash
   cp .env.example .env
   ```

## ⚙️ Configuration

### 1. Environment Variables (.env)

Edit the `.env` file with your settings:

```env
# Absolute path to your GeForce Experience clips folder
GAME_CLIPS_PATH=/path/to/your/GeForce Experience/game/clips

# Enable game name replacements (optional)
ENABLE_REPLACEMENT_NAMES=true
```

**Example for Windows:**
```env
GAME_CLIPS_PATH=C:\Users\Username\Videos\GeForce Experience
ENABLE_REPLACEMENT_NAMES=false
```

**Example for macOS/Linux:**
```env
GAME_CLIPS_PATH=/Users/username/Videos/GeForce Experience
ENABLE_REPLACEMENT_NAMES=false
```

### 2. Game Name Replacements (Optional)

Edit `src/replacement_dict.py` to add custom game names:

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

## 🎯 Usage

### ⚠️ Important: File Organization

**The tool processes ONLY files in "Cutted" folders!** This is a deliberate safety measure to prevent unedited/uncutted original clips from being accidentally renamed.

**Typical folder structure:**
```
GeForce Experience/
├── Game Name 1/
│   ├── Game Name 1 2024.08.15.mp4               # ❌ These will NOT be processed
│   ├── Game Name 1 Screenshot 2024.08.15.png    # ❌ These will NOT be processed
│   └── Cutted/                                  # ✅ Only these will be renamed
│       ├── Game Name 1 2023.08.15.mp4
│       └── Game Name 1 Screenshot 2023.08.15.png
└── Game Name 2/
    ├── Game Name 2 2024.08.15.mp4               # ❌ These will NOT be processed
    ├── Game Name 2 Screenshot 2024.08.15.png    # ❌ These will NOT be processed
    └── Cutted/                                  # ✅ Only these will be renamed
        └── Game Name 2 2023.08.16.mp4
```

### Basic Usage

```bash
python main.py
```

### Example Output

```
Checking game clips inside: /path/to/clips/Cool Game/Cutted
	Renamed: Cool Game 2023.08.15 - 12.64.12.75.DVR.mp4 → Cool_Game_2023-08-15.mp4
	Renamed: Cool Game Screenshot 2023.08.15 - 12.64.12.75.DVR.png → Cool_Game_Screenshot_2023-08-15.png

Checking game clips inside: /path/to/clips/Another Game/Cutted
	Renamed: Another Game 2022.12.01_extra_info - 12.64.12.75.DVR.mp4 → Another_Game_2022-12-01_extra_info.mp4
	No filename updates made.

4 files were updated.
```

## 📋 Supported File Formats and Naming Patterns

### 🎬 Video Files (.mp4)

The tool recognizes and converts the following MP4 filename patterns:

**Basic Format (GeForce Experience Standard):**
```
Input:  Game Name 2023.08.15 - 12.64.12.75.DVR.mp4
Output: Game_Name_2023-08-15.mp4
```

**With Additional Information:**
```
Input:  Game Name 2023.08.15_extra_info - 12.64.12.75.DVR.mp4
Output: Game_Name_2023-08-15_extra_info.mp4
```

### 🖼️ Screenshot Files (.png)

The tool recognizes and converts the following PNG filename patterns:

**Basic Format (GeForce Experience Standard):**
```
Input:  Game Name Screenshot 2023.08.15 - 12.64.12.75.DVR.png
Output: Game_Name_Screenshot_2023-08-15.png
```

**With Additional Information:**
```
Input:  Game Name Screenshot 2023.08.15_boss_fight - 12.64.12.75.DVR.png
Output: Game_Name_Screenshot_2023-08-15_boss_fight.png
```

### 🧹 GeForce Experience Metadata Removal

**Important**: The tool automatically detects and removes GeForce Experience timestamps and DVR suffixes from any filename. Common patterns that get removed include:
- `- 12.64.12.75.DVR` (timestamp + DVR suffix)
- `- 00.23.54.12.DVR` (different timestamp format)
- `- Copy` (duplicate file suffix)
- Any trailing text after the date that doesn't match the expected pattern

This ensures clean, consistent filenames regardless of GeForce Experience's automatic naming conventions.

### 🚫 Unsupported Formats

Example files which will be **skipped** and not renamed:

```
❌ Game Name 22.12.01.mp4          # Wrong date format (YY instead of YYYY)
❌ InvalidFileName.mp4             # No recognized pattern
❌ Game_Name_2023-08-15.mp4        # Already correctly formatted
❌ Game Name 2023.08.15.avi        # Unsupported format
❌ Screenshot 2023.08.15.png       # No game name present
```

## 🧪 Running Tests

```bash
# All tests
python -m unittest discover -s tests -p "test_*.py" -v

# Specific test file
python -m unittest tests.test_adapt_file_names -v
```

## ⚠️ Important Notes

- **🔒 Safety through "Cutted" folders**: The tool exclusively processes files in folders named "Cutted". This protects your unedited original clips from accidental renaming
- **Backup recommended**: Create a backup of your clips before first execution
- **Folder structure matters**: Make sure your edited clips are located in "Cutted" folders
- **Already renamed files**: Are automatically skipped
- **Invalid formats**: Files with unrecognized naming patterns will be skipped

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🐛 Troubleshooting

### Common Issues

**Issue**: "No filename updates made" for all files
- **Solution**: Check the `GAME_CLIPS_PATH` in the `.env` file
- **Solution**: Make sure your edited clips are in "Cutted" folders
- **Solution**: Verify that the folder structure is correct (files must be in a subfolder named "Cutted")

**Issue**: Certain files are not being renamed
- **Solution**: Check the filename format - it must follow the GeForce Experience schema
- **Solution**: Make sure the files are in a "Cutted" folder

**Issue**: Tool doesn't find any files
- **Solution**: Check if your clips are organized in folders named "Cutted"
- **Solution**: The tool deliberately ignores all other folders to protect unedited clips

**Issue**: ModuleNotFoundError
- **Solution**: Run `pip install -r requirements.txt`

### Debug Mode

For detailed information, you can enable logging or use the tests as reference:

```bash
python -m unittest tests.test_adapt_file_names.TestAdaptMP4FileNames.test__should_adapt_mp4_file_name -v
```


