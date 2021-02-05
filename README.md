# RealAndoridBot

[![RAB Video Demo](https://img.youtube.com/vi/wtpJ9_av-qc/0.jpg)](https://www.youtube.com/watch?v=wtpJ9_av-qc)

## Changelog
### RAB 1.07
**NOTE:** Due to the recent announcement by Polygon#, we will be removing Network mode of Polygon# from RAB. What does this mean? It mean Polygon# users will no longer be able to teleport to exactly where pokestops/pokemon are. No longer able to automatically capture shiny or 100 Polygon# found. All features of Polygon# will be removed.

Due to this sudden changes, we are unable to fully optimize support for Polygon# users and you might see your avatar stuck at different places frequently. As such I suggest you switch to Pokemod temporary.

- Added send enounter/caught information to Discord
- Changed default `spin_pokestop` from false to true
- Bug Fix: Team Rocket manage pokemon button not recognized 
- Bug Fix: Not feeding berries
- Auto scripts for Windows User to simplify installation process
- Remove network setting for Polygon#. Now Polygon# will work just like HAL. 
- Options orginally meant for Polygon# are removed
- Added only_shiny mode. Also known as shiny tap. It will only catch if poke is shiny, else flee.
- Added navigation_offset option. For phones with buttons and you can't disable/remove them, we now have an option for you to remove it. Set the height of your navigation bar here.

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

## Polygon# Enhancer Support
### Advanced
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
3. Enter the C drive directory by using ```cd C:\```
4. Clone this repo by using the command ```git clone --recursive https://github.com/MerlionRock/RealAndroidBot.git```
You will find the RealAndroidBot folder present in the C drive directory after executing this command 

## Setting up the project
1. (Windows Only) ==> Open the RealAndroidBot folder (Which is present in the C drive) in FileExplorer.
   - 1.1 (Ubuntu/Linux) Open terminal and type: `cd ~/`
2. (Windows Only) ==> Right click on the Auto_1.ps1 and select 'Run with PowerShell'
3. (Windows Only) ==> The installation will take a little time and it will prompt you for confirmation to reboot, press y and enter to reboot (While the process is ongoing the powershell may ask you to prompt for installation, for that just type 'y' and enter everytime).
4. (Mac and Linux) Install Python 3.7 or later (https://www.python.org/downloads/)
5. (Windows Only) ==> After the reboot go to the c:\RealAndroidBot again in your FileExplorer and right click on Auto_2.ps1 and select 'Run with PowerShell'(This will install the visual c++ build tools).
6. (Windows Only) ==> Now use `cd C:\` and Follow by using `python3 -m venv RealAndroidBot`
Note: If your screen return python after this command, please type in this instead `python -m venv RealAndroidBot` 
(Mac and Linux) Follow the same step but skip the `cd ..` part
7. Follow by (Mac and Linux) `source RealAndroidBot/bin/activate` (Windows) `RealAndroidBot\Scripts\activate`
8. Follow by `cd RealAndroidBot`
9. Copy config.example.yaml to rab/config.yaml and configure it by using either notepad or notepad++. 
10. Back to Terminal or PowerShell, type `pip install -r requirements.txt`
11. Follow by `cd rab`
12. Setup your phone according to app requirements as instructed above and run all required apps on phone
13. Make sure your Pokemon Go is at map page and **zoomed out to the max**.
14. Make sure your device are connected to your machine, run this command in Terminal or PowerShell `python -m uiautomator2 init`. Check your phone and allow installation of automator on your Phone
15. Please ensure you have copied config.example.yaml to rab/config.yaml and configure it, then run 
   `python run.py` in your terminal or powershell
16. To run multiple devices, first run adb devices to get all your device ID connected to your computer
17. Then run each command on their own terminal/shell console
    `python run.py --device-id YOUR_DEVICE_ID`
18. To use a different config file (good for multiple devices setup) run
    `python run.py --device-id YOUR_DEVICE_ID --config-filename YOUR_CONFIG_FILE_NAME`
19. Ctrl + C to terminate the program (you might have to do it more than once)
20. Whenever you want to run the scripts again, remember to run Step 7 first follow by (mac/linux) `cd RealAndroidBot/rab` or (Windows) `cd RealAndroidBot\rab`
21. To update your files from github repo, type `git pull`

## Disclaimer
©2016 Niantic, Inc. ©2016 Pokémon. ©1995–2016 Nintendo / Creatures Inc. / GAME FREAK inc. © 2016 Pokémon/Nintendo Pokémon and Pokémon character names are trademarks of Nintendo. Other trademarks are the property of their respective owners.
[Privacy Policy](http://www.pokemon.com/us/privacy-policy/)

[RealAndroidBot](https://github.com/MerlionRock/RealAndroidBot) is intended for academic purposes and should not be used to play the game *PokemonGo* as it is unfair to the community. Use the bot **at your own risk**.
