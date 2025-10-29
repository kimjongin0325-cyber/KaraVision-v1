from pathlib import Path

ROOT = Path(__file__).parent.parent


RESOURCES_DIR = ROOT / "resources"
kara_MARK_TEMPLATE_IMAGE_PATH = RESOURCES_DIR / "karamark_template.png"

kara_MARK_DETECT_YOLO_WEIGHTS = RESOURCES_DIR / "best.pt"

OUTPUT_DIR = ROOT / "output"

OUTPUT_DIR.mkdir(exist_ok=True, parents=True)


DEFAULT_karaMARK_REMOVE_MODEL = "lama"

WORKING_DIR = ROOT / "working_dir"
WORKING_DIR.mkdir(exist_ok=True, parents=True)

LOGS_PATH = ROOT / "logs"
LOGS_PATH.mkdir(exist_ok=True, parents=True)

DATA_PATH = ROOT / "data"
DATA_PATH.mkdir(exist_ok=True, parents=True)

SQLITE_PATH = DATA_PATH / "db.sqlite3"
