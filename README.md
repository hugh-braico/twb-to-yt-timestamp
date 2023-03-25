# twb-to-yt-timestamp

Converts [tunawithbacon](http://tunawithbacon.com/)-formatted csv files to timestamps
for YouTube video descriptions.

## How to use

Download the release exe from the 
[releases page](https://github.com/hugh-braico/twb-to-yt-timestamp/releases/), 
then click-and-drag TWB-formatted csv files onto it. The output will automatically be
copied to your clipboard.

Example output

```
Timestamps: 
0:26:09 aeroshire (PC/DB/BB) vs dekillsage (FI/CE/BB) 
0:40:58 FuLLBLeeD (MF/BB) vs ShakyFingers (RF/BB/CE) 
1:00:30 SonicFox (AN) vs PME (RF/PW/MF) 

Timestamps without teams: 
0:26:09 aeroshire vs dekillsage
0:40:58 FuLLBLeeD vs ShakyFingers
1:00:30 SonicFox vs PME
```

## Building your own release exe

```bash
pyinstaller --onefile -i bigband.ico csv_to_stamp.py
```
