===================
List of CVARs
===================

Enemy Territory: Legacy, just like the original Wolfenstein: Enemy Territory, offers a wide range of console variables, so-called *CVARs*. These are options that can be used to customize the game's behaviour, setup and appearance to accommodate the player's needs or preferences. They can be set from inside a configuration file _(.cfg)_ , the command line or, in most cases from the console. For help on how to use and set CVARs, please refer to the [[FAQ_(new)#How-can-I-customize-my-game| "How can I customize my game?"]] section in the [[FAQ_(new)|FAQ]].

.. contents:: `Table of contents`
   :depth: 1
   :local:
   
--------

   +----------------------------------------------+---------------------------------+
   | |ETL logo| Symbols                           | Legend of Tags                  |
   +==============================================+=================================+
   | |CVAR removed|                               | CVAR removed                    |
   +----------------------------------------------+---------------------------------+
   | |CVAR changed|                               | CVAR changed                    |
   +----------------------------------------------+---------------------------------+
   | |CVAR added|                                 | CVAR added                      |
   +----------------------------------------------+---------------------------------+
   | |CVAR protected|                             | CVAR cheat-protected            |
   +----------------------------------------------+---------------------------------+
   | |CVAR private|                               | CVAR for internal purposes only |
   +----------------------------------------------+---------------------------------+
	
.. |CVAR removed|   image:: https://i.imgur.com/5hXJzMU.png
						:width:  256 px
						:height: 128 px
						:scale:  20 %
.. |CVAR changed|   image:: https://i.imgur.com/swu617s.png
						:width:  256 px
						:height: 128 px
						:scale:  20 %
.. |CVAR added|     image:: https://i.imgur.com/T11StpW.png
						:width:  256 px
						:height: 128 px
						:scale:  20 %
.. |CVAR protected| image:: https://i.imgur.com/6Fs1PjK.png
						:width:  256 px
						:height: 128 px
						:scale:  20 %
.. |CVAR private|   image:: https://i.imgur.com/7XQuKlF.png
						:width:  256 px
						:height: 128 px
						:scale:  20 %
.. |ETL logo|       image:: https://raw.githubusercontent.com/etlegacy/etlegacy-assets/master/logo/regular_black.png
					      :width:  1592 px
					      :height: 1990 px
					      :scale:  10 %
						  
.. |ss| raw:: html

   <s>

.. |se| raw:: html

   </s>
   
--------

*CF_* (Game Stats)
-----

*cf_wstats*
^^^^

{TODO} *Doesn't seem to have any effect.*

 - *Default:* "1.2" 
 - Specifies the font scale of the +wstats window.

.. image:: https://i.imgur.com/i3fGQDN.jpg 

--------

*cf_wtopshots*
^^^^

{TODO} *Doesn't seem to have any effect.*

 - *Default:* "1.0" 
 - specifies the font scale of the +wtopshots window 

.. image:: https://i.imgur.com/i3fGQDN.jpg 

--------

*CG_* (Client Game)
-----

*cg_altHud* |CVAR added|
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = style 1; "2" = style 2; "3" = style 3
 - Choose from different premade HUD styles. 

.. image:: https://i.imgur.com/6dKSdbB.jpg 

--------

*cg_altHudFlags* |CVAR added|
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Move the spawn timer and mission timer down above the weapon icon. 

.. image:: https://i.imgur.com/lGjIJmo.jpg 

--------

*cg_animSpeed* |CVAR protected|
^^^^

{TODO} *Seems to have the same result as [[List_of_Cvars_(new)/#cg_noPlayerAnims|cg_noPlayerAnims]].*

 - *Default:* "1" = enabled | *Possible values:* "0" = disabled; "1" = enabled. 
 - Toggle linear interpolation between successive frames in a player animation. Essentially, it toggles the display of player animations. 
 - *See also:* [[List_of_Cvars_(new)/#cg_noPlayerAnims|cg_noPlayerAnims]] 

--------

|ss|cg_animState|se| |CVAR removed|
^^^^

 - *Default:* "0" | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

*cg_announcer*
^^^^

 - *Default:* "1" = enabled | *Possible values:* "0" = disabled; "1" = enabled. 
 - Toggles the announcer voice on map start _("FIGHT!")_, and _("Prepare to Fight!")_. 

--------

*cg_antilag* |CVAR added|
^^^^

{TODO} *Why is that necessary when g_antilag exists?*

 - *Default:* "1" = enabled | *Possible values:* "0" = disabled; "1" = enabled
 - Internal CVAR. 

--------

*cg_atmosphericEffects*
^^^^

 - *Default:* "1" = enabled | *Possible values:* "0" = disabled; "1" = enabled. 
 - Toggles display of atmospheric map effects like rain and snow. 

--------

*cg_autoAction*
^^^^

 - *Default:* "0" = none| *Bit flags:* "0" = none; "1" = demo; "2" = screenshot; "4" = log stats. 
 - Automatically performs given actions at the start or end of a round.
 - Refer to the [[Path_and_File_Structure|Path and File Structure]] wiki article for where to find the saved files. 

--------

*cg_autoActivate*
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled. 
 - Toggles automatically picking up items such as ammo/health packs, weapons, objectives, etc. 

.. image:: https://i.imgur.com/xqTpCtd.jpg 

--------

*cg_autoMapZoom* |CVAR added|
^^^^

 - *Default:* "5.159"| *Possible range:* "0" = disabled; < ?
 - Adjust the zoom level of the compass minimap. 

.. image:: https://i.imgur.com/Hbct0DD.jpg 

--------

*cg_autoReload*
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled. 
 - Automatically reload weapon when clip becomes empty. Keep in mind that reloading can't be cancelled! 

--------

*cg_autoSwitch*
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled. 
 - Automatically switch to a new weapon when out of ammunition. 
 - *CAREFUL:* Do not confuse with [[List_of_Cvars_(new)/#cg_noAmmoAutoSwitch|cg_noAmmoAutoSwitch]]!

--------

|ss|cg_bigFont|se| |CVAR removed|
^^^^

 - *Default:* "0.4"| *Possible values:* 
 - CVAR was unused and has therefore been removed.
 - *Likely intention:* Implement context sensitive bot menu. 

--------

|ss|cg_blinktime|se| |CVAR removed|
^^^^

 - *Default:* "100" | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

*cg_blood* |CVAR added|
^^^^

{TODO} *Why can we not use cg_showBlood?*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Internal CVAR used in handling the display of blood effects. 

--------

*cg_bloodDamageBlend*
^^^^

 - *Default:* "1.0" = opaque| *Possible range:* "0.0" = transparent; "0.25" = light; "0.5" = medium; "0.75" = heavy; "1.0" = opaque
 - Opaqueness of on-screen blood splatter effect when you are being shot. 

.. image:: https://i.imgur.com/EVsomjX.jpg 

--------

*cg_bloodFlash*
^^^^

{TODO} *Doesn't seem to have any effect.*

 - *Default:* "1.0" = full| *Possible range:* "0.0" = none; "0.25" = light; "0.5" = medium; "0.75" = heavy; "1.0" = full
 - Toggles the blood effect when you are shot. _(source: antman)_
 - Red blood \"flash\" scale when receiving damage. _(source: UI Options)_ 

--------

*cg_bloodTime*
^^^^

 - *Default:* "120" = 2 min. | *Possible range:* "0" = none; < ?
 - Display duration of blood puddle effects on the world _(walls, floors, etc.)_ in *seconds*. 
 - *See also:* [[List_of_Cvars_(new)/#cg_brassTime|cg_brassTime]] and [[List_of_Cvars_(new)/#cg_markTime|cg_markTime]] 

--------

*cg_bluelimbotime* |CVAR added|
^^^^

 - *Default:* "30000" | *Possible range:* 
 - Internal CVAR communicated by systeminfo and used for spawn timers, in *milliseconds*. 

--------

*cg_bobPitch*
^^^^

 - *Default:* "0.002"| *Possible range:* "0.0" = disabled; < ?
 - Simulates a head 'bobbing' effect when moving by giving the camera a forwards/backwards movement similar to nodding. 

--------

*cg_bobRoll*
^^^^

 - *Default:* "0.002"| *Possible range:* "0.0" = disabled; < ?
 - Simulates a head 'bobbing' effect when moving by giving the camera a left/right movement similar to "sideways-nodding". 

--------

*cg_bobUp*
^^^^

 - *Default:* "0.005"| *Possible range:* "0.0" = disabled; < ?
 - Simulates a vertical body 'bobbing' effect when taking a step by giving the camera a vertical jerk. Feels inconsistent. 

--------

|ss|cg_bobYaw|se| |CVAR removed|
^^^^

 - *Default:* "0.002"| *Possible range:* 
 - CVAR was unused and has therefore been removed.
 - *Likely intention:* Simulate a sideways body 'bobbing' effect when taking a step by turning the camera left and right. 

--------

|ss|cg_botMenuType|se| |CVAR removed|
^^^^

 - *Default:* "0"| *Possible values:*  
 - CVAR was unused and has therefore been removed.
 - *Likely intention:* CVAR intended to implement context sensitive bot menu. If this is set to "engineer", for instance, then only engineer commands will show up. "[Reference]":https://github.com/id-Software/Enemy-Territory/blob/40342a9e3690cb5b627a433d4d5cbf30e3c57698/src/ui/ui_main.c#L8455

--------

*cg_brassTime*
^^^^

 - *Default:* "2500"| *Possible range:* "15000" = high; "2500" = medium; "0" = disabled 
 - Sets the duration ejected bullet shells last for, in *milliseconds*. 
 - See also: [[List_of_Cvars_(new)/#cg_bloodTime|cg_bloodTime]]  and [[List_of_Cvars_(new)/#cg_markTime|cg_markTime]] 

--------

*cg_buildScript* |CVAR private|
^^^^

 - *Default:* "0"| *Possible values:* "0" = disabled; "01" = enabled
 - Internal CVAR forcing loading of all possible data and error on failures. 

--------

|ss|cg_cameraMode|se| |CVAR removed|
^^^^

 - *Default:* "0"| *Possible values:*  
 - CVAR was unused and has therefore been removed. 

--------

|ss|cg_cameraOrbit|se| |CVAR removed|
^^^^

 - *Default:* "0"| *Possible values:*  
 - CVAR was unused and has therefore been removed.
 - *Likely intention:* Associated with cinematic camera spinning around when dead. 

--------

|ss|cg_cameraOrbitDelay|se| |CVAR removed|
^^^^

 - *Default:* "50"| *Possible values:*  
 - CVAR was unused and has therefore been removed.
 - *Likely intention:* Associated with cinematic camera spinning around when dead. 

--------

*cg_centerTime*
^^^^

 - *Default:* "5"| *Possible range:* "0" = disabled; < ? 
 - Duration for which center print popups are displayed, in *seconds*.
 - *See also:* [[List_of_Cvars_(new)#cg_fontScaleCP|cg_fontScaleCP]] 

.. image:: https://i.imgur.com/4mH3cw3.jpg 

--------

|ss|cg_clipboardName|se| |CVAR removed|
^^^^

 - *Default:* " "| *Possible values:*  
 - CVAR was unused and has therefore been removed. 

--------

*cg_complaintPopUp*
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled 
 - Display the UI popup to file complaints against teammates who teamkill you. 

.. image:: https://i.imgur.com/KFBjriT.jpg 

--------

*cg_coronaFarDist*
^^^^

 - *Default:* "1536" | *Possible range:* "0" = disabled; "800" = near; "1536" = normal; "4096" = far; "16000" = extreme. 
 - Sets the maximum distance coronas are displayed before fading from view, in *in-game units*. 
 - See [[List_of_Cvars_(new)/#cg_coronas|cg_coronas]] for toggling the effect. 

.. image:: https://i.imgur.com/6WWVH6w.jpg 

--------

*cg_coronas*
^^^^

{TODO} *why is "2":https://github.com/etlegacy/etlegacy/blob/033b393c8096d50935c10c38317e4bf65d7b8671/src/cgame/cg_draw.c#L3716 a thing when cg_coronaFarDist exists?*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled; "2" = unlimited
 - Toggles the display of coronas.  
 - See [[List_of_Cvars_(new)/#cg_coronaFarDist|cg_coronaFarDist]] for adjusting the draw distance of the effect. 

.. image:: https://i.imgur.com/7qJQQts.jpg 

--------

*cg_countryflags* |CVAR added|
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled, "1" = enabled 
 - Displays players' country flags in score board. 

.. image:: https://i.imgur.com/mKfD3X1.jpg 

--------

*cg_crosshairAlpha*
^^^^

 - *Default:* "1.0" = opaque| *Possible range:* "0.0" = transparent; "1.0" = opaque
 - Set the transparency level for the primary crosshair. 

.. image:: https://i.imgur.com/UzkWonW.jpg 

--------

*cg_crosshairAlphaAlt*
^^^^

 - *Default:* "1.0" = opaque| *Possible range:* "0.0" = transparent; "1.0" = opaque
 - Set the transparency level for the secondary crosshair. 

.. image:: https://i.imgur.com/DFO1ot1.jpg 

--------

*cg_crosshairColor*
^^^^

 - *Default:* "white"|<{width:600px}. *Possible values:* "white"; "yellow"; "red"; "green"; "blue"; "magenta"; "cyan"; "orange"; "0xa0c0ff" (light blue); "mdblue"; "0xffc0a0" (light red); "mdred"; "0xa0ffc0" (light green); "mdgreen"; "dkgreen"; "mdcyan"; "mdyellow"; "mdorange"; "ltgrey"; "mdgrey"; "dkgrey"; "black". *You can also use custom Hex colour codes in this format: 0xFF1E00*
 - Set the colour for the secondary crosshair. 

.. image:: https://i.imgur.com/30FkqjJ.jpg 

--------

*cg_crosshairColorAlt*
^^^^

 - *Default:* "white"|<{width:600px}. *Possible values:* "white"; "yellow"; "red"; "green"; "blue"; "magenta"; "cyan"; "orange"; "0xa0c0ff" (light blue); "mdblue"; "0xffc0a0" (light red); "mdred"; "0xa0ffc0" (light green); "mdgreen"; "dkgreen"; "mdcyan"; "mdyellow"; "mdorange"; "ltgrey"; "mdgrey"; "dkgrey"; "black". *You can also use custom Hex colour codes in this format: 0xFF1E00*
 - Set the colour for the secondary crosshair. 

.. image:: https://i.imgur.com/FYbv4bX.jpg 

--------

*cg_crosshairHealth*
^^^^

 - *Default:* "0" = disabled|<{width:600px}. *Possible values:* "0" = disabled; "1" = enabled
 - Colors the crosshair based on current health _(overrides cg_crosshairColor settings)_. 

.. image:: https://i.imgur.com/2rDVcSQ.jpg 

--------

*cg_crosshairPulse*
^^^^

 - *Default:* "1" = enabled|<{width:600px}. *Possible values:* "0" = disabled; "1" = enabled
 - Increases the crosshair spread/sizing while moving, shooting, etc. to provide a visual representation of actual weapon spread. 

.. image:: https://i.imgur.com/a3WyWQl.jpg 

--------

*cg_crosshairSize*
^^^^

 - *Default:* "48"|<{width:600px}. *Possible range:* "24" = tiny; "32" = small; "48" = medium; "64" = large; "96" = huge
 - Sets the size of the displayed crosshair, in *pixels*. 

.. image:: https://i.imgur.com/BSDGLLk.jpg 

--------

*cg_crosshairX*
^^^^

 - *Default:* "0" = center|<{width:600px}. *Possible range:* "0" = center; positive values = right; negative values = left
 - Offset of the crosshair position on-screen, in *pixels*. 

.. image:: https://i.imgur.com/PClrjlj.jpg 

--------

*cg_crosshairY*
^^^^

 - *Default:* "0" = center|<{width:600px}. *Possible range:* "0" = center; positive values = down; negative values = up
 - Offset of the crosshair position on-screen, in *pixels*. 

.. image:: https://i.imgur.com/zc7YuSS.jpg 

--------

*cg_cursorHints*
^^^^

 - *Default:* "1" = enabled|<{width:600px}. *Possible values:* "0" = disabled; "1" = enabled
 - Displays hint and information icons for certain actions when near interactive objects. 

.. image:: https://i.imgur.com/1F4sy6Q.jpg 

--------

*cg_cycleAllWeaps*
^^^^

{TODO} *Doesn't seem to be doing anything. Would propose to delete anyway.*

 - *Default:* "1" = enabled|<{width:600px}. *Possible values:* "0" = disabled; "1" = enabled
 - Include non-weapon items when cycling through inventory. 

--------

*cg_debugAnim* |CVAR protected|
^^^^

 - *Default:* "0" = disabled|<{width:600px}. *Possible values:* "0" = disabled; "1" = player anim; "2" = weapon anim
 - Used to debug player model and weapon animations. 
 - When set to "1", the game prints the frametime and title of drawn player model animation in the console.
 - When set to "2", the game prints the drawn weapon animation in the console. 

.. image:: https://i.imgur.com/0qGZ2wF.jpg 

--------

*cg_debugEvents* |CVAR protected|
^^^^

 - *Default:* "0" = disabled|<{width:600px}. *Possible values:* "0" = disabled; "1" = enabled
 - Used to debug entity events. When enabled, prints debug information in the console.  "Reference":https://github.com/etlegacy/etlegacy/blob/72fc9e39193945d82be24208dcbb9c29cba8d596/src/cgame/cg_event.c#L1824

.. image:: https://i.imgur.com/QwBp8MF.jpg 

--------

*cg_debugPlayerHitboxes* |CVAR protected|
^^^^

{TODO} *CVAR to be reworked! "Ticket":https://dev.etlegacy.com/issues/1120*

 - *Default:* "0" = disabled| *Bit flags:* "0" = disabled; "1" = hitbox; "2" = head axis; "4" = position marker
 - Used to debug player hitboxes. 

.. image:: https://i.imgur.com/WkDk0qn.jpg 

--------

*cg_debugPosition* |CVAR protected|
^^^^

 - *Default:* "0" = disabled|<{width:600px}. *Possible values:* "0" = disabled; "1" = enabled
 - Used to debug player entity yaw angle. When enabled, prints debug information in the console. "Reference":https://github.com/etlegacy/etlegacy/blob/d912b5f5c6bf89feb5068b8f08121f5090e2a209/src/cgame/cg_players.c#L3108

.. image:: https://i.imgur.com/b4SOkv1.jpg 

--------

*cg_debugSkills*
^^^^

{TODO} "*Doesn't seem to be doing anything*":https://github.com/etlegacy/etlegacy/blob/72fc9e39193945d82be24208dcbb9c29cba8d596/src/cgame/cg_draw_hud.c#L1472

 - *Default:* "0" = disabled|<{width:600px}. *Possible values:* "0" = disabled; "1" = enabled
 - Description needed. 

--------

|ss|cg_deferPlayers|se| |CVAR removed|
^^^^

 - *Default:* "0" | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

*cg_descriptiveText*
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Displays additional descriptive text on the screen. 

.. image:: https://i.imgur.com/R1xIDPO.jpg 

--------

*cg_draw2D*
^^^^

 - *Default:* "1" = enabled | *Possible values:* "0" = disabled; "1" = enabled
 - Display all UI and HUD elements. 

.. image:: https://i.imgur.com/zre7ptp.jpg 

--------

*cg_drawBuddies*
^^^^

{TODO} *Safe to delete?*

 - *Default:* "1" = enabled | *Possible values:* "0" = disabled; "1" = enabled
 - CVAR is unused. 

--------

*cg_drawCompass*
^^^^

 - *Default:* "1" = enabled | *Possible values:* "0" = disabled; "1" = enabled
 - Display the HUD compass. 

.. image:: https://i.imgur.com/3qj74wJ.jpg 

--------

*cg_drawCrosshair*
^^^^

 - *Default:* "1" = enabled | *Possible values:* "0"; "1"; "2"; "3"; "4"; "5"; "6"; "7"; "8"; "9"
 - Choose from 10 different crosshair styles. 

.. image:: https://i.imgur.com/mtP9tm5.jpg 

--------

*cg_drawCrosshairInfo*
^^^^

{TODO} *Implement bitflag 4 for names and remove [[List_of_Cvars_(new)/#cg_drawCrosshairNames|cg_drawCrosshairNames]]*

 - *Default:* "3"| *Bit flags:* "0" = nothing; "1" = class; "2" = rank
 - Displays player info when the crosshair is over a teammate. 

.. image:: https://i.imgur.com/s8bt3oP.jpg 

--------

*cg_drawCrosshairNames*
^^^^

{TODO} *Remove CVAR and add it as bitflag 4 to [[List_of_Cvars_(new)/#cg_drawCrosshairInfo|cg_drawCrosshairInfo]].*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Display names of teammates when hovering over them with your crosshair.
 - *See also:* [[List_of_Cvars_(new)/#cg_fontScaleCN|cg_fontScaleCN]] 

.. image:: https://i.imgur.com/mUeYd3j.jpg 

--------

*cg_drawCrosshairPickups*
^^^^

{TODO} *No visible difference between "1" and "2". I propose to remove and move functionality to [[List_of_Cvars_(new)/#cg_cursorHints|cg_cursorHints]].*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled; "2" = "force highlights":https://github.com/etlegacy/etlegacy/blob/52219af45338681566120a427b9b3124f1e13946/src/cgame/cg_ents.c#L835
 - Give pickup items a highlight. Very subtle. 

.. image:: https://i.imgur.com/B37zyuF.jpg 

--------

*cg_drawFireteamOverlay*
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Display Fireteam HUD window. 

.. image:: https://i.imgur.com/VlztNc5.jpg 

--------

*cg_drawFPS*
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Display a FPS counter in the HUD below the compass. 

.. image:: https://i.imgur.com/sygCXOw.jpg 

--------

*cg_drawGun*
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Display equipped weapon. 

.. image:: https://i.imgur.com/CWhbxLt.jpg 

--------

*cg_drawNotifyText*
^^^^

{TODO} *Safe to delete?*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - CVAR is unused. 

--------

*cg_drawPing*
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Display the ping in the HUD below the compass. 

.. image:: https://i.imgur.com/m7MAfpu.jpg 

--------

*cg_drawReinforcementTime*
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Display reinforcement timer for your team in the HUD below the compass (in light blue).
 - *See also:* [[List_of_Cvars_(new)/#cg_drawRoundTimer|cg_drawRoundTimer]] 

.. image:: https://i.imgur.com/j4aNyKk.jpg 

--------

*cg_drawRoundTimer*
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Display remaining mission time in the HUD below the compass. 
 - *NOTE:* Also disables [[List_of_Cvars_(new)/#cg_drawReinforcementTime|cg_drawReinforcementTime]] 

.. image:: https://i.imgur.com/ldF48BY.jpg 

--------

*cg_drawSmallPopupIcons*
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Use small icons for obituary messages. 
 - *See also:* [[List_of_Cvars_(new)#cg_fontScaleSP|cg_fontScaleSP]] 

.. image:: https://i.imgur.com/aCVVRTo.jpg 

--------

*cg_drawSnapshot*
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Display the snapshot counter in the HUD below the compass. 

.. image:: https://i.imgur.com/9rRZePK.jpg 

--------

*cg_drawSpeed* |CVAR added|
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Displays current player speed in the HUD below the compass, in *in-game units per second*. 

.. image:: https://i.imgur.com/7X5XnYM.jpg 

--------

*cg_drawSpreadScale*
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled for scoped weapons; "2" = enabled for all weapons
 - Displays a coloured bar on the left of the screen showing the current weapon spread. Increases when turning around, shooting, etc.
 - A value of "1" enables it for scoped weapons only.
 - A value of "2" enables it for all weapons.
 - A value of "0" disables it entirely. 

.. image:: https://i.imgur.com/rYo8syD.jpg 

--------

*cg_drawStatus*
^^^^

{TODO} *Check if it works and take screenshots*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - The alpha (transparency) of the watermark HUD display, if the server has one.  "Reference":https://github.com/etlegacy/etlegacy/blob/033b393c8096d50935c10c38317e4bf65d7b8671/src/cgame/cg_draw.c#L3505

--------

*cg_drawTeamOverlay*
^^^^

 - *Default:* "2" = enabled| *Possible values:* 
 - CVAR is not used, however, has to be kept for compatibility. 

--------

*cg_drawTime* |CVAR added|
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Display local time. 

.. image:: https://i.imgur.com/dX18GjL.jpg 

--------

*cg_drawWeaponIconFlash*
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Flashes the weapon icon on the bottom right during certain events. 

.. image:: https://i.imgur.com/NpvFv5g.jpg 

--------

|ss|cg_enableBreath|se| |CVAR removed|
^^^^

 - *Default:* "1" | *Possible values:* 
 - CVAR was a q3 relic and has therefore been removed. 

--------

*cg_errorDecay*
^^^^

 - *Default:* "100" | *Possible range:* "0" = disabled; < ?
 - Supposed to decay prediction errors over several frames instead of correcting in one jerk, in *frames*. 

--------

|ss|cg_etVersion|se| |CVAR private|
^^^^

 - *Default:* " " | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

|ss|cg_fastSolids|se| |CVAR removed|
^^^^

 - *Default:* "1" | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

*cg_fireteamLatchedClass* |CVAR added|
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Draw latched class of fireteam members in the fireteam overlay. 

.. image:: https://i.imgur.com/gyey9ae.jpg 

--------

*cg_fontScaleCN* |CVAR added|
^^^^

 - *Default:* "0.25"| *Possible range:* "0" = disabled; < ?
 - Set font scale for entitiy/player names when aiming crosshair at them.
 - *See:* [[List_of_Cvars_(new)/#cg_drawCrosshairNames|cg_drawCrosshairNames]] 

.. image:: https://i.imgur.com/fRBur8Y.jpg 

--------

*cg_fontScaleCP* |CVAR added|
^^^^

 - *Default:* "0.22"| *Possible range:* "0" = disabled; < ?
 - Set font scale for center prints. 
 - *See also:* [[List_of_Cvars_(new)#cg_centerTime|cg_centerTime]] 

.. image:: https://i.imgur.com/7LrbjeX.jpg 

--------

*cg_fontScaleSP* |CVAR added|
^^^^

 - *Default:* "0.22"| *Possible range:* "0" = disabled; < ?
 - Set font scale for side prints. 
 - *See also:* [[List_of_Cvars_(new)#cg_drawSmallPopupIcons|cg_drawSmallPopupIcons]] and [[List_of_Cvars_(new)#cg_graphicObituaries|cg_graphicObituaries]] 

.. image:: https://i.imgur.com/92QJUZO.jpg 

--------

*cg_fontScaleTP* |CVAR added|
^^^^

 - *Default:* "0.35"| *Possible range:* "0" = disabled; < ?
 - Set font scale for top of the screen prints. 

--------

|ss|cg_footsteps|se| |CVAR removed|
^^^^

 - *Default:* "1" | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

*cg_fov*
^^^^

 - *Default:* "90" | *Possible range:* "90" - "160"
 - Sets the Field of View. 

--------

*cg_gameType* |CVAR added|
^^^^

{TODO} *Why is that necessary when g_gametype exists?*

 - *Default:* "0" | *Possible values:* 
 - Internal CVAR communicated by systeminfo. 

--------

*cg_gibs*
^^^^

{TODO} *Doesn't seem to be doing anything.*

 - *Default:* "1" | *Possible values:* "0" = disabled; "1" = enabled
 - Likely intended to toggle display remaining bodyparts from splatted bodies.
 - Seems to be unused in ET and ET: Legacy. 

--------

*cg_graphicObituaries* |CVAR added|
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = Victim Weapon Killer; "2" = Killer Weapon Victim
 - Display simple graphic kill messages to safe space.
 - *See also:* [[List_of_Cvars_(new)#cg_fontScaleSP|cg_fontScaleSP]] 

.. image:: https://i.imgur.com/2s36V33.jpg 

--------

*cg_gun_frame*
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = frame 1; etc. 
 - Freeze weapon in the specified _(CVAR value)_ frame. 

--------

*cg_gunX*
^^^^

 - *Default:* "0" = center| *Possible range:* "0" = center; positive values = forwards; negative values = backwards
 - Offset of equipped weapon on screen along the X-axis, in *in-game units*. 

.. image:: https://i.imgur.com/nBCOM4o.jpg 

--------

*cg_gunY*
^^^^

 - *Default:* "0" = center| *Possible range:* "0" = center; positive values = left; negative values = right
 - Offset of equipped weapon on screen along the Y-axis, in *in-game units*. 

.. image:: https://i.imgur.com/JtHtcg0.jpg 

--------

*cg_gunZ*
^^^^

 - *Default:* "0" = center| *Possible range:* "0" = center; positive values = up; negative values = down
 - Offset of equipped weapon on screen along the Z-axis, in *in-game units*. 

.. image:: https://i.imgur.com/nn6DXdO.jpg 

--------

*cg_hitSounds* |CVAR added|
^^^^

 - *Default:* "1" = all| *Bit flags:* "0" = none; "1" = all; "2" = *disable* body; "4" = *disable head; "8" = *disable* team
 - Set active hit sounds. 

--------

*cg_hudAlpha*
^^^^

{TODO} *Safe to delete?*

 - *Default:*  | *Possible values:* 
 - CVAR is unused. 

--------

|ss|cg_ignore|se| |CVAR removed|
^^^^

 - *Default:* "0" | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

*cg_instantTapOut*
^^^^

{TODO} *Doesn't seem to be working*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled 
 - Likely intended to put you directly into the respawn queue without waiting for a revive. 

--------

*cg_lagometer*
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled 
 - Displays a lag'o'meter in the HUD below the compass checking for lag spikes. 

.. image:: https://i.imgur.com/C5ycQph.jpg 

--------

*cg_letterbox*
^^^^

{TODO} *WTF?!*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled 
 - Adds an overlay to the game underneath the HUD at the bottom and top of the screen simulating widescreen. 

.. image:: https://i.imgur.com/4sNnpaN.jpg 

--------

*cg_locations* |CVAR added|
^^^^

 - {FIXME} *Some values don't work and the setup is confusing. Ask ryven, he can help*

 - *Default:* "3"  | *Bit flags:* "0" = coordinates only; "1" = loc in fireteam chat; "2" = loc in team chat; "3" = loc in team and fireteam chat
 - Displays locations instead of map coordinates. Uses data from loc.dat file. 

--------

*cg_logFile*  |CVAR added|
^^^^

 - *Default:* " "| *Possible values:* strings
 - Sets the name of the chat log file or if empty logging is disabled. 

--------

*cg_markTime*
^^^^

 - *Default:* "20000" | *Possible range:* "0" = disabled; < ? 
 - Controls behaviour of location views.
 - *See also:* [[List_of_Cvars_(new)/#cg_brassTime|cg_brassTime]] and [[List_of_Cvars_(new)/#cg_bloodTime|cg_bloodTime]] 

--------

|ss|cg_message|se| |CVAR removed|
^^^^

 - *Default:* "1" | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

|ss|cg_messagePlayer|se| |CVAR removed|
^^^^

 - *Default:* " " | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

|ss|cg_messagePlayerName|se| |CVAR removed|
^^^^

 - *Default:* " " | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

*cg_messageType*
^^^^

{TODO} *What does that CVAR do really?*

 - *Default:* "1" = global| *Possible values:* "1" = global; "2" = team; "3" = fireteam; 
 - Select the destination of your message. 

--------

*cg_modVersion* |CVAR private|
^^^^

 - *Default:* " " | *Possible values:* 
 - Internal CVAR storing the ET: Legacy version number of the client for the server to check. 

--------

|ss|cg_movespeed|se| |CVAR removed|
^^^^

 - *Default:* "76" | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

*cg_muzzleFlash*
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled. 
 - Toggles display of muzzle flash when shooting. 

.. image:: https://i.imgur.com/Z4oHZXu.jpg 

--------

*cg_noAmmoAutoSwitch*
^^^^

{TODO} *Merge with [[List_of_Cvars_(new)/#cg_autoSwitch|cg_autoSwitch]]*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Automatically switch to a new weapon when out of ammunition.
 - *CAREFUL:* Do not confuse with [[List_of_Cvars_(new)/#cg_autoSwitch|cg_autoSwitch]]!

--------

*cg_noPlayerAnims* |CVAR protected|
^^^^

{TODO} *Rename to cg_playerAnims and merge with [[List_of_Cvars_(new)/#cg_animSpeed|cg_animSpeed]]*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Toggles display of player animations. If enabled, animation is fixed in a single frame.
 - *See also:* [[List_of_Cvars_(new)/#cg_animSpeed|cg_animSpeed]] 

--------

*cg_noPredict* |CVAR protected|
^^^^

{TODO} *Is there a real reason for this? Shouldn't this be enabled always anyway?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Toggles prediction of player actions _(e.g. movement)_. 

--------

|ss|cg_noRender|se| |CVAR removed|
^^^^

 - *Default:* " " | *Possible values:* 
 - CVAR was obsolete nonsense and has therefore been removed. 

--------

|ss|cg_noTaunt|se| |CVAR removed|
^^^^

 - *Default:* " " | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

|ss|cg_noVoiceChats|se| |CVAR removed|
^^^^

 - *Default:* " " | *Possible values:* 
 - CVAR was replaced by [[List_of_Cvars_(new)/#cg_voiceChats|cg_voiceChats]]. 

--------

|ss|cg_noVoiceText|se| |CVAR removed|
^^^^

 - *Default:* " " | *Possible values:* 
 - CVAR was replaced by [[List_of_Cvars_(new)/#cg_voiceText|cg_voiceText]]. 

--------

*cg_optimizePrediction* |CVAR added|
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Enables unlagged optimized prediction. 

--------

*cg_paused* |CVAR added|
^^^^

 - *Default:* "0" = unpaused| *Possible values:* "0" = unpaused; "1" = paused
 - Internal CVAR used to let the game behave differently when paused. 

--------

*cg_popupFadeTime* |CVAR added|
^^^^

 - *Default:* "2500" = 2.5 sec| *Possible values:* "0" = disabled; < ?
 - Duration of the fading effect of popup messages.
 - *See also:* [[List_of_Cvars_(new)/#cg_popupStayTime|cg_popupStayTime]], [[List_of_Cvars_(new)/#cg_popupFilter|cg_popupFilter]] 

--------

*cg_popupBigFilter* |CVAR added|
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; 1 = filter skill promotions, 2 = filter rank promotions
 - Filter promotion popups. 

--------

*cg_popupFilter* |CVAR added|
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; 1 = filter connect, 2 = filter team join, 4 = filter mission, 8 = filter pickup, 16 = filter death
 - Filter message popups.
 - *See also:* [[List_of_Cvars_(new)/#cg_popupStayTime|cg_popupStayTime]],  [[List_of_Cvars_(new)/#cg_popupFadeTime|cg_popupFadeTime]] 

--------

*cg_popupLimboMenu*
^^^^

 - *Default:* "1" = enabled| *Possible values:* 
 - CVAR is not used, however, has to be kept for compatibility. 

--------

h### *cg_popupStayTime* |CVAR added|

 - *Default:* "2000" = 2 sec| *Possible values:* "0" = disabled; < ?
 - Duration for which popup messages stay active.
 - *See also:* [[List_of_Cvars_(new)/#cg_popupFadeTime|cg_popupFadeTime]],  [[List_of_Cvars_(new)/#cg_popupFilter|cg_popupFilter]] 

--------

*cg_predefinedDemoKeys* |CVAR added|
^^^^

{TODO} *What is this used for?*

 - *Default:* "1" | *Possible values:* 
 - Description needed. 

--------

*cg_predictItems*
^^^^

{TODO} *Doesn't seem to be doing anything*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Toggles use of prediction for picking up items. 

--------

*cg_printObjectiveInfo*
^^^^

{TODO} *Doesn't seem to be doing anything*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Prints important game messages to the console. 

--------

*cg_quickChat* |CVAR added|
^^^^

{TODO} *Doesn't seem to be doing anything*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = team chat; "2" = fireteam chat
 - Specify receiver of quick radio messages. 

--------

*cg_quickMessageAlt*
^^^^

 - *Default:* "1" = numerical| *Possible values:* "0" = alphabetical; "1" = numerical
 - Toggles using either numbers or letters for the quick chat menu. 

.. image:: https://i.imgur.com/Xejzj5x.jpg 

--------

|ss|cg_railTrailTime|se| |CVAR removed|
^^^^

 - *Default:* " " | *Possible values:* 
 - CVAR was unused and has therefore been removed. It has been replaced with a static value of 50

--------

*cg_rconPassword* |CVAR added|
^^^^

{TODO} *Why is that necessary when auth_rconPassword exists?*

 - *Default:* " " | *Possible values:* 
 - Internal CVAR. 

--------

*cg_recoilPitch*
^^^^

{TODO} *Since it's read-only anyway and the client should not be able to set this, can it be removed?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Read-only CVAR encoding the kick angles into a 24-bit number, for sending to the client exe. 

--------

*cg_recording_Statusline*
^^^^

 - *Default:* "9" = top| *Possible range:* "9" = top; positive values = lower; negative values = higher
 - Offset of the recording statusline on screen. 

.. image:: https://i.imgur.com/RlEBmbl.jpg 

--------

*cg_redLimboTime* |CVAR added|
^^^^

 - *Default:* "30000" | *Possible values:* 
 - Internal CVAR communicated by systeminfo and used for spawn timers, in *milliseconds*. 

--------

*cg_refereePassword* |CVAR added|
^^^^

{TODO} *Why is that necessary when auth_refereePassword exists?*

 - *Default:* " " | *Possible values:* 
 - Internal CVAR. 

--------

|ss|cg_runpitch|se| |CVAR removed|
^^^^

 - *Default:* "0.002" | *Possible values:* 
 - CVAR was bugged and has therefore been removed. 

--------

|ss|cg_runroll|se| |CVAR removed|
^^^^

 - *Default:* "0.005" | *Possible values:*
 - CVAR was bugged and has therefore been removed. 

--------

*cg_scoreboard* |CVAR added|
^^^^

 - *Default:* "1" = SR| *Possible values:* "0" = XP; "1" = SR
 - Used to cycle between XP and Skill Rating (SR) scoreboard. 

.. image:: https://i.imgur.com/1IBwm4U.jpg 

--------

*cg_selectedPlayer*
^^^^

{TODO} *Doesn't seem to have any effect.*

 - *Default:* " " | *Possible values:*
 - Select a "team leader"?. 

--------

*cg_selectedPlayerName*
^^^^

{TODO} *Doesn't seem to have any effect.*

 - *Default:* " " | *Possible values:* 
 - Select a "team leader"?. 

--------

*cg_shadows*
^^^^

 - *Default:* "1" | *Possible values:* "0" = disabled; "1" = blob; "2" = Stencil; "3" = Projection; "4" = Polygon 
 - Display player shadows underneath the player.
 - *NOTE:* It is not recommended to have it enabled, as it lowers FPS quite significantly. "Reference":https://dev.etlegacy.com/issues/1078 
 - Also note that Stencil, Projection and Polygon are currently broken. 

.. image:: https://i.imgur.com/4yP4d05.jpg 

--------

*cg_showBlood*
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Toggles showing blood spurt effect when players are shot

.. image:: https://i.imgur.com/XlEbfZl.jpg 

--------

*cg_showMiss*
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Print faulty predictions into the console, for debugging purposes. 

.. image:: https://i.imgur.com/IjZ08dk.jpg 

--------

*cg_simpleItems* |CVAR added|
^^^^

 - {FIXME} *"Bugged atm":https://github.com/etlegacy/etlegacy/blob/master/src/cgame/cg_main.c#L569

 - *Default:* "0" = disabled | *Possible values:* "0" = disabled; "1" = enabled; "2" = enabled, but objectives use regular 3D models 
 - Use minimalistic icons for item pick-ups. 

.. image:: https://i.imgur.com/jbFplDS.jpg 

--------

*cg_skybox* |CVAR protected|
^^^^

{TODO} *Doesn't seem to be doing anything*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Likely intended to toggle display of the skybox. 

--------

|ss|cg_smallFont|se| |CVAR removed|
^^^^

 - *Default:* "0.25"| *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

*cg_spawnTimer_period*  |CVAR added|
^^^^

{TODO} *This is bad! Don't add CVARs that can, but shouldn't be modified!!*

 - *Default:* "0"| *Possible values:* 
 - *CAREFUL:* Don’t modify. Use console commands /timerSet and /resetTimer instead. 

--------

*cg_spawnTimer_set*  |CVAR added|
^^^^

{TODO} *This is bad! Don't add CVARs that can, but shouldn't be modified!!*

 - *Default:* "-1"| *Possible values:* 
 - *CAREFUL:* Don’t modify. Use console commands /timerSet and /resetTimer instead. 

--------

*cg_specHelp*
^^^^

{TODO} *Necessary?*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Toggle display of spectator help, *only* in multiview. 

--------

|ss|cg_specSwing|se| |CVAR removed|
^^^^

 - *Default:* | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

*cg_stats*
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Prints client frame in the console, for debugging purposes. 

.. image:: https://i.imgur.com/za4IiP3.jpg 

--------

|ss|cg_stereoSeparation|se| |CVAR removed|
^^^^

 - *Default:* "0.4" | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

*cg_swingSpeed* |CVAR protected|
^^^^

 - *Default:* "0.1"| *Possible range:* "0" = never turn; < ?
 - Speed at which the thirdperson player model turns around when looking around. 

--------

*cg_synchronousClients* |CVAR added|
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Internal CVAR communicated by systeminfo. 

--------

*cg_teamChatHeight*
^^^^

{TODO} *Rename to cg_chatHeight as it is not restricted to team chat*

 - *Default:* "8" = 8 lines| *Possible values:* "0" = disabled; "1" = 1 line; etc. 
 - Specifies the amount to chat messages are displayed at max, in *lines*. 

--------

*cg_teamChatsOnly*
^^^^

{TODO} *Replace with bitflag CVAR to choose which chats to display.*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Filers global chat messages and only displays team and fireteam chat. 

--------

*cg_teamChatTime*
^^^^

{TODO} *Rename to cg_chatTime as it is not restricted to team chat*

 - *Default:* "8000" = 8 sec| *Possible range:* "0" = disabled; < ?
 - Duration for which messages in the chat are kept on display, in *milliseconds*. 

--------

*cg_thirdPerson* |CVAR protected|
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Enables a thirdperson perspective. 

.. image:: https://i.imgur.com/rd96Eue.jpg 

--------

*cg_thirdPersonAngle* |CVAR protected|
^^^^

 - *Default:* "0" = behind| *Possible range:* "0" / "360" = from behind; "180" = from ahead
 - Specifies the angle of the thirdperson perspective. 

.. image:: https://i.imgur.com/gKOe7wl.jpg 

--------

*cg_thirdPersonRange* |CVAR protected|
^^^^

 - *Default:* "80"| *Possible range:* ? < ;"0" = above head; < ?
 - Specifies the distance from camera to player origin, in *in-game units*. 

.. image:: https://i.imgur.com/RjlD4xn.jpg 

--------

*cg_timescale* |CVAR private|
^^^^

{TODO} *Description needed.*

 - *Default:* "1"| *Possible values:* 
 - unknown CVAR in-game, but used in code. 

--------

|ss|cg_timescaleFadeEnd|se| |CVAR removed|
^^^^

 - *Default:* "1"| *Possible values:*  
 - CVAR was unused and has therefore been removed. 

--------

|ss|cg_timescaleFadeSpeed|se| |CVAR removed|
^^^^

 - *Default:* "0"| *Possible values:*  
 - CVAR was unused and has therefore been removed. 

--------

*cg_tracers* |CVAR added|
^^^^

 - *Default:* "1" = all| *Possible values:* "0" = none; "1" = all; "2" = own tracers only; "3" = other's tracers only
 - Choosing which tracers to display. 

--------

*cg_tracerChance* |CVAR protected|
^^^^

 - *Default:* "0.4"| *Possible range:* "0" = never; "1" = always
 - Probability that a shot creates a bullet tracer. 

--------

*cg_tracerLength* |CVAR protected|
^^^^

 - *Default:* "160"| *Possible range:* "0" = disabled; < ?
 - Length of bullet tracers. 

--------

*cg_tracerSpeed* |CVAR protected|
^^^^

 - *Default:* "4500"| *Possible range:* "0" = static; < ?
 - Speed of bullet tracers. 

--------

*cg_tracerWidth* |CVAR protected|
^^^^

 - *Default:* "0"| *Possible range:* "0" = disabled; < ?
 - Width of bullet tracers. 

--------

*cg_ui_voteFlags*
^^^^

 - *Default:* "0"| *Bit flags:* see below
 - *Displays the sum of available voting flags.*
 - config = "1"
 - gametype= "2"
 - kick = "4"
 - map = "8"
 - match reset = "16"
 - mute specs = "32"
 - next map = "64"
 - referee = "128"
 - shuffle teams by XP = "256"
 - shuffle teams by SR = "512"
 - swap teams = "1024"
 - friendly fire = "2048"
 - timelimit = "4096"
 - warm-up damage = "8192"
 - anti-lag = "16384"
 - balanced teams = "32768"
 - muting = "65536"
 - surrender = "131072"
 - restart campaign = "262144"
 - next campaign = "524288"
 - poll = "1048576"
 - map restart = "2097152"
 - shuffle teams by XP (NO RESTART) = "4194304"
 - shuffle teams by SR (NO RESTART) = "8388608"

--------

*cg_uinfo*
^^^^

{TODO} *Since it's read-only, can it be removed?*

 - *Default:* "0"| *Possible values:* 
 - Read-only CVAR holding flags identifying rights of the player. 

--------

*cg_useWeapsForZoom*
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled 
 - Allows the use of weapon switching keys for zooming. 

--------

|ss|cg_viewsize|se| |CVAR removed|
^^^^

 - *Default:* "100"| *Possible values:*  
 - CVAR was unused and has therefore been removed.
 - *Likely intention:* Set the % of screen actually displaying rendered game. 

--------


*cg_visualEffects* |CVAR added|
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Draws additional visual effects _(airstrike planes, debris)_. 

.. image:: https://i.imgur.com/I2anIBj.jpg 

--------

*cg_voiceChats* |CVAR added|
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Play voice chat sound file in-game when using quick chat _(e.g. v21 for Need a Medic!)_. 
 - *See also:*  [[List_of_Cvars_(new)/#cg_voiceText|cg_voiceText]] 

--------

*cg_voiceText* |CVAR added|
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Show voice text lines in-game when using quick chat _(e.g. v21 for Need a Medic!)_.
 - *See also:*  [[List_of_Cvars_(new)/#cg_voiceChats|cg_voiceChats]] 

--------

*cg_voiceSpriteTime*
^^^^

 - *Default:* "6000" = 6 sec| *Possible range:* "0" = disabled; < ? 
 - Duration for which the chat icon appears above other players' heads, in *milliseconds*. 

.. image:: https://i.imgur.com/BMKja5I.jpg 

--------

*cg_weapAltReloads*
^^^^

{TODO} *What does that CVAR do?*

 - *Default:* "0" | *Possible values:* "0" = disabled; "0" = enabled
 - No description available. Also there is "this":https://github.com/etlegacy/etlegacy/blob/b162f0450129a1fa1a1f0198f48c3e2bd92c8b45/src/cgame/cg_weapons.c#L3757 

--------

*cg_weaponCycleDelay*
^^^^

 - *Default:* "150" | *Possible range:* "0" = disabled; < ? 
 - Duration for which a pause is enforced so keeping the weapon switch key activated won't trigger too fast, in *milliseconds*. 

--------

*cg_wolfparticles*
^^^^

 - *Default:* "1" = enabled | *Possible values:* "0" = disabled; "1" = enabled
 - Toggles display of 'particle effects' like explosions and non-player smoke.
 - Smoke from player abilities _(e.g. cvop's smokebomb, fieldop's airstrike marker)_ are exempt. 

.. image:: https://i.imgur.com/ensN5Ux.jpg 

--------

|ss|cg_zoomDefaultBinoc|se| |CVAR removed|
^^^^

 - *Default:* "22.5" = enabled| *Possible values:*  
 - CVAR was unused and has therefore been removed. 

--------


|ss|cg_zoomDefaultFG|se| |CVAR removed|
^^^^

 - *Default:* "55" = enabled| *Possible values:*  
 - CVAR was unused and has therefore been removed. 

--------

*cg_zoomDefaultSniper*
^^^^

{TODO} *This CVAR is horribly implemented! Fix (or remove) and rename to cg_zoomDefault since it's not limited to sniper.*

 - *Default:* "20"| *Possible range:* "0" = disabled; < ? 
 - Sets the default level of zoom for binoculars, sniper and FG42.
 - This CVAR is absolutely borked!!!
 - A value of 0 disables zooming, but also screws up the display.
 - It is possible to set a value of 1 for closer zoom than allowed.
 - It is possible to set values significantly above 20 zooming out! 
 - you can actually set a higher zoom as default and have an FG42 with closer zoom, breaking its intended behaviour! 
 - It would therefore be possible to have different default zoom binds and simply unscope, change and scope in to adjust FG42 zoom. 

--------

|ss|cg_zoomDefaultSnooper|se| |CVAR removed|
^^^^

 - *Default:* "40" = enabled| *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

|ss|cg_zoomFOV|se| |CVAR removed|
^^^^

 - *Default:* "22.5" = enabled| *Possible values:*  
 - CVAR was unused and has therefore been removed. 

--------

|ss|cg_zoomStepBinoc|se| |CVAR removed|
^^^^

 - *Default:* "3" = enabled| *Possible values:*  
 - CVAR was unused and has therefore been removed. 

--------

|ss|cg_zoomStepFG|se| |CVAR removed|
^^^^

 - *Default:* "10" = enabled| *Possible values:*  
 - CVAR was unused and has therefore been removed. 

--------

*cg_zoomStepSniper*
^^^^

{TODO} *Rename to cg_zoomStep as it's not limited to sniper.*

 - *Default:* "2"| *Possible range:* "0" = disabled; < ? 
 - Specifies the amount of levels one key activation zooms in or out.
 - This CVAR applies to binoculars, snipers and FG42. 

--------

|ss|cg_zoomStepSnooper|se| |CVAR removed|
^^^^

 - *Default:* "5" = enabled| *Possible values:*  
 - CVAR was unused and has therefore been removed. 

--------

*CL_* (Client Engine)
-----

*cl_activateLean* 
^^^^

{TODO} *CVAR seems to have no effect?*

 - *Default:* "1" = enabled| *Possible values:*
 - Description needed. 

--------

*cl_activeAction* 
^^^^

{TODO} *unkown CVAR ingame. What is it used for?*

 - *Default:* " " | *Possible values:*
 - Description needed. 

--------

*cl_allowDownload* 
^^^^


 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled; "2" = enabled, but suppressed sound
 - Download missing files when available.
 - *See also:* [[List_of_Cvars_(new)#cl_wwwDownload|cl_wwwDownload]] 

--------

*cl_angleSpeedKey* 
^^^^

{TODO} *CVAR unused in ET and ET: Legacy. Safe to remove?*

 - *Default:* "1.5"| *Possible values:* 
 - CVAR is unused. 
 - Likely intended to adjust the speed for turning around. 

--------

*cl_anonymous* 
^^^^

{TODO} *Safe to remove?*

 - *Default:* "0"| *Possible values:* 
 - CVAR is unused. 

--------

*cl_autoRecord* 
^^^^


 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - CVAR looks unused. Also [[List_of_Cvars_(new)/#cg_autoAction|cg_autoAction]] is a thing. 

--------

*cl_aviDemo*
^^^^

{TODO} *Couldn't test in-game. Check if it works*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Likely saves the specified amount of jpeg screenshots per second. 

--------

*cl_aviDemoType* |CVAR added|
^^^^

{TODO} *There are way too many avi demo related CVARs. Are all of them necessary?*

 - *Default:* "0"| *Possible values:* 
 - Description needed. 

--------

*cl_aviMotionJpeg*
^^^^

{TODO} *There are way too many avi demo related CVARs. Are all of them necessary?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Description needed. 

--------

*cl_bypassMouseInput*
^^^^

{TODO} *The user should not be able to set this! This should be hard-coded behaviour anyway. Can CVAR be removed?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Used to bypass mouse input in-game while menus are active. 

--------

*cl_cacheGathering*
^^^^

{TODO} *No official description found! Please check*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Enables some sort of data caching. Maps seem to load faster when loaded again. No info on what exactly gets cached found. 

--------

*cl_conXOffset*
^^^^

{TODO} *What does this CVAR do?*

 - *Default:* "0" = disabled| *Possible values:* 
 - No description available. 

--------

*cl_consoleKeys*
^^^^

{TODO} *can this be renamed to con_consoleKeys, because shouldn't it be rather in the [[List_of_Cvars_(new)#CON_-Console|console related section]]?*

 - *Default:* "~ ` 0x7e 0x60"| *Possible values:* keys
 - Bind opening the console to the specified key. e.g. cl_consoleKeys ~ 

--------

*cl_debugMove*
^^^^


 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled 
 - Display a bar on the bottom of the screen containing bar charts representing mouse movement. 

.. image:: https://i.imgur.com/0nB4zb4.jpg 

--------

|ss|cl_debugTranslation|se| |CVAR removed|
^^^^

 - *Default:* "0" = disabled| *Possible values:*  
 - CVAR was unused and has therefore been removed. 

--------

*cl_defaultProfile* |CVAR private| 
^^^^

{TODO} *can this be combined with [[List_of_Cvars_(new)/#cl_profile|cl_profile]]?*

 - *Default:* " " | *Possible values:*  
 - Read-only CVAR setting the default user profile. Go to the PROFILE section in the main menu to set a default profile.
 - *See also:* [[List_of_Cvars_(new)/#cl_profile|cl_profile]] 

--------

*cl_demoFileName* |CVAR private|
^^^^

 - *Default:* " "| *Possible values:* strings
 - Internal read-only CVAR used for demo recording. 

--------

*cl_demoOffset* |CVAR private|
^^^^

 - *Default:* "0"| *Possible values:* 
 - Internal read-only CVAR used for demo recording. 

--------

*cl_demoRecording* |CVAR private|
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Internal read-only CVAR used for demo recording. 

--------

*cl_doubleTapDelay*
^^^^

{TODO} *What is this actually used for? Are there double taps in ET?*

 - *Default:* "350" | *Possible range:* "0" = disabled; < ? 
 - Delay between registering key presses for double tapping binds, in *milliseconds*. 

--------

*cl_downloadName*
^^^^

{TODO} *Why is that a thing?*

 - *Default:* " " | *Possible values:* strings 
 - Stores name of file you're downloading when connecting to a server. 

.. image:: https://i.imgur.com/OC0foUC.jpg 

--------

*cl_forceAviDemo*
^^^^

{TODO} *CVAR seems to be unused?*

 - *Default:* "0" = disabled | *Possible values:* "0" = disabled; "1" = enabled
 - Description needed. 

--------

*cl_freeLook*
^^^^

{TODO} *CVAR seems pointless*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Enables 'freelook'. When "disabled" only left/right camera movement is possible, up/down is deactivated. 

--------

*cl_freezeDemo*
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Lock or freeze a demo in its current frame. Useful for per frame advances.
 - *NOTE:* This freezes both time *and* movement. Spectator camera can't be moved around. "[Reference]":https://github.com/etlegacy/etlegacy/blob/88bc7e08027aab9c84325db6113788e2c2128d97/docs/demos/README-serverside-demos_ETL.md#changelog-newest-to-the-bottom

--------

*cl_guid*
^^^^

 - *Default:* " " | *Possible values:* 
 - A GUID, sometimes also referred to as "etkey", is an automatically generated alpha-numerical sequence used to uniquely identify players.
 - It is stored in the etkey file [[Path_and_file_structure|(path and file structure)]] and in-game in this read-only CVAR. 

--------

|ss|cl_inGameVideo|se| |CVAR removed|
^^^^

 - *Default:* "1" | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

*cl_lang* |CVAR added|
^^^^

 - *Default:* "en" = English| *Possible values:* en = English; fr = French; de = German; it = Italian; es = Spanish; pl = Polish;
 -  - nl = Dutch; cs = Czech; se = Swedish; fi = Finnish; da = Danish; pt = Portugese; no = Norwegian
ET: Legacy comes with translations created by the community. In case you would like to contribute, please refer to "Transifex":https://www.transifex.com/etlegacy/etlegacy/

--------

*cl_langDebug* |CVAR added|
^^^^

{TODO} *Is this necessary? Isn't this the point of Transifex?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Prints a list of missing translations for the selected language to console and also creates a text file with missing translations. 

--------

|ss|cl_language|se| |CVAR removed|
^^^^

 - *Default:* "0" = English| *Possible values:* 
 - CVAR was removed in favour of [[List_of_Cvars_(new)/#cl_lang|cl_lang]] for improved language support. 

--------

*cl_maxPackets*
^^^^

{TODO} *What unit is this in? As in, what does the 125 represent?*

 - *Default:* "125"| *Possible range:* "15" < "125"
 - Cap for upstream data packet transmissions. 

--------

*cl_maxPing*
^^^^

 - *Default:* "800"| *Possible range:* "100" < "999"
 - Specify the max allowed ping to a server. Servers exceeding this ping will not be displayed in the server browser. 

--------

|ss|cl_motd|se| |CVAR removed|
^^^^

 - *Default:* "1"| *Possible values:* 
 - CVAR was unused and has therefore been removed.
 - *Likely use:* Fetch the "Message-Of-The-Day" from the masterserver. 

--------

|ss|cl_motdString|se| |CVAR removed|
^^^^

 - *Default:* " "| *Possible values:* 
 - CVAR was unused and has therefore been removed.
 - *Likely use:* Storing the fetched "Message-Of-The-Day" from the masterserver. 

--------

*cl_mouseAccel*
^^^^

{TODO} *CVAR looks unused. Safe to delete?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - CVAR seems to be unused. Likely intended to toggle mouse acceleration. 

--------

*cl_noDelta*
^^^^

{TODO} *CVAR looks unused. Safe to delete?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - CVAR seems to be unused. 

--------

*cl_noPrint*
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Enable printing of information in the console. 

--------

*cl_packetDelay* |CVAR protected|
^^^^

{TODO} *What does that CVAR do?*

 - *Default:* "0" = disabled| *Possible values:*  
 - Description needed. 

--------

*cl_packetDUP*
^^^^

{TODO} *Description copied from antman. Correct?*

 - *Default:* "1"| *Possible range:* "0" < "5"
 - Number of duplicates for every data packet sent upstream. 

--------

*cl_packetLoss* |CVAR protected|
^^^^

{TODO} *What does that CVAR do?*

 - *Default:* "0" = disabled| *Possible values:*  
 - Description needed. 

--------

*cl_paused* |CVAR private| 
^^^^

{TODO} *Can this be combined with [[List_of_Cvars_(new)/#cg_paused|cg_paused]]?*

 - *Default:* "0" = unpaused| *Possible values:* "0" = unpaused; "1" = paused
 - Internal read-only CVAR to toggle functionality of paused games. 

--------

*cl_pitchSpeed* 
^^^^

{TODO} *+up and +down have been removed so this CVAR is pointless, no?*

 - *Default:* "140" | *Possible values:* 
 - Specify the speed of +up and +down keys. 

--------

*cl_profile* |CVAR private| 
^^^^

{TODO} *Can this be combined with [[List_of_Cvars_(new)/#cl_defaultProfile|cl_defaultProfile]]? Also, can this be made non-read-only?*

 - *Default:* " " | *Possible values:* 
 - Read-only CVAR specifying the currently selected profile. To change the profile, you need to go to the "PROFILE" section in the main menu.
 - *See also:* [[List_of_Cvars_(new)/#cl_defaultProfile|cl_defaultProfile]] 

--------

*cl_punkbuster* |CVAR private|
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Enable "Punkbuster":http://evenbalance.com/.
 - *NOTE:* Punkbuster "dropped support":https://dev.etlegacy.com/projects/etlegacy/wiki/FAQ_(new)#PunkBuster-is-not-supported for ET. This CVAR is only present to ensure compatibility. 

--------

*cl_recoilPitch* 
^^^^

{TODO} *unkown CVAR ingame. What is it used for?*

 - *Default:* "0" | *Possible values:*
 - Unknown CVAR, but mentioned in code. Points to cg_recoilPitch. 

--------

*cl_renderer* |CVAR added|
^^^^

 - *Default:* "opengl1"| *Possible values:* "opengl1"; "opengl2"
 - Select your renderer of choice.
 - *NOTE:* "opengl2" remains in experimental state for now. 

--------

*cl_run* 
^^^^

{TODO} *Is this really necessary? Maybe remove CVAR, have enabled default and replace +speed with +walk?*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Toggle between walk and run. If enabled, +forward is  running speed and if disabled it's walking speed. To toggle to the other mode use the combination of +speed (capslock) + +forward. 

--------

*cl_running* |CVAR private| 
^^^^

{TODO} *CVAR seems to be unused. Safe to remove?*

 - *Default:* "0" = not running| *Possible values:* "0" = not running; "1" = running
 - Can be used to check the status of the client game. _"Is it running or not?"_. 

--------

*cl_sensitivity* 
^^^^

{TODO} *unkown CVAR ingame. What is it used for?*

 - *Default:* "5" | *Possible values:*
 - Is this a duplicate of sensitivity?. 

--------

*cl_serverStatusResendTime* 
^^^^

{TODO} *What does that CVAR do?*

 - *Default:* "750"| *Possible values:* 
 - Description needed. 

--------

*cl_showMouseRate* 
^^^^


 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Prints the speed of mouse movement to the console. 

.. image:: https://i.imgur.com/zjoMi4L.jpg 

--------

*cl_showNet* 
^^^^

{TODO} *Description copied from antman, correct?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Prints the latency of each packet to the console. 

.. image:: https://i.imgur.com/VTwFGF8.jpg 

--------

*cl_showNumEnts* 
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Prints the number of entities per packet to the console. 

.. image:: https://i.imgur.com/roAjvYj.jpg 

--------

*cl_showSend* 
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled 
 - Prints each sent packet to the console. 

.. image:: https://i.imgur.com/KwUUt6c.jpg 

--------

*cl_showServerCommands* 
^^^^

{TODO} *What does this CVAR do?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Description needed. 

--------

*cl_showTimeDelta* 
^^^^

{TODO} *Check description*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Prints the time delta of each packet to the console. 

.. image:: https://i.imgur.com/PmLTIpx.jpg 

--------

*cl_timedemo* 
^^^^

{TODO} *unkown CVAR ingame. What is it used for?*

 - *Default:* "0"| *Possible values:*
 - Unknown CVAR, but mentioned in code. 

--------

*cl_timeNudge* 
^^^^

{TODO} *Description copied from antman, check*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Supposed to be for adjusting prediction for your ping. Don't bother, use antilag. 

--------

*cl_timeout* 
^^^^

{TODO} *Description copied from antman, check*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Seems to be duration of receiving nothing from server for client to decide it must be disconnected. 

--------

|ss|cl_updateAvailable|se| |CVAR removed|
^^^^

 - *Default:* "0" | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

|ss|cl_updateFiles|se| |CVAR removed|
^^^^

 - *Default:* " " | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

|ss|cl_visibleClients|se| |CVAR removed|
^^^^

 - *Default:* "0" | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

|ss|cl_waitForFire|se| |CVAR removed|
^^^^

 - *Default:* "0" | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

*cl_waveFileName* |CVAR private|
^^^^

 - *Default:* " "| *Possible values:* strings
 - Internal read-only CVAR used for wave demo recording. 

--------

*cl_waveFileRecord*
^^^^

{TODO} *Can this be merged with cg_autoAction?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Start recording a .wav audio file upon loading a demo. 

--------

*cl_waveOffset* |CVAR private|
^^^^

 - *Default:* "0"| *Possible values:* 
 - Internal read-only CVAR used for wave demo recording. 

--------

*cl_waveRecording* |CVAR private|
^^^^

 - *Default:* "0"| *Possible values:* 
 - Internal read-only CVAR used for wave demo recording. 

--------

*cl_wwwDownload*
^^^^

{TODO} *Merge with cl_allowDownload*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Enables http/ftp downloads.
 - *See also:* [[List_of_Cvars_(new)#cl_allowDownload|cl_allowDownload]] 

--------

*cl_yawSpeed*
^^^^

 - *Default:* "140"| *Possible range:* "0" = disabled; < ?
 - Specify the speed of +left and +right keys. 

--------

*COM_* (Common)
-----

*com_altivec* |CVAR added|
^^^^

{TODO} *What is this used for?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 -  Description needed. 

--------

*com_ansiColor* |CVAR added|
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 -  Enables color output in the system console. 

--------

*com_buildScript*
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 -  Force loading of all possible data and error on failures for automated data building scripts. 

--------

|ss|com_cameraMode|se| |CVAR removed|
^^^^

 - *Default:* "0"| *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

*com_cl_running* |CVAR private|
^^^^

{TODO} *What is this used for? "Unknown CVAR" ingame*

 - *Default:* "0"| *Possible values:* 
 -  Non-user CVAR

--------

*com_cleanWhiteList* |CVAR added|
^^^^

{TODO} *Shouldn't this be read-only?*

 - *Default:* "z_hdet"| *Possible values:* 
 -  Files listed in the com_cleanWhitelist cvar are protected during deletion of incomplete downloads and other garbage. 

--------

*com_crashed*
^^^^

{TODO} *Is this supposed to be accessible by the user? It sounds like this should be an automated internal CVAR.*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 -  Enable in case of a crash to prevent CVAR_UNSAFE variables from being set from a cfg.
 - *See also:* [[List_of_Cvars_(new)/#com_ignoreCrash|com_ignoreCrash]] 

--------

*com_dedicated* |CVAR private|
^^^^

{TODO} *What is this used for? "Unknown CVAR" ingame*

 - *Default:* "0" = hidden| *Possible values:* "0" = hidden; "1" = LAN; "2" = Internet
 -  Non-user CVAR used to set mode of server? 

--------

*com_developer* |CVAR private|
^^^^

{TODO} *What is this used for? "Unknown CVAR" ingame*

 - *Default:* | *Possible values:* 
 -  Non-user CVAR to toggle some sort of developer mode? 

--------

*com_downloadURL* |CVAR private|
^^^^

 - *Default:* " " = Windows| *Possible values:* address string
 -  Non-user CVAR specifying the address which is used for the download command. 

--------

*com_dropSim* |CVAR protected|
^^^^

{TODO} *What's the point of this CVAR?*

 - *Default:* "0.0" = disabled| *Possible range:* "0.0" < "1.0"
 -  Simulated packet drops. 

--------

*com_errorDiagnoseIP* |CVAR private|
^^^^

{TODO} unknown CVAR ingame. Check.

 - *Default:* " "| *Possible values:* server address 
 -  Catch a connection process that would turn bad. 

--------

*com_fixedtime* |CVAR private|
^^^^

{TODO} *What is this used for? "Unknown CVAR" ingame*

 - *Default:* "0" | *Possible values:* 
 -  Non-user CVAR to fix time? 

--------

*com_hunkMegs*
^^^^

 - *Default:* "128"| *Possible values:* 
 -  Amount of memory (RAM) assigned to the hunk, *in MB*.
 - *See also:* [[List_of_Cvars_(new)/#com_soundMegs|com_soundMegs]] and [[List_of_Cvars_(new)/#com_zoneMegs|com_zoneMegs]] 

--------

*com_hunkUsed*
^^^^

{TODO} *Should this be accessible to the user? This sounds like it should be read-only*
{TODO} *Which unit is this?*

 - *Default:* "0"| *Possible values:* 
 -  Size of the currently used hunk, *in [?]*. 

--------

*com_ignoreCrash*
^^^^

{TODO} *Combine with com_crashed*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 -  Let ET override CVAR_UNSAFE in case of crash. Use only if you know what you are doing!
 - *See also:* [[List_of_Cvars_(new)/#com_crashed|com_crashed]] 

--------

*com_introPlayed*
^^^^

{TODO} *Should this be accessible to the user? This sounds like it should be read-only*
{TODO} *Also, since we don't have an intro, can this be removed?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 -  CVAR seems to have no effect in ETL and ET. Likely intended to fetch the status of the game at startup? 

--------

*com_journal* |CVAR private|
^^^^

{TODO} *What is this used for? "Unknown CVAR" ingame*

 - *Default:* "0" | *Possible values:* 
 -  Non-user CVAR to open a journal? 

--------

*com_logfile* |CVAR private|
^^^^

{TODO} *What is this used for? "Unknown CVAR" ingame*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = buffer log; "2" = flush after each print
 -  Non-user CVAR

--------

|ss|com_logosPlaying|se| |CVAR removed|
^^^^

 - *Default:* "0" | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

*com_maxFPS*
^^^^

 - *Default:* "85"| *Possible range:* "20" < "333"
 -  Specifies the maximum frames per second the game can reach for a stable render rate. 

--------

*com_minimized* |CVAR added|
^^^^

{TODO} *Shouldn't this be read-only?*

 - *Default:* "0" = maximized| *Possible values:* "0" = maximized; "1" = minimized
 -  Used  to catch the state of the game. Is the window minimized or not? 

--------

*com_missingFiles* |CVAR private|
^^^^

 - *Default:* " "| *Possible values:* 
 -  Non-user CVAR storing information regarding missing files. Used for displaying error messages to the user. 

--------

*com_motd* |CVAR added|
^^^^

{TODO} *What exactly is this used to? "0" also displays the MOTD*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Display the official ET: Legacy "message of the day". 

--------

*com_motdString* |CVAR added|
^^^^

{TODO} *Description correct?*

 - *Default:* " "| *Possible values:* string
 - The official ET: Legacy "message of the day" string used to communicate news to players. 

--------

*com_pid* |CVAR private|
^^^^

 - *Default:* | *Possible values:* 
 -  Read-only CVAR storing process id. 

--------

*com_pidFile* |CVAR added|
^^^^

 - *Default:* | *Possible values:* "profiles/name/profile.pid" = client
 -  - "etlegacy_server.pid" = server
 Full path to the pid file (contains process id). 

--------

*com_recommended* |CVAR private|
^^^^

{TODO} *This CVAR is used once during the entire installation lifecycle. Is it necessary?*

 - *Default:* " "| *Possible values:* 
 -  Non-user CVAR used during the profile creation. Use recommended settings or not? 

--------

*com_recommendedSet*
^^^^

{TODO} *Combine with com_recommended.*

 - *Default:* " "| *Possible values:* 
 -  When enabled, the game uses default (recommended) values during profile creation. 

--------

*com_showTrace* |CVAR protected|
^^^^

{TODO} *What information is printed here?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 -  Prints trace information to the console. Used for debugging. 

.. image:: https://i.imgur.com/qJ3hTM8.jpg 

--------

*com_soundMegs*
^^^^

 - *Default:* "160"| *Possible values:* 
 -  Amount of memory (RAM) allocated for loading sound files, *in MB*. 
 - *See also:* [[List_of_Cvars_(new)/#com_hunkMegs|com_hunkMegs]] and [[List_of_Cvars_(new)/#com_zoneMegs|com_zoneMegs]] 

--------

*com_speeds*
^^^^

{TODO} *What information is printed here?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 -  Prints speed information per frame to the console. Used for debugging. 

.. image:: https://i.imgur.com/lXq6Lv3.jpg 

--------

*com_sv_running* |CVAR private|
^^^^

{TODO} *What is this used for? "Unknown CVAR" ingame*

 - *Default:* "0"| *Possible values:* 
 -  Non-user CVAR

--------

*com_timeDemo* |CVAR private|
^^^^

{TODO} *What is this used for? "Unknown CVAR" ingame*

 - *Default:* "0"| *Possible values:* 
 -  Non-user CVAR

--------

*com_timeScale* |CVAR private|
^^^^

{TODO} *What is this used for? "Unknown CVAR" ingame*

 - *Default:* "1.0"| *Possible values:* 
 -  Non-user CVAR used to change speed of the game?
 - From code: if com_timescale below 1.0, then we pass one frame on "1.0/com_timescale" (eg: com_timescale = 0.5, then 1.0/0.5 = 2, so we pass one frame on two) 

--------

*com_unfocused* |CVAR added|
^^^^

{TODO} *Shouldn't this be read-only?!*

 - *Default:* "0" = focused| *Possible values:* "0" = focused; "1" = unfocused
 -  Used mainly in windowed mode to catch the state of the game. Is the window active or not? 

--------

*com_updateAvailable* |CVAR private|
^^^^

 - *Default:* "0" = no| *Possible values:* "0" = no; "1" = yes
 - If there is a newer version than the current one this CVAR is enabled. 

--------

*com_updateFiles* |CVAR private|
^^^^

 - *Default:* " " | *Possible values:* 
 - Stores information regarding remainging files needed for the update. 

--------

*com_updateMessage* |CVAR private|
^^^^

{TODO} *Shouldn't this be read-only? Or rather, shouldn't this be hardcoded without a CVAR?*

 - *Default:* "New version available. Do you want to update now?" | *Possible values:* 
 - Stores the string used for the pop-up when there is a new update. 

--------

*com_version* |CVAR private|
^^^^

{TODO} *What is this used for? "Unknown CVAR" ingame*

 - *Default:* " "| *Possible values:*
 -  Non-user CVAR. 

--------

*com_viewLog* |CVAR private|
^^^^

{TODO} *What is this used for? "Unknown CVAR" ingame*

 - *Default:* "0" = hidden| *Possible values:* "0" = hidden, "1" = visible, "2" = minimized
 -  Non-user CVAR used to view the log? 

--------

*com_watchdog* |CVAR private|
^^^^

 - *Default:* "60"| *Possible values:* 
 -  Non-user CVAR used to check whether the game died with an ERR_DROP or any situation leading to server running with no map. 
 - *See also:* [[List_of_Cvars_(new)/#com_watchdog_cmd|com_watchdog_cmd]] 

--------

*com_watchdog_cmd* |CVAR private|
^^^^

 - *Default:* " "| *Possible values:* e.g. "exec mapvotecycle.cfg" 
 -  Non-user CVAR specifying the actions in an event where com_watchdog triggers. 
 - *See also:* [[List_of_Cvars_(new)/#com_watchdog|com_watchdog]] 

--------

*com_zoneMegs*
^^^^

 - *Default:* " "| *Possible values:* 
 -  Amount of memory (RAM) allocated for the random block zone, *in MB*.
 - *NOTE:* com_zoneMegs can only be set on the command line, and not in etconfig.cfg or Com_StartupVariable. "[Reference]":https://github.com/etlegacy/etlegacy/blob/f0bf85d7e1b1675b9e69ce6b47d3c12604406560/src/qcommon/common.c#L1674
 - *See also:* [[List_of_Cvars_(new)/#com_hunkMegs|com_hunkMegs]] and [[List_of_Cvars_(new)/#com_soundMegs|com_soundMegs]] 

--------

*CON_* (Console)
-----

*con_autoClear*
^^^^

{TODO} *CVAR looks unused.*

 - *Default:* "1" | *Possible values:* 
 -  Description needed. 

--------

|ss|con_debug|se| |CVAR removed|
^^^^

 - *Default:* "0" | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

*con_drawNotify* |CVAR protected|
^^^^

{TODO} *CVAR to be reworked! "Ticket":https://dev.etlegacy.com/issues/1258*

 - *Default:* "0" = disabled | *Possible values:* "0" = disabled; "1" = enabled 
 -  Prints the last few lines of console output transparently on the top of the screen. 
 - *See also:* [[List_of_Cvars_(new)/#con_notifyTime|con_notifyTime]], [[List_of_Cvars_(new)/#con_numNotifies  |con_numNotifies  ]] 

--------

*con_notifyTime*
^^^^

 - *Default:* "7" | *Possible range:* "0" = disabled; < ?
 -  Duration for which the notification prints on the top of the screen are displayed, in *seconds*.
 - *See also:* [[List_of_Cvars_(new)/#con_drawNotify|con_drawNotify]], [[List_of_Cvars_(new)/#con_numNotifies|con_numNotifies]]  

--------

*con_numNotifies*
^^^^

 - *Default:* "7" | *Possible range:* "0" = disabled; < ?
 -  Change number of drawable notifies. Allows to draw up to 10 lines.
 - *See also:* [[List_of_Cvars_(new)/#con_drawNotify|con_drawNotify]], [[List_of_Cvars_(new)/#con_numNotifies|con_numNotifies]]  

--------

|ss|con_restricted|se| |CVAR removed|
^^^^

 - *Default:* "0" | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

*DEMO_* (Demo)
-----

*demo_autoTimeScale* |CVAR added| 
^^^^

{TODO} *Check description and send kemon a screenshot of it in action please.*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Automatically adjust demo playback speed depending on currently active weapon? 

--------

*demo_autoTimeScaleWeapons* |CVAR added| 
^^^^

{TODO} *Check description and send kemon a screenshot of it in action please.*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Define timescales for different weapons? 

--------

*demo_avifpsF1*
^^^^

 - *Default:* "0" | *Possible values:* 
 -  Presets for the rate of avi demos, in *screenshots per second*. 

--------

*demo_avifpsF2*
^^^^

 - *Default:* "10" | *Possible values:* 
 -  Presets for the rate of avi demos, in *screenshots per second*. 

--------

*demo_avifpsF3*
^^^^

 - *Default:* "15" | *Possible values:* 
 -  Presets for the rate of avi demos, in *screenshots per second*. 

--------

*demo_avifpsF4*
^^^^

 - *Default:* "20" | *Possible values:* 
 -  Presets for the rate of avi demos, in *screenshots per second*. 

--------

*demo_avifpsF5*
^^^^

 - *Default:* "24" | *Possible values:* 
 -  Presets for the rate of avi demos, in *screenshots per second*. 

--------

*demo_drawTimeScale*
^^^^

{TODO} *Only works if set before loading the demo. Can't be changed during runtime of demo. Timescale pop-up only remains on-screen for a few seconds and then can't be brought back.*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Prints the current timescale (demo playback speed) on the screen. 

.. image:: https://i.imgur.com/RmA0Zl7.jpg 

--------

*demo_followDistance* |CVAR added| 
^^^^

{TODO} *Check description and send kemon a screenshot of it in action please.*

 - *Default:* "50 0 20"| *Possible values:* integers for X Y Z
 - Specifies the distance from the player origin for all axes. 

--------

*demo_freeCamSpeed* |CVAR added| 
^^^^

{TODO} *Check description and send kemon a screenshot of it in action please.*

 - *Default:* "800"| *Possible range:* "0" = static [?]; < ?
 - Define the speed of the free camera, *in in-game units per second* 

--------

*demo_infoWindow*
^^^^

{TODO} *Only works if set before loading the demo. Can be activated if it was 0 before loading demo, but can't be disabled/reactivated again.*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Prints an infobox on the screen for useful keybinds. 

.. image:: https://i.imgur.com/eXvhfpu.jpg 

--------

*demo_lookAt* |CVAR added| 
^^^^

{TODO} *Check description and send kemon a screenshot of it in action please.*

 - *Default:* "-1"| *Possible values:*  
 - Specify the number of the entity the camera should focus on. 

--------

*demo_noPitch* |CVAR added| 
^^^^

{TODO} *Check description and send kemon a screenshot of it in action please.*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Description needed. 

--------

*demo_pvsHint* |CVAR added| 
^^^^

{TODO} *Check description and send kemon a screenshot of it in action please.*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Description needed. 

--------

*demo_teamOnlyMissileCam* |CVAR added| 
^^^^

{TODO} *Check description and send kemon a screenshot of it in action please.*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Description needed. 

--------

*demo_weaponCam* |CVAR added| 
^^^^

{TODO} *Send kemon a screenshot of it in action please.*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Triggers weapon cam view. 

--------

*demo_yawPitchRollSpeed* |CVAR added| 
^^^^

{TODO} *Check description and send kemon a screenshot of it in action please.*

 - *Default:* "140 140 140"| *Possible values:* integers for yawturn-; pitchturn-; roll-speed
 - Specifies the yawturn-, pitchturn- and roll-speed values for demo playback. 

--------

*FS_* (File System)
-----

|ETL logo| NOTE: File system CVARs need to be set before game start and can't be changed during runtime 

*fs_baseGame*
^^^^

{TODO} *Description needed*

 - *Default:* " "| *Possible values:* 
 - Write-protected CVAR displaying exactly what?

--------

*fs_basePath*
^^^^

{TODO} *Displays only a single dot and not a path to the installation folder, why is that?*

 - *Default:* "."| *Possible values:* 
 - Write-protected CVAR specifying the path to the ET installation folder.
 - *See also:* [[Path_and_file_structure#Homepath-fs_basepath|Path and File Structure]] 

--------

|ss|fs_buildGame|se| |CVAR removed|
^^^^

 - *Default:* " " | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

|ss|fs_buildPath|se| |CVAR removed|
^^^^

 - *Default:* " " | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

|ss|fs_CDpath|se| |CVAR removed|
^^^^

 - *Default:* " " | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

|ss|fs_copyFiles|se| |CVAR removed|
^^^^

 - *Default:* " " | *Possible values:* 
 - CVAR was unused and has therefore been removed. 

--------

*fs_debug*
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Run the game in debug mode. Prints additional information regarding read files into the console. 

.. image:: https://i.imgur.com/ShVviJn.jpg 

--------

*fs_game*
^^^^

 - *Default:* "legacy"| *Possible values:* mod names _(aka folder names in fs_homepath)_
 - Run the game with this default mod. 

--------

*fs_homePath*
^^^^

 - *Default:* "OS dependent":https://dev.etlegacy.com/projects/etlegacy/wiki/Path_and_file_structure#Homepath-fs_homepath| *Possible values:* paths to directories
 - Contains all downloaded pk3, log, config and extracted binary files.
 - *See also:* [[Path_and_file_structure#Homepath-fs_homepath|Path and File Structure]] 

--------

*fs_openedList*
^^^^

{TODO} *Please add explanation of difference to fs_referencedList to the description.*

 - *Default:* " "| *Possible values:* 
 - Prints a list of opened PK3 names and their path to the console. 

--------

*fs_referencedList*
^^^^

{TODO} *Please add explanation of difference to fs_openedList to the description.*

 - *Default:* " "| *Possible values:* 
 - Prints a list of referenced PK3 names to the console. 

--------

|ss|fs_restrict|se| |CVAR removed|
^^^^

 - *Default:* " " | *Possible values:* 
 - Restrictions on mod/content usage. Demo and beta testing relic. 

--------

*fs_gameDirVar*
^^^^

{TODO} *CVAR looks unused. Safe to remove?*

 - *Default:* " "| *Possible values:* 
 - Description needed. 

--------

*G_* (Game)
-----

*g_alliedMapXP*
^^^^

{TODO} *Seems to never change its value. What does it do exactly?*

 - *Default:* "0"| *Possible values:* 
 - Likely intended to store the accumulated XP of the entire Allied team of the current map/campaign?
 - *See also:* [[List_of_Cvars_(new)/#g_axisMapXP|g_axisMapXP]] 

--------

*g_alliedMaxLives*
^^^^

 - *Default:* "0"| *Possible values:* 
 - Specifies the amount of lives each Allied player has individually. These lives are not shared across the team. The HUD counter seen in the screenshot displays the amount of respawns you have left.
 - *See also:* [[List_of_Cvars_(new)/#g_axisMaxLives|g_axisMaxLives]] 

.. image:: https://i.imgur.com/qEaZYch.jpg 

--------

*g_alliedWins*
^^^^

{TODO} *Is it necessary that this works like bitflags? Feels a bit counter-intuitive.*

 - *Default:* "0"| *Possible values:* 
 - Stores the amount of wins of the Allied team in the currently active campaign.
 - *NOTE:* This works like bitflags (1, 2, 4, 8, etc.) So, if the Allied team has three wins the CVAR has a value of 7 (1 + 2 + 4).
 - *See also:* [[List_of_Cvars_(new)/#g_axisWins|g_axisWins]] 

--------

*g_altStopwatchMode*
^^^^

 - *Default:* "0" = A-B-B-A| *Possible values:* "0" = A-B-B-A; "1" = A-B-A-B
 - Switches between two different Stopwatch types of attacker team turns. 

--------

*g_antiLag*
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - https://i.imgur.com/6b2wv1f.png!:https://i.imgur.com/6b2wv1f.png Enables modem-friendly server support. 
 - *See also:* 
 - [[List_of_Cvars_(new)/#g_balancedTeams|g_balancedTeams]] 

--------

*g_autoFireteams*
^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Toggles providing players with a popup asking to join a Fireteam when joining a team. 

--------

*g_axisMapXP*
^^^^

{TODO} *Seems to never change its value. What does it do exactly?*

 - *Default:* "0"| *Possible values:* 
 - Likely intended to store the accumulated XP of the entire Axis team of the current map/campaign?
 - *See also:* [[List_of_Cvars_(new)/#g_alliedMapXP|g_alliedMapXP]] 

--------

*g_axisMaxLives*
^^^^

 - *Default:* "0"| *Possible values:* 
 - Specifies the amount of lives each Axis player has individually. These lives are not shared across the team. The HUD counter seen in the screenshot displays the amount of respawns you have left. 
 - *See also:* [[List_of_Cvars_(new)/#g_alliedMaxLives|g_alliedMaxLives]] 

.. image:: https://i.imgur.com/qEaZYch.jpg 

--------

*g_axisWins*
^^^^

{TODO} *Is it necessary that this works like bitflags? Feels a bit counter-intuitive.*

 - *Default:* "0"| *Possible values:* 
 - Stores the amount of wins of the Axis team in the currently active campaign.
 - *NOTE:* This works like bitflags (1, 2, 4, 8, etc.) So, if the Axis team has three wins the CVAR has a value of 7 (1 + 2 + 4). 
 - *See also:* [[List_of_Cvars_(new)/#g_alliedWins|g_alliedWins]] 

--------

*g_balancedTeams*
^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - https://i.imgur.com/gLcBd4P.png!:https://i.imgur.com/gLcBd4P.png If enabled, players are prevented from joinging the team with more players.
 - *See also:* 
 - [[List_of_Cvars_(new)/#g_antiLag|g_antiLag]] 

--------

*R_* (Renderer)
-----

*r_allowExtensions*
^^^^

 - *Default:* "1.2"| *Possible values:*  "0" = disabled; "1" = enabled. 
 - Enables/Disables global OpenGL extensions. 

--------

*r_ambientScale* |CVAR protected|
^^^^

{TODO} *Add images.*

 - *Default:* "0.5"| *Possible values:* "0.0" = disabled; "2.0" = max. 
 - Sets light intensity of dynamic game entities _(e.g. player models, construction crates and tanks)_. 

--------

|ss|r_ati_fsaa_samples|se| |CVAR removed|
^^^^

{TODO} *Seems to be removed in ETL, please check.*

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

|ss|r_ati_truform_normalmode|se| |CVAR removed|
^^^^

 - *Default:* | *Possible values:* 
 - Obsolete ATI specific extensions. 

--------

|ss|r_ati_truform_pointmode|se| |CVAR removed|
^^^^

 - *Default:* | *Possible values:* 
 - Obsolete ATI specific extensions. 

--------

|ss|r_ati_truform_tess|se| |CVAR removed|
^^^^

 - *Default:* | *Possible values:* 
 - Obsolete ATI specific extensions. 

--------

*r_bonesDebug* |CVAR protected|
^^^^

{TODO} *Seems to be under development. Value of "8" and "9" flood a todo message in console.*

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_buildScript*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_cache*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_cacheGathering*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_cacheModels*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_cacheShaders*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_clampToEdge*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_clear*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_colorbits*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_colorMipLevels*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_customaspect*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_customheight*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_customwidth*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_debugLight*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_debugSort*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_debugSurface*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_depthbits*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_detailTextures*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_directedScale*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_displayRefresh*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_dlightBacks*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_drawBuffer*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_drawentities*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_drawfoliage*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_drawSun*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_drawworld*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_dynamiclight*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_ext_ATI_pntriangles*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_ext_compiled_vertex_array*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_ext_compressed_textures*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_ext_gamma_control*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_ext_multitexture*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_ext_NV_fog_dist*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_ext_texture_env_add*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_ext_texture_filter_anisotropic*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_facePlaneCull*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_fastsky*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_finish*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_flareFade*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_flares*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_flareSize*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_fullscreen*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_gamma*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_glDriver*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_glIgnoreWicked3D*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_highQualityVideo*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_ignore*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_ignoreFastPath*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_ignoreGLErrors*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_ignorehwgamma*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_inGameVideo*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_intensity*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_lightmap*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_lockpvs*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_lodbias*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_lodCurveError*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_lodscale*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_logFile*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_mapOverBrightBits*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_maxpolys*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_maxpolyverts*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_measureOverdraw*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_mode*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_nobind*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_nocull*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_nocurves*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_noportals*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_norefresh*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_normallength*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_novis*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_nv_fogdist_mode*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_offsetFactor*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_offsetUnits*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_oldMode*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_overBrightBits*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_picmip*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_portalOnly*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_portalsky*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_primitives*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_printShaders*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_railCoreWidth*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_railSegmentLength*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_railWidth*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_rmse*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_roundImagesDown*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_saveFontData*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_shadows*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_showcluster*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_showImages*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_shownormals*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_showmodelbounds*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_showsky*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_showSmp*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_showtris*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_simpleMipMaps*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_singleShader*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_skipBackEnd*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_smp*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_speeds*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_stencilbits*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_stereo*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_subdivisions*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_swapInterval*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_textureAnisotropy*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_texturebits*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_textureMode*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_trisColor*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_uiFullScreen*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_verbose*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_wolffog*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_zfar*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_znear*
^^^^

 - *Default:* | *Possible values:* 
 - Description needed. 

--------
