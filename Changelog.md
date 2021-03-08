# Changelog
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

### RAB 1.08 Beta

**Note** Polygon Network mode is back! Only for Polygon# paid user. Free Polygon users please use `Polygon` for the client option and Paid user please use `Polygon Paid` as the option for client.  

- Added 'Polygon Paid' as an option for client
- Added back all the feature of Polygon# for Polygon# paid users
- Added `auto_offset` to config. Defaulted to `true`. RAB will now attempt to auto test your screen to see if it's compatible with RAB. It will then suggest some values where you can add them to your config file. You can then set `auto_offset` to false if you are happy with what RAB suggested to you.
- Bug Fix (PGSharp): Waited very long to throw a second pokeball
- Bug Fix: Pokemon Management will be messed up if there's a lucky pokemon
- Bug Fix: RAB will powerup level 1 pokemon despite quest set to false. This is fixed.
- Bug Fix: RAB will be stuck at a lot of places using snipe and shiny check feature
- Bug Fix: Stuck at collect component screen

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

### RAB 1.06
- Added Pokemon Inventory Mangement. RAB will now auto keep or release pokemon in your bag when it is full
- New options for Pokemon Inventory Mangement are `enable_poke_management`, `manage_poke_on_start`, `inventory_iv` and `stop_check_at`. Please check config.example.yaml and update your exising config accordingly.
- `keep_strong_shadow` and `keep_legendary` options added under catch

### RAB 1.05
- PGSharp is now fully supported. Paid users try to shift your joystick to somewhere that wont be click on or block important text.
- Added `auto_route` option under `client`. PGSharp free users and Polygon# users please set this to false. PGSharp Paid users please set this to true if using auto walk or route.
- Added `screen_offset` option. Some phones, especially those with front camera build right atb the top middle of the screen, certain page in Pokemon Go will be shifted slightly downwards. To test if you need to add a number here, set clear_item_on_start to true, and see if the name of the items are correctly captured. If not, set a number here or seek help in discord. (try 80)

### RAB 1.04
- Added PGSharp (Free Version) Support. 

### RAB 1.03
- Added Polygon Support. (Please do `pip install -r requirements.txt` to get new requirements needed.
- Added client type option in config.
- Added network settings. (Polygon Only)
- Added `stop_at_ball` and `resume_at_ball` options (Polygon Only)
- added `catchpoke_every_x_spin` option. Catch a poke in between x pokestop spinning. (Polygon Only)
- Snipe support for Polygon#. Works differently from Pokemod/HAL. (Snipe is still not availibe for public, more information will be release in our Discord Channel)
- Auto catch shiny Pokemon detected by Polygon. (Polygon Only)
- Added `last_item_quit` to item_management option. Set something here for the bot to know when to quit item page. Example set to `Incense` and RAB will auto quit when it see Incense in item page
- Added `last_quest_quit` to quest option. RAB will auto quit when it sees the key word here. Example, if you set to `Mythical`, RAB will quit special research page when it sees the quest A Mythical Discovery.

### RAB 1.02r2
- Hot Fix: Auto Max (HAL Only)

### RAB 1.02r1
- Hot Fix: Stuck at berry selection page

### RAB 1.02
- If `manual_set_resolution` is set to true, exiting bot will no longer change screen resolution
- Added `power_up_lvl` to config. How many times do you want to powerup a level 1 pokemon.
- Added `select_ball` to config. Default auto select ball. Set to false to use default ball without selecting
- Speed up catching for users using `transfer_on_catch` options

### RAB 1.01
- Added `use_berry` option, defaulted to true
- Added `manual_set_resolution`, defaulted to false

### RAB 1.0
- First Commit