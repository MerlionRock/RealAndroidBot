# RealAndroidBot

[![RAB Video Demo](https://img.youtube.com/vi/wtpJ9_av-qc/0.jpg)](https://www.youtube.com/watch?v=wtpJ9_av-qc)

## Changelog

### RAB 1.11.0

Note: There is no patch file for this version. You are required to download the full version.

- PGSharp: Fix “RAB will attempt to walk...” when in Auto Route (GPX) mode
- Added device id to Discord notification
- Clear Pokemon inventory flag once clear Pokemon action is done
- Improves detection for Shinx
- Added dim screen as an option 
- Fix unable to connect to Telegram issue
- If using HAL and keep Pokemon, quick catch is enabled, and a Pokemon is eligible to be kept, volume down will be triggered to disable HAL’s auto transfer for current Pokemon

### RAB 1.9.0

**BREAKING CHANGE**
From v1.7.1 onwards, PGSharp users using sniper or nearby feed, **Joystick MUST be removed** (from PGSharp option)

Note for Polygon# Enhancer users: Every enhancer feature can be now used with a free enhancer key with effect from Polygon# Version 0.8.4 

You can follow the paid instructions for Polygon# if you want backend data support.

- RAB now save a file that contain locations of device. This will help RAB to do debugging when necessary 
- Turtwig, Pidgey added to maintain throwing height list
- Minor text fix
- Location query for Google Pixel 4, android 11, fixed
- Fix `name 'lat' is not defined` error
- Will no longer check for encounter position for PGSharp Paid users
- RPC update: Fix polygon paid data issue
- Fix Mod/HAL shiny detection. RAB wrongly detect Shiny for Mod/HAL users
- Added Chase after Pokemon (Polygon Paid Only)
- Fix: Quit unknown battle
- Fix: Clear item on start when item_management is disabled
- Added Duskull detection
- Pumpkaboo and Gourgeist form and value fix

**Known Issue**

**Samsung phones is confirmed not working for the features listed below**

1. Enchanced PGSharp Mode
2. PGSharp 100IV Shiny Hunting Mode 
3. Fast identification of Pokemon caught status during encounter (Caught, Missed, Escaped, etc) 

[Changelog History](https://github.com/MerlionRock/RealAndroidBot/blob/master/Changelog.md)

## Discord
Join our [Discord Channel](https://discord.gg/Xw2DKBhRJu)

## Donation
If you simply want to bless the team, feel free to donate through

- BTC: 1Bs6sueNBYBusYYA3FKuxmyoQTV15QEM3G
- ETH: 0x3ef0faf691a78ff09622e8f06f9f88acf85a80a3

Note: The above donation is purely to bless us in our work. There will be no added benefit by donating through the above method

## Features
- Auto Catch
- Auto Keep or Transfer base on IV (100 or PvP)
- Auto Select Berries
- Auto Select Balls
- Auto Clear Quests
- Auto Hatch
- Auto Item management
- Auto Pokemon Bag management
- Auto Team Rocket Battle (PGSharp Paid, HAL & Polygon# Only)
- Catch Shiny that 3rd Party App Found (Polygon# Paid Only)
- 100IV Shiny Hunt using PGSharp sniper feed. (PGSharp only)
- (PGSharp Free/Paid) Hunt pokemon with Nearby feed (RAB PGSharp Enhance Mode)
- Non rooted support with PGSharp Free or Paid version (**NO NOT USE IT ON MAIN ACCOUNT**)
- Wifi Mode

### Enhanced Features (Donors Features)
Requires telegram account and donor status

- (Rooted Only) Integration with Telegram feed to allow 100IV Snipe 
- (Rooted Only) Integration with Telegram feed to allow Shiny Checking 
- (PGSharp Free/Paid) 100IV Shiny Pokemon tapping with Sniper feed 

## Phone Requirements
1. Rooted or PGSharp (non-rooted solution)
2. For rooted phones, you are strongly advise to use [Smali Patcher](https://forum.xda-developers.com/t/module-smali-patcher-7-3.3680053/) to take advantage of all the features of RAB 
3. Your phone must be able to run Pokemon Go if it's rooted
4. USB Debugging Enabled ([Under Developer Options](https://developer.android.com/studio/debug/dev-options))
5. Phone with Screen Resolution 720 x 1280 and above
6. Recommended 2GB RAM and above
7. Recommended Snapdragon 625 and above
8. Additional settings needed for Samsung, Xiaomi and Oppo phones (Refer to Additional Setup required by phone brand below)

## System Requirements
64 bit system is required to run RAB (Windows 10 - 64bit)

## Release Download

- Window users can download RAB from [here](https://github.com/MerlionRock/RealAndroidBot/releases) 
- Please read the sections below on how to setup your phone to run RAB
- There are no release version for Mac and Linux version yet. Please read on for the instructions on how to setup RAB on your system.

## Setting up USB Debugging mode option
1. Launch the Settings application on your phone.
2. Tap the About Phone option generally near the bottom of the list.
3. Then tap the Build Number option 7 times to enable Developer Mode. You will see a toast message when it is done.
4. Now go back to the main Settings screen and you should see a new Developer Options menu you can access.
5. Go in there and enable the USB Debugging mode option. 

## Additional Setup required by phone brand
1. Xiaomi/Poco phone: Also Enable USB Debugging (Security settings). 
2. Realme/Oppo: Enable "Disable permission monitoring".
3. Samsung: Settings -> Display -> Navigation bar -> select 'Full screen gesture' and turn-off 'gesture hints'
4. Check your phone's color display. Make sure it's `Natural` instead of `Vivid`. For Samsung users, this setting can be found at `Settings > Display > Screen Mode`. Other brand and models you have to find this option yourself.

## Additional Apps needed and their settings

1. (Optional) Install [Pokemod or HAL](https://pokemod.dev/) or [Polygon#](https://discord.gg/QURp9gA) or [PGSharp](https://www.pgsharp.com/) Please ensure their enabled/disabled Modules matches with the client settings of RAB 
2. (Pokemod, HAL and Polygon# Only) GPS Joystick, unlock version. Download from their [official website](http://gpsjoystick.theappninjas.com/faq/) You can also use GPS Joystick without any of those 3rd party apps.
- (Pokemod, HAL, Polygon# Only) Create/download a GPX Route and run it in background. Make sure joystick are hidden from view. [GPX Routes in public domain](https://drive.google.com/drive/folders/1c1ztNRY6bAXBwI0dIl_XUtNeKiBEMitt)
- (PGSharp Paid Only) Create/download a GPX Route and run it. Do not hide PGSharp. Move joystick away from location that will block text.
- (Pokemod, HAL, Polygon# Only) Recommended Speed 7km per hour or less
3. (Optional, if phone is rooted) Go to playstore and download Easy DPI Changer (or https://www.apkmirror.com/apk/chornerman_studio/easy-dpi-changer-root/). You can use this if your phone resized and you need to reset it immediately. Non-rooted users, you can use the tools tab in RAB to help you reset your phone resolution.
4. Your Pokemon Go Game MUST BE in English.
5. When running the scripts at your computer, the following app/services must be running on your phone
- GPS Joystick (Not needed for PGSharp)
- (optional) MAD Enhancer, Pokemod Espresso, Pokemod HAL, Polygon# or PGSharp
- Pokemon Go
   
## Pokemod/HAL Support

### Settings
- (**Pokemod**) IV Display format --> Toast | (**HAL**) Enable Toasts
- (**Pokemod**) IV Display Information --> verbose | (**HAL**) Toast verbosity --> Informative
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

*Enable or disable the settings in RAB's GUI accordingly*

## Polygon# Enhancer Support

Important Note: From Polygon version Polygon# v0.8.4 onwards, all paid enhancer features are now free. Please follow the paid intructions if you want RAB use backend data that's send by Polygon#. Make sure you are using v0.8.4 if you want the paid feature.

### Settings for Free version
- Set a route in GPS Joystick and loop it

### Advanced
- Encounter nameplates format `{default} LVL{lvl}\nIV{prc0}% {ivs}`
- Pokemon panel nameplate format `{default} LVL{lvl} {ivs}`

### Settings for Paid version
- Note that RAB will attempt to gather a few information from Polygon# Paid version first before starting to catch Pokemon. As such you might see RAB attempt to spin pokestops continously for a few mintues before catching. It is normal.

### Advanced
- Enable `Send data to custom backend`
- Set backend IP Address to the IP of the machine that you are running RAB
- How to find your machine's IP Guide [Windows](https://www.wikihow.com/Check-a-Computer-IP-Address) | [Mac](https://www.hellotech.com/guide/for/how-to-find-ip-address-on-mac)
- Enter a port number that you set in config. Default 5120. If you are using more than one device, each device must have their own config and with their own port number set.
- Encounter nameplates format `{default} LVL{lvl}\nIV{prc0}% {ivs}`
- Pokemon panel nameplate format `{default}`

*Enable or disable the settings in RAB's GUI accordingly*

## MAD Enhancer Support
### Overlay Settings
- Overlay Enabled
- Show IV Overlay Enabled

### App Settings
- Disable notifications Enabled (Notification will interrupt RAB detection)

### Location Settings
- Disable MAD Enchancer Spoof Location. Please Use GPS Joystick instead

### Additional Settings
- Enhance Throws, set to your preferred
- Speedup animations having hit a mon, set to either `Speedup` or `Quick`. If using Speedup, Disable RAB's `Quick Catch`. If using Quick, Enable RAB's `Quick Catch`
- Stun Mon, you are encouraged to use `Immobilized`

### Inventory Management Settings
- Set your own Inventory management here. Disable RAB's Inventory management

### Encounter Name Settings
- Do not enable anything here

*Enable or disable the settings in RAB's GUI accordingly*

## PGSharp Support

### Settings for Free Version
- Spoofing Enabled
- Hide PGSharp Disabled, move joystick to somewhere that wont block the screen
- Enhanced Throw on Excellent and Curved
- Tap to `Walk` Enabled 
- `Inventory IV` Enabled
- `Encounter IV` Enabled
- `Caught Preview` Enabled
- `Joystick` Disabled
- Set your walking speed to less than 7km/hr
- Set a location with the Map or enter coordinates 

### Settings for Paid Version
- Spoofing Enabled
- Hide PGSharp Disabled, move joystick to somewhere that wont block the screen
- Enhanced Throw on Excellent and Curved throw is preferred for faster catching
- Tap to `Walk` or `Teleport` Disabled. (Enable this option if you are using RAB PGSharp Enhance Mode, refer to the section below on this mode)
- `Inventory IV` Enabled
- `Encounter IV` Enabled
- `Caught Preview` Enabled
- `Joystick` Disabled
- `Skip Cutscenes` Enabled (Skip Encounter Intro enabled in RAB setting)
- `Quick Catch` Optional. Enable `Quick Catch` in RAB if you set this option to true.
- `Instant Beat Team Rocket` Optional. Set `Teamrocket Blast Off` to true in RAB if you set this option to true.
- The rest of options are optional
- Then click on PGSharp's icon and choose either auto walk or GPX route (this option is in map)

### RAB PGSharp Enhance Mode
- Enable nearby feed will trigger RAB PHSharp enhance mode. (Do not enable cooldown timer). RAB will automatic place Nearby feed, Joystick and Menu Icon to its prefered location. And will try to retrieve it's starting location. If RAB is unable to achieve these, you are advised to use normal mode instead of Enhance mode (It mean that enhance mode is not compatible with your device)
- Make sure tap to `Walk` is Enabled. 
- Do not use route (gpx) for this mode.
- Set your starting location to a place with lots of Pokestop. RAB will teleport back to this location if it runs out of ball (which will potentially help you get out from a place without any pokestop).

### RAB PGSharp 100IV Shiny Tap (Donor Feature)
- If RAB is unable to get your starting location, it also mean that 100IV Shiny tap feature will not work for you. (Do not donate for this feature, unless you just want to bless the team)
- If using 100IV Shiny tap feature (**Donor Feature**), enable Sniper feed only, enable 100IV Shiny Hunt in RAB Configuration tab. 
- Enable 


*Enable or disable the settings in RAB's GUI accordingly*

## PC/MAC/LINUX Requirements

Windows users who **downloaded the release version**, you just need to configure RAB, configure your phone and plug in to your PC and run RAB.exe will do. **You do not need to follow the steps below.** Remember to **ctrl+c** when you want to exit from RAB.

### <span style="color:red">Windows users who downloaded the release version, you do not need to read any further!</span>

## Install Tesseract

### Mac User
1. Install via Homebrew (https://brew.sh/)
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
2. Install Pyhton & Tesseract
```
brew install python-tk tesseract
```
3. Install ADB
```
brew install --cask android-platform-tools
```
4. Connect your device to your mac and run the following to see if it can detect your device
```
adb devices
```

### Linux
1. Install tesseract and pyhton via apt by using the command
```
sudo apt-get install python-tk
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
4. (Windows Only) ==> Now use `cd C:\` and Follow by using `python3 -m venv RealAndroidBot`
Note: If your screen return python after this command, please type in this instead `python -m venv RealAndroidBot` 
(Mac and Linux) Follow the same step but skip the `cd ..` part
5. Follow by (Mac and Linux) `source RealAndroidBot/bin/activate` (Windows) `RealAndroidBot\Scripts\activate`
6. Follow by `cd RealAndroidBot`
7. Back to Terminal or PowerShell, type `pip install -r requirements.txt`
8. (Linux) Enter the following to install tkinter `sudo apt-get install python3-tk python3-pil python3-pil.imagetk`
9. Follow by `cd rab`
10. Setup your phone according to app requirements as instructed above and run all required apps on phone
11. Make sure your Pokemon Go is at map page and **zoomed out to the max**.
12. Make sure your device are connected to your machine, run this command in Terminal or PowerShell `python -m uiautomator2 init`. Check your phone and allow installation of automator on your Phone
13. Run `python run.py` in your terminal or powershell
14. To run multiple devices, first run `adb devices` to get all your device ID connected to your computer
15. Then run each command on their own terminal/shell console
    `python run.py --device-id YOUR_DEVICE_ID`
16. To use a different config file (good for multiple devices setup) run
    `python run.py --device-id YOUR_DEVICE_ID --config-filename YOUR_CONFIG_FILE_NAME`
17. Ctrl + C to terminate the program (you might have to do it more than once)
18. Whenever you want to run the scripts again, remember to run Step 7 first follow by (mac/linux) `cd RealAndroidBot/rab` or (Windows) `cd RealAndroidBot\rab`
19. To update your files from github repo, type `git pull`

## Troubleshooting
**RAB Mess up my screen resolution and my navigation bar went missing!!**

(Linux & Mac Users) Open your terminal, type in the following command. (press enter before entering the other)
`adb shell wm size reset`
`adb shell wm density reset`
`adb shell wm overscan 0,0,0,0`

(Windows) Use RAB.exe Under Tool tab, you can reset your phone resolution. Make sure your phone is plugged in.

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
