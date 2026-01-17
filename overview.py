import xml.etree.ElementTree as ET
import re
from pathlib import Path

from pathlib import Path

def make_dir(outpath,log):
    base = Path(outpath)
    if not base.exists():
        log("path doesn't exit")
        return

    overview = base / "overview"
    overview.mkdir(parents=True, exist_ok=True)
    log("overview folder created")


def genrate_overview(file_path,out,log):
    if not file_path:
        log("No file selected")
        return None

    try:
        tree = ET.parse(file_path)

    except FileNotFoundError:
        log("File not found")
        return

    except ET.ParseError as e:
        log(f"Invalid XML file: {e}")
        return

    except PermissionError:
        log("Permission denied")
        return

    except Exception as e:
        log(f" Unexpected error: {e}")
        return

    root = tree.getroot()

    make_dir(out,log)
    count=0
    log("Creating Overview........")
    for game in root.iterfind('game'):

        # get desc
        desc = game.findtext('desc')
        if not desc or not desc.strip():
            # no <desc> tag or empty skip file creation
            continue

        # path (remove extension)
        path_elem = game.find('path')
        path = path_elem.text if path_elem is not None else ''

        if not path:
            continue

        # remove leading ./ or .\
        path = re.sub(r'^[.][\\/]', '', path)
        # remove file extension
        path = re.sub(r"\.[^.]*$", "", path)

        # write file only when desc is valid
        with open(f"{out}/overview/{path}.txt", 'w', encoding='utf-8') as f:
            f.write(
                desc.replace("&quot;", "\"")
                .replace("&gt;", ">")
                .replace("&lt;", "<")
                .replace("&amp;", "&")
            )
            log(f"Created: {path}.txt")
            count+=1
    log(f"Total Overviews:{count}")
    log("Completed!!!")