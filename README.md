# RealAndoridBot
## Changelog
### RAB 1.0
- First Commit

## Features
- Auto Catch
- Keep or Transfer base on IV (100 or PvP)
- Auto Select Berries
- Auto Select Balls
- Auto Clear Quests
- Auto Hatch
- Auto Item management
- Integration with Telegram feed to allow PvP/100IV Snipe
- Integration with Telegram feed to allow Shiny Checking

## Phone Requirements
1. Magisk Rooted
2. USB Debugging Enabled (Under Developer Options)
3. Recommended phone with Screen Resolution 1080 x 1920 and above (Additional App needed for devices above 1080 x 1920)
4. 4GB RAM and above
5. Snapdragon 625 and above

## Setting up USB Debugging mode option
1. Launch the Settings application on your phone.
2. Tap the About Phone option generally near the bottom of the list.
3. Then tap the Build Number option 7 times to enable Developer Mode. You will see a toast message when it is done.
4. Now go back to the main Settings screen and you should see a new Developer Options menu you can access.
5. Go in there and enable the USB Debugging mode option.

## Additional Apps needed and their settings

1. (Optional) Install [Pokemod](https://pokemod.dev/) Please set the correct client settings in config file
2. GPS Joystick, unlock version. Download from their [official website](http://gpsjoystick.theappninjas.com/faq/)
- Create/download a GPX Route and run it in background. Make sure joystick are hidden from view.
- Recommended Speed 7km per hour or less
3. (Optional, if your phone's resolution is more than 1920 x 1080) Go to playstore and download Easy DPI Changer (or https://www.apkmirror.com/apk/chornerman_studio/easy-dpi-changer-root/), resize your phone to 1080 x 1920, reset it when you are not running the script
4. Your Pokemon Go Game MUST BE English
5. When running the scripts at your computer, the following app/services must be running on your phone
- GPS Joystick (running on a looped route)
- (optional) Pokemod Public Version or Pokemond Explorer Version
- Pokemon Go
   
## Pokemod/HAL Settings

### Settings
- (Pokemod) IV Display format --> Toast | (HAL) Enable Toasts
- (Pokemod) IV Display Information --> verbose | (HAL) Toast verbosity --> Informative
- Toast Location/Position --> Top

### Enable Modules
- Enable Prefect Throw
- Enable Skip Encounter Intro
- Enable Show Encounter IV (Enable Toasts in Settings)
- Replace Names with IVs in Encounters

### Disable Modules
- Disable Replace Names with IVs in Encounters
- Disable Block Non-Shiny Encounters 
- Disable Mass Transfer any Pokémon (To prevent accident transfer of your fav lengenary Pokemon)

### Optional Modules
- Team Rocket Blastoff (HAL Only)
- Instant Spin
- Instant Catch and Transfer on Catch (HAL Only) (When Transfer on Catch is enabled, the bot will not be able to prevent PvP eligible Pokemon from being transfered)

*Enable or disable the modules in config.yaml accordingly*

## PC/MAC/LINUX Requirements

## Install Tesseract

### Mac User
1. Install via Homebrew (https://brew.sh/)
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
2. Install Tesseract
```
brew install tesseract (install homebrew if you have not)
```

### Linux
```sudo apt-get install tesseract-ocr```

### Windows
- Install from [tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
- [Full Installation Instructions](https://tesseract-ocr.github.io/tessdoc/Home.html)


*To test if you have successfully install Tesseract, run "tesseract" at your OS's terminal/command prompt.*

## Install ADB

### Mac User

1. Using Terminal, install homebrew if you do not have it
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
2. Install adb
```
brew cask install android-platform-tools
```
3. Connect your device to your mac and run the following to see if it can detect your device
```
adb devices
```

## Windows User/Linux

Follow this Guide, follow the instructions for Windows/Linux
1. [Install ADB](https://www.xda-developers.com/install-adb-windows-macos-linux/)

Then set your ADB to PATH system variable, follow this [guide](https://www.xda-developers.com/adb-fastboot-any-directory-windows-linux/)

## Setting up the project
1. Install Python 3.7 or later (https://www.python.org/downloads/)
2. `git clone --recursive https://github.com/MerlionRock/RealAndroidBot.git`
3. `python3 -m venv RealAndroidBot`
4. `source RealAndroidBot/bin/activate`
5. `cd RealAndroidBot`
6. Copy config.example.yaml to rab/config.yaml and configure it.
7. `pip3 install -r requirements.txt`
8. `cd rab`
9. Setup your phone according to app requirements as instructed above and run all required apps on phone
10. Make sure your Pokemon Go is at map page and **zoomed out to the max**.
11. Make sure your device are connected to your machine, run this command
   `python3 run.py`
12. Allow installation of automator on your Phone
13. To run multiple devices, first run adb devices to get all your device ID connected to your computer
14. Then run each command on their own terminal/shell console
    `python3 run.py --device-id YOUR_DEVICE_ID`
15. To use a different config file (good for multiple devices setup) run
    `python3 run.py --device-id YOUR_DEVICE_ID --config-filename YOUR_CONFIG_FILE_NAME`
16. Ctrl + C to terminate the program (you might have to do it more than once)

## Disclaimer
©2016 Niantic, Inc. ©2016 Pokémon. ©1995–2016 Nintendo / Creatures Inc. / GAME FREAK inc. © 2016 Pokémon/Nintendo Pokémon and Pokémon character names are trademarks of Nintendo. Other trademarks are the property of their respective owners.
[Privacy Policy](http://www.pokemon.com/us/privacy-policy/)

[RealAndroidBot](https://github.com/MerlionRock/RealAndroidBot) is intended for academic purposes and should not be used to play the game *PokemonGo* as it is unfair to the community. Use the bot **at your own risk**.