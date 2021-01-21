# Changelog
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