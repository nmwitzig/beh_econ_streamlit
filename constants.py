from pathlib import Path

AUTHOR = "Niklas Witzig"
CONFERENCE_DATE = "Summer 2024"
CONFERENCE_NAME = "Tutorial Behavioral Economics"
TITLE = "Additional files and tools for the JGU Behavioral Economics Tutorial"
TITLE_SHORT = "Helper Tutorial"

ROOT_DIR = Path(__file__).resolve().parent
IMAGES_DIR = ROOT_DIR / "images"
PAGES_DIR = ROOT_DIR / "pages"
CODE_SAMPLES_DIR = ROOT_DIR / "code_samples"

CONFERENCE_LOGO_PATH = IMAGES_DIR / "jgu.png"
CONFERENCE_FULL_LOGO_PATH = IMAGES_DIR / "jgu.png"

# CSS STYLES
FULL_HEIGHT_PIXELS = 760

# Pipeline code
CODE_DIR = ROOT_DIR / "src"
PIPELINE_PATH = CODE_DIR / "dvc.yaml"
PARAMS_PATH = CODE_DIR / "params.yaml"

# Pages
CHAPTER_INTRODUCTION = "Problem Set 1️⃣"
CHATER_PS2 = "Problem Set 2️⃣"
CHAPTER_PS3 = "Problem Set 3️⃣"
CHAPTER_FEEDBACK = "Feedback"

CHAPTERS = [
    CHAPTER_INTRODUCTION,
    CHAPTER_PS3,
    CHAPTER_FEEDBACK,
]
