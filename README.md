# RealAndoridBot

[![RAB Video Demo](https://img.youtube.com/vi/wtpJ9_av-qc/0.jpg)](https://www.youtube.com/watch?v=wtpJ9_av-qc)

## Changelog
### RAB 1.09

Note that for this version, manual installation will need to re-run `pip install -r requirement.txt`. You will also need to update your Source Defender by running `pip install sourcedefender -U`. You are also advised to delete your exisiting config.yaml before running the bot.

This version has multi-language support (GUI Only). If anyone interested to translate the GUI to your onw language, a german language example has been included in lang.yaml and you can use notepad++ to copy and paste to the end and change it your language.

Don't forget to send me a copy so that I can include it in next version.

- Fixed: RAB will mistaken pokemon still in catch page as caught/flee for quick catch users
- Fixed: pytesseract not found message for exe version
- Fixed: When there's a quest pokemon caught being done, RAB will ALWAYS click on pokeball. This is fixed
- Fix: Polygon will not auto close pokestop if it's under cooldown
- Bug Fix: Much quicker response time after catching a pokemon in quick catch (instant transfer) mode
- Added Graphical User Interface
- Multi-language support (GUI Only), German example is in current version (translated with Google Translate)
- Attempt to fix not getting Level
- RAB is now able to determine if a Pokemon is caught in quick catch mode. PGSharp user please enable caught preview.
- Config.example is now in rab folder
- RAB will auto create config.yaml if not found
- Attempt to fix stuck at team rocket leader
- Added learning ability to aid in identifying Pokemon (slightly more accurate over time)
- Attempt to fix not identifying poke ball on Windows machine
- Added `notify_all_caught` option to Discord webhook
- Updated getting IV from Appraisal. Should have improved results than v1.08
- Minor refinement of clicking positions
- If `power_up_lvl` is 0, RAB will now delete power quest
- Added Pokemon tracking for PGSharp and Pure GPS Joystick users (Client = None). This might not work all the time especially when the Pokemon starts to move before RAB can located it’s location
- Shiny was previously not reported to web hook in v1.08, this is fixed.
- RAB will now detect 0 balls. Will quit catch screen
- Added detection for 12 km egg
- RAB will quit if Pokemon Go is no longer running on phone.
- Added `last_quest_quit_today` option. RAB will move on when it encounter this given text in Today’s quest page. You are strongly advise to set `last_quest_quit_today`, `last_quest_quit` and `last_item_quit` if RAB get suck in these screens.
- Console will now show caught information for Polygon # paid user (Exp, candies,XL and stardust earned)


[Changelog History](https://github.com/MerlionRock/RealAndroidBot/blob/master/Changelog.md)

## Discord
Join our [Discord Channel](https://discord.gg/Xw2DKBhRJu)

## Features
- Auto Catch
- Auto Keep or Transfer base on IV (100 or PvP)
- Auto Select Berries
- Auto Select Balls
- Auto Clear Quests
- Auto Hatch
- Auto Item management
- (NEW) Auto Pokemon Bag management
- Auto Team Rocket Battle (HAL & Polygon# Only)
- Integration with Telegram feed to allow PvP/100IV Snipe (Not Live Yet)
- Integration with Telegram feed to allow Shiny Checking (Not Live Yet)
- Non rooted support with PGSharp Free or Paid version (**NO NOT USE IT ON MAIN ACCOUNT**)

## Phone Requirements
1. Rooted (Optional)
2. Your phone must be able to run Pokemon Go if it's rooted
3. USB Debugging Enabled ([Under Developer Options](https://developer.android.com/studio/debug/dev-options))
4. Phone with Screen Resolution 1080 x 1920 and above
5. Recommended 2GB RAM and above
6. Recommended Snapdragon 625 and above
7. Full screen mode (or guesture mode) without navigation butttons on screen

## System Requirements
64 bit system is required to run RAB

## Release Download

- Window users can download RAB from [here](https://github.com/MerlionRock/RealAndroidBot/releases) 
- Please read the sections below on how to setup your phone to run RAB
- There are no release version for Mac and Linux version yet. Please read on for the instructions on how to setup RAB on your system.

## Setting up USB Debugging mode option
1. Launch the Settings application on your phone.
2. Tap the About Phone option generally near the bottom of the list.
3. Then tap the Build Number option 7 times to enable Developer Mode. You will see a toast message when it is done.
4. Now go back to the main Settings screen and you should see a new Developer Options menu you can access.
5. Go in there and enable the USB Debugging mode option. Some Phones will have Install via USB option and USB debugging (Security settings) options or any options that's related simulating input, enable them too.

## Additional Apps needed and their settings

1. (Optional) Install [Pokemod or HAL](https://pokemod.dev/) or [Polygon#](https://discord.gg/QURp9gA) or [PGSharp](https://www.pgsharp.com/) Please set the correct client settings in config file
2. (Pokemod, HAL and Polygon# Only) GPS Joystick, unlock version. Download from their [official website](http://gpsjoystick.theappninjas.com/faq/) 
- (Pokemod, HAL, Polygon# Only) Create/download a GPX Route and run it in background. Make sure joystick are hidden from view.
- (PGSharp Paid Only) Create/download a GPX Route and run it. Do not hide PGSharp. Move joystick away from location that will block text.
- (Pokemod, HAL, Polygon# Only) Recommended Speed 7km per hour or less
3. (Optional, if your phone's resolution is more than 1920 x 1080) Go to playstore and download Easy DPI Changer (or https://www.apkmirror.com/apk/chornerman_studio/easy-dpi-changer-root/), resize your phone to 1080 x 1920, reset it when you are not running the script. (**Update**: The bot now auto change your phone size. However, it's handy to have this app installed in case the bot is unable to reset back your phone to orginal screen resolution.)
4. Your Pokemon Go Game MUST BE English
5. When running the scripts at your computer, the following app/services must be running on your phone
- GPS Joystick (Not needed for PGSharp)
- (optional) Pokemod, HAL, Polygon# or PGSharp
- Pokemon Go
   
## Pokemod/HAL Support

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
- Disable Block Non-Shiny Encounters 
- Disable Mass Transfer any Pokémon (To prevent accident transfer of your fav lengenary Pokemon)

### Optional Modules
- Team Rocket Blastoff (HAL Only)
- Instant Spin
- Instant Catch and Transfer on Catch (HAL Only) (When Transfer on Catch is enabled, the bot will not be able to prevent PvP eligible Pokemon from being transfered)

*Enable or disable the modules in config.yaml accordingly*

## Polygon# Enhancer (Free Version) Support

- Use `Polygon` in your config file
- Set `auto_route` in your config file to `true`
- Set a route in GPS Joystick and loop it

### Advanced
- Encounter nameplates format `{default} LVL{lvl}\nIV{prc0}% {ivs}`
- Pokemon panel nameplate format `{default}`

## Polygon# Enhancer (Paid Version) Support

- Use `Polygon Paid` in your config file
- Set `auto_route` in your config file to `false`
- Instant catch is not recommended to be disabled for Polygon#, settings related to keeping Pokemon in config will not apply to Polygon#
- Note that RAB will attempt to gather a few information from Polygon# Paid version first before starting to catch Pokemon. As such you might see RAB attempt to spin pokestops continously for a few mintues before catching. It is normal.

### Advanced
- Enable `Send data to custom backend`
- Set backend IP Address to the IP of the machine that you are running RAB
- How to find your machine's IP Guide [Windows](https://www.wikihow.com/Check-a-Computer-IP-Address) | [Mac](https://www.hellotech.com/guide/for/how-to-find-ip-address-on-mac)
- Enter a port number that you set in config. Default 5120. If you are using more than one device, each device must have their own config and with their own port number set.
- Encounter nameplates format `{default} LVL{lvl}\nIV{prc0}% {ivs}`
- Pokemon panel nameplate format `{default}`

## PGSharp Support

### Settings for Free Version
- Spoofing Enabled
- Hide PGSharp Disabled, move joystick to somewhere that wont block the screen
- Enhanced Throw on Excellent and Curved
- Tap to `Walk` Enabled. 
- Set your walking speed to less than 7km/hr
- Set a location with the Map or enter coordinates 

### Settings for Paid Version
- Spoofing Enabled
- Hide PGSharp Disabled, move joystick to somewhere that wont block the screen
- Enhanced Throw on Excellent and Curved throw is preferred for faster catching
- Tap to `Walk` or `Teleport` Disabled. 
- `Inventory IV` Enabled
- `Encounter IV` Enabled
- `Quick Catch` Optional. Set `transfer on catch` to true in RAB config if you set this option to true.
- The rest of options are optional
- Then click on PGSharp's icon and choose either auto walk or GPX route (this option is in map)

*Enable or disable the modules in config.yaml accordingly*

## PC/MAC/LINUX Requirements

Windows users who **downloaded the release version**, you just need to edit config.yaml, configure your phone and plug in to your PC and run RAB.exe will do. **You do not need to follow the steps below.** Remember to **ctrl+c** when you want to exit from RAB.

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
3. Install ADB
```
brew cask install android-platform-tools
```
4. Connect your device to your mac and run the following to see if it can detect your device
```
adb devices
```

### Linux
1. Install tesseract via apt by using the command
```
sudo apt-get install tesseract-ocr
```
2. Install adb via apt by using the command
```
sudo apt-get install adb
```


## Installing all dependencies via choclatey (Windows User Only)
- Windows user are encouraged to use the [release version](https://github.com/MerlionRock/RealAndroidBot/releases). **If you are using the release version, you do not need to follow the steps below anymore**.
- For those who don't know what choclatey is, it's just like apt-get in ubuntu/Debian if u know what it is. If u want to know more about it before you use it please visit this [link](https://chocolatey.org/) 
### Installing Choclatey
1. Open the PowerShell as administrator
2. You must ensure Get-ExecutionPolicy is not Restricted, for that you can use the following command in the powershell
   ```Set-ExecutionPolicy Unrestricted```
3. Now run the command
```
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1')) 
```

### Installing Git with choclatey and downloading RAB
1. Open PowerShell as administrator
2. Use the command ```choco install git -y``` to install git. (Type "y" and enter if it prompts to).
3. Restart your PowerShell or use the command `refreshenv`(Restarting is recommended).  
4. Enter the C drive directory by using ```cd C:\```
5. Clone this repo by using the command ```git clone --recursive https://github.com/MerlionRock/RealAndroidBot.git```
You will find the RealAndroidBot folder present in the C drive directory after executing this command 

## Setting up the project
1. (Windows Only) ==> Open the RealAndroidBot folder (Which is present in the C drive) in FileExplorer.
   - 1.1 (Ubuntu/Linux) Open terminal and type: `cd ~/`
2. (Windows Only) ==> Right click on the `Install.ps1` and select 'Run with PowerShell'
3. (Windows Only) ==> The installation will take a little time and it will prompt press any key to continue (press any key) and then u will be directed to the `PS C:\Windows\system32>` directory.
4. (Mac and Linux) Install Python 3.7 or later (https://www.python.org/downloads/)
5. (Windows Only) ==> Now use `cd C:\` and Follow by using `python3 -m venv RealAndroidBot`
Note: If your screen return python after this command, please type in this instead `python -m venv RealAndroidBot` 
(Mac and Linux) Follow the same step but skip the `cd ..` part
6. Follow by (Mac and Linux) `source RealAndroidBot/bin/activate` (Windows) `RealAndroidBot\Scripts\activate`
7. Follow by `cd RealAndroidBot`
8. Copy config.example.yaml to rab/config.yaml and configure it by using notepad++. **Do not use notepad to edit.!**
9. Back to Terminal or PowerShell, type `pip install -r requirements.txt`
10. Follow by `cd rab`
11. Setup your phone according to app requirements as instructed above and run all required apps on phone
12. Make sure your Pokemon Go is at map page and **zoomed out to the max**.
13. Make sure your device are connected to your machine, run this command in Terminal or PowerShell `python -m uiautomator2 init`. Check your phone and allow installation of automator on your Phone
14. Please ensure you have copied config.example.yaml to rab/config.yaml and configure it, then run 
   `python run.py` in your terminal or powershell
15. To run multiple devices, first run `adb devices` to get all your device ID connected to your computer
16. Then run each command on their own terminal/shell console
    `python run.py --device-id YOUR_DEVICE_ID`
17. To use a different config file (good for multiple devices setup) run
    `python run.py --device-id YOUR_DEVICE_ID --config-filename YOUR_CONFIG_FILE_NAME`
18. Ctrl + C to terminate the program (you might have to do it more than once)
19. Whenever you want to run the scripts again, remember to run Step 7 first follow by (mac/linux) `cd RealAndroidBot/rab` or (Windows) `cd RealAndroidBot\rab`
20. To update your files from github repo, type `git pull`

## Troubleshooting
**RAB Mess up my screen resolution and my navigation bar went missing!!**
Open your terminal or PowerShell, type in the following command. (press enter before entering the other)
`adb shell wm size reset`
`adb shell wm density reset`
`adb shell wm overscan 0,0,0,0`

To prevent it from happening again, always use ctrl+c to close RAB

**After entering python run.py, nothing happens or it ask me to install requirements.text when all requirements are already installed**

Please ensure that you have installed the required software. Tesseract and adb needs to be installed. 

If you are sure you have installed adb, follow [this guide](https://www.xda-developers.com/adb-fastboot-any-directory-windows-linux/) to add adb to your system path

If all required are install and you still did not see anything, make sure you have done step 9 correctly.

Additional Steps to if it still doesn't help:
1. Update your pip by using: python -m pip install --upgrade pip
2. Reinstall your requirements, cd c:\RealAndroidBot follow by pip install -r requirements.txt

RAB only works with 64bit system. You can't run RAB if you run a 32bit system.

Lastly, for Windows users, when all options failed, just use the .exe version found [here](https://github.com/MerlionRock/RealAndroidBot/releases) 

## Disclaimer
©2016 Niantic, Inc. ©2016 Pokémon. ©1995–2016 Nintendo / Creatures Inc. / GAME FREAK inc. © 2016 Pokémon/Nintendo Pokémon and Pokémon character names are trademarks of Nintendo. Other trademarks are the property of their respective owners.
[Privacy Policy](http://www.pokemon.com/us/privacy-policy/)

[RealAndroidBot](https://github.com/MerlionRock/RealAndroidBot) is intended for academic purposes and should not be used to play the game *PokemonGo* as it is unfair to the community. Use the bot **at your own risk**.
