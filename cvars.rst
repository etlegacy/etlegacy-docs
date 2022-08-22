===================
List of CVARs
===================

Enemy Territory: Legacy, just like the original Wolfenstein: Enemy Territory, offers a wide range of console variables, so-called *CVARs*. These are options that can be used to customize the game's behaviour, setup and appearance to accommodate the player's needs or preferences. Most can be set from the menu. But all can be set from inside a configuration file _(.cfg)_ , the command line or, in most cases from the console.

Version goes here:

.. contents:: `Table of contents`
   :depth: 1
   :local:
   
--------

.. |ETL logo|       image:: https://raw.githubusercontent.com/etlegacy/etlegacy-assets/master/logo/regular_black.png
					      :width:  1592 px
					      :height: 1990 px
					      :scale:  2 %
						  
.. |ss| raw:: html

   <s>

.. |se| raw:: html

   </s>

*Non prefixed CVARS*
----------------------------------------
.. contents:: `CVAR Types`
   :depth: 1
   :local:

Player cvars
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*sensitivity*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-------------------------------------------+
  | Default                             | 5.0                                       |
  +-------------------------------------+-------------------------------------------+
  | Range start                         | Range end                                 |
  +=====================================+===========================================+
  | 0                                   | No functional limit                       |
  +-------------------------------------+-------------------------------------------+
  | .. centered:: Defines the sensitivity of mouse movements. E.g. looking around.  |
  |               Higher is faster                                                  |
  +---------------------------------------------------------------------------------+

--------

Developer cvars
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*timescale*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-------------------------------------------+
  | Default                             | 1.0                                       |
  +-------------------------------------+-------------------------------------------+
  | Range start                         | Range end                                 |
  +=====================================+===========================================+
  | 0                                   | No functional limit                       |
  +-------------------------------------+-------------------------------------------+
  | .. centered:: Scale of which time passes by                                     |
  +---------------------------------------------------------------------------------+

--------

*CG_* (Client Game)
----------------------------------------
.. contents:: `CVAR Types`
   :depth: 1
   :local:

Player cvars
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*cg_activateLean*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 0       | 1       | 0        |
  +---------+---------+----------+

 - Lean while using the activate button

--------

*cg_altHud*
""""""""""""""""""""""""""""""""""""""""
  +-------------------------------------+------------------------------------------+
  | Default                             | 0                                        |
  +-------------------------------------+------------------------------------------+
  | Value                               | Effect                                   |
  +=====================================+==========================================+
  | 0                                   | Selects default hud                      |
  +-------------------------------------+------------------------------------------+
  | 1                                   | Selects alternative hud 1                |
  +-------------------------------------+------------------------------------------+
  | 2                                   | Selects alternative hud 2                |
  +-------------------------------------+------------------------------------------+
  | 3                                   | Selects `alternative hud 3`_             |
  +-------------------------------------+------------------------------------------+

 - Choose from different premade HUD styles.
 - Works in combination with cg_altHudFlags.

.. _alternative hud 3: https://i.imgur.com/6dKSdbB.jpg

--------

*cg_altHudFlags*
""""""""""""""""""""""""""""""""""""""""
  +-------------------------------------+-------------------------------------------+
  | Default                             | 0                                         |
  +-------------------------------------+-------------------------------------------+
  | Value                               | Effect                                    |
  +=====================================+===========================================+
  | 0                                   | Default HUD                               |
  +-------------------------------------+-------------------------------------------+
  | 1                                   | `Moves timers to a alternative position`_ |
  +-------------------------------------+-------------------------------------------+
  | 2                                   | Removes ranks                             |
  +-------------------------------------+-------------------------------------------+
  | 3                                   | Combines effect of 1 & 2                  |
  +-------------------------------------+-------------------------------------------+
  | 4                                   | Moves popups to a alternative position    |
  +-------------------------------------+-------------------------------------------+
  | 5                                   | Combines effect of 1 & 4                  |
  +-------------------------------------+-------------------------------------------+
  | 6                                   | Combines effect of 2, 4                   |
  +-------------------------------------+-------------------------------------------+
  | 7                                   | Combines effect of 1, 2, 4                |
  +-------------------------------------+-------------------------------------------+

 - Move the spawn timer and mission timer and other HUD elements to a alternative location.
 - The value is a bitflag. A bit flag is a number that combines multiple values in a single number.
 - This cvar will be removed in the future, see `HUD Rework`_.

.. _Moves timers to a alternative position: https://i.imgur.com/lGjIJmo.jpg
.. _HUD Rework: https://github.com/etlegacy/etlegacy/issues/1967

--------

*cg_announcer*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Toggles the announcer voice on map start _("FIGHT!")_, and _("Prepare to Fight!")_.

--------

*cg_atmosphericEffects*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Toggles display of atmospheric map effects like rain and snow.

--------

*cg_autoAction*
""""""""""""""""""""""""""""""""""""""""
  +-------------------------------------+------------------------------------------+
  | Default                             | 0                                        |
  +-------------------------------------+------------------------------------------+
  | Value                               | Effect                                   |
  +=====================================+==========================================+
  | 0                                   | No action                                |
  +-------------------------------------+------------------------------------------+
  | 1                                   | Record demo at start of map / round      |
  +-------------------------------------+------------------------------------------+
  | 2                                   | Screenshot at end of map / round         |
  +-------------------------------------+------------------------------------------+
  | 3                                   | Combines effect of 1 & 2                 |
  +-------------------------------------+------------------------------------------+
  | 4                                   | Save player stats to .txt file on disk   |
  +-------------------------------------+------------------------------------------+
  | 5                                   | Combines effect of 4 & 1                 |
  +-------------------------------------+------------------------------------------+
  | 6                                   | Combines effect of 4 & 2                 |
  +-------------------------------------+------------------------------------------+
  | 7                                   | Combines effect of 1, 2, 4               |
  +-------------------------------------+------------------------------------------+

  - The value is a bitflag. A bit flag is a number that combines multiple values in a single number.
  - Refer to the [[Path_and_File_Structure|Path and File Structure]] wiki article for where to find the saved files.

--------

*cg_autoActivate*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Toggles automatically picking up items such as ammo/health packs, weapons, objectives, etc.

--------

*cg_autoMapZoom*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-------------------------------------------+
  | Default                             | 5.159                                     |
  +-------------------------------------+-------------------------------------------+
  | Range start                         | Range end                                 |
  +=====================================+===========================================+
  | 1                                   | 7.43                                      |
  +-------------------------------------+-------------------------------------------+
  |                   .. centered:: Higher value is more zoomed in.                 |
  +---------------------------------------------------------------------------------+

 - Adjust the zoom level of the compass minimap.
 - There is no limit on the range when setting the cvar manually.

--------

*cg_autoReload*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Automatically reload weapon when clip becomes empty. Keep in mind that reloading can't be cancelled!

--------

*cg_autoSwitch*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Automatically switch to a new weapon when out of ammunition.
 - *CAREFUL:* Do not confuse with `cg_noAmmoAutoSwitch`_!

--------

*cg_showBlood*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Toggles showing blood spurt effect when players are shot

--------

*cg_bloodDamageBlend*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 1.0                                           |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0.0                                 | 1.0                                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Opaqueness of on-screen blood splatter effect when you are being shot |
  +-------------------------------------------------------------------------------------+

 - Menu entries are None, Light, Medium, Heavy, Full. Value increased by 0.25 per step respectively.

--------

*cg_bloodFlash*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 1.0                                           |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0.0                                 | 1.0                                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Scale of on-screen blood splatter effect when you are being shot      |
  +-------------------------------------------------------------------------------------+

 - Menu entries are None, Light, Medium, Heavy, Full. Value increased by 0.25 per step respectively.

--------

*cg_bloodTime*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 120                                           |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0                                   | No functional limit                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Duration of blood puddle effects _(walls, floors, etc.)_ in *seconds* |
  +-------------------------------------------------------------------------------------+

 - *See also:* `cg_brassTime`_ and `cg_markTime`_

--------

*cg_brassTime*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 2500                                          |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0                                   | No functional limit                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Duration ejected bullet shells last for, in *milliseconds*            |
  +-------------------------------------------------------------------------------------+

 - Menu entries are Off, Med, High. Values are 0, 2500 and 15000 respectively.
 - See also: `cg_bloodTime`_ and `cg_markTime`_

--------

*cg_centerTime*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 5                                             |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0                                   | No functional limit                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Duration for which center print popups are displayed, in *seconds*    |
  +-------------------------------------------------------------------------------------+

 - See `example <https://i.imgur.com/4mH3cw3.jpg>`__
 - *See also:* `cg_fontScaleCP`_

--------

*cg_complaintPopUp*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Display the UI popup to file complaints against teammates who teamkill you.
 - See `example <https://i.imgur.com/KFBjriT.jpg>`__

--------

*cg_coronaFarDist*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 1536                                          |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0                                   | No functional limit                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Maximum distance coronas are displayed before fading from view        |
  +-------------------------------------------------------------------------------------+

 - Menu entries are Off, Near, Normal, Far. Values are 0, 800 and 1536, 4096, 16000 respectively.
 - See `cg_coronas`_ for toggling the effect.

--------

*cg_coronas*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+---------------------------------------------------+
  | Default                             | 1                                                 |
  +-------------------------------------+---------------------------------------------------+
  | Value                               | Effect                                            |
  +=====================================+===================================================+
  | 0                                   | Disabled                                          |
  +-------------------------------------+---------------------------------------------------+
  | 1                                   | Enabled                                           |
  +-------------------------------------+---------------------------------------------------+
  | 2                                   | Traces everything and ignores `cg_coronaFarDist`_ |
  +-------------------------------------+---------------------------------------------------+

 - Toggles the display of coronas.
 - See `cg_coronaFarDist`_ for adjusting the draw distance of the effect.

--------

*cg_countryflags*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Displays players' country flags in score board.
 - See `example <https://i.imgur.com/mKfD3X1.jpg>`__

--------

*cg_crosshairAlpha*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 1.0                                           |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0.0                                 | 1.0                                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Transparency level for the primary crosshair                          |
  +-------------------------------------------------------------------------------------+

--------

*cg_crosshairAlphaAlt*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 1.0                                           |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0.0                                 | 1.0                                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Transparency level for the secondary crosshair                        |
  +-------------------------------------------------------------------------------------+

--------

*cg_crosshairColor*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "white". For menu values see :ref:`menu-colors`
 - You can also use custom Hex colour codes in this format: 0xFF1E00
 - Set the colour for the primary crosshair.
 - See `example <https://i.imgur.com/30FkqjJ.jpg>`__

--------

*cg_crosshairColorAlt*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "white". For menu values see :ref:`menu-colors`
 - You can also use custom Hex colour codes in this format: 0xFF1E00
 - Set the colour for the secondary crosshair.
 - See `example <https://i.imgur.com/FYbv4bX.jpg>`__

--------

*cg_crosshairHealth*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 0       | 1       | 0        |
  +---------+---------+----------+

 - Colors the crosshair based on current health _(overrides `cg_crosshairColor`_ settings)_.
 - See `example <https://i.imgur.com/2rDVcSQ.jpg>`__

--------

*cg_crosshairPulse*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Increases the crosshair spread/sizing while moving, shooting, etc. to provide a visual representation of actual weapon spread.
 - See `example <https://i.imgur.com/a3WyWQl.jpg>`__

--------

*cg_crosshairSize*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 48                                            |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0                                   | No functional limit                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Size of the displayed crosshair, in *pixels*                          |
  +-------------------------------------------------------------------------------------+

 - Menu entries are Tiny, Small, Medium, Large, Huge. Values are 24, 32, 48, 64 and 96 respectively.
 - See `example <https://i.imgur.com/BSDGLLk.jpg>`__

--------

*cg_crosshairX*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 0                                             |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | (Your resolution / 2) * -1          | Your resolution / 2                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Offset of the crosshair position on-screen, in *pixels*. Left - Right |
  +-------------------------------------------------------------------------------------+

 - See `example <https://i.imgur.com/PClrjlj.jpg>`__

--------

*cg_crosshairY*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 0                                             |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | (Your resolution / 2) * -1          | Your resolution / 2                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Offset of the crosshair position on-screen, in *pixels*. Up - Down    |
  +-------------------------------------------------------------------------------------+

 - See `example <https://i.imgur.com/zc7YuSS.jpg>`__

--------

*cg_cursorHints*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Displays hint and information icons for certain actions when near interactive objects.
 - See `example <https://i.imgur.com/1F4sy6Q.jpg>`__

--------

*cg_cycleAllWeaps*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - When enabled loops around while cycling through inventory.
 - Include non-weapon items when cycling through inventory.

--------


*cg_drawCompass*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+------------------------------------------+
  | Default                             | 1                                        |
  +-------------------------------------+------------------------------------------+
  | Value                               | Effect                                   |
  +=====================================+==========================================+
  | 0                                   | Disable compass                          |
  +-------------------------------------+------------------------------------------+
  | 1                                   | Selects default compass                  |
  +-------------------------------------+------------------------------------------+
  | 2                                   | Selects alternative compass              |
  +-------------------------------------+------------------------------------------+

 - Display the HUD compass.

--------

*cg_drawCrosshair*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "1", See :ref:`crosshairs`

--------

*cg_drawCrosshairInfo*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+------------------------------------------+
  | Default                             | 3                                        |
  +-------------------------------------+------------------------------------------+
  | Value                               | Effect                                   |
  +=====================================+==========================================+
  | 0                                   | Disabled                                 |
  +-------------------------------------+------------------------------------------+
  | 1                                   | Shows player class                       |
  +-------------------------------------+------------------------------------------+
  | 2                                   | Shows player rank                        |
  +-------------------------------------+------------------------------------------+
  | 3                                   | Shows player class + rank                |
  +-------------------------------------+------------------------------------------+
  | 4                                   | Shows player prestige                    |
  +-------------------------------------+------------------------------------------+
  | 5                                   | Shows player class + prestige            |
  +-------------------------------------+------------------------------------------+
  | 6                                   | Shows player rank + prestige             |
  +-------------------------------------+------------------------------------------+
  | 7                                   | Shows player class + rank + prestige     |
  +-------------------------------------+------------------------------------------+

 - Displays player info when the crosshair is over a teammate.
 - See `example <https://i.imgur.com/s8bt3oP.jpg>`__

--------

*cg_drawCrosshairNames*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+------------------------------------------+
  | Default                             | 1                                        |
  +-------------------------------------+------------------------------------------+
  | Value                               | Effect                                   |
  +=====================================+==========================================+
  | 0                                   | Disabled                                 |
  +-------------------------------------+------------------------------------------+
  | 1                                   | Enabled, white names                     |
  +-------------------------------------+------------------------------------------+
  | 2                                   | Enabled, coloured names                  |
  +-------------------------------------+------------------------------------------+

 - Display names of teammates when hovering over them with your crosshair.
 - See `example <https://i.imgur.com/mUeYd3j.jpg>`__
 - *See also:* `cg_fontScaleCN`_

--------

*cg_drawCrosshairPickups*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+------------------------------------------+
  | Default                             | 1                                        |
  +-------------------------------------+------------------------------------------+
  | Value                               | Effect                                   |
  +=====================================+==========================================+
  | 0                                   | Disabled                                 |
  +-------------------------------------+------------------------------------------+
  | 1                                   | Enabled                                  |
  +-------------------------------------+------------------------------------------+
  | 2                                   | Enabled, force highlights                |
  +-------------------------------------+------------------------------------------+

 - Give pickup items a highlight. Very subtle.
 - See `example <https://i.imgur.com/B37zyuF.jpg>`__

--------

*cg_drawFireteamOverlay*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Display Fireteam HUD window. See `example <https://i.imgur.com/VlztNc5.jpg>`__

--------

*cg_drawFPS*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 0       | 1       | 0        |
  +---------+---------+----------+

 - Display a FPS counter in the HUD below the compass. See `example <https://i.imgur.com/sygCXOw.jpg>`__

--------

*cg_drawGun*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Display equipped weapon. See `example <https://i.imgur.com/CWhbxLt.jpg>`__

--------

*cg_drawNotifyText*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Shows notifications in console.

--------

*cg_drawPing*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 0       | 1       | 0        |
  +---------+---------+----------+

 - Display the ping in the HUD below the compass. See `example <https://i.imgur.com/m7MAfpu.jpg>`__

--------

*cg_drawReinforcementTime*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Display reinforcement(spawn) timer for your team in the HUD below the compass (in light blue). See `example <https://i.imgur.com/j4aNyKk.jpg>`__
 - *See also:* `cg_drawRoundTimer`_

--------

*cg_drawRoundTimer*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Display remaining mission time in the HUD below the compass. See `example <https://i.imgur.com/ldF48BY.jpg>`__
 - *NOTE:* Also disables `cg_drawReinforcementTime`_

--------

*cg_drawSmallPopupIcons*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Use small icons for obituary messages. See `example <https://i.imgur.com/aCVVRTo.jpg>`__
 - *See also:* `cg_fontScaleSP`_

--------

*cg_drawSnapshot*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Display the snapshot counter in the HUD below the compass. See `example <https://i.imgur.com/9rRZePK.jpg>`__

--------

*cg_drawSpectatorNames*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+------------------------------------------+
  | Default                             | 2                                        |
  +-------------------------------------+------------------------------------------+
  | Value                               | Effect                                   |
  +=====================================+==========================================+
  | 0                                   | Disabled                                 |
  +-------------------------------------+------------------------------------------+
  | 1                                   | Enabled, white names                     |
  +-------------------------------------+------------------------------------------+
  | 2                                   | Enabled, coloured names                  |
  +-------------------------------------+------------------------------------------+

 - Display names of players when spectating or playing demos.

--------

*cg_drawSpeed*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 0       | 1       | 0        |
  +---------+---------+----------+

 - Displays current player speed in the HUD below the compass, in *in-game units per second*. See `example <https://i.imgur.com/7X5XnYM.jpg>`__

--------

*cg_drawSpreadScale*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+------------------------------------------+
  | Default                             | 1                                        |
  +-------------------------------------+------------------------------------------+
  | Value                               | Effect                                   |
  +=====================================+==========================================+
  | 0                                   | Disabled                                 |
  +-------------------------------------+------------------------------------------+
  | 1                                   | Enabled, for scoped weapons              |
  +-------------------------------------+------------------------------------------+
  | 2                                   | Enabled, for all weapons                 |
  +-------------------------------------+------------------------------------------+

 - Displays a coloured bar on the left of the screen showing the current weapon spread. Increases when turning around, shooting, etc. See `example <https://i.imgur.com/rYo8syD.jpg>`__

--------

*cg_drawStatus*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - The alpha (transparency) of the watermark HUD display, if the server has one.

--------

*cg_drawTime*  
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Display local time. See `example <https://i.imgur.com/dX18GjL.jpg>`__

--------

*cg_drawWeaponIconFlash*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Flashes the weapon icon on the bottom right during certain events. See `example <https://i.imgur.com/NpvFv5g.jpg>`__

--------

*cg_descriptiveText*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Displays additional descriptive text on the screen. See `example <https://i.imgur.com/R1xIDPO.jpg>`__

--------

*cg_draw2D*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Display all UI and HUD elements. See `example <https://i.imgur.com/zre7ptp.jpg>`__

--------

*cg_fireteamLatchedClass*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Draw latched class of fireteam members in the fireteam overlay. See `example <https://i.imgur.com/gyey9ae.jpg>`__

--------

*cg_fontScaleCN*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 0.25                                          |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0.00                                | No functional limit                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Font scale for entitiy/player names when aiming crosshair at them     |
  +-------------------------------------------------------------------------------------+

 - See `example <https://i.imgur.com/fRBur8Y.jpg>`__
 - *See:* `cg_drawCrosshairNames`_

--------

*cg_fontScaleCP*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 0.22                                          |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0.00                                | No functional limit                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Font scale for center prints                                          |
  +-------------------------------------------------------------------------------------+

 - See `example <https://i.imgur.com/7LrbjeX.jpg>`__
 - *See also:* `cg_centerTime`_

--------

*cg_fontScaleSP*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 0.22                                          |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0.00                                | No functional limit                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Font scale for side prints                                            |
  +-------------------------------------------------------------------------------------+

 - See `example <https://i.imgur.com/92QJUZO.jpg>`__
 - *See also:* `cg_drawSmallPopupIcons`_ and `cg_graphicObituaries`_

--------

*cg_fontScaleTP*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 0.35                                          |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0.00                                | No functional limit                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Font scale for top of the screen prints                               |
  +-------------------------------------------------------------------------------------+

--------

*cg_etVersion*
""""""""""""""""""""""""""""""""""""""""

 - Shows client mod version when connected to a server.

--------

*cg_fov*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 90                                            |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 75                                  | 120                                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Sets the Field of View                                                |
  +-------------------------------------------------------------------------------------+

--------

*cg_gibs*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Likely intended to toggle display remaining bodyparts from splatted bodies.

--------

*cg_graphicObituaries*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+------------------------------------------+
  | Default                             | 0                                        |
  +-------------------------------------+------------------------------------------+
  | Value                               | Effect                                   |
  +=====================================+==========================================+
  | 0                                   | Disabled                                 |
  +-------------------------------------+------------------------------------------+
  | 1                                   | Victim -> Weapon -> Killer               |
  +-------------------------------------+------------------------------------------+
  | 2                                   | Killer -> Weapon -> Victim               |
  +-------------------------------------+------------------------------------------+

 - Display simple graphic kill messages to safe space. See `example <https://i.imgur.com/2s36V33.jpg>`__
 - *See also:* `cg_fontScaleSP`_

--------

*cg_gunX*
""""""""""""""""""""""""""""""""""""""""

  +----------------------------------------+-----------------------------------------------+
  | Default                                | 0 (center)                                    |
  +----------------------------------------+-----------------------------------------------+
  | Range start                            | Range end                                     |
  +========================================+===============================================+
  | No functional negative value (forward) | No functional positive value (backward)       |
  +----------------------------------------+-----------------------------------------------+
  | .. centered:: Offset of equipped weapon on screen along the X-axis, in *in-game units* |
  +----------------------------------------------------------------------------------------+

 - See `example <https://i.imgur.com/nBCOM4o.jpg>`__

--------

*cg_gunY*
""""""""""""""""""""""""""""""""""""""""

  +----------------------------------------+-----------------------------------------------+
  | Default                                | 0 (center)                                    |
  +----------------------------------------+-----------------------------------------------+
  | Range start                            | Range end                                     |
  +========================================+===============================================+
  | No functional negative value (right)   | No functional positive value (left)           |
  +----------------------------------------+-----------------------------------------------+
  | .. centered:: Offset of equipped weapon on screen along the Y-axis, in *in-game units* |
  +----------------------------------------------------------------------------------------+

 - See `example <https://i.imgur.com/JtHtcg0.jpg>`__

--------

*cg_gunZ*
""""""""""""""""""""""""""""""""""""""""

  +----------------------------------------+-----------------------------------------------+
  | Default                                | 0 (center)                                    |
  +----------------------------------------+-----------------------------------------------+
  | Range start                            | Range end                                     |
  +========================================+===============================================+
  | No functional negative value (down)    | No functional positive value (up)             |
  +----------------------------------------+-----------------------------------------------+
  | .. centered:: Offset of equipped weapon on screen along the Z-axis, in *in-game units* |
  +----------------------------------------------------------------------------------------+

 - See `example <https://i.imgur.com/nn6DXdO.jpg>`__

--------

*cg_hitSounds*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-------------------------------------------+
  | Default                             | 1                                         |
  +-------------------------------------+-------------------------------------------+
  | Value                               | Effect                                    |
  +=====================================+===========================================+
  | 0                                   | None                                      |
  +-------------------------------------+-------------------------------------------+
  | 1                                   | All                                       |
  +-------------------------------------+-------------------------------------------+
  | 3                                   | Disable body hitsounds                    |
  +-------------------------------------+-------------------------------------------+
  | 5                                   | Disable headshot hitsounds                |
  +-------------------------------------+-------------------------------------------+
  | 7                                   | Disable body and headshot hitsounds       |
  +-------------------------------------+-------------------------------------------+
  | 11                                  | Disable body and team hitsounds           |
  +-------------------------------------+-------------------------------------------+
  | 13                                  | Disable headshot and team hitsounds       |
  +-------------------------------------+-------------------------------------------+
  | 25                                  | Disable team hitsounsd                    |
  +-------------------------------------+-------------------------------------------+

 - Set active hit sounds.

--------

*cg_instantTapOut*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 0       | 1       | 0        |
  +---------+---------+----------+

 - Puts you directly into the respawn queue without waiting for a revive. Only certain situations in LMS or with limited spawns available.

--------

*cg_lagometer*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 0       | 1       | 0        |
  +---------+---------+----------+

 - Displays a lag'o'meter in the HUD below the compass checking for lag spikes. See `example <https://i.imgur.com/C5ycQph.jpg>`__

--------

*cg_letterbox*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 0       | 1       | 0        |
  +---------+---------+----------+

 - Adds an overlay to the game underneath the HUD at the bottom and top of the screen simulating widescreen. See `example <https://i.imgur.com/4sNnpaN.jpg>`__

--------

*cg_locations*
""""""""""""""""""""""""""""""""""""""""

 - {FIXME} *Some values don't work and the setup is confusing. Ask ryven, he can help*

 - *Default:* "3"  | *Bit flags:* "0" = coordinates only; "1" = loc in fireteam chat; "2" = loc in team chat; "3" = loc in team and fireteam chat
 - Displays locations instead of map coordinates. Uses data from loc.dat file.

--------

*cg_logFile*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* ""| *Possible values:* strings(text)
 - Sets the name of the chat log file or if empty logging is disabled.

--------

*cg_markTime*
""""""""""""""""""""""""""""""""""""""""

  +----------------------------------------+-----------------------------------------------+
  | Default                                | 20000                                         |
  +----------------------------------------+-----------------------------------------------+
  | Range start                            | Range end                                     |
  +========================================+===============================================+
  | 0                                      | No functional limit                           |
  +----------------------------------------+-----------------------------------------------+
  | .. centered:: Duration of bullet marks on walls                                        |
  +----------------------------------------------------------------------------------------+

 - *See also:* `cg_brassTime`_ and `cg_bloodTime`_

--------

*cg_muzzleFlash*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Toggles display of muzzle flash when shooting. See `example <https://i.imgur.com/Z4oHZXu.jpg>`__

--------

*cg_noAmmoAutoSwitch*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Automatically switch to a new weapon when out of ammunition.
 - *CAREFUL:* Do not confuse with `cg_autoSwitch`_!

--------

*cg_optimizePrediction*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Enables unlagged optimized prediction.

--------

*cg_popupFadeTime*
""""""""""""""""""""""""""""""""""""""""

  +----------------------------------------+-----------------------------------------------+
  | Default                                | 2500                                          |
  +----------------------------------------+-----------------------------------------------+
  | Range start                            | Range end                                     |
  +========================================+===============================================+
  | 0                                      | No functional limit                           |
  +----------------------------------------+-----------------------------------------------+
  | .. centered:: Duration of the fading effect of popup messages                          |
  +----------------------------------------------------------------------------------------+

 - *See also:* `cg_popupStayTime`_ and `cg_popupFilter`_

--------

*cg_popupBigFilter*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-------------------------------------------+
  | Default                             | 0                                         |
  +-------------------------------------+-------------------------------------------+
  | Value                               | Effect                                    |
  +=====================================+===========================================+
  | 0                                   | Disabled                                  |
  +-------------------------------------+-------------------------------------------+
  | 1                                   | Filter skill promotions                   |
  +-------------------------------------+-------------------------------------------+
  | 2                                   | Filter rank promotions                    |
  +-------------------------------------+-------------------------------------------+
  | 3                                   | Filter skill and rank promotions          |
  +-------------------------------------+-------------------------------------------+
  | 4                                   | Filter prestige promotions                |
  +-------------------------------------+-------------------------------------------+
  | 5                                   | Filter skill and prestige promotions      |
  +-------------------------------------+-------------------------------------------+
  | 6                                   | Filter rank and prestige promotions       |
  +-------------------------------------+-------------------------------------------+
  | 7                                   | Filter skill, rank, prestige promotions   |
  +-------------------------------------+-------------------------------------------+

 - Filter promotion popups.

--------

*cg_popupFilter*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-------------------------------------------+
  | Default                             | 0                                         |
  +-------------------------------------+-------------------------------------------+
  | Value                               | Effect                                    |
  +=====================================+===========================================+
  | 0                                   | Disabled                                  |
  +-------------------------------------+-------------------------------------------+
  | 1                                   | Filter connect                            |
  +-------------------------------------+-------------------------------------------+
  | 2                                   | Filter team join                          |
  +-------------------------------------+-------------------------------------------+
  | 4                                   | Filter mission                            |
  +-------------------------------------+-------------------------------------------+
  | 8                                   | Filter pickup                             |
  +-------------------------------------+-------------------------------------------+
  | 16                                  | Filter death                              |
  +-------------------------------------+-------------------------------------------+

 - Filter message popups. Combining effects is done by combining the values together.
 - *See also:* `cg_popupStayTime`_ and `cg_popupFadeTime`_

--------

*cg_popupStayTime*
""""""""""""""""""""""""""""""""""""""""

  +----------------------------------------+-----------------------------------------------+
  | Default                                | 2000                                          |
  +----------------------------------------+-----------------------------------------------+
  | Range start                            | Range end                                     |
  +========================================+===============================================+
  | 0                                      | No functional limit                           |
  +----------------------------------------+-----------------------------------------------+
  | .. centered:: Duration for which popup messages stay active                            |
  +----------------------------------------------------------------------------------------+

 - *See also:* `cg_popupFadeTime`_ and `cg_popupFilter`_

--------

*cg_predefinedDemoKeys*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Use predefined key bindings to control actions in a demo such as fast forward. This way existing binds are ignored.

--------

*cg_printObjectiveInfo*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Prints important game messages to the console.

--------

*cg_quickChat*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-------------------------------------------+
  | Default                             | 0                                         |
  +-------------------------------------+-------------------------------------------+
  | Value                               | Effect                                    |
  +=====================================+===========================================+
  | 0                                   | Disabled                                  |
  +-------------------------------------+-------------------------------------------+
  | 1                                   | Team chat                                 |
  +-------------------------------------+-------------------------------------------+
  | 2                                   | Fireteam chat                             |
  +-------------------------------------+-------------------------------------------+

 - Specify receiver of quick radio messages. Quick radio messages are trigger when using alt weapon key bind and holding a specific weapon. Like "Fire in the hole" when holding a grenade.

--------

*cg_quickMessageAlt*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-------------------------------------------+
  | Default                             | 1                                         |
  +-------------------------------------+-------------------------------------------+
  | Value                               | Effect                                    |
  +=====================================+===========================================+
  | 0                                   | Disabled                                  |
  +-------------------------------------+-------------------------------------------+
  | 1                                   | Alphabetical                              |
  +-------------------------------------+-------------------------------------------+
  | 2                                   | Numerical                                 |
  +-------------------------------------+-------------------------------------------+

 - Toggles using either numbers or letters for the quick chat menu. See `example <https://i.imgur.com/Xejzj5x.jpg>`__

--------

*cg_scoreboard*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-------------------------------------------+
  | Default                             | 1                                         |
  +-------------------------------------+-------------------------------------------+
  | Value                               | Effect                                    |
  +=====================================+===========================================+
  | 0                                   | XP                                        |
  +-------------------------------------+-------------------------------------------+
  | 1                                   | SR                                        |
  +-------------------------------------+-------------------------------------------+

 - Used to cycle between XP and Skill Rating (SR) scoreboard. See `example <https://i.imgur.com/1IBwm4U.jpg>`__

--------

*cg_shadows*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-------------------------------------------+
  | Default                             | 1                                         |
  +-------------------------------------+-------------------------------------------+
  | Value                               | Effect                                    |
  +=====================================+===========================================+
  | 0                                   | Disabled                                  |
  +-------------------------------------+-------------------------------------------+
  | 1                                   | Blob                                      |
  +-------------------------------------+-------------------------------------------+
  | 2                                   | Stencil                                   |
  +-------------------------------------+-------------------------------------------+
  | 3                                   | Projection                                |
  +-------------------------------------+-------------------------------------------+
  | 4                                   | Polygon                                   |
  +-------------------------------------+-------------------------------------------+

 - Display player shadows underneath the player.
 - *NOTE*: Stencil, Projection and Polygon are currently disabled.
 - See `example <https://i.imgur.com/4yP4d05.jpg>`__

--------

*cg_showMiss*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 0       | 1       | 0        |
  +---------+---------+----------+

 - Print faulty predictions into the console, for debugging purposes. See `example <https://i.imgur.com/IjZ08dk.jpg>`__

--------

*cg_simpleItems*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-------------------------------------------+
  | Default                             | 0                                         |
  +-------------------------------------+-------------------------------------------+
  | Value                               | Effect                                    |
  +=====================================+===========================================+
  | 0                                   | Disabled                                  |
  +-------------------------------------+-------------------------------------------+
  | 1                                   | Enabled except objectives                 |
  +-------------------------------------+-------------------------------------------+
  | 2                                   | Enabled for all items                     |
  +-------------------------------------+-------------------------------------------+

 - Use minimalistic icons for item pick-ups. See `example <https://i.imgur.com/jbFplDS.jpg>`__

--------

*cg_skybox*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 0       | 1       | 0        |
  +---------+---------+----------+

 - Likely intended to toggle display of the skybox. Also requires skybox origin the be defined in config string.

--------

*cg_specHelp*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 0       | 1       | 0        |
  +---------+---------+----------+

 - Toggle display of spectator help, *only* in multiview.

--------

*cg_stats*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 0       | 1       | 0        |
  +---------+---------+----------+

 - Prints client frame in the console, for debugging purposes. See `example <https://i.imgur.com/za4IiP3.jpg>`__

--------

*cg_teamChatHeight*
""""""""""""""""""""""""""""""""""""""""

  +----------------------------------------+-----------------------------------------------+
  | Default                                | 8                                             |
  +----------------------------------------+-----------------------------------------------+
  | Range start                            | Range end                                     |
  +========================================+===============================================+
  | 0                                      | 8                                             |
  +----------------------------------------+-----------------------------------------------+
  | .. centered:: Amount of lines of chat messages displayed at once (maximum)             |
  +----------------------------------------------------------------------------------------+

--------

*cg_teamChatsOnly*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 0       | 1       | 0        |
  +---------+---------+----------+

 - Filers global chat messages and only displays team and fireteam chat.

--------

*cg_teamChatTime*
""""""""""""""""""""""""""""""""""""""""

  +----------------------------------------+-----------------------------------------------+
  | Default                                | 8000                                          |
  +----------------------------------------+-----------------------------------------------+
  | Range start                            | Range end                                     |
  +========================================+===============================================+
  | 0                                      | No functional limit                           |
  +----------------------------------------+-----------------------------------------------+
  | .. centered:: Duration of chat messages that are kept on display, in *milliseconds*    |
  +----------------------------------------------------------------------------------------+

--------

*cg_tracers*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-------------------------------------------+
  | Default                             | 1                                         |
  +-------------------------------------+-------------------------------------------+
  | Value                               | Effect                                    |
  +=====================================+===========================================+
  | 0                                   | None                                      |
  +-------------------------------------+-------------------------------------------+
  | 1                                   | All tracers                               |
  +-------------------------------------+-------------------------------------------+
  | 2                                   | Own tracers only                          |
  +-------------------------------------+-------------------------------------------+
  | 3                                   | Other's tracers only                      |
  +-------------------------------------+-------------------------------------------+

 - Choosing which tracers to display.

--------

*cg_useWeapsForZoom*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Weapon switch will zoom in and out while scoped, rather than switch weapons.

--------

*cg_visualEffects*  
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Draws additional visual effects _(airstrike planes, debris)_. See `example <https://i.imgur.com/I2anIBj.jpg>`__

--------

*cg_voiceChats*  
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Play voice chat sound file in-game when using quick chat _(e.g. v21 for Need a Medic!)_.
 - *See also:*  `cg_voiceText`_

--------

*cg_voiceText*  
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Show voice text lines in-game when using quick chat _(e.g. v21 for Need a Medic!)_.
 - *See also:*  `cg_voiceChats`_

--------

*cg_voiceSpriteTime*
""""""""""""""""""""""""""""""""""""""""

  +----------------------------------------+-----------------------------------------------+
  | Default                                | 6000                                          |
  +----------------------------------------+-----------------------------------------------+
  | Range start                            | Range end                                     |
  +========================================+===============================================+
  | 0                                      | No functional limit                           |
  +----------------------------------------+-----------------------------------------------+
  | .. centered:: Duration of chat icons shown above players their head, in *milliseconds* |
  +----------------------------------------------------------------------------------------+

 - See `example <https://i.imgur.com/BMKja5I.jpg>`__

--------

*cg_weapAltReloads*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 0       | 1       | 0        |
  +---------+---------+----------+

 - Provide an alternative way to reload a weapon that doesn't have weapon an alternative fire.

--------

*cg_weapaltSwitches*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Provide an alternative way to use an alt weapon by pressing the respective weaponbank bind

--------

*cg_weaponCycleDelay*
""""""""""""""""""""""""""""""""""""""""

  +----------------------------------------+-----------------------------------------------+
  | Default                                | 150                                           |
  +----------------------------------------+-----------------------------------------------+
  | Range start                            | Range end                                     |
  +========================================+===============================================+
  | 0                                      | No functional limit                           |
  +----------------------------------------+-----------------------------------------------+
  | .. centered:: Duration for which a pause is enforced so keeping the weapon switch key  |
  |               activated won't trigger too fast, in *milliseconds*                      |
  +----------------------------------------------------------------------------------------+

--------

*cg_zoomDefaultSniper*
""""""""""""""""""""""""""""""""""""""""

  +----------------------------------------+-----------------------------------------------+
  | Default                                | 20                                            |
  +----------------------------------------+-----------------------------------------------+
  | Range start                            | Range end                                     |
  +========================================+===============================================+
  | 4                                      | 32                                            |
  +----------------------------------------+-----------------------------------------------+
  | .. centered:: Set the default zoom level for scopes                                    |
  +----------------------------------------------------------------------------------------+

--------

*cg_zoomStepSniper*
""""""""""""""""""""""""""""""""""""""""

  +----------------------------------------+-----------------------------------------------+
  | Default                                | 2                                             |
  +----------------------------------------+-----------------------------------------------+
  | Range start                            | Range end                                     |
  +========================================+===============================================+
  | 0                                      | 28                                            |
  +----------------------------------------+-----------------------------------------------+
  | .. centered:: Set the default zoom level for scopes                                    |
  +----------------------------------------------------------------------------------------+

 - Specifies the amount of levels one key activation zooms in or out.
 - This CVAR applies to binoculars, snipers and FG42.
 - See `cg_zoomDefaultSniper`_ for the step range.

--------

Developer cvars
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A cheat protected cvar is usually used by developers to help during development.

*cg_animSpeed*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 1       | 1       | 0        |
  +---------+---------+----------+

 - Display of player animations
 - *See also:* `cg_noPlayerAnims`_

--------

*cg_debugAnim*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-------------------------------------------+
  | Default                             | 1                                         |
  +-------------------------------------+-------------------------------------------+
  | Value                               | Effect                                    |
  +=====================================+===========================================+
  | 0                                   | Disabled                                  |
  +-------------------------------------+-------------------------------------------+
  | 1                                   | Player animations                         |
  +-------------------------------------+-------------------------------------------+
  | 2                                   | Weapon animations                         |
  +-------------------------------------+-------------------------------------------+
  | 3                                   | Old and current weapon animations         |
  +-------------------------------------+-------------------------------------------+
  | > 3                                 | Print debug when time > lf->frameTime     |
  +-------------------------------------+-------------------------------------------+

 - Used to debug player model and weapon animations by printing info. See `example <https://i.imgur.com/0qGZ2wF.jpg>`__

--------

*cg_debugBullets*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 0       | 1       | 0        |
  +---------+---------+----------+

 - Used to debug bullets. See `cg_railTrailTime`_

--------

*cg_debugEvents*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 0       | 1       | 0        |
  +---------+---------+----------+

 - Used to debug entity events. When enabled, prints debug information in the console. See `example <https://i.imgur.com/QwBp8MF.jpg>`__

--------

*cg_debugPlayerHitboxes*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-------------------------------------------+
  | Default                             | 1                                         |
  +-------------------------------------+-------------------------------------------+
  | Value                               | Effect                                    |
  +=====================================+===========================================+
  | 0                                   | Disabled                                  |
  +-------------------------------------+-------------------------------------------+
  | 1                                   | Hitbox                                    |
  +-------------------------------------+-------------------------------------------+
  | 2                                   | Head axis                                 |
  +-------------------------------------+-------------------------------------------+
  | 3                                   | Hitbox and head axis                      |
  +-------------------------------------+-------------------------------------------+
  | 4                                   | Position marker                           |
  +-------------------------------------+-------------------------------------------+
  | 5                                   | Hitbox and position marker                |
  +-------------------------------------+-------------------------------------------+
  | 6                                   | Head axis and position marker             |
  +-------------------------------------+-------------------------------------------+
  | 7                                   | Hitbox, head axis and position marker     |
  +-------------------------------------+-------------------------------------------+

 - Used to debug player hitboxes. See `example <https://i.imgur.com/WkDk0qn.jpg>`__

--------

*cg_debugPosition*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 0       | 1       | 0        |
  +---------+---------+----------+

 - Used to debug player entity yaw angle. When enabled, prints debug information in the console. See `example <https://i.imgur.com/b4SOkv1.jpg>`__

--------

*cg_debugSkills*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 0       | 1       | 0        |
  +---------+---------+----------+

 - Prints debug information to console when gaining a skill level and/or xp. Exact circumstances are unknown.

--------

*cg_errorDecay*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 100                                           |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0                                   | 500                                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Decay prediction errors over several frames instead of                |
  |               correcting in one jerk, in *frames*                                   |
  +-------------------------------------------------------------------------------------+

--------

*cg_gun_frame*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 0                                             |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0                                   | Maximum frame of current gun animation        |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Freeze weapon in the specified _(CVAR value)_ frame                   |
  +-------------------------------------------------------------------------------------+

--------

*cg_noPlayerAnims*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 0       | 1       | 0        |
  +---------+---------+----------+

 - Toggles display of player animations. If enabled, animation is fixed in a single frame.
 - *See also:* `cg_animSpeed`_

--------

*cg_noPredict*
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 0       | 1       | 0        |
  +---------+---------+----------+

 - Toggles prediction of player actions _(e.g. movement)_.

--------

cg_railTrailTime
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 750                                           |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0                                   | No functional limit                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Specifies the time the trail a bullet takes is visualized             |
  |               , in *milliseconds*                                                   |
  +-------------------------------------------------------------------------------------+

 - See also `cg_debugBullets`_ and `cg_debugPlayerHitboxes`_

--------

*cg_swingSpeed*  
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 0.1                                           |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0                                   | No functional limit                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Speed at which the thirdperson player model turns around              |
  |               when looking around                                                   |
  +-------------------------------------------------------------------------------------+

--------

*cg_thirdPerson*  
""""""""""""""""""""""""""""""""""""""""

  +---------+---------+----------+
  | Default | Enabled | Disabled |
  +=========+=========+==========+
  | 0       | 1       | 0        |
  +---------+---------+----------+

 - Enables a thirdperson perspective. See `example <https://i.imgur.com/rd96Eue.jpg>`__

--------

*cg_thirdPersonAngle*  
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 0                                             |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0                                   | 360                                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Specifies the angle of the thirdperson perspective, angle in degrees  |
  +-------------------------------------------------------------------------------------+

 - See `example <https://i.imgur.com/gKOe7wl.jpg>`__

--------

*cg_thirdPersonRange*  
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 80                                            |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0                                   | No functional limit                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Specifies the distance from camera to player origin                   |
  |               , in *in-game units*                                                  |
  +-------------------------------------------------------------------------------------+

 - See `example <https://i.imgur.com/RjlD4xn.jpg>`__

--------

*cg_tracerChance*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 0.4                                           |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0                                   | 1                                             |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Probability that a shot creates a bullet tracer, % in decimal         |
  +-------------------------------------------------------------------------------------+

--------

*cg_tracerLength*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 160                                           |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0                                   | No functional limit                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Length of bullet tracers, in *in-game units*                          |
  +-------------------------------------------------------------------------------------+

--------

*cg_tracerSpeed*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 4500                                          |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0                                   | No functional limit                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Speed of bullet tracers. Setting it to 0 creates a static tracer      |
  +-------------------------------------------------------------------------------------+

--------

*cg_tracerWidth*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 0                                             |
  +-------------------------------------+-----------------------------------------------+
  | Range start                         | Range end                                     |
  +=====================================+===============================================+
  | 0                                   | No functional limit                           |
  +-------------------------------------+-----------------------------------------------+
  | .. centered:: Width of bullet tracers                                               |
  +-------------------------------------------------------------------------------------+

--------

*cg_uinfo*
""""""""""""""""""""""""""""""""""""""""

  +-------------------------------------+-----------------------------------------------+
  | Default                             | 0                                             |
  +=====================================+===============================================+
  | .. centered:: Consists of values from `cg_autoAction`_, `cg_autoactivate`_          |
  |               cg_predictItems, `cg_activateLean`_, `cl_timenudge`_ and              |
  |               `cl_maxpackets`_                                                      |
  +-------------------------------------------------------------------------------------+

--------

*CL_* (Client Engine)
----------------------------------------
.. contents:: `CVAR Types`
   :depth: 1
   :local:

Player cvars
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*cl_allowDownload*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled; "2" = enabled, but suppressed sound
 - Download missing files when available.
 - *See also:* [[List_of_Cvars_(new)#cl_wwwDownload|cl_wwwDownload]]

--------

*cl_angleSpeedKey*
""""""""""""""""""""""""""""""""""""""""

{TODO} *CVAR unused in ET and ET: Legacy. Safe to remove?*

 - *Default:* "1.5"| *Possible values:*
 - CVAR is unused.
 - Likely intended to adjust the speed for turning around. For example for controller / keyboard button

--------

*cl_aviDemo*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Couldn't test in-game. Check if it works*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Likely saves the specified amount of jpeg screenshots per second.

--------

*cl_aviDemoType*  
""""""""""""""""""""""""""""""""""""""""

{TODO} *There are way too many avi demo related CVARs. Are all of them necessary?*

 - *Default:* "0"| *Possible values:*
 - Description needed.

--------

*cl_aviMotionJpeg*
""""""""""""""""""""""""""""""""""""""""

{TODO} *There are way too many avi demo related CVARs. Are all of them necessary?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Description needed.

--------

*cl_cacheGathering*
""""""""""""""""""""""""""""""""""""""""

{TODO} *No official description found! Please check*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Enables some sort of data caching. Maps seem to load faster when loaded again. No info on what exactly gets cached found.

--------

*cl_conXOffset*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What does this CVAR do?*

 - *Default:* "0" = disabled| *Possible values:*
 - No description available.

--------

*cl_consoleKeys*
""""""""""""""""""""""""""""""""""""""""

{TODO} *can this be renamed to con_consoleKeys, because shouldn't it be rather in the [[List_of_Cvars_(new)#CON_-Console|console related section]]?*

 - *Default:* "~ ` 0x7e 0x60"| *Possible values:* keys
 - Bind opening the console to the specified key. e.g. cl_consoleKeys ~

--------

*cl_debugMove*
""""""""""""""""""""""""""""""""""""""""


 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Display a bar on the bottom of the screen containing bar charts representing mouse movement.

.. image:: https://i.imgur.com/0nB4zb4.jpg

--------

*cl_doubleTapDelay*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What is this actually used for? Are there double taps in ET?*

 - *Default:* "350" | *Possible range:* "0" = disabled; < ?
 - Delay between registering key presses for double tapping binds, in *milliseconds*.

--------

*cl_forceAviDemo*
""""""""""""""""""""""""""""""""""""""""

{TODO} *CVAR seems to be unused?*

 - *Default:* "0" = disabled | *Possible values:* "0" = disabled; "1" = enabled
 - Description needed.

--------

*cl_freeLook*
""""""""""""""""""""""""""""""""""""""""

{TODO} *CVAR seems pointless*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Enables 'freelook'. When "disabled" only left/right camera movement is possible, up/down is deactivated.

--------

*cl_freezeDemo*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Lock or freeze a demo in its current frame. Useful for per frame advances.
 - *NOTE:* This freezes both time *and* movement. Spectator camera can't be moved around. "[Reference]":https://github.com/etlegacy/etlegacy/blob/88bc7e08027aab9c84325db6113788e2c2128d97/docs/demos/README-serverside-demos_ETL.md#changelog-newest-to-the-bottom

--------

*cl_lang*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "en" = English| *Possible values:* en = English; fr = French; de = German; it = Italian; es = Spanish; pl = Polish;
 -  - nl = Dutch; cs = Czech; se = Swedish; fi = Finnish; da = Danish; pt = Portugese; no = Norwegian

ET: Legacy comes with translations created by the community. In case you would like to contribute, please refer to "Transifex":https://www.transifex.com/etlegacy/etlegacy/

--------

*cl_langDebug*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Is this necessary? Isn't this the point of Transifex?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Prints a list of missing translations for the selected language to console and also creates a text file with missing translations.

--------

*cl_maxPackets*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What unit is this in? As in, what does the 125 represent?*

 - *Default:* "125"| *Possible range:* "15" < "125"
 - Cap for upstream data packet transmissions.

--------

*cl_maxPing*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "800"| *Possible range:* "100" < "999"
 - Specify the max allowed ping to a server. Servers exceeding this ping will not be displayed in the server browser.

--------

*cl_mouseAccel*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Intended to toggle mouse acceleration.

--------

*cl_noPrint*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Enable printing of information in the console.

--------

*cl_packetDUP*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Description copied from antman. Correct?*

 - *Default:* "1"| *Possible range:* "0" < "5"
 - Number of duplicates for every data packet sent upstream.

--------

*cl_pitchSpeed*
""""""""""""""""""""""""""""""""""""""""

{TODO} *+up and +down have been removed so this CVAR is pointless, no?*

 - *Default:* "140" | *Possible values:*
 - Specify the speed of +up and +down keys.

--------

*cl_renderer*  
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "opengl1"| *Possible values:* "opengl1"; "opengl2"
 - Select your renderer of choice.
 - *NOTE:* "opengl2" remains in experimental state for now.

--------

*cl_run*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Is this really necessary? Maybe remove CVAR, have enabled default and replace +speed with +walk?*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Toggle between walk and run. If enabled, +forward is  running speed and if disabled it's walking speed. To toggle to the other mode use the combination of +speed (capslock) + +forward.

--------

*cl_serverStatusResendTime*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What does that CVAR do?*

 - *Default:* "750"| *Possible values:*
 - Time in ms between resending serverstatus requests.

--------

*cl_showMouseRate*
""""""""""""""""""""""""""""""""""""""""


 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Prints the speed of mouse movement to the console.

.. image:: https://i.imgur.com/zjoMi4L.jpg

--------

*cl_showNet*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Description copied from antman, correct?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Prints the latency of each packet to the console.

.. image:: https://i.imgur.com/VTwFGF8.jpg

--------

*cl_showNumEnts*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Prints the number of entities per packet to the console.

.. image:: https://i.imgur.com/roAjvYj.jpg

--------

*cl_showSend*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Prints each sent packet to the console.

.. image:: https://i.imgur.com/KwUUt6c.jpg

--------

*cl_showServerCommands*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What does this CVAR do?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Only works if in debug mode e.g. developer = 1

--------

*cl_showTimeDelta*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Check description*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Prints the time delta of each packet to the console.

.. image:: https://i.imgur.com/PmLTIpx.jpg

--------

*cl_timedemo*
""""""""""""""""""""""""""""""""""""""""

{TODO} *unkown CVAR ingame. What is it used for?*

 - *Default:* "0"| *Possible values:*
 - Unknown CVAR, but mentioned in code.

--------

*cl_timeNudge*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Description copied from antman, check*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Supposed to be for adjusting prediction for your ping. Don't bother, use antilag.

--------

*cl_timeout*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Description copied from antman, check*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Seems to be duration of receiving nothing from server for client to decide it must be disconnected.

--------

*cl_waveFileRecord*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Can this be merged with cg_autoAction?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Start recording a .wav audio file upon loading a demo.

--------

*cl_wwwDownload*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Merge with cl_allowDownload*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Enables http/ftp downloads.
 - *See also:* [[List_of_Cvars_(new)#cl_allowDownload|cl_allowDownload]]

--------

*cl_yawSpeed*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "140"| *Possible range:* "0" = disabled; < ?
 - Specify the speed of +left and +right keys.

--------

Cheat protected cvars
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*cl_packetDelay*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What does that CVAR do?*

 - *Default:* "0" = disabled| *Possible values:*
 - Description needed.

--------

*cl_packetLoss*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What does that CVAR do?*

 - *Default:* "0" = disabled| *Possible values:*
 - Description needed.

--------

Internal cvars
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*cl_activeAction* 
""""""""""""""""""""""""""""""""""""""""

{TODO} *unkown CVAR ingame. What is it used for?*

 - *Default:* " " | *Possible values:*
 - Description needed. 

--------

*cl_autoRecord* 
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - CVAR looks internally used. Also [[List_of_Cvars_(new)/#cg_autoAction|cg_autoAction]] is a thing.

--------

*cl_bypassMouseInput*
""""""""""""""""""""""""""""""""""""""""

{TODO} *The user should not be able to set this! This should be hard-coded behaviour anyway. Can CVAR be removed?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Used to bypass mouse input in-game while menus are active. 

--------

*cl_defaultProfile*
""""""""""""""""""""""""""""""""""""""""

{TODO} *can this be combined with [[List_of_Cvars_(new)/#cl_profile|cl_profile]]?*

 - *Default:* " " | *Possible values:*  
 - Read-only CVAR setting the default user profile. Go to the PROFILE section in the main menu to set a default profile.
 - *See also:* [[List_of_Cvars_(new)/#cl_profile|cl_profile]] 

--------

*cl_demoFileName*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* " "| *Possible values:* strings
 - Internal read-only CVAR used for demo recording. 

--------

*cl_demoOffset*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "0"| *Possible values:* 
 - Internal read-only CVAR used for demo recording. 

--------

*cl_demoRecording*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Internal read-only CVAR used for demo recording. 

--------

*cl_downloadName*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Why is that a thing?*

 - *Default:* " " | *Possible values:* strings 
 - Stores name of file you're downloading when connecting to a server. 

.. image:: https://i.imgur.com/OC0foUC.jpg 

--------

*cl_guid*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* " " | *Possible values:* 
 - A GUID, sometimes also referred to as "etkey", is an automatically generated alpha-numerical sequence used to uniquely identify players.
 - It is stored in the etkey file [[Path_and_file_structure|(path and file structure)]] and in-game in this read-only CVAR. 

--------

*cl_noDelta*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - When enabled sets last snapshot / frame to NULL so there is nothing to delta from.
 - Should only used by developers who know what they are doing.

--------

*cl_paused*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Can this be combined with [[List_of_Cvars_(new)/#cg_paused|cg_paused]]?*

 - *Default:* "0" = unpaused| *Possible values:* "0" = unpaused; "1" = paused
 - Internal read-only CVAR to toggle functionality of paused games. 

--------

*cl_profile*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Can this be combined with [[List_of_Cvars_(new)/#cl_defaultProfile|cl_defaultProfile]]? Also, can this be made non-read-only?*

 - *Default:* " " | *Possible values:* 
 - Read-only CVAR specifying the currently selected profile. To change the profile, you need to go to the "PROFILE" section in the main menu.
 - *See also:* [[List_of_Cvars_(new)/#cl_defaultProfile|cl_defaultProfile]] 

--------

*cl_running*
""""""""""""""""""""""""""""""""""""""""

{TODO} *CVAR seems to be unused. Safe to remove?*

 - *Default:* "0" = not running| *Possible values:* "0" = not running; "1" = running
 - Can be used to check the status of the client game. _"Is it running or not?"_. 

--------

*cl_waveFileName*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* " "| *Possible values:* strings
 - Internal read-only CVAR used for wave demo recording. 

--------

*cl_waveOffset*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "0"| *Possible values:* 
 - Internal read-only CVAR used for wave demo recording. 

--------

*cl_waveRecording*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "0"| *Possible values:* 
 - Internal read-only CVAR used for wave demo recording. 

--------

*COM_* (Common)
----------------------------------------

.. contents:: `CVAR Types`
   :depth: 1
   :local:

Player cvars
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*com_altivec*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What is this used for?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 -  Description needed. 

--------

*com_ansiColor*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 -  Enables color output in the system console. 

--------

*com_buildScript*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 -  Force loading of all possible data and error on failures for automated data building scripts. 

--------

*com_hunkMegs*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "128"| *Possible values:*
 -  Amount of memory (RAM) assigned to the hunk, *in MB*.
 - *See also:* [[List_of_Cvars_(new)/#com_soundMegs|com_soundMegs]] and [[List_of_Cvars_(new)/#com_zoneMegs|com_zoneMegs]]

--------

*com_logfile* / *logfile*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What is this used for? "Unknown CVAR" ingame*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = buffer log; "2" = flush after each print
 -  Non-user CVAR

--------

*com_maxFPS*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "85"| *Possible range:* "20" < "333"
 -  Specifies the maximum frames per second the game can reach for a stable render rate.

--------

*com_soundMegs*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "160"| *Possible values:*
 -  Amount of memory (RAM) allocated for loading sound files, *in MB*.
 - *See also:* [[List_of_Cvars_(new)/#com_hunkMegs|com_hunkMegs]] and [[List_of_Cvars_(new)/#com_zoneMegs|com_zoneMegs]]

--------

*com_zoneMegs*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* " "| *Possible values:*
 -  Amount of memory (RAM) allocated for the random block zone, *in MB*.
 - *NOTE:* com_zoneMegs can only be set on the command line, and not in etconfig.cfg or Com_StartupVariable. "[Reference]":https://github.com/etlegacy/etlegacy/blob/f0bf85d7e1b1675b9e69ce6b47d3c12604406560/src/qcommon/common.c#L1674
 - *See also:* [[List_of_Cvars_(new)/#com_hunkMegs|com_hunkMegs]] and [[List_of_Cvars_(new)/#com_soundMegs|com_soundMegs]]

--------

Internal / developer cvars
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*com_crashed*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Is this supposed to be accessible by the user? It sounds like this should be an automated internal CVAR.*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 -  Enable in case of a crash to prevent CVAR_UNSAFE variables from being set from a cfg.
 - *See also:* [[List_of_Cvars_(new)/#com_ignoreCrash|com_ignoreCrash]]

--------

*com_downloadURL*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* " " = Windows| *Possible values:* address string
 -  Non-user CVAR specifying the address which is used for the download command.

--------

*com_hunkUsed*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Should this be accessible to the user? This sounds like it should be read-only*
{TODO} *Which unit is this?*

 - *Default:* "0"| *Possible values:*
 -  Size of the currently used hunk, *in [?]*.

--------

*com_errorDiagnoseIP*
""""""""""""""""""""""""""""""""""""""""

{TODO} unknown CVAR ingame. Check.

 - *Default:* " "| *Possible values:* server address
 -  Catch a connection process that would turn bad.

--------

*com_ignoreCrash*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Combine with com_crashed*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 -  Let ET override CVAR_UNSAFE in case of crash. Use only if you know what you are doing!
 - *See also:* [[List_of_Cvars_(new)/#com_crashed|com_crashed]]

--------

*com_introPlayed*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Should this be accessible to the user? This sounds like it should be read-only*
{TODO} *Also, since we don't have an intro, can this be removed?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 -  CVAR seems to have no effect in ETL and ET. Likely intended to fetch the status of the game at startup?

--------

*com_journal* / *journal*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What is this used for? "Unknown CVAR" ingame*

 - *Default:* "0" | *Possible values:*
 -  Non-user CVAR to open a journal?

--------

*com_masterServer*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "master.etlegacy.com:27950" = maximized| *Possible values:* domain:port
 -  Allow to override the default master server

--------

*com_minimized*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Shouldn't this be read-only?*

 - *Default:* "0" = maximized| *Possible values:* "0" = maximized; "1" = minimized
 -  Used  to catch the state of the game. Is the window minimized or not?

--------

*com_missingFiles*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* " "| *Possible values:*
 -  Non-user CVAR storing information regarding missing files. Used for displaying error messages to the user.

--------

*com_motd*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What exactly is this used to? "0" also displays the MOTD*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Display the official ET: Legacy "message of the day".

--------

*com_motdServer*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "motd.etlegacy.com:27951" = maximized| *Possible values:* domain:port
 -  Allow to override the default motd server

--------

*com_motdString*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Description correct?*

 - *Default:* " "| *Possible values:* string
 - The official ET: Legacy "message of the day" string used to communicate news to players.

--------

*com_pid*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 -  Read-only CVAR storing process id.

--------

*com_pidFile*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:* "profiles/name/profile.pid" = client
 -  - "etlegacy_server.pid" = server

 Full path to the pid file (contains process id).

--------

*net_dropSim*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What's the point of this CVAR?*

 - *Default:* "0.0" = disabled| *Possible range:* "0.0" < "1.0"
 -  Simulated packet drops.

--------

*com_fixedtime*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What is this used for? "Unknown CVAR" ingame*

 - *Default:* "0" | *Possible values:*
 -  Non-user CVAR to fix time?

--------

*com_recommended*
""""""""""""""""""""""""""""""""""""""""

{TODO} *This CVAR is used once during the entire installation lifecycle. Is it necessary?*

 - *Default:* " "| *Possible values:*
 -  Non-user CVAR used during the profile creation. Use recommended settings or not?

--------

*com_recommendedSet*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Combine with com_recommended.*

 - *Default:* " "| *Possible values:*
 -  When enabled, the game uses default (recommended) values during profile creation.

--------

*com_showTrace*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What information is printed here?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 -  Prints trace information to the console. Used for debugging.

.. image:: https://i.imgur.com/qJ3hTM8.jpg

--------

*com_speeds*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What information is printed here?*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 -  Prints speed information per frame to the console. Used for debugging.

.. image:: https://i.imgur.com/lXq6Lv3.jpg

--------

*com_sv_running* / *sv_running*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What is this used for? "Unknown CVAR" ingame*

 - *Default:* "0"| *Possible values:*
 -  Non-user CVAR

--------

*com_timeDemo* / *timedemo*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What is this used for? "Unknown CVAR" ingame*

 - *Default:* "0"| *Possible values:*
 -  Non-user CVAR

--------

*com_timeScale* / *timescale*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What is this used for? "Unknown CVAR" ingame*

 - *Default:* "1.0"| *Possible values:*
 -  Non-user CVAR used to change speed of the game?
 - From code: if com_timescale below 1.0, then we pass one frame on "1.0/com_timescale" (eg: com_timescale = 0.5, then 1.0/0.5 = 2, so we pass one frame on two)

--------

*com_unfocused*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Shouldn't this be read-only?!*

 - *Default:* "0" = focused| *Possible values:* "0" = focused; "1" = unfocused
 -  Used mainly in windowed mode to catch the state of the game. Is the window active or not?

--------

*com_updateAvailable*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "0" = no| *Possible values:* "0" = no; "1" = yes
 - If there is a newer version than the current one this CVAR is enabled.

--------

*com_updateFiles*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* " " | *Possible values:*
 - Stores information regarding remainging files needed for the update.

--------

*com_updateMessage*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Shouldn't this be read-only? Or rather, shouldn't this be hardcoded without a CVAR?*

 - *Default:* "New version available. Do you want to update now?" | *Possible values:*
 - Stores the string used for the pop-up when there is a new update.

--------

*com_updateServer*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "update.etlegacy.com:27951" = maximized| *Possible values:* domain:port
 -  Allow to override the default update server

--------

*com_version* / *version*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What is this used for? "Unknown CVAR" ingame*

 - *Default:* " "| *Possible values:*
 -  Non-user CVAR.

--------

*com_viewLog* / *viewlog*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What is this used for? "Unknown CVAR" ingame*

 - *Default:* "0" = hidden| *Possible values:* "0" = hidden, "1" = visible, "2" = minimized
 -  Non-user CVAR used to view the log?

--------

*com_watchdog*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "60"| *Possible values:*
 -  Non-user CVAR used to check whether the game died with an ERR_DROP or any situation leading to server running with no map.
 - *See also:* [[List_of_Cvars_(new)/#com_watchdog_cmd|com_watchdog_cmd]]

--------

*com_watchdog_cmd*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* " "| *Possible values:* e.g. "exec mapvotecycle.cfg"
 -  Non-user CVAR specifying the actions in an event where com_watchdog triggers.
 - *See also:* [[List_of_Cvars_(new)/#com_watchdog|com_watchdog]]

--------

Server cvars
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*com_dedicated* / *dedicated*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What is this used for? "Unknown CVAR" ingame*

 - *Default:* "0" = hidden| *Possible values:* "0" = hidden; "1" = LAN; "2" = Internet
 -  Non-user CVAR used to set mode of server? 

--------

*CON_* (Console)
----------------------------------------

Player cvars
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*con_autoClear*
""""""""""""""""""""""""""""""""""""""""

{TODO} *CVAR looks unused.*

 - *Default:* "1" | *Possible values:* 
 -  Description needed. 

--------

Developer cvars
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*com_developer* / *developer*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What is this used for? "Unknown CVAR" ingame*

 - *Default:* | *Possible values:*
 -  Non-user CVAR to toggle some sort of developer mode?

--------

*con_drawNotify*
""""""""""""""""""""""""""""""""""""""""

{TODO} *CVAR to be reworked! "Ticket":https://dev.etlegacy.com/issues/1258*

 - *Default:* "0" = disabled | *Possible values:* "0" = disabled; "1" = enabled 
 -  Prints the last few lines of console output transparently on the top of the screen. 
 - *See also:* `con_notifyTime`_, `con_numNotifies`_

--------

*com_dropSim* / *net_dropsim*
""""""""""""""""""""""""""""""""""""""""

{TODO} *What's the point of this CVAR?*

 - *Default:* "0.0" = disabled| *Possible range:* "0.0" < "1.0"
 -  Simulated packet drops.

--------

*con_notifyTime*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "7" | *Possible range:* "0" = disabled; < ?
 -  Duration for which the notification prints on the top of the screen are displayed, in *seconds*.
 - *See also:* `con_drawNotify`_, `con_numNotifies`_

--------

*con_numNotifies*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "7" | *Possible range:* "0" = disabled; < ?
 -  Change number of drawable notifies. Allows to draw up to 10 lines.
 - *See also:* `con_drawNotify`_, `con_numNotifies`_

--------

*DEMO_* (Demo)
----------------------------------------

*demo_autoTimeScale*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{TODO} *Check description and send kemon a screenshot of it in action please.*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Automatically adjust demo playback speed depending on currently active weapon? 

--------

*demo_autoTimeScaleWeapons*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{TODO} *Check description and send kemon a screenshot of it in action please.*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Define timescales for different weapons? 

--------

*demo_avifpsF1*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 - *Default:* "0" | *Possible values:* 
 -  Presets for the rate of avi demos, in *screenshots per second*. 

--------

*demo_avifpsF2*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 - *Default:* "10" | *Possible values:* 
 -  Presets for the rate of avi demos, in *screenshots per second*. 

--------

*demo_avifpsF3*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 - *Default:* "15" | *Possible values:* 
 -  Presets for the rate of avi demos, in *screenshots per second*. 

--------

*demo_avifpsF4*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 - *Default:* "20" | *Possible values:* 
 -  Presets for the rate of avi demos, in *screenshots per second*. 

--------

*demo_avifpsF5*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 - *Default:* "24" | *Possible values:* 
 -  Presets for the rate of avi demos, in *screenshots per second*. 

--------

*demo_drawTimeScale*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{TODO} *Only works if set before loading the demo. Can't be changed during runtime of demo. Timescale pop-up only remains on-screen for a few seconds and then can't be brought back.*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Prints the current timescale (demo playback speed) on the screen. 

.. image:: https://i.imgur.com/RmA0Zl7.jpg 

--------

*demo_followDistance*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{TODO} *Check description and send kemon a screenshot of it in action please.*

 - *Default:* "50 0 20"| *Possible values:* integers for X Y Z
 - Specifies the distance from the player origin for all axes. 

--------

*demo_freeCamSpeed*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{TODO} *Check description and send kemon a screenshot of it in action please.*

 - *Default:* "800"| *Possible range:* "0" = static [?]; < ?
 - Define the speed of the free camera, *in in-game units per second* 

--------

*demo_infoWindow*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{TODO} *Only works if set before loading the demo. Can be activated if it was 0 before loading demo, but can't be disabled/reactivated again.*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Prints an infobox on the screen for useful keybinds. 

.. image:: https://i.imgur.com/eXvhfpu.jpg 

--------

*demo_lookAt*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{TODO} *Check description and send kemon a screenshot of it in action please.*

 - *Default:* "-1"| *Possible values:*  
 - Specify the number of the entity the camera should focus on. 

--------

*demo_noPitch*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{TODO} *Check description and send kemon a screenshot of it in action please.*

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Description needed. 

--------

*demo_pvsHint*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{TODO} *Check description and send kemon a screenshot of it in action please.*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Description needed. 

--------

*demo_teamOnlyMissileCam*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{TODO} *Check description and send kemon a screenshot of it in action please.*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Description needed. 

--------

*demo_weaponCam*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{TODO} *Send kemon a screenshot of it in action please.*

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Triggers weapon cam view. 

--------

*demo_yawPitchRollSpeed*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{TODO} *Check description and send kemon a screenshot of it in action please.*

 - *Default:* "140 140 140"| *Possible values:* integers for yawturn-; pitchturn-; roll-speed
 - Specifies the yawturn-, pitchturn- and roll-speed values for demo playback. 

--------

*FS_* (File System)
----------------------------------------

|ETL logo| NOTE: File system CVARs need to be set before game start and can't be changed during runtime 

*fs_baseGame*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{TODO} *Description needed*

 - *Default:* " "| *Possible values:* 
 - Write-protected CVAR displaying exactly what?

--------

*fs_basePath*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{TODO} *Displays only a single dot and not a path to the installation folder, why is that?*

 - *Default:* "."| *Possible values:* 
 - Write-protected CVAR specifying the path to the ET installation folder.
 - *See also:* [[Path_and_file_structure#Homepath-fs_basepath|Path and File Structure]] 

--------

*fs_debug*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - Run the game in debug mode. Prints additional information regarding read files into the console. 

.. image:: https://i.imgur.com/ShVviJn.jpg 

--------

*fs_game*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 - *Default:* "legacy"| *Possible values:* mod names _(aka folder names in fs_homepath)_
 - Run the game with this default mod. 

--------

*fs_homePath*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 - *Default:* "OS dependent":https://dev.etlegacy.com/projects/etlegacy/wiki/Path_and_file_structure#Homepath-fs_homepath| *Possible values:* paths to directories
 - Contains all downloaded pk3, log, config and extracted binary files.
 - *See also:* [[Path_and_file_structure#Homepath-fs_homepath|Path and File Structure]] 

--------

*fs_openedList*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{TODO} *Please add explanation of difference to fs_referencedList to the description.*

 - *Default:* " "| *Possible values:* 
 - Prints a list of opened PK3 names and their path to the console. 

--------

*fs_referencedList*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{TODO} *Please add explanation of difference to fs_openedList to the description.*

 - *Default:* " "| *Possible values:* 
 - Prints a list of referenced PK3 names to the console. 

--------

*fs_gameDirVar*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{TODO} *CVAR looks unused. Safe to remove?*

 - *Default:* " "| *Possible values:* 
 - Description needed. 

--------

*G_* (Game)
----------------------------------------

*g_alliedMapXP*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{TODO} *Seems to never change its value. What does it do exactly?*

 - *Default:* "0"| *Possible values:* 
 - Likely intended to store the accumulated XP of the entire Allied team of the current map/campaign?
 - *See also:* [[List_of_Cvars_(new)/#g_axisMapXP|g_axisMapXP]] 

--------

*g_alliedMaxLives*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 - *Default:* "0"| *Possible values:* 
 - Specifies the amount of lives each Allied player has individually. These lives are not shared across the team. The HUD counter seen in the screenshot displays the amount of respawns you have left.
 - *See also:* [[List_of_Cvars_(new)/#g_axisMaxLives|g_axisMaxLives]] 

.. image:: https://i.imgur.com/qEaZYch.jpg 

--------

*g_alliedWins*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{TODO} *Is it necessary that this works like bitflags? Feels a bit counter-intuitive.*

 - *Default:* "0"| *Possible values:* 
 - Stores the amount of wins of the Allied team in the currently active campaign.
 - *NOTE:* This works like bitflags (1, 2, 4, 8, etc.) So, if the Allied team has three wins the CVAR has a value of 7 (1 + 2 + 4).
 - *See also:* [[List_of_Cvars_(new)/#g_axisWins|g_axisWins]] 

--------

*g_altStopwatchMode*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 - *Default:* "0" = A-B-B-A| *Possible values:* "0" = A-B-B-A; "1" = A-B-A-B
 - Switches between two different Stopwatch types of attacker team turns. 

--------

*g_antiLag*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - https://i.imgur.com/6b2wv1f.png!:https://i.imgur.com/6b2wv1f.png Enables modem-friendly server support. 
 - *See also:* 
 - [[List_of_Cvars_(new)/#g_balancedTeams|g_balancedTeams]] 

--------

*g_autoFireteams*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 - *Default:* "1" = enabled| *Possible values:* "0" = disabled; "1" = enabled
 - Toggles providing players with a popup asking to join a Fireteam when joining a team. 

--------

*g_axisMapXP*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{TODO} *Seems to never change its value. What does it do exactly?*

 - *Default:* "0"| *Possible values:* 
 - Likely intended to store the accumulated XP of the entire Axis team of the current map/campaign?
 - *See also:* [[List_of_Cvars_(new)/#g_alliedMapXP|g_alliedMapXP]] 

--------

*g_axisMaxLives*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 - *Default:* "0"| *Possible values:* 
 - Specifies the amount of lives each Axis player has individually. These lives are not shared across the team. The HUD counter seen in the screenshot displays the amount of respawns you have left. 
 - *See also:* [[List_of_Cvars_(new)/#g_alliedMaxLives|g_alliedMaxLives]] 

.. image:: https://i.imgur.com/qEaZYch.jpg 

--------

*g_axisWins*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{TODO} *Is it necessary that this works like bitflags? Feels a bit counter-intuitive.*

 - *Default:* "0"| *Possible values:* 
 - Stores the amount of wins of the Axis team in the currently active campaign.
 - *NOTE:* This works like bitflags (1, 2, 4, 8, etc.) So, if the Axis team has three wins the CVAR has a value of 7 (1 + 2 + 4). 
 - *See also:* [[List_of_Cvars_(new)/#g_alliedWins|g_alliedWins]] 

--------

*g_balancedTeams*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 - *Default:* "0" = disabled| *Possible values:* "0" = disabled; "1" = enabled
 - https://i.imgur.com/gLcBd4P.png!:https://i.imgur.com/gLcBd4P.png If enabled, players are prevented from joinging the team with more players.
 - *See also:* 
 - [[List_of_Cvars_(new)/#g_antiLag|g_antiLag]] 

--------

*R_* (Renderer)
----------------------------------------

Player cvars
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*r_allowExtensions*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* "1.2"| *Possible values:*  "0" = disabled; "1" = enabled. 
 - Enables/Disables global OpenGL extensions. 

--------

*r_cache*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_cacheModels*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_cacheShaders*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_colorbits*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_colorMipLevels*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_customaspect*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_customheight*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_customwidth*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_depthbits*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_detailTextures*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_displayRefresh*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_drawSun*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_dynamiclight*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_ext_compressed_textures*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_ext_multitexture*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_ext_texture_env_add*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_ext_texture_filter_anisotropic*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_facePlaneCull*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_fastsky*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_finish*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_flares*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_fullscreen*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_gamma*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_ignoreFastPath*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_ignoreGLErrors*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_ignorehwgamma*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_intensity*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_lodbias*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_lodCurveError*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_mapOverBrightBits*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_maxpolys*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_maxpolyverts*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_mode*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_normallength*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_overBrightBits*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_picmip*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_printShaders*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_railCoreWidth*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_railSegmentLength*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_railWidth*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_shadows*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_showImages*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_stencilbits*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_subdivisions*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_swapInterval*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_texturebits*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_textureMode*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_trisColor*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_wolffog*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

Protected cvars
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*r_ambientScale*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Add images.*

 - *Default:* "0.5"| *Possible values:* "0.0" = disabled; "2.0" = max. 
 - Sets light intensity of dynamic game entities _(e.g. player models, construction crates and tanks)_. 

--------

*r_clear*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_directedScale*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_drawfoliage*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_drawworld*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_flareFade*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_flareSize*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_lodscale*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_showsky*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_zfar*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_znear*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

Developer cvars
^^^^^^^^^^^^^^^

*r_bonesDebug*
""""""""""""""""""""""""""""""""""""""""

{TODO} *Seems to be under development. Value of "8" and "9" flood a todo message in console.*

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_debugLight*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_debugSort*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_debugSurface*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_drawBuffer*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_drawentities*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_ignore*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_lightmap*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_lockpvs*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_logFile*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_measureOverdraw*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_nobind*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_nocull*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_nocurves*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_noportals*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_norefresh*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_novis*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_offsetFactor*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_offsetUnits*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_portalOnly*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_roundImagesDown*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_showcluster*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_shownormals*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_showtris*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_simpleMipMaps*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_singleShader*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_skipBackEnd*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

*r_speeds*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:*
 - Description needed.

--------

Internal cvars
^^^^^^^^^^^^^^

*r_oldMode*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

*r_uiFullScreen*
""""""""""""""""""""""""""""""""""""""""

 - *Default:* | *Possible values:* 
 - Description needed. 

--------

Removed cvars
-------------
  +---------------------------+--------------------+-------------------------------+
  | CVAR                      | Reason             | Replacement                   |
  +===========================+====================+===============================+
  | cg_animState              | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_bigFont                | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_blinktime              | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_bobYaw                 | Combined in 1 CVAR | cg_bobbing                    |
  +---------------------------+--------------------+-------------------------------+
  | cg_bobPitch               | Combined in 1 CVAR | cg_bobbing                    |
  +---------------------------+--------------------+-------------------------------+
  | cg_bobRoll                | Combined in 1 CVAR | cg_bobbing                    |
  +---------------------------+--------------------+-------------------------------+
  | cg_bobUp                  | Combined in 1 CVAR | cg_bobbing                    |
  +---------------------------+--------------------+-------------------------------+
  | cg_cameraMode             | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_cameraOrbit            | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_cameraOrbitDelay       | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_clipboardName          | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_deferPlayers           | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_enableBreath           | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_fastSolids             | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_footsteps              | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_ignore                 | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_fastSolids             | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_message                | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_messagePlayer          | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_messagePlayerName      | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_modVersion             | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_movespeed              | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_noRender               | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_noTaunt                | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_noVoiceChats           | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_noVoiceText            | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_recording_Statusline   | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_runpitch               | Bugged             | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_runroll                | Bugged             | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_smallFont              | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_specSwing              | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_stereoSeparation       | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_timescaleFadeEnd       | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_timescaleFadeSpeed     | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_viewsize               | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_wolfparticles          | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_zoomDefaultBinoc       | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_zoomDefaultFG          | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_zoomDefaultSnooper     | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_zoomFOV                | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_zoomStepBinoc          | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_zoomStepFG             | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cg_zoomStepSnooper        | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cl_activateLean           | Was not used       | cg_activateLean               |
  +---------------------------+--------------------+-------------------------------+
  | cl_anonymous              | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cl_debugTranslation       | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cl_inGameVideo            | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cl_language               | Was not used       | cl_lang                       |
  +---------------------------+--------------------+-------------------------------+
  | cl_motd                   | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cl_motdString             | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cl_punkbuster             | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cl_updateAvailable        | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cl_updateFiles            | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cl_visibleClients         | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | cl_waitForFire            | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | com_cameraMode            | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | com_cleanWhiteList        | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | com_logosPlaying          | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | con_debug                 | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | con_restricted            | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | fs_buildGame              | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | fs_buildPath              | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | fs_CDpath                 | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | fs_copyFiles              | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | fs_restrict               | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | r_ati_fsaa_samples        | Was not used       | ENFORCED FOR VANILLA CLIENTS  |
  +---------------------------+--------------------+-------------------------------+
  | r_ati_truform_normalmode  | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | r_ati_truform_pointmode   | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | r_ati_truform_tess        | Was not used       | ENFORCED FOR VANILLA CLIENTS  |
  +---------------------------+--------------------+-------------------------------+
  | r_clampToEdge             | Was not used       | ENFORCED FOR VANILLA CLIENTS  |
  +---------------------------+--------------------+-------------------------------+
  | r_dlightBacks             | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | r_ext_ATI_pntriangles     | Was not used       | ENFORCED FOR VANILLA CLIENTS  |
  +---------------------------+--------------------+-------------------------------+
  | r_nv_fogdist_mode         | Was not used       | ENFORCED FOR VANILLA CLIENTS  |
  +---------------------------+--------------------+-------------------------------+
  | r_portalsky               | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+
  | r_primitives              | Was not used       | None                          |
  +---------------------------+--------------------+-------------------------------+


