# twb-to-yt-timestamp

Converts [tunawithbacon](http://tunawithbacon.com/)-formatted csv files to timestamps
for YouTube video descriptions.

## How to use

Download the release exe from the 
[releases page](https://github.com/hugh-braico/twb-to-yt-timestamp/releases/), 
then click-and-drag TWB-formatted csv files onto it. The output will automatically be
copied to your clipboard.

## Building your own release exe

```bash
pyinstaller --onefile -i bigband.ico csv_to_stamp.py
```
