===================
HUD Editor
===================

Introduction
^^^^^^^^^^^^
Since the 2.81.0, ET:Legacy introduced a new way to fully customize all HUD components by using the in-game editor and using the extended json hud file.

50 components are currently customizable, with generic customization options and for some more specifics linked to styles options.

The HUD file is compatible with both 4:3 and 16:9 resolution. Position adjustment is done automaticly and component aspect ratio are conserved.

The HUD view is a 640 per 480 virtual grid, rescaled horizontaly depending of aspect ratio.

Old `hud.dat` file is still compatible with new system, but the visual aspect may changes depending of the component.

New `hud.dat` file path has changed. The new storage location is under `fs_homepath` at `legacy/profiles/<name>` directory (see https://github.com/etlegacy/etlegacy/wiki/Path-and-File-Structure#homepath---fs_homepath)

TODO: Anchor behaviour

In-game editor
^^^^^^^^^^^^^^
Overview
""""""""

The in-game editor is reachable by using the menu UI ``Menu`` -> ``Options`` -> ``View`` -> ``HUD Editor`` or by typing in console the edithud command.

**Note**: The HUD editor is not available from main menu.

The HUD editor is divided in 3 differents frames : 

* Rescaled in-game view 
* Customization panel on the left
* Components selection panel on the bottom

Components can be toogle visible / invisble, which allow their usage or not. An invisible component is not rendered at all and the related functionnality aren't called.

HUD 0 (aka ``ETmain``) is the default HUD and can't be modified or deleted.

To start creating / setting a custom HUD, it is required to ``clone`` (copy) an existing HUD or using an existing one but HUD 0.

HUD view window
""""""""""""""""""""""
The rescaled HUD view allow reposionning visible elements by selecting them with left mouse buton then doing a drag & drop movement.

Drag & drop is achievable by holding left mouse buton on a component, moving the mouse cursor in the HUD view and release the left mouse butoon to the new wanted position.

On fly over a visible component with mouse cursor, a green rectangle outline the component indicating the possibility to select it. Also, a tooltip showing the component name is displayed.

Once selected, the component outline color change to yellow and it gain the focus for customization.

When 2 or more components are stacked under the same cursor position, it is possible to do multiple left mouse buton click to select the differents components.

Components selection panel
""""""""""""""""""""""""""
The components selection panel list all the components availables for customization and allow selection of a component.
The text color may change depending of the components visibily and/or selection state :

* Yellow : The current selected component
* Green  : Visible components
* Red    : Invisible components

Invisible components can only be selected from this panel.

Settings customization panel
""""""""""""""""""""""""""""""
The settings customization panel provide options to manage HUDs and customize selected component in HUD view or component selection panel.
The panel is divided in 4 differents categories :

* HUD setup, to select and manipulate HUD:
	- Select HUD : list of HUD index number used to select the HUD to display/use.
		- **NOTE**: This modify the related ``cg_altHud`` cvar.
	- Save : Save ALL the HUDs mofication into `hud.dat` file
	- Clone : Duplicate the selected HUD to a free HUD index and select it. It doesn't save it in `hud.dat` file.
	- Delete : Delete the selected HUD from `hud.dat` file. The selected HUD will change to the default one ``(0: ETmain)``
	- Reset component : Reset **ALL** settings from the selected component to the default values from HUD ``(0: ETmain)``
	- Name : HUD name which can be used to select HUD with ``cg_altHud`` cvar from the name
* Position & Size, to modify component position and size according 4 values:
	- X : abscissa coordinate
	- Y : ordinate coordinate
	- W : Width
	- H : Height
* Text, to modify font size and style
	- S : Scale ratio, depending of original font size, where 100% is the default
	- Style : Font Style, see :ref:`Style Text`
	- Align : Font alignment depending of component position, see :ref:`Align Text`
* Color & Style, to colorize the component and customize the style: 
	- Main : Main color, see :ref:`Component Color`
	- Second : Secondary color, see :ref:`Component Color`
	- Backgrnd : Background color, delimited by the size of the component
	- Border : Border color, delimited by the size of the component with a width of 1px
	- R: Red color selector ranged from 0 to 255
	- G: Green color selector ranged from 0 to 255
	- B: Blue color selector ranged from 0 to 255
	- A: Alpha (aka transparency) selector ranged from 0 to 255
	- Style: Customizable options separated in 2 categories, generic option and specific one. All component have access to generic option, but not all use specific one. See :ref:`Component Style`.
		- Visible : Toogle the component visibility 
		- AutoAdj : Toogle the automatic adjustement of the border position and size depending of the content
		- Background : Toogle the background visibility
		- Border : Toogle the border visibility

Usage
"""""

+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Key Sequences                      | Description                                                                                                          |
+=====================+==============+======================================================================================================================+
| Down Arrow                         | Move down a component by 1px                                                                                         |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Left Arrow                         | Move left a component by 1px                                                                                         |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Up Arrow                           | Move up a component by 1px                                                                                           |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Right Arrow                        | Move right a component by 1px                                                                                        |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| CTRL (hold) + Arrow                | Move to direction by 0.1px                                                                                           |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| SHIFT (hold) + Arrow               | Move to direction by 5px                                                                                             |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ALT (hold) + Arrow                 | Resize by enlarging to the right / down or shrinking to the left / up by 1px                                         |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ALT (hold) + CTRL (hold) + Arrow   | Resize by 0.1px to pressed arrow direction                                                                           |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ALT (hold) + SHIFT (hold) + Arrow  | Resize by 5px to pressed arrow direction                                                                             |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Mouse wheel down                   | Enlarge by 1px the width and the height without moving the component                                                 |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Mouse wheel up                     | Shrink by 1px the width and the height without moving the component                                                  |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| CTRL (hold) + Mouse wheel down/up  | Resize on position by 0.1px                                                                                          |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Insert                             | Move component to the center of the HUD                                                                              |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Home                               | Move component to the middle width of the HUD (if on the right of it) or to the left of the HUD                      |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| End                                | Move component to the middle width of the HUD (if on the left of it) or to the right of the HUD                      |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Page up                            | Move component to the middle height of the HUD (if under it) or to the top of the HUD                                |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Page Down                          | Move component to the middle height of the HUD (if above it) or to the bottom of the HUD                             |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| l                                  | Toogle the layout visibilty of **ALL** components (aka outline)                                                      |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| h                                  | Toogle the help window visibility                                                                                    |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+

New hud.dat json file
^^^^^^^^^^^^^^^^^^^^^

Annexe
^^^^^^

Components list
"""""""""""""""

+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
| Components Name    | Description                                                                                                 | Game type Availabilty |
+====================+=============================================================================================================+=======================+
|    banner          | The banner text display custom message received from server `bp` command (Banner Print)                     | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    breathbar       | The breath bar indicating the remaining time to hold breath under water before starting to drow             | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    breathtext      | The breath text in "%" indicating the remaining time to hold breath under water before starting to drow     | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    centerprint     | The center text display custom or kill/revive message received from server `cp` command (Center Print)      | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    chat            | Meow                                                                                                        | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    compass         | The minimap indicating players/objectives position, players quick chat call, wounded players                | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    crosshair       | The crosshair used to aim at something, such as ground, sky, tree, bullet and so on                         | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    crosshairbar    | The health bar of the aimed entity, such as player, vehicules, breakable, and so on                         | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    crosshairtext   | The name of the aimed entity, such as player, vehicules, breakable, and so on                               | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    cursorhints     | The icon indicating interraction with near entity, such as construcible, door, cabinet, and so on           | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    demotext        | The text of the current demo or replay record state                                                         | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    disconnect      | The icon and text displayed when the connection between client and server has been interrupted              | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    fireteam        | The window listing the current players states in the joined fireteam                                        | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    followtext      | The text and icon used to display the current spected / followed player name, team and rank                 | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    fps             | The text indicating the number of procedeed frame per second by the client                                  | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    healthbar       | The player health bar. At 0, the player is wounded                                                          | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    healthtext      | The player health numeric value. Suffixed with "HP"                                                         | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    hudhead         | The head of the incarnate caractere. The animation depend of the player action and states                   | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    lagometer       | Display graphic showing how unplayable the game is depending of player or server connection                 | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    limbotext       | The text indicating player is wounded/dead, waiting for a medic or not and display remaining spawn time     | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    livesleft       | Indicate the number of lives left in Last Man Standing game type (LMS). Doesn't show on other game types.   | Last Man Standing     |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    localtime       | The text indicating the current time at client location                                                     | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    missilecamera   | The window showing missile heading view until impact or explosion                                           | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    objectives      | The icons tracking objectives status, depending of the teams holding/stealing/dropping it                   | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    objectivetext   | The text displaying the nearest Point Of Interest description                                               | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    ping            | The text indicating the delay for communicate between client and server (implicitly in ms)                  | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    pmitemsbig      | The text and icon indicating ranking/skill/prestige gain up                                                 | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    popupmessages   | The pop-up list feed for objectives/kill/connection/dynamites/mines/constructions states or custom message  | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    powerups        | The icon indicating player invulnerability, under adrealine, disguised or carrying objective                | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    ranktext        | The player rank mini name (Trigram) depending of the team (Axis / Allies)                                   | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    reinforcement   | The text indicating the remaining time before next respawn                                                  | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    roundtimer      | The text indicating the remaining time before end of the map/round                                          | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    snapshot        | Debug information indicating server time, last spapshot number and number of server commmand received       | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    spawntimer      | Indicate the estimated remaining time before enemy respawn. The timer is set with `cg_sharetimertext` cvar  | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    spectatorstatus | The text indicating if player is in spectator/freecam/weaponcam mod                                         | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    spectatortext   | The text indicating instruction for opening limbo/multiview or key usage for following players              | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    speed           | The player speed movement exprimed in Unit / Metric / Imperial unit per second. Sufixed UPS / KPS / MPS     | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    sprinttext      | The sprint text in "%" indicating the remaining endurance to sprint. At 0, sprint is not possible           | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    staminabar      | The endurance bar indicating the remaining sprint availability. Also drained by jump                        | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    stats           | Quick view displaying player stats (Kill, Death, Self Kill, Damage Given, Damage received)                  | Demo replay only      |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    statsdisplay    | The skill level for current class, battle sense and light (heavy for tank and nested-MG) weapon skill       | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    votetext        | The text related to the current pending vote, asking for casting a reponse and/or showing vote status       | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    warmuptext      | The warmup status text indicating current loaded server configuration and action to do before match begin   | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    warmuptitle     | The warmup count down or status before match begin                                                          | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    weaponammo      | The current weapon amount of ammo in clip/reserve                                                           | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    weaponchargebar | The weapon usage capability, drained depending of class and weapon usage                                    | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    weaponchargetext| The weapon charge text in "%" indicating the remaining weapon usage capability.                             | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    weaponicon      | The icon of the current selected (in hand) weapon. Also display the overheat bar of the current weapon      | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    weaponstability | The stability bar indicating the current aim spread applied to the weapon (from 0 to 255)                   | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
|    xptext          | The player experience numeric value. Suffixed with "XP"                                                     | All                   |
+--------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+

Options list
""""""""""""
+--------------------+-----------------------------------------------------------------------------------+-------------------------------------------------+
| Options            | Description                                                                       | Range                                           |
+====================+===================================================================================+=================================================+
| x                  | X coordinate                                                                      | 0 - 640 (visible grid limit, can be out ranged) |
+--------------------+-----------------------------------------------------------------------------------+-------------------------------------------------+
| y                  | Y coordinate                                                                      | 0 - 480 (visible grid limit, can be out ranged) |
+--------------------+-----------------------------------------------------------------------------------+-------------------------------------------------+
| w                  | Component Width                                                                   | 0 - 640 (visible grid limit, can be out ranged) |
+--------------------+-----------------------------------------------------------------------------------+-------------------------------------------------+
| h                  | Component Height                                                                  | 0 - 480 (visible grid limit, can be out ranged) |
+--------------------+-----------------------------------------------------------------------------------+-------------------------------------------------+
| visible            | Toogle component visibility                                                       | 0 - 1 (boolean)                                 |
+--------------------+-----------------------------------------------------------------------------------+-------------------------------------------------+
| style              | Customize component depending of his usage (if available)                         | See Style Section                               |
+--------------------+-----------------------------------------------------------------------------------+-------------------------------------------------+
| scale              | Change font scale where 100 is the default value (normalized)                     | 0 - 300 (recommanded range, can be out ranged)  |
+--------------------+-----------------------------------------------------------------------------------+-------------------------------------------------+
| colorMain          | Change either the font color (text component) or main component color (specific)  | See :ref:`Color Usage`                          |
+--------------------+-----------------------------------------------------------------------------------+-------------------------------------------------+
| colorSecondary     | Change secondary component color (specific, not available for text component)     | See :ref:`Color Usage`                          |
+--------------------+-----------------------------------------------------------------------------------+-------------------------------------------------+
| showBackGround     | Toogle background visibility                                                      | 0 - 1 (boolean)                                 |
+--------------------+-----------------------------------------------------------------------------------+-------------------------------------------------+
| colorBackground    | Change the component background color                                             | See :ref:`Color Usage`                          |
+--------------------+-----------------------------------------------------------------------------------+-------------------------------------------------+
| showBorder         | Toogle border visibility                                                          | 0 - 1 (boolean)                                 |
+--------------------+-----------------------------------------------------------------------------------+-------------------------------------------------+
| colorBorder        | Change the component border color                                                 | See :ref:`Color Usage`                          |
+--------------------+-----------------------------------------------------------------------------------+-------------------------------------------------+
| styleText          | Customize font style aspect (only available for component with text only)         | See :ref:`Style Text`                           |
+--------------------+-----------------------------------------------------------------------------------+-------------------------------------------------+
| alignText          | Customize font alignment position (only available for component with text only)   | See :ref:`Align Text`                           |
+--------------------+-----------------------------------------------------------------------------------+-------------------------------------------------+
| autoAdjust         | Adjust border and background size to component content (available for text only)  | 0 - 1 (boolean)                                 |
+--------------------+-----------------------------------------------------------------------------------+-------------------------------------------------+

Component Color
"""""""""""""""

Component Style
"""""""""""""""

+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Component          | Style                 | Description                                                                                        | Values |
+====================+=======================+====================================================================================================+========+
|    banner          | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    breathbar       |                       |                                                                                                    |        |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    breathtext      | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    centerprint     | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    chat            | No Team Flag          | Toogle team flag visibility next to the chat line                                                  | 1      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    compass         |                       |                                                                                                    |        |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|                    | Pulse                 | Enlarge the crosshair main part depending of aim spread                                            | 1      |
|                    +-----------------------+----------------------------------------------------------------------------------------------------+--------+
|                    | Pulse Alt             | Enlarge the crosshair secondary part depending of aim spread                                       | 2      |
|    crosshair       +-----------------------+----------------------------------------------------------------------------------------------------+--------+
|                    | Dynamic Color         | Change the crosshair main part color depending of player health                                    | 4      |
|                    +-----------------------+----------------------------------------------------------------------------------------------------+--------+
|                    | Dynamic Color Alt     | Change the crosshair secondary part color depending of player health                               | 8      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    crosshairbar    |                       |                                                                                                    |        |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    crosshairtext   | Full Color            | Color the targeted entity name in it custom color instead of white                                 | 1      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    cursorhints     |                       |                                                                                                    |        |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    demotext        | Details               | Print a more details string containing file name and size of the current demo/audio recorded       | 1      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    disconnect      | No Text               | Toogle string visibility "Connection Interrupted" when client loast connection to server           | 1      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    fireteam        |                       |                                                                                                    |        |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    followtext      | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    fps             | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    healthbar       |                       |                                                                                                    |        |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    healthtext      | Dynamic Color         | Gradient the text color depending of player HP: White (>100) yellow (>66) orange (> 0) red (>0)    | 1      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    hudhead         | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    lagometer       | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    limbotext       | No Wounded Msg        | Toogle string visibility "You are wounded and waiting for a medic"                                 | 1      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    livesleft       | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|                    | Second                | Toogle seconds visibility                                                                          | 1      |
|    localtime       +-----------------------+----------------------------------------------------------------------------------------------------+--------+
|                    | 12 Hours              | Change hours time format between 24 or 12 suffixed by AM / PM                                      | 2      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    missilecamera   | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    objectives      | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    objectivetext   | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    ping            | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    pmitemsbig      |                       |                                                                                                    |        |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    popupmessages   |                       |                                                                                                    |        |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    powerups        | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    ranktext        | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    reinforcement   | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    roundtimer      | Simple                | Don't show reinforcement and enemy spaw timer next to round timer                                  | 1      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    snapshot        | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    spawntimer      | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    spectatorstatus | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    spectatortext   | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    speed           | Max Speed             | Show maximum reached speed visibility                                                              | 1      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    sprinttext      | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    staminabar      |                       |                                                                                                    |        |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    stats           |                       |                                                                                                    |        |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    statsdisplay    | Column                | Display skills rank in column format with skill icons and skill levels above it                    | 1      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    votetext        | Complaint             | Toogle complaint proposal text visibility on player getting team killed                            | 1      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    warmuptext      | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    warmuptitle     | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    weaponammo      | Dynamic Color         | Gradient the text color depending of weapon ammo left in clip/reserve                              | 1      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    weaponchargebar |                       |                                                                                                    |        |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    weaponchargetext| N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    weaponicon      | Icon Flash            | Highlight the weapon icon in yellow while switching/reloading and in red while firing              | 1      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    weaponstability |                       |                                                                                                    |        |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+
|    xptext          | N/A                   | -                                                                                                  | -      |
+--------------------+-----------------------+----------------------------------------------------------------------------------------------------+--------+

Color Usage
"""""""""""

There are 3 formats to customize colors : 

+-------------+-----------------------------------------------------------------------------------------------+--------------------------------------------+
| Format      | Description                                                                                   | Values And Range                           |
+=============+===============================================================================================+============================================+
| Hexadecimal | RRGGBB[AA] => RR is Red value, GG is green value, BB is blue value and AA is alpha (optional) | 00 to FF (Double Hexa value)               |
+-------------+-----------------------------------------------------------------------------------------------+--------------------------------------------+
|             |                                                                                               | 0.0 to 1.0 color normalized (float)        |
| Decimal     | R G B [A]  => R is Red value, G is green value, B is blue value and A is alpha (optional)     | or                                         |
|             |                                                                                               | 0 to 255 color component (integer)         |
+-------------+-----------------------------------------------------------------------------------------------+--------------------------------------------+
|             |                                                                                               | "white"                                    |
|             |                                                                                               | "red"                                      |
|             |                                                                                               | "green"                                    |
|             |                                                                                               | "blue"                                     |
|             |                                                                                               | "yellow"                                   |
|             |                                                                                               | "magenta"                                  |
|             |                                                                                               | "cyan"                                     |
|             |                                                                                               | "orange"                                   |
|             |                                                                                               | "mdred"                                    |
| String      | Predefined color as string values with Alpha set to 1.0 (255)                                 | "mdgreen"                                  |
|             |                                                                                               | "dkgreen"                                  |
|             |                                                                                               | "mdcyan"                                   |
|             |                                                                                               | "mdyellow"                                 |
|             |                                                                                               | "mdorange"                                 |
|             |                                                                                               | "mdblue"                                   |
|             |                                                                                               | "ltgrey"                                   |
|             |                                                                                               | "mdgrey"                                   |
|             |                                                                                               | "dkgrey"                                   |
|             |                                                                                               | "black"                                    |
+-------------+-----------------------------------------------------------------------------------------------+--------------------------------------------+

Style Text
""""""""""

Align Text
""""""""""""""
