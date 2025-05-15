# for getting custom logger
import logging
# redirect stdout
import sys
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo


def get_logger(filepath: Path):
    """
        Define logger to write logs in specific file.
        mode='a' is appending if file already exists
    """
    logging.basicConfig(
        level=logging.INFO,
        encoding='utf-8',
        format="[{asctime},{msecs:03.0f}]:[{levelname}]:{message}",
        datefmt='%d.%m.%Y %H:%M:%S',
        style='{',
        handlers=[
            logging.FileHandler(filepath, mode='a'),
            logging.StreamHandler(sys.stdout),
        ]
    )
    logging.Formatter.converter = lambda *args: datetime.now(tz=ZoneInfo('UTC')).timetuple()
