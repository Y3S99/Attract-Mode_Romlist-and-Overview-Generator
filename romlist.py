import xml.etree.ElementTree as ET
import re

#header file for AM
HEADER = (
    "#Name;Title;Emulator;CloneOf;Year;Manufacturer;Category;Players;"
    "Rotation;Control;Status;DisplayCount;DisplayType;AltRomname;"
    "AltTitle;Extra;Buttons\n"
)

def genrate_rom(file_path,emulator_name,out,log):
    if not file_path:
        log("No file selected")
        return None
    #file error handling 
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
    count=0
    log("Emulator Name:"+emulator_name)
    log("Creating Romlist........")
    #file creation
    with open(out+"/"+emulator_name+'.txt', 'w', encoding='utf-8') as f:
        f.write(HEADER) 

        for game in root.iterfind('game'):

            path = (game.findtext('path') or '').strip()
            if path:
                path = re.sub(r'^[.][\\/]', '', path)  # remove leading ./ or .\
                path = re.sub(r'\.[^.]*$', '', path)   # remove file extension

            name = (game.findtext('name') or '').strip()
            developer = (game.findtext('developer') or '').strip()
            genre = (game.findtext('genre') or '').strip()
            players = (game.findtext('players') or '').strip()

            releasedate_text = game.findtext('releasedate') or ''
            match = re.match(r'\d{4}', releasedate_text)
            releasedate = match.group(0) if match else ''

            line = (
                f"{path};{name};{emulator_name};;{releasedate};"
                f"{developer};{genre};{players}"
                ";;;;;;;;;;;;;;;;;;\n"
            )
            count+=1
            f.write(line)
    log(f"Total roms:{count}")
    log("Completed!!!")
