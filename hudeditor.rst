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

New `hud.dat` file path has changed. The new storage location is under `fs_homepath` at `legacy/profiles/<name>` directory, see [Path and File Structure](https://github.com/etlegacy/etlegacy/wiki/Path-and-File-Structure#homepath---fs_homepath)

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

Components can be toogle visible / invisible, which allow their usage or not. An invisible component is not rendered at all and the related functionnality aren't called.

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
	- Main : Main color, see Component ``Color``
	- Second : Secondary color, see Component ``Color``
	- Backgrnd : Background color, delimited by the size of the component
	- Border : Border color, delimited by the size of the component with a width of 1px
	- R: Red color selector ranged from 0 to 255
	- G: Green color selector ranged from 0 to 255
	- B: Blue color selector ranged from 0 to 255
	- A: Alpha (aka transparency) selector ranged from 0 to 255
	- Style: Customizable options separated in 2 categories, generic option and specific one. All component have access to generic option, but not all use specific one. See Component ``Style``.
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
| n                                  | Toogle the noise generator to simulate components animation                                                          |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| f                                  | Toogle the HUD editor in full screen (back to normal resolution and hiding component and settings panel)             |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+

Components List
^^^^^^^^^^^^^^^

banner
""""""

:Description: The banner text display custom message received from server `bp` command (Banner Print)

:Game type Availability: All

:Type: Multiline Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

breathbar
"""""""""

:Description: The breath bar indicating the remaining time to hold breath under water before starting to drow

:Game type Availability: All

:Type: Bar

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Bar Background color                                                                                        |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | Bar border color                                                                                            |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Left                  | Move maximum on left. If ``Vertical`` is set, maximum is on top. Ignored if ``Center`` is set      | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Center                | The minimum start from the center of the bar and is filled to both of the opposite direction       | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Vertical              | Change the bar orientation vertically                                                              | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Alpha              | Unused                                                                                             | 8      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Bckgrnd           | Draw background color for the bar only. The color is set by ``Main Color``                         | 16     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y5                 | Avoid the 5px margin on X. Applied if ``Bar Bckgrnd`` is set                                       | 32     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y0                 | Avoid the 5px margin on X and Y. Applied if ``Bar Bckgrnd`` is set                                 | 64     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Lerp Color            | Gradient the color alpha depending of bar values                                                   | 128    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Border            | Draw the bar border with a thickness of 2px. Tickness value is overwritted if Border Tiny is set   | 256    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Border Tiny           | Reduce the bar border thickness to 1px. Applied if ``Bar Border`` is set                           | 512    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Decor                 | Draw the decor outlining the bar                                                                   | 1024   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Icon                  | Draw the icon depending of ``Left`` and ``Vertical`` values set                                    | 2048   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

breathtext
""""""""""

:Description: The breath text in "%" indicating the remaining time to hold breath under water before starting to drow   

:Game type Availability: All

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

centerprint
"""""""""""

:Description: The center text display custom or kill/revive message received from server `cp` command (Center Print)

:Game type Availability: All

:Type: Multiline Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

chat
""""

:Description: Meow

:Game type Availability: All

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| No Team Flag          | Toogle team flag visibility next to the chat line                                                  | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

compass
"""""""

:Description: The minimap indicating players/objectives position, players quick chat call, wounded players

:Game type Availability: All

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Square                | Change the compass shape to square                                                                 | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Draw Item             | Draw item icon (objective carriable) on compass                                                    | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Draw Sec Obj          | Draw secondary objective on compass                                                                | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Draw Prim Obj         | Draw primary objective on compass                                                                  | 8      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Decor                 | Draw the compass border decor. Not available with ``Square`` compass                               | 16     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Direction             | Draw the red arrow pointing to the cardinal pointing direction                                     | 32     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Cardinal Pts          | Draw the cardinal points with tick with circle compass and N, W, S, E letter with squared compass  | 64     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Always Draw           | Always draw the compass even if the full map is draw on display                                    | 128    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

crosshair
"""""""""

:Description: The crosshair used to aim at something, such as ground, sky, tree, bullet and so on

:Game type Availability: All

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Crosshair main part                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | Crosshair secondary (alternate) part                                                                        |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Pulse                 | Enlarge the crosshair main part depending of aim spread                                            | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Pulse Alt             | Enlarge the crosshair secondary part depending of aim spread                                       | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Dynamic Color         | Change the crosshair main part color depending of player health                                    | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Dynamic Color Alt     | Change the crosshair secondary part color depending of player health                               | 8      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

crosshairbar
""""""""""""

:Description: The health bar of the aimed entity, such as player, vehicules, breakable, and so on 

:Game type Availability: All

:Type: Bar

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Bar Background color                                                                                        |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | Bar border color                                                                                            |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Left                  | Move maximum on left. If ``Vertical`` is set, maximum is on top. Ignored if ``Center`` is set      | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Center                | The minimum start from the center of the bar and is filled to both of the opposite direction       | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Vertical              | Change the bar orientation vertically                                                              | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Alpha              | Unused                                                                                             | 8      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Bckgrnd           | Draw background color for the bar only. The color is set by ``Main Color``                         | 16     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y5                 | Avoid the 5px margin on X. Applied if ``Bar Bckgrnd`` is set                                       | 32     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y0                 | Avoid the 5px margin on X and Y. Applied if ``Bar Bckgrnd`` is set                                 | 64     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Lerp Color            | Gradient the color alpha depending of bar values                                                   | 128    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Border            | Draw the bar border with a thickness of 2px. Tickness value is overwritted if Border Tiny is set   | 256    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Border Tiny           | Reduce the bar border thickness to 1px. Applied if ``Bar Border`` is set                           | 512    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Decor                 | Draw the decor outlining the bar                                                                   | 1024   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Icon                  | Draw the icon depending of ``Left`` and ``Vertical`` values set                                    | 2048   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

crosshairtext
"""""""""""""

:Description: The name of the aimed entity, such as player, vehicules, breakable, and so on

:Game type Availability: All

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Full Color            | Color the targeted entity name in it custom color instead of white                                 | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

cursorhints
"""""""""""

:Description: The icon indicating interraction with near entity, such as construcible, door, cabinet, and so on

:Game type Availability: All

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Size Pulse            | Increase/decrease the icon size. Ignored if ``Strobe Pulse`` is set                                | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Strobe Pulse          | Increase the icon size until max and reset back to initial size. Overwrite ``Size Pulse`` if set   | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Alpha Pulse           | Fade in/out the icon alpha                                                                         | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

demotext
""""""""

:Description: The text of the current demo or replay record state

:Game type Availability: All

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Details               | Print a more detailled string containing file name and size of the current demo/audio recorded     | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

disconnect
""""""""""

:Description: The icon and text displayed when the connection between client and server has been interrupted

:Game type Availability: All

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| No Text               | Toogle string visibility "Connection Interrupted" when client loast connection to server           | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

fireteam
""""""""

:Description: The window listing the current players states in the joined fireteam

:Game type Availability: All

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Latched Class         | Draw the team mate selected class on next respawn if different from the current one                | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Header             | Toogle header visibility (frame with fireteam name)                                                | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

followtext
""""""""""

:Description: The text and icon used to display the current spected / followed player name, team and rank

:Game type Availability: All

:Type: Multiline Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

fps
"""

:Description: The text indicating the number of procedeed frame per second by the client

:Game type Availability: All

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

healthbar
"""""""""

:Description: The player health bar. At 0, the player is wounded

:Game type Availability: All

:Type: Bar

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Bar Background color                                                                                        |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | Bar border color                                                                                            |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Left                  | Move maximum on left. If ``Vertical`` is set, maximum is on top. Ignored if ``Center`` is set      | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Center                | The minimum start from the center of the bar and is filled to both of the opposite direction       | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Vertical              | Change the bar orientation vertically                                                              | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Alpha              | Unused                                                                                             | 8      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Bckgrnd           | Draw background color for the bar only. The color is set by ``Main Color``                         | 16     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y5                 | Avoid the 5px margin on X. Applied if ``Bar Bckgrnd`` is set                                       | 32     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y0                 | Avoid the 5px margin on X and Y. Applied if ``Bar Bckgrnd`` is set                                 | 64     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Lerp Color            | Gradient the color alpha depending of bar values                                                   | 128    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Border            | Draw the bar border with a thickness of 2px. Tickness value is overwritted if Border Tiny is set   | 256    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Border Tiny           | Reduce the bar border thickness to 1px. Applied if ``Bar Border`` is set                           | 512    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Decor                 | Draw the decor outlining the bar                                                                   | 1024   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Icon                  | Draw the icon depending of ``Left`` and ``Vertical`` values set                                    | 2048   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

healthtext
""""""""""

:Description: The player health numeric value. Suffixed with "HP"

:Game type Availability: All

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Dynamic Color         | Gradient the text color depending of player HP: White (>100) yellow (>66) orange (> 0) red (>0)    | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

hudhead
"""""""

:Description: The head of the incarnate caractere. The animation depend of the player action and states

:Game type Availability: All

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

lagometer
"""""""""

:Description: Display graphic showing how unplayable the game is depending of player or server connection

:Game type Availability: All

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

limbotext
"""""""""

:Description: The text indicating player is wounded/dead, waiting for a medic or not and display remaining spawn time

:Game type Availability: All

:Type: Multiline Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| No Wounded Msg        | Toogle string visibility "You are wounded and waiting for a medic"                                 | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

livesleft
"""""""""

:Description: Indicate the number of lives left in Last Man Standing game type (LMS). Doesn't show on other game types.

:Game type Availability: Last Man Standing

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

localtime
"""""""""

:Description: The text indicating the current time at client location 

:Game type Availability: All

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Second                | Toogle seconds visibility                                                                          | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| 12 Hours              | Change hours time format between 24 or 12 suffixed by AM / PM                                      | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+


missilecamera
"""""""""""""

:Description: The window showing missile heading view until impact or explosion

:Game type Availability: All

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

objectives
""""""""""

:Description: The icons tracking objectives status, depending of the teams holding/stealing/dropping it

:Game type Availability: All

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

objectivetext
"""""""""""""

:Description: The text displaying the nearest Point Of Interest description

:Game type Availability: All

:Type: Multiline Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

ping
""""

:Description: The text indicating the delay for communicate between client and server (implicitly in ms)

:Game type Availability: All

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

pmitemsbig
""""""""""

:Description: The text and icon indicating ranking/skill/prestige gain up

:Game type Availability: All

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| No Skill              | Filter out skill up message                                                                        | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Rank               | Filter out rank up message                                                                         | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Prestige           | Filter out prestige gain message                                                                   | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

popupmessages
"""""""""""""

:Description: The pop-up list feed for objectives/kill/connection/dynamites/mines/constructions states or custom message

:Game type Availability: All

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| No Connect            | Filter out connection / deconnection message                                                       | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No TeamJoin           | Filter out player join allies / axis / spectator team                                              | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Mission            | Filter out objectives messages                                                                     | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Pickup             | Filter out item pickup messages                                                                    | 8      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Death              | Filter out death messages                                                                          | 16     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Weapon Icon           | Draw weapon used to kill someone instead of a text describing the means of death                   | 32     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Alt Weap Icons        | Draw weapon icon without outline. Applied if ``Weapon Icon`` is set                                | 64     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Swap V<->K            | Swap the victim and killer name text. Applied if ``Weapon Icon`` is set                            | 128    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Force Colors          | Force the font color by using defined ``Main Color``                                               | 256    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

powerups
""""""""

:Description: The icon indicating player invulnerability, under adrealine, disguised or carrying objective

:Game type Availability: All

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

ranktext
""""""""

:Description: The player rank mini name (Trigram) depending of the team (Axis / Allies)

:Game type Availability: All

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

reinforcement
"""""""""""""

:Description: The text indicating the remaining time before next respawn

:Game type Availability: All

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+


roundtimer
""""""""""

:Description: The text indicating the remaining time before end of the map/round

:Game type Availability: All

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Simple                | Don't show reinforcement and enemy spaw timer next to round timer                                  | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

snapshot
""""""""

:Description: Debug information indicating server time, last spapshot number and number of server commmand received

:Game type Availability: All

:Type: Multiline Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

spawntimer
""""""""""

:Description: Indicate the estimated remaining time before enemy respawn. The timer is set with `cg_sharetimertext` cvar

:Game type Availability: All

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

spectatorstatus
"""""""""""""""

:Description: The text indicating if player is in spectator/freecam/weaponcam mod

:Game type Availability: All

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

spectatortext
"""""""""""""

:Description: The text indicating instruction for opening limbo/multiview or key usage for following players

:Game type Availability: All

:Type: Multiline Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

speed
"""""

:Description: The player speed movement exprimed in Unit / Metric / Imperial unit per second. Sufixed UPS / KPS / MPS

:Game type Availability: All

:Type: Multiline Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Max Speed             | Show maximum reached speed visibility                                                              | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

sprinttext
""""""""""

:Description: The sprint text in "%" indicating the remaining endurance to sprint. At 0, sprint is not possible

:Game type Availability: All

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

staminabar
""""""""""

:Description: The endurance bar indicating the remaining sprint availability. Also drained by jump

:Game type Availability: All

:Type: Bar

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Bar Background color                                                                                        |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | Bar border color                                                                                            |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Left                  | Move maximum on left. If ``Vertical`` is set, maximum is on top. Ignored if ``Center`` is set      | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Center                | The minimum start from the center of the bar and is filled to both of the opposite direction       | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Vertical              | Change the bar orientation vertically                                                              | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Alpha              | Unused                                                                                             | 8      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Bckgrnd           | Draw background color for the bar only. The color is set by ``Main Color``                         | 16     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y5                 | Avoid the 5px margin on X. Applied if ``Bar Bckgrnd`` is set                                       | 32     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y0                 | Avoid the 5px margin on X and Y. Applied if ``Bar Bckgrnd`` is set                                 | 64     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Lerp Color            | Gradient the color alpha depending of bar values                                                   | 128    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Border            | Draw the bar border with a thickness of 2px. Tickness value is overwritted if Border Tiny is set   | 256    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Border Tiny           | Reduce the bar border thickness to 1px. Applied if ``Bar Border`` is set                           | 512    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Decor                 | Draw the decor outlining the bar                                                                   | 1024   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Icon                  | Draw the icon depending of ``Left`` and ``Vertical`` values set                                    | 2048   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

stats
"""""

:Description: Quick view displaying player stats (Kill, Death, Self Kill, Damage Given, Damage received)

:Game type Availability: Demo replay only

:Type: Multiline Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Kill                  | Filter player kill count                                                                           | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Death                 | Filter player death count                                                                          | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Self Kill             | Filter player self kill count                                                                      | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| DmgGiven              | Filter player damage given count                                                                   | 8      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| DmgRcvd               | Filter player damage received count                                                                | 16     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

statsdisplay
""""""""""""

:Description: The skill level for current class, battle sense and light (heavy for tank and nested-MG) weapon skill

:Game type Availability: All

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Column                | Display skills rank in column format with skill icons and skill levels above it                    | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

votetext
""""""""

:Description: The text related to the current pending vote, asking for casting a reponse and/or showing vote status

:Game type Availability: All

:Type: Multiline Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Complaint             | Toogle complaint proposal text visibility on player getting team killed                            | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

warmuptext
""""""""""

:Description: The warmup status text indicating current loaded server configuration and action to do before match begin

:Game type Availability: All

:Type: Multiline Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

warmuptitle
"""""""""""

:Description: The warmup count down or status before match begin

:Game type Availability: All

:Type: Multiline Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

weaponammo
""""""""""

:Description: The current weapon amount of ammo in clip/reserve

:Game type Availability: All

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Dynamic Color         | Gradient the text color depending of weapon ammo left in clip/reserve                              | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

weaponchargebar
"""""""""""""""

:Description: The weapon usage capability, drained depending of class and weapon usage

:Game type Availability: All

:Type: Bar

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Bar Background color                                                                                        |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | Bar border color                                                                                            |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Left                  | Move maximum on left. If ``Vertical`` is set, maximum is on top. Ignored if ``Center`` is set      | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Center                | The minimum start from the center of the bar and is filled to both of the opposite direction       | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Vertical              | Change the bar orientation vertically                                                              | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Alpha              | Unused                                                                                             | 8      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Bckgrnd           | Draw background color for the bar only. The color is set by ``Main Color``                         | 16     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y5                 | Avoid the 5px margin on X. Applied if ``Bar Bckgrnd`` is set                                       | 32     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y0                 | Avoid the 5px margin on X and Y. Applied if ``Bar Bckgrnd`` is set                                 | 64     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Lerp Color            | Gradient the color alpha depending of bar values                                                   | 128    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Border            | Draw the bar border with a thickness of 2px. Tickness value is overwritted if Border Tiny is set   | 256    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Border Tiny           | Reduce the bar border thickness to 1px. Applied if ``Bar Border`` is set                           | 512    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Decor                 | Draw the decor outlining the bar                                                                   | 1024   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Icon                  | Draw the icon depending of ``Left`` and ``Vertical`` values set                                    | 2048   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

weaponchargetext
""""""""""""""""

:Description: The weapon charge text in "%" indicating the remaining weapon usage capability

:Game type Availability: All

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

weaponicon
""""""""""

:Description: The icon of the current selected (in hand) weapon. Also display the overheat bar of the current weapon

:Game type Availability: All

:Type: Multiline Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Icon color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Icon Flash            | Highlight the weapon icon in yellow while switching/reloading and in red while firing              | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

weaponstability
"""""""""""""""

:Description: The stability bar indicating the current aim spread applied to the weapon (from 0 to 255)

:Game type Availability: All

:Type: Bar

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Always                | Draw the bar even if the weapon is not a scoped weapon                                             | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Left                  | Move maximum on left. If ``Vertical`` is set, maximum is on top. Ignored if ``Center`` is set      | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Center                | The minimum start from the center of the bar and is filled to both of the opposite direction       | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Vertical              | Change the bar orientation vertically                                                              | 8      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Alpha              | Unused                                                                                             | 16     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Bckgrnd           | Draw background color for the bar only. The color is set by ``Main Color``                         | 32     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y5                 | Avoid the 5px margin on X. Applied if ``Bar Bckgrnd`` is set                                       | 64     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y0                 | Avoid the 5px margin on X and Y. Applied if ``Bar Bckgrnd`` is set                                 | 128    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Lerp Color            | Gradient the color alpha depending of bar values                                                   | 256    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Border            | Draw the bar border with a thickness of 2px. Tickness value is overwritted if `Border Tiny` is set | 512    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Border Tiny           | Reduce the bar border thickness to 1px. Applied if ``Bar Border`` is set                           | 1024   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Decor                 | Draw the decor outlining the bar                                                                   | 2048   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Icon                  | Draw the icon depending of ``Left`` and ``Vertical`` values set                                    | 4096   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

xptext
""""""

:Description: The player experience numeric value. Suffixed with "XP"

:Game type Availability: All

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary             | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

Annexe
^^^^^^

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

+-------------------+----------------------------------------------------------------------------------------------------------------------------+---------+
| Name              | Description                                                                                                                | Values  |
+===================+============================================================================================================================+=========+
| Normal            | Normal text                                                                                                                | 0       |
+-------------------+----------------------------------------------------------------------------------------------------------------------------+---------+
| Blink             | Blink the text with a period of 500ms                                                                                      | 1       |
+-------------------+----------------------------------------------------------------------------------------------------------------------------+---------+
| Pulse             | Pulse the text with a period of 200ms                                                                                      | 2       |
+-------------------+----------------------------------------------------------------------------------------------------------------------------+---------+
| Shawdowed         | Shawdow the text by printing a bottom offsetted extra black character behind the initial text                              | 3       |
+-------------------+----------------------------------------------------------------------------------------------------------------------------+---------+
| Outlined          | Outline the text by printing a top offsetted extra colored character in front the initial text                             | 4       |
+-------------------+----------------------------------------------------------------------------------------------------------------------------+---------+
| Outlined Shadowed | Outline and Shawdow the text                                                                                               | 5       |
+-------------------+----------------------------------------------------------------------------------------------------------------------------+---------+
| Shadowed More     | Bold more the shawdow effect                                                                                               | 6       |
+-------------------+----------------------------------------------------------------------------------------------------------------------------+---------+

Align Text
""""""""""""""

Elements contained in component are aligned horizontaly regarding the component size bound:

+---------+--------------------------------------------------------------------------------------------------------------------------------------+---------+
| Name    | Description                                                                                                                          | Values  |
+=========+======================================================================================================================================+=========+
| Left    | Align / start drawing elements in component to the left side                                                                         | 0       |
+---------+--------------------------------------------------------------------------------------------------------------------------------------+---------+
| Right   | Align / end drawing elements in component to the right side                                                                          | 1       |
+---------+--------------------------------------------------------------------------------------------------------------------------------------+---------+
| Center  | Center elements in component and keep equal margin on the left and on the right of the elements                                      | 2       |
+---------+--------------------------------------------------------------------------------------------------------------------------------------+---------+
| Center2 | Center elements in component, align element in left justify adjusted to the longest elements and keep equal margin on left and right | 3       |
+---------+--------------------------------------------------------------------------------------------------------------------------------------+---------+
