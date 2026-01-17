## AttractMode romlist and overview generator


This Python GUI program generates romlists and an overview for the Attract-Mode frontend using the EmulationStation gamelist.xml file.

### Romlist 

* Select the gamelist.xml file.
* Enter emulator name.
* Select the output folder.
* Click on generate romlist

### Overview

* Select the gamelist.xml file.
* Select the output folder.
* Click on generate Overview


 
 Example Structure of Gamelist.xml
```xml
<gameList>
 <provider>
  <System>NES</System>
  <software>Skraper</software>
  <database>ScreenScraper.fr</database>
  <web>http://www.screenscraper.fr</web>
 </provider>
 <game id="1658" source="ScreenScraper.fr">
  <path>./10-Yard Fight (USA, Europe).zip</path>
  <name>10-Yard Fight</name>
  <desc>10-Yard Fight..... Fight.</desc>
  <rating>0.4</rating>
  <releasedate>19851206T000000</releasedate>
  <developer>Irem</developer>
  <publisher>Nintendo</publisher>
  <genre>Sports / Football (American)-Sports</genre>
  <players>1-2</players>
  <hash>C986CDA2</hash>
  <genreid>1538</genreid>
 </game>`
</gamelist>
```
Used ScreenScraper(SkraperUI) to generate gamelist xml type: `EMULATIONSTATION GAMELIST.XML`

### All dependencies are listed in `requirements.txt`


### Installation
Run : `pip install -r requirements.txt` --> `python main.py`  
Build : `pip install pyinstaller` --> `AM_RomlistandOverviewGenerator.spec`


### Links
Attract-Mode: http://attractmode.org/

