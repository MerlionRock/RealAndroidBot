# RealAndoridBot

[![RAB Video Demo](https://img.youtube.com/vi/wtpJ9_av-qc/0.jpg)](https://www.youtube.com/watch?v=wtpJ9_av-qc)

## Changelog
### RAB 1.08

**Note** Polygon Network mode is back! Only for Polygon# paid user. Free Polygon users please use `Polygon` for the client option and Paid user please use `Polygon Paid` as the option for client.  

- Added 'Polygon Paid' as an option for client
- Added back all the feature of Polygon# for Polygon# paid users
- Added `auto_offset` to config. Defaulted to `true`. RAB will now attempt to auto test your screen to see if it's compatible with RAB. It will then suggest some values where you can add them to your config file. You can then set `auto_offset` to false if you are happy with what RAB suggested to you.
- Bug Fix (PGSharp): Waited very long to throw a second pokeball
- Bug Fix: Pokemon Management will be messed up if there's a lucky pokemon
- Bug Fix: RAB will powerup level 1 pokemon despite quest set to false. This is fixed.
- Bug Fix: RAB will be stuck at a lot of places using snipe and shiny check feature
- Bug Fix: Stuck at collect component screen

[Changelog History](https://github.com/MerlionRock/RealAndroidBot/blob/master/Changelog.md)

## Discord
Join our [Discord Channel](https://discord.gg/HZXCzDXXJJ)

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
- Hide PGSharp Enabled
- Enhanced Throw on Excellent and Curved
- Tap to `Teleport` Enabled. By default this option is tap to walk, it will not work for free version. Please change to Tap to Teleport
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

## Disclaimer
©2016 Niantic, Inc. ©2016 Pokémon. ©1995–2016 Nintendo / Creatures Inc. / GAME FREAK inc. © 2016 Pokémon/Nintendo Pokémon and Pokémon character names are trademarks of Nintendo. Other trademarks are the property of their respective owners.
[Privacy Policy](http://www.pokemon.com/us/privacy-policy/)

[RealAndroidBot](https://github.com/MerlionRock/RealAndroidBot) is intended for academic purposes and should not be used to play the game *PokemonGo* as it is unfair to the community. Use the bot **at your own risk**.
