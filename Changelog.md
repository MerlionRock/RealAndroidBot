# Changelog
### RAB 1.2.0
- Updated PGSharp enhance mode vaild date till 27 May 2021
- Level will not be considered (during transfer) if it's unkown when doing Pokemon Inventory management
- Level will not be considered for None (or GPS Joystick only) user
- Added Default Location for Telegram Sniping. This is to tell RAB where to teleport to after teleport to check for snipping. This value should be the first coordinate of your GPX Route.
- Fix stuck at Pokestop for non auto spinning users
- Added: Attempt to calcualte Pokemon Level if RAB failed to get from screenshot. (Accuracy +- 0.5)
- (NEW) Basic MAD support. Ensure IV toast is enabled
- Fix: When keep lucky pokemon is enabled, shiny check will always be enabled. This causes RAB not catching pokemon but leave the screen immediately.
- Fix: RAB mistake pokemon page as egg hatch and tries to do transfer instead of catching it.
- **IMPORTANT** The condition to keep pokemon has changed back to the orginal default: Atk AND Def AND Sta AND Min Level. There's now an option if you want to use Or condition for Min Level.
- Fix: Polygon# Paid cooldown issue. RAB now uses your phone system location rather than in game location data.
- Added Disable Auto Restart Module option
- (PGSharp) Added 100IV Shiny Hunt Module. Please use only sniper feed for this option.
- Attempt to improve CP detection during apprisal (This will slow down overall apprisal detection, will explore for other methods in future).
- Telegram module is now enabled for PGSharp users. PGSharp users who donated can now login in with telegram to get the additional benifits after the trial period is over.
- Attempt to detect PGSharp icon
- Options that are not supposed to be enabled, are now disabled
- Minor Bug Fix

### RAB 1.1.2
- (Polygon# Paid Fix) Fix INVENTORY\_FULL looping
- (Polygon# Paid Fix) Faster tapping
- RAB will now auto zoomout if you didn't
- RAB will attempt to restart if prolong period of no activity
- Auto close Detail Page after restart
- (Non HAL) RAB will now just click minus (-) sign to delete all items
- Added zoom out method option. (Select pinch in or punch out to zoom out)
- Added advance berry check option. Only use it when RAB is not able to detect berries
- Added Enchanced PGSharp Mode. 
- 1. Enable nearby radar and flash it all the way to exterme left. 
- 2. The PHSharp icon flash all the to the right
- If auto goplus is not availible in Enchanced PGSharp Mode, RAB will look for a pokestop to spin after encounter a pokemon.
- Attempt to fix Pokemon Magement (transfer) feature.
- Fix RAB not searching and spinning pokestop in PGSharp Enhanced Mode
- Fix RAB not transfering on some devices
- Hidden Option: hyper\_mode. maanually add 'hyper_mode': true under 'client' option to activate it. This is to help to speed up some process. **Work in process, Work for some people only.**
- 1. Hyper Mode: Speed up closing of pokemon caught summary page for those without quick catch option.
- Minor Bug Fix

### RAB 1.1.1

This is a bug fix update. You are encourage to update to this version if you have issue with the telegram features.

We have now included a patch file update for RAB v1.1.1. If you already have RAB v1.1.0 installed, you can simply download the patch file, unzip and overwrite the files in your v1.1.0 RAB Folder. This is so that you don't have to redownload the 100+mb file all over again.

- Faster Gym detection
- Fix Index Out of Range
- RAB will now pasue for any key to show summary before exiting
- RAB will now ask user to select from list if there are more than one device detected
- UI Update. CTRL+C reminder now in RED
- Attempt to fix Egg Hatch but did not incubate new egg
- Attempt to fix not identifying encounter while claiming rewards in quest
- (Team Rocket) Slot Pokemon if there are any empty slots. RAB will no longer swipe at Team Rocket Encounter screen.
- Fix Telegram features not working on Windows

### RAB 1.1.0
Note that for this version, manual installation will need to re-run `pip install -r requirement.txt`. If you have not update to RAB 1.0.9 previously, you'll nned to run `pip install sourcedefender -U` too.

Bot is now faster but some people might have issue. RAB might not catch any pokemon. When that happens, set `Delay Time` under Configuration tab to 2.5 secs (if still cannot, increase 0.5 and test try again)

We welcome new translations. If you have your own translation, free feel to message RAB Admin in discord. 

- Adjust the scrolling for quest for phones with offset (To solve issue of quest that are done, but didn’t get cleared)
- (Polygon Enhancer Paid) Check for gyms with slots and attempt to slot pokemon.
- Attempt to reconnect Go Plus (If user have one or using HAL/PGSharp Paid’s virtual Go Plus)
- Fix: Stuck at “Going too fast” 
- Added `notify_all_encountered` option
- Time adjustment done for `None` preset (GPS Joystick with route) `None` Preset should now be fixed and users can choose to use this without any 3rd party. 
- Added Keep Event Pokemon 
- Telegram tab updated (GUI)
- Donation feed is now live. You can now use our telegram feed to do Shiny Hunting. Or even SHundo hunting. Instructions on how to donate is at Telegram Tab.
- German Translation partially updated.
- Fix (None Profile): Not able to detect catch page when encounter Pokemon during at quest page
- 720x1280 (720p) support. RAB will automatically detect and change to either 1080p or 720p base on what your phone support.
- Notify all encountered (Good to inform you what Pokemon RAB has seen if you are just doing shiny Tap)
- Fine tuning to various page detection
- Lower Resolution Option
- Farmer Discord Notification. Please note that all catch will be send to your webhook in this version. More options for farmer will be availible in next version
- Only one screenshot will saved/overwrite for new users. Existing users you can turn screenshot off by manually all the screenshot options in config.yaml to false
- Restart Pokemon Go if map is blank during shiny feed check (Polygon#).
- Fix starting quest check, “RAB didn't manage to tap into quest page” error
- Fixed None Profile (GPS Joystick only users)
- Summary when RAB quits
- Add delay timing option (will add more controls in future) for users with slower PC/Phones

### RAB 1.0.9

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

### RAB 1.0.8 Beta

**Note** Polygon Network mode is back! Only for Polygon# paid user. Free Polygon users please use `Polygon` for the client option and Paid user please use `Polygon Paid` as the option for client.  

- Added 'Polygon Paid' as an option for client
- Added back all the feature of Polygon# for Polygon# paid users
- Added `auto_offset` to config. Defaulted to `true`. RAB will now attempt to auto test your screen to see if it's compatible with RAB. It will then suggest some values where you can add them to your config file. You can then set `auto_offset` to false if you are happy with what RAB suggested to you.
- Bug Fix (PGSharp): Waited very long to throw a second pokeball
- Bug Fix: Pokemon Management will be messed up if there's a lucky pokemon
- Bug Fix: RAB will powerup level 1 pokemon despite quest set to false. This is fixed.
- Bug Fix: RAB will be stuck at a lot of places using snipe and shiny check feature
- Bug Fix: Stuck at collect component screen

### RAB 1.0.7
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

### RAB 1.0.6
- Added Pokemon Inventory Mangement. RAB will now auto keep or release pokemon in your bag when it is full
- New options for Pokemon Inventory Mangement are `enable_poke_management`, `manage_poke_on_start`, `inventory_iv` and `stop_check_at`. Please check config.example.yaml and update your exising config accordingly.
- `keep_strong_shadow` and `keep_legendary` options added under catch

### RAB 1.0.5
- PGSharp is now fully supported. Paid users try to shift your joystick to somewhere that wont be click on or block important text.
- Added `auto_route` option under `client`. PGSharp free users and Polygon# users please set this to false. PGSharp Paid users please set this to true if using auto walk or route.
- Added `screen_offset` option. Some phones, especially those with front camera build right atb the top middle of the screen, certain page in Pokemon Go will be shifted slightly downwards. To test if you need to add a number here, set clear_item_on_start to true, and see if the name of the items are correctly captured. If not, set a number here or seek help in discord. (try 80)

### RAB 1.0.4
- Added PGSharp (Free Version) Support. 

### RAB 1.0.3
- Added Polygon Support. (Please do `pip install -r requirements.txt` to get new requirements needed.
- Added client type option in config.
- Added network settings. (Polygon Only)
- Added `stop_at_ball` and `resume_at_ball` options (Polygon Only)
- added `catchpoke_every_x_spin` option. Catch a poke in between x pokestop spinning. (Polygon Only)
- Snipe support for Polygon#. Works differently from Pokemod/HAL. (Snipe is still not availibe for public, more information will be release in our Discord Channel)
- Auto catch shiny Pokemon detected by Polygon. (Polygon Only)
- Added `last_item_quit` to item_management option. Set something here for the bot to know when to quit item page. Example set to `Incense` and RAB will auto quit when it see Incense in item page
- Added `last_quest_quit` to quest option. RAB will auto quit when it sees the key word here. Example, if you set to `Mythical`, RAB will quit special research page when it sees the quest A Mythical Discovery.

### RAB 1.0.2r2
- Hot Fix: Auto Max (HAL Only)

### RAB 1.0.2r1
- Hot Fix: Stuck at berry selection page

### RAB 1.0.2
- If `manual_set_resolution` is set to true, exiting bot will no longer change screen resolution
- Added `power_up_lvl` to config. How many times do you want to powerup a level 1 pokemon.
- Added `select_ball` to config. Default auto select ball. Set to false to use default ball without selecting
- Speed up catching for users using `transfer_on_catch` options

### RAB 1.0.1
- Added `use_berry` option, defaulted to true
- Added `manual_set_resolution`, defaulted to false

### RAB 1.0
- First Commit