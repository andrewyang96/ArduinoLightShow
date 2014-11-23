ArduinoLightShow
================

Hack with Arduino and PyDub at WildHacks 2014.
Tested with Arduino Uno. Check pics folder for configuration.
LED lights are plugged into pins 6-12.
One multicolor light is plugged into pins 3-5.

Steps
-----
1. Modify and run script.py with appropriate values. (FILENAME, CUTOFF, THRESHOLD)
2. Modify .ino template with appropriate values. (DIFFLENGTH, TRIGGERSLENGTH, length of triggers)
3. Upload .ino to Arduino.
4. Load music in your favorite music player.
5. Open Serial Monitor and press play in sync with countdown.
6. Enjoy the light show.

Future Improvements
-------------------
- Automate python script input -> .ino output **OR** modify .ino to read files.
- Remove triggers that are too close to each other.
- If possible, automatically play music in sync with lights (when program starts).