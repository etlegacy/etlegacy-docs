===================
HUD Editor
===================

Introduction
^^^^^^^^^^^^
Since the 2.81.0, ET:Legacy introduced a new way to fully customize all HUD components by using the in-game editor and using the extended json hud file.

More than 60 components are currently customizable, with generic customization options and for some more specifics linked to styles options.

The HUD file is compatible with both 4:3 and 16:9 resolution. Position adjustment is done automatically and component aspect ratio is conserved.

The HUD view is a 640 per 480 virtual grid, rescaled horizontaly depending of aspect ratio.

Old `hud.dat` file is still compatible with new system, but the visual aspect may changes depending of the component.

New `hud.dat` file path has changed. The new storage location is under `fs_homepath` at `legacy/profiles/<name>` directory, see [Path and File Structure](https://github.com/etlegacy/etlegacy/wiki/Path-and-File-Structure#homepath---fs_homepath)

TODO: Anchor behaviour

In-game editor
^^^^^^^^^^^^^^
Overview
""""""""

The in-game editor is reachable by using the menu UI ``Menu`` -> ``Options`` -> ``View`` -> ``HUD Editor``,
or by typing in console the `edithud` command,
or by using binded `F7` key (customizable).

**Note**: The HUD editor is not available from main menu.

The HUD editor is divided in 3 different frames : 

* Rescaled in-game view 
* Customization panel on the left
* Components selection panel on the bottom

Components can be toggled visible / invisible, which allows their usage or not. An invisible component is not rendered at all and the related functionality is not called.

There are 6 pre-existing HUDs available. They can't be modified or deleted :

* ``ETmain`` (HUD 0 the default)
* ``Alternate Hud 1``
* ``Alternate Hud 2``
* ``Alternate Hud 3``
* ``Competitor Hud``
* ``Shoutcaster``

To start creating / setting a custom HUD, it is required to ``clone`` (copy) an existing HUD.

HUD view window
""""""""""""""""""""""
The rescaled HUD view allow reposionning visible elements by selecting them with left mouse buton then doing a drag & drop movement.

Drag & drop is achievable by holding left mouse buton on a component, moving the mouse cursor in the HUD view and release the left mouse butoon to the new wanted position.

On fly over a visible component with mouse cursor, a green rectangle outline the component indicating the possibility to select it. Also, a tooltip showing the component name is displayed.

Once selected, the component outline color change to yellow and it gain the focus for customization.

When 2 or more components are stacked under the same cursor position, it is possible to do multiple left clicks with the mouse to select the different components.

Components selection panel
""""""""""""""""""""""""""
The components selection panel list all the components availables for customization and allow selection of a component.
The text color may change depending of the components visibility and/or selection state :

* Yellow : The current selected component
* Green  : Visible components
* Red    : Invisible components

Settings customization panel
""""""""""""""""""""""""""""
The settings customization panel provides options to manage HUDs and customize the selected component in HUD view or component selection panel.
The panel is divided in a HUD setup area, always displayed component options and a set of tabs depending of the component type.

* HUD setup, to select and manipulate HUDs:
	- Select HUD : dropdown list of the available HUDs used to select the HUD to display/use.
		- **NOTE**: This modifies the related ``cg_altHud`` cvar.
	- Save : Save **ALL** the HUDs modifications into `hud.dat` file
	- Clone : Duplicate the selected HUD to a free HUD index and select it. It doesn't save it in `hud.dat` file.
	- Delete : Delete the selected HUD from `hud.dat` file. The selected HUD will change to the default one ``(0: ETmain)``
	- Reset Component : Reset **ALL** settings from the selected component to the default values from HUD ``(0: ETmain)``
	- Name : HUD name which can be used to select HUD with ``cg_altHud`` cvar from the name
	- Parent : HUD parent name used to default value components. If No parent is selected, the saved HUD will copy all the component values in the HUD file. The HUD becomes standalone.
		- **NOTE**: Editing a default HUD automatically clone it first, so the changes are applied to the copy.
* Position & Size, always displayed when a component is selected:
	- X : Abscissa coordinate
	- Y : Ordinate coordinate
	- W : Width
	- H : Height
	- Visible : Toggle the component visibility
	- AutoAdj : Toggle the automatic adjustment of the border position and size depending of the content
	- Background : Toggle the background visibility
	- Border : Toggle the border visibility
* The remaining options are grouped in tabs, depending of the component type:
	- ``Color`` (default tab), to colorize the component:
		- Main : Main color, see Component ``Color``
		- Second : Secondary color, see Component ``Color``
		- Backgrnd : Background color, delimited by the size of the component
		- Border : Border color, delimited by the size of the component with a width of 1px
		- R: Red color selector ranged from 0 to 255
		- G: Green color selector ranged from 0 to 255
		- B: Blue color selector ranged from 0 to 255
		- A: Alpha (aka transparency) selector ranged from 0 to 255
	- ``Style``, to customize the component specific options, see Component ``Style Name`` table.
	- ``Font``, to modify font size and style (not available for ``Bar`` components):
		- Scale : Font scale ratio, depending of original font size, where 100 is the default
		- Align : Font alignment depending of component position, see :ref:`Align Text`
		- Style : Font Style, see :ref:`Style Text`
	- ``Bar``, to customize the bar (only available for ``Bar`` components):
		- Density : Number of points used to draw the circular bar
		- Start Angle : Starting angle of the circular bar
		- End Angle : Ending angle of the circular bar
		- Thickness : Thickness of the circular bar
		- Bar Style : Bar specific options, see Component ``Bar Style`` table.
	- ``Feed``, to customize the feed timing (only available for ``Feed`` components):
		- Time : Display duration of a feed line in milliseconds
		- Stay Time : Additional display duration before the feed line fade out in milliseconds
		- Fade Time : Fade in/out duration of a feed line in milliseconds

Usage
"""""

+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Key Sequences                      | Description                                                                                                          |
+====================================+======================================================================================================================+
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
| ALT (hold) + Mouse Wheel down/up   | Resize scale/text size instead of component size                                                                     |
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
| l                                  | Toggle the layout visibility of **None** / **Visible** / **All** components (aka outline)                            |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| h                                  | Toggle the help window visibility                                                                                    |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| n                                  | Toggle the noise generator to simulate components animation                                                          |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| f                                  | Toggle the HUD editor in full screen (back to normal resolution and hiding the component and settings panels)        |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| v                                  | Toggle visibility of focused component                                                                               |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ALT (hold) + SHIFT (hold) + v      | Sets all components visible                                                                                          |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| a                                  | Toggle the force alignment of component position on the grid when displayed                                          |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| o                                  | Toggle the micro grid visibility                                                                                     |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| c                                  | Toggle the grid visibility to different levels from None / Major / Major + Minor / Major + Minor + Rectangle Centered|
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| d                                  | Toggle the grid scaling to different levels of precision .25 / .125 / .1 (see Scale Table below)                     |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| t                                  | Toggle showing only the focused component                                                                            |
+------------------------------------+----------------------------------------------------------------------------------------------------------------------+

Scale Table
"""""""""""

+-----------+--------------------+---------------------+---------------------+------------------------------------------------------------------------------+
| Grid      | .25 / tick (1:4)   | .125 / tick (1:8)   | .1 / tick (1:10)    | Tickness (px)                                                                |
+===========+====================+=====================+=====================+==============================================================================+
| Major     | 25 %               | 12.5%               | 10%                 | 0.5px                                                                        |
+-----------+--------------------+---------------------+---------------------+------------------------------------------------------------------------------+
| Minor     | 12.5%              | 6.25%               | 5%                  | 0.25px                                                                       |
+-----------+--------------------+---------------------+---------------------+------------------------------------------------------------------------------+
| Rectangle | 25%                | 12.5 / 25 / 37.5%   | 10 / 20 / 30 / 40%  | 1.25px                                                                       |
+-----------+--------------------+---------------------+---------------------+------------------------------------------------------------------------------+
| Micro     | 6.25%              | 1,5625%             | 1%                  | 0.1px                                                                        |
+-----------+--------------------+---------------------+---------------------+------------------------------------------------------------------------------+

Components List
^^^^^^^^^^^^^^^

banner
""""""

:Description: The banner text displays custom messages received from the server `bp` command (Banner Print)

:Game type Availability: All

:Type: Multiline Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

breathbar
"""""""""

:Description: The breath bar indicating the remaining time to hold breath under water before starting to drown

:Game type Availability: All

:Type: Bar

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Bar color. If ``Lerp Color`` is set, used as Max value color                                                |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | Bar Min color if ``Lerp Color`` is set                                                                      |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

**Bar Style**

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Left                  | Move maximum on left. If ``Vertical`` is set, maximum is on top. Ignored if ``Center`` is set      | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Center                | The minimum start from the center of the bar and is filled to both of the opposite directions      | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Vertical              | Change the bar orientation vertically                                                              | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Alpha              | Unused                                                                                             | 8      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Bckgrnd           | Draw background color for the bar only. The color is set by ``Background Color``                   | 16     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y5                 | Avoid the 5px margin on X. Applied if ``Bar Bckgrnd`` is set                                       | 32     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y0                 | Avoid the 5px margin on X and Y. Applied if ``Bar Bckgrnd`` is set                                 | 64     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Lerp Color            | Gradient the color alpha depending of ``Main Color`` and ``Secondary Color``                       | 128    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Border            | Draw the bar border with a thickness of 2px. Overwritten if ``Border Tiny`` is set                 | 256    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Border Tiny           | Reduce the bar border thickness to 1px. Applied if ``Bar Border`` is set                           | 512    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Decor                 | Draw the decor outlining the bar                                                                   | 1024   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Icon                  | Draw the bar icon depending of ``Left`` and ``Vertical`` values set                                | 2048   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Needle                | Draw a needle on the bar indicating a secondary value (e.g. bonus health, minimum stamina)         | 4096   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Circular              | Draw the bar as a circular gauge. Configure the gauge shape with the ``Bar`` tab options           | 8192   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

breathtext
""""""""""

:Description: The breath text in "%" indicating the remaining time to hold breath under water before starting to drown

:Game type Availability: All

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Draw Suffix           | Draw the % Suffix                                                                                  | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

centerprint
"""""""""""

:Description: The center text displays custom or kill/revive messages received from the server `cp` command (Center Print)

:Game type Availability: All

:Type: Multiline Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

chat
""""

:Description: The chat feed displaying team and global chat messages with the speaker team flag

:Game type Availability: All

:Type: Feed

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Text alpha. The text is drawn white, only the alpha channel of this color is used                           |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| No Team Flag          | Toggle team flag visibility next to the chat line                                                  | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

clipbar
"""""""

:Description: The current weapon clip ammo bar. At 0, the clip is empty and a reload is needed

:Game type Availability: All

:Type: Bar

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Bar color. If ``Lerp Color`` is set, used as Max value color. Ignored if ``Dynamic Color`` is set           |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | Bar Min color if ``Lerp Color`` is set. Ignored if ``Dynamic Color`` is set                                 |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Dynamic Color         | Gradient the bar color depending of the remaining ammo in clip/reserve                             | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

**Bar Style**

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Left                  | Move maximum on left. If ``Vertical`` is set, maximum is on top. Ignored if ``Center`` is set      | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Center                | The minimum start from the center of the bar and is filled to both of the opposite directions      | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Vertical              | Change the bar orientation vertically                                                              | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Alpha              | Unused                                                                                             | 8      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Bckgrnd           | Draw background color for the bar only. The color is set by ``Background Color``                   | 16     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y5                 | Avoid the 5px margin on X. Applied if ``Bar Bckgrnd`` is set                                       | 32     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y0                 | Avoid the 5px margin on X and Y. Applied if ``Bar Bckgrnd`` is set                                 | 64     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Lerp Color            | Gradient the color alpha depending of ``Main Color`` and ``Secondary Color``                       | 128    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Border            | Draw the bar border with a thickness of 2px. Overwritten if ``Border Tiny`` is set                 | 256    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Border Tiny           | Reduce the bar border thickness to 1px. Applied if ``Bar Border`` is set                           | 512    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Decor                 | Draw the decor outlining the bar                                                                   | 1024   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Icon                  | Draw the bar icon depending of ``Left`` and ``Vertical`` values set                                | 2048   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Needle                | Draw a needle on the bar indicating a secondary value (e.g. bonus health, minimum stamina)         | 4096   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Circular              | Draw the bar as a circular gauge. Configure the gauge shape with the ``Bar`` tab options           | 8192   |
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
| Secondary Color       | N/A                                                                                                         |
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
| Point North           | Point the compass toward north instead of the player facing direction                              | 256    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Icons Inside          | Draw the objective / player icons inside the compass instead of on its border                      | 512    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Dynamic Ticks         | Draw the compass ticks dynamically depending of the map size                                       | 1024   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Dynamic Direction     | Draw the compass direction arrow dynamically depending of the map size                             | 2048   |
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
| Secondary Color       | Crosshair secondary (alternate) part                                                                        |
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

:Description: The health bar of the aimed entity, such as player, vehicles, breakable, and so on

:Game type Availability: All

:Type: Bar

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Bar color. If ``Lerp Color`` is set, used as Max value color. Ignored if ``Dynamic Color`` is set           |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | Bar Min color if ``Lerp Color`` is set. Ignored if ``Dynamic Color`` is set                                 |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Class                 | Toggle class icon visibility of targeted player                                                    | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Rank                  | Toggle rank icon visibility of targeted player                                                     | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Dynamic Color         | Gradient the bar color depending of the target HP: White (>100) yellow (>66) orange (>33) red (>0) | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

**Bar Style**

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Left                  | Move maximum on left. If ``Vertical`` is set, maximum is on top. Ignored if ``Center`` is set      | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Center                | The minimum start from the center of the bar and is filled to both of the opposite directions      | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Vertical              | Change the bar orientation vertically                                                              | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Alpha              | Unused                                                                                             | 8      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Bckgrnd           | Draw background color for the bar only. The color is set by ``Background Color``                   | 16     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y5                 | Avoid the 5px margin on X. Applied if ``Bar Bckgrnd`` is set                                       | 32     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y0                 | Avoid the 5px margin on X and Y. Applied if ``Bar Bckgrnd`` is set                                 | 64     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Lerp Color            | Gradient the color alpha depending of ``Main Color`` and ``Secondary Color``                       | 128    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Border            | Draw the bar border with a thickness of 2px. Overwritten if ``Border Tiny`` is set                 | 256    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Border Tiny           | Reduce the bar border thickness to 1px. Applied if ``Bar Border`` is set                           | 512    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Decor                 | Draw the decor outlining the bar                                                                   | 1024   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Icon                  | Draw the bar icon depending of ``Left`` and ``Vertical`` values set                                | 2048   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Needle                | Draw a needle on the bar indicating a secondary value (e.g. bonus health, minimum stamina)         | 4096   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Circular              | Draw the bar as a circular gauge. Configure the gauge shape with the ``Bar`` tab options           | 8192   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

crosshairtext
"""""""""""""

:Description: The name of the aimed entity, such as player, vehicles, breakable, and so on

:Game type Availability: All

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Full Color            | Color the targeted entity name in it custom color instead of white                                 | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Explosive Owner       | Display the team owner of deployed dynamite / landmines / satchel                                  | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

cursorhints
"""""""""""

:Description: The icon indicating interaction with a nearby entity, such as constructible, door, cabinet, and so on

:Game type Availability: All

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
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

cursorhintsbar
""""""""""""""

:Description: The bar used to display the current health / tick percentage of the aimed construction / arming / disarming target

:Game type Availability: All

:Type: Bar

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Bar alpha. The bar is drawn white, only the alpha channel of this color is used                             |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | Bar Min color if ``Lerp Color`` is set                                                                      |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

**Bar Style**

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Left                  | Move maximum on left. If ``Vertical`` is set, maximum is on top. Ignored if ``Center`` is set      | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Center                | The minimum start from the center of the bar and is filled to both of the opposite directions      | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Vertical              | Change the bar orientation vertically                                                              | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Alpha              | Unused                                                                                             | 8      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Bckgrnd           | Draw background color for the bar only. The color is set by ``Background Color``                   | 16     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y5                 | Avoid the 5px margin on X. Applied if ``Bar Bckgrnd`` is set                                       | 32     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y0                 | Avoid the 5px margin on X and Y. Applied if ``Bar Bckgrnd`` is set                                 | 64     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Lerp Color            | Gradient the color alpha depending of ``Main Color`` and ``Secondary Color``                       | 128    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Border            | Draw the bar border with a thickness of 2px. Overwritten if ``Border Tiny`` is set                 | 256    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Border Tiny           | Reduce the bar border thickness to 1px. Applied if ``Bar Border`` is set                           | 512    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Decor                 | Draw the decor outlining the bar                                                                   | 1024   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Icon                  | Draw the bar icon depending of ``Left`` and ``Vertical`` values set                                | 2048   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Needle                | Draw a needle on the bar indicating a secondary value (e.g. bonus health, minimum stamina)         | 4096   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Circular              | Draw the bar as a circular gauge. Configure the gauge shape with the ``Bar`` tab options           | 8192   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

cursorhintstext
"""""""""""""""

:Description: The text of the remaining percentage of construction / arming / disarming target. Suffixed with "%"

:Game type Availability: All

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Draw Suffix           | Draw the % Suffix                                                                                  | 1      |
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
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Details               | Print a more detailed string containing file name and size of the current demo/audio recorded      | 1      |
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
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| No Text               | Toggle string visibility "Connection Interrupted" when client lost connection to server            | 1      |
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
| Secondary Color       | Row background color                                                                                        |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Latched Class         | Draw the team mate selected class on next respawn if different from the current one                | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Header             | Toggle header visibility (frame with fireteam name)                                                | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Colorless Name        | Color player name color to white or full color                                                     | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Status Color Name     | Color player name depending of status (White: Alive / Yellow: Wounded / Red: Dead)                 | 8      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Status Color Row      | Color player row depending of his status (White: Alive / Yellow: Wounded / Red: Dead)              | 16     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Spawn Point           | Draw the spawn point number of each team mate                                                      | 32     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Spawn Point Location  | Draw the spawn point location name of each team mate                                               | 64     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Minor Spawn Point     | Also draw the minor spawn point number                                                             | 128    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Health Text           | Draw the health numeric value of each team mate                                                    | 256    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Mini Health Bar       | Draw a small health bar for each team mate                                                         | 512    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

followtext
""""""""""

:Description: The text and icon used to display the current spectated / followed player name, team and rank

:Game type Availability: All

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| No Countdown          | Hide deployment countdown                                                                          | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

fps
"""

:Description: The text indicating the number of processed frame per second by the client

:Game type Availability: All

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Draw Suffix           | Draw the FPS Suffix                                                                                | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

healthbar
"""""""""

:Description: The player health bar. At 0, the player is wounded

:Game type Availability: All

:Type: Bar

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Bar color. If ``Lerp Color`` is set, used as Max value color. Ignored if ``Dynamic Color`` is set           |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | Bar Min color if ``Lerp Color`` is set. Ignored if ``Dynamic Color`` is set                                 |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Dynamic Color         | Gradient the bar color depending of player HP: White (>100) yellow (>66) orange (>33) red (>0)     | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

**Bar Style**

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Left                  | Move maximum on left. If ``Vertical`` is set, maximum is on top. Ignored if ``Center`` is set      | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Center                | The minimum start from the center of the bar and is filled to both of the opposite directions      | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Vertical              | Change the bar orientation vertically                                                              | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Alpha              | Unused                                                                                             | 8      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Bckgrnd           | Draw background color for the bar only. The color is set by ``Background Color``                   | 16     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y5                 | Avoid the 5px margin on X. Applied if ``Bar Bckgrnd`` is set                                       | 32     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y0                 | Avoid the 5px margin on X and Y. Applied if ``Bar Bckgrnd`` is set                                 | 64     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Lerp Color            | Gradient the color alpha depending of ``Main Color`` and ``Secondary Color``                       | 128    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Border            | Draw the bar border with a thickness of 2px. Overwritten if ``Border Tiny`` is set                 | 256    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Border Tiny           | Reduce the bar border thickness to 1px. Applied if ``Bar Border`` is set                           | 512    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Decor                 | Draw the decor outlining the bar                                                                   | 1024   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Icon                  | Draw the bar icon depending of ``Left`` and ``Vertical`` values set                                | 2048   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Needle                | Draw a needle on the bar indicating a secondary value (e.g. bonus health, minimum stamina)         | 4096   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Circular              | Draw the bar as a circular gauge. Configure the gauge shape with the ``Bar`` tab options           | 8192   |
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
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Dynamic Color         | Gradient the text color depending of player HP: White (>100) yellow (>66) orange (>33) red (>0)    | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Draw Suffix           | Draw the HP Suffix                                                                                 | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

hudhead
"""""""

:Description: The head of the incarnate character. The animation depends of the player action and states

:Game type Availability: All

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

iconfeed
""""""""

:Description: The feed of kill icons indicating the latest kills (normal, self-kill and team-kill)

:Game type Availability: All

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
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
| Main Color            | Font color of the snapshot/s text                                                                           |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
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
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| No Wounded Msg        | Toggle string visibility "You are wounded and waiting for a medic"                                 | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

livesleft
"""""""""

:Description: Indicate the number of lives left. Hidden in Last Man Standing game type (LMS).

:Game type Availability: All except Last Man Standing

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
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
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Second                | Toggle seconds visibility                                                                          | 1      |
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
| Secondary Color       | N/A                                                                                                         |
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
| Secondary Color       | N/A                                                                                                         |
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
| Secondary Color       | N/A                                                                                                         |
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
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Draw Prefix           | Draw the Ping Prefix                                                                               | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

pmitemsbig
""""""""""

:Description: The text and icon indicating ranking/skill gain up

:Game type Availability: All

:Type: Feed

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| No Skill              | Filter out skill up message                                                                        | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Rank               | Filter out rank up message                                                                         | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

popupmessages
"""""""""""""

:Description: The pop-up list feed for objectives/kill/connection/dynamites/mines/constructions states or custom message.

**Note**: This component is available in 4 distinct components, allowing to display different list feeds independently.

:Game type Availability: All

:Type: Feed

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
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
| No Echo               | Filter out echo (server) messages                                                                  | 32     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Weapon Icon           | Draw weapon used to kill someone instead of a text describing the means of death                   | 64     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Alt Weap Icons        | Draw weapon icon without outline. Applied if ``Weapon Icon`` is set                                | 128    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Swap V<->K            | Swap the victim and killer name text. Applied if ``Weapon Icon`` is set                            | 256    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Force Colors          | Force the font color by using defined ``Main Color``                                               | 512    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Scroll Down           | Toggle pop-up appearance beginning from Up or Bottom                                               | 1024   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Announce           | Filter out announcement messages                                                                   | 2048   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Enemy Team         | Filter out enemy team messages                                                                     | 4096   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Own Team           | Filter out own team messages                                                                       | 8192   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Self               | Filter out messages about the player itself                                                        | 16384  |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Suicide            | Filter out suicide messages                                                                        | 32768  |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

powerups
""""""""

:Description: The icon indicating player invulnerability, under adrenaline, disguised or carrying objective

:Game type Availability: All

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

ranktext
""""""""

:Description: The player rank mini name (Trigram) depending of the team (Axis / Allies)

:Game type Availability: All except Last Man Standing

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
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
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Double Digits         | Display the timer with double digits (e.g. 05 instead of 5)                                        | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Reinforce Warning     | Blink the timer when the reinforcement warning time is reached                                     | 2      |
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
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Simple                | Don't show reinforcement and enemy spawn timer next to round timer                                 | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Double Digits         | Display the timer with double digits (e.g. 05 instead of 5)                                        | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Reinforce Warning     | Blink the timer when the reinforcement warning time is reached                                     | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

scPlayerListAllies
""""""""""""""""""

:Description: The list containing allies player status, used in shoutcaster mode to display up to 6 allies players

:Game type Availability: Shoutcaster only

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | Health bar color                                                                                            |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

scPlayerListAxis
""""""""""""""""

:Description: The list containing axis player status, used in shoutcaster mode to display up to 6 axis players

:Game type Availability: Shoutcaster only

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | Health bar color                                                                                            |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

scTeamNamesAllies
"""""""""""""""""

:Description: The banner text containing custom name for allies team

:Game type Availability: Shoutcaster only

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | Font shadow color                                                                                           |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Show Score            | Show the team score next to the team name                                                          | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Swap Score            | Swap the team name and score position                                                              | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

scTeamNamesAxis
"""""""""""""""

:Description: The banner text containing custom name for axis team

:Game type Availability: Shoutcaster only

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | Font shadow color                                                                                           |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Show Score            | Show the team score next to the team name                                                          | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Swap Score            | Swap the team name and score position                                                              | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

snapshot
""""""""

:Description: Debug information indicating server time, last snapshot number and number of server command received

:Game type Availability: All

:Type: Multiline Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
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
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Double Digits         | Display the timer with double digits (e.g. 05 instead of 5)                                        | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

spectatorstatus
"""""""""""""""

:Description: The text indicating if player is in spectator/freecam/weaponcam mode

:Game type Availability: All

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

spectatortext
"""""""""""""

:Description: The text indicating instructions for opening limbo/multiview or key usage for following players

:Game type Availability: All

:Type: Multiline Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

speed
"""""

:Description: The player speed movement expressed in Unit / Metric / Imperial unit per second. Suffixed UPS / KPS / MPS

:Game type Availability: All

:Type: Multiline Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Max Speed             | Show maximum reached speed visibility                                                              | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Draw Suffix           | Draw the speed unit suffix (UPS / KPH / MPH)                                                       | 2      |
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
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Draw Suffix           | Draw the % Suffix                                                                                  | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

staminabar
""""""""""

:Description: The endurance bar indicating the remaining sprint availability. Also drained by jump

:Game type Availability: All

:Type: Bar

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Bar color. If ``Lerp Color`` is set, used as Max value color                                                |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | Bar Min color if ``Lerp Color`` is set                                                                      |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Empty Warning         | Color the stamina bar icon in orange when the player has no stamina left (can't sprint)            | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

**Bar Style**

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Left                  | Move maximum on left. If ``Vertical`` is set, maximum is on top. Ignored if ``Center`` is set      | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Center                | The minimum start from the center of the bar and is filled to both of the opposite directions      | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Vertical              | Change the bar orientation vertically                                                              | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Alpha              | Unused                                                                                             | 8      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Bckgrnd           | Draw background color for the bar only. The color is set by ``Background Color``                   | 16     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y5                 | Avoid the 5px margin on X. Applied if ``Bar Bckgrnd`` is set                                       | 32     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y0                 | Avoid the 5px margin on X and Y. Applied if ``Bar Bckgrnd`` is set                                 | 64     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Lerp Color            | Gradient the color alpha depending of ``Main Color`` and ``Secondary Color``                       | 128    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Border            | Draw the bar border with a thickness of 2px. Overwritten if ``Border Tiny`` is set                 | 256    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Border Tiny           | Reduce the bar border thickness to 1px. Applied if ``Bar Border`` is set                           | 512    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Decor                 | Draw the decor outlining the bar                                                                   | 1024   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Icon                  | Draw the bar icon depending of ``Left`` and ``Vertical`` values set                                | 2048   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Needle                | Draw a needle on the bar indicating a secondary value (e.g. bonus health, minimum stamina)         | 4096   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Circular              | Draw the bar as a circular gauge. Configure the gauge shape with the ``Bar`` tab options           | 8192   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

stats
"""""

:Description: Banner displaying player stats (Kill, Death, Self Kill, Damage Given, Damage received) and status

:Game type Availability: Demo replay and Shoutcaster

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | Health bar color                                                                                            |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

statsdisplay
""""""""""""

:Description: The skill level for current class, battle sense and light (heavy for tank and nested-MG) weapon skill

:Game type Availability: All except Last Man Standing

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Skill level number color                                                                                    |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
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
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Complaint             | Toggle complaint proposal text visibility on player getting team killed                            | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

warmuptext
""""""""""

:Description: The warmup status text indicating the current loaded server configuration and actions to do before the match begins

:Game type Availability: All

:Type: Multiline Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

warmuptitle
"""""""""""

:Description: The warmup countdown or status before the match begins

:Game type Availability: All

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
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
| Secondary Color       | N/A                                                                                                         |
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
| Main Color            | Bar color. If ``Lerp Color`` is set, used as Max value color                                                |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | Bar Min color if ``Lerp Color`` is set                                                                      |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

**Bar Style**

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Left                  | Move maximum on left. If ``Vertical`` is set, maximum is on top. Ignored if ``Center`` is set      | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Center                | The minimum start from the center of the bar and is filled to both of the opposite directions      | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Vertical              | Change the bar orientation vertically                                                              | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Alpha              | Unused                                                                                             | 8      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Bckgrnd           | Draw background color for the bar only. The color is set by ``Background Color``                   | 16     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y5                 | Avoid the 5px margin on X. Applied if ``Bar Bckgrnd`` is set                                       | 32     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y0                 | Avoid the 5px margin on X and Y. Applied if ``Bar Bckgrnd`` is set                                 | 64     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Lerp Color            | Gradient the color alpha depending of ``Main Color`` and ``Secondary Color``                       | 128    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Border            | Draw the bar border with a thickness of 2px. Overwritten if ``Border Tiny`` is set                 | 256    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Border Tiny           | Reduce the bar border thickness to 1px. Applied if ``Bar Border`` is set                           | 512    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Decor                 | Draw the decor outlining the bar                                                                   | 1024   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Icon                  | Draw the bar icon depending of ``Left`` and ``Vertical`` values set                                | 2048   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Needle                | Draw a needle on the bar indicating a secondary value (e.g. bonus health, minimum stamina)         | 4096   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Circular              | Draw the bar as a circular gauge. Configure the gauge shape with the ``Bar`` tab options           | 8192   |
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
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Draw Suffix           | Draw the % Suffix                                                                                  | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

weaponheatbar
"""""""""""""

:Description: The current weapon heat bar, accumulating while firing. At maximum, the weapon overheats

:Game type Availability: All

:Type: Bar

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Bar color. If ``Lerp Color`` is set, used as Min value color                                                |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | Bar Max color if ``Lerp Color`` is set                                                                      |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| N/A                   | N/A                                                                                                | N/A    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

**Bar Style**

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Left                  | Move maximum on left. If ``Vertical`` is set, maximum is on top. Ignored if ``Center`` is set      | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Center                | The minimum start from the center of the bar and is filled to both of the opposite directions      | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Vertical              | Change the bar orientation vertically                                                              | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Alpha              | Unused                                                                                             | 8      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Bckgrnd           | Draw background color for the bar only. The color is set by ``Background Color``                   | 16     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y5                 | Avoid the 5px margin on X. Applied if ``Bar Bckgrnd`` is set                                       | 32     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y0                 | Avoid the 5px margin on X and Y. Applied if ``Bar Bckgrnd`` is set                                 | 64     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Lerp Color            | Gradient the color alpha depending of ``Main Color`` and ``Secondary Color``                       | 128    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Border            | Draw the bar border with a thickness of 2px. Overwritten if ``Border Tiny`` is set                 | 256    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Border Tiny           | Reduce the bar border thickness to 1px. Applied if ``Bar Border`` is set                           | 512    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Decor                 | Draw the decor outlining the bar                                                                   | 1024   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Icon                  | Draw the bar icon depending of ``Left`` and ``Vertical`` values set                                | 2048   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Needle                | Draw a needle on the bar indicating a secondary value (e.g. bonus health, minimum stamina)         | 4096   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Circular              | Draw the bar as a circular gauge. Configure the gauge shape with the ``Bar`` tab options           | 8192   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

weaponicon
""""""""""

:Description: The icon of the current selected (in hand) weapon

:Game type Availability: All

:Type: Specific

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Icon color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Icon Flash            | Highlight the weapon icon in yellow while switching/reloading and in red while firing              | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Only Ticking          | Only draw the weapon icon while a grenade is ticking                                               | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

weaponstability
"""""""""""""""

:Description: The stability bar indicating the current aim spread applied to the weapon (from 0 to 255)

:Game type Availability: All

:Type: Bar

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | N/A (bar color is fixed: green when stable, red when unstable)                                              |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Always                | Draw the bar even if the weapon is not a scoped weapon                                             | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

**Bar Style**

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Left                  | Move maximum on left. If ``Vertical`` is set, maximum is on top. Ignored if ``Center`` is set      | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Center                | The minimum start from the center of the bar and is filled to both of the opposite directions      | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Vertical              | Change the bar orientation vertically                                                              | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Alpha              | Unused                                                                                             | 8      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Bckgrnd           | Draw background color for the bar only. The color is set by ``Background Color``                   | 16     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y5                 | Avoid the 5px margin on X. Applied if ``Bar Bckgrnd`` is set                                       | 32     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| X0 Y0                 | Avoid the 5px margin on X and Y. Applied if ``Bar Bckgrnd`` is set                                 | 64     |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Lerp Color            | Gradient the color alpha depending of ``Main Color`` and ``Secondary Color``                       | 128    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Bar Border            | Draw the bar border with a thickness of 2px. Overwritten if ``Border Tiny`` is set                 | 256    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Border Tiny           | Reduce the bar border thickness to 1px. Applied if ``Bar Border`` is set                           | 512    |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Decor                 | Draw the decor outlining the bar                                                                   | 1024   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Icon                  | Draw the bar icon depending of ``Left`` and ``Vertical`` values set                                | 2048   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Needle                | Draw a needle on the bar indicating a secondary value (e.g. bonus health, minimum stamina)         | 4096   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Circular              | Draw the bar as a circular gauge. Configure the gauge shape with the ``Bar`` tab options           | 8192   |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

xpgain
""""""

:Description: The gained player experience pop-up.

:Game type Availability: All

:Type: Feed

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | XP number color                                                                                             |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | XP reason text color                                                                                        |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Scroll Down           | Toggle pop-up appearance beginning from Up or Bottom                                               | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Reason             | Toggle XP gain message visibility and draw skill icon + gain only                                  | 2      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No Stack              | Don't merge message (expect for construction / repairing)                                          | 4      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| No XP Add up          | Don't merge XP gain values for same message (expect for construction / repairing)                  | 8      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

xptext
""""""

:Description: The total player experience numeric value. Suffixed with "XP"

:Game type Availability: All except Last Man Standing

:Type: Text

+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Color                 | Description                                                                                                 |
+=======================+=============================================================================================================+
| Main Color            | Font color                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------+
| Secondary Color       | N/A                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------+

+-----------------------+----------------------------------------------------------------------------------------------------+--------+
| Style Name            | Description                                                                                        | Values |
+=======================+====================================================================================================+========+
| Draw Suffix           | Draw the XP Suffix                                                                                 | 1      |
+-----------------------+----------------------------------------------------------------------------------------------------+--------+

Annexe
^^^^^^

Options list
""""""""""""
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| Options               | Description                                                                    | Range                                           |
+=======================+================================================================================+=================================================+
| location              | Rect location, set the 4 coordinates at once                                   | ``<x> <y> <w> <h>``                             |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| x                     | X coordinate                                                                   | 0 - 640 (visible grid limit, can be out ranged) |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| y                     | Y coordinate                                                                   | 0 - 480 (visible grid limit, can be out ranged) |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| w                     | Component Width                                                                | 0 - 640 (visible grid limit, can be out ranged) |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| h                     | Component Height                                                               | 0 - 480 (visible grid limit, can be out ranged) |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| position              | Position preset name or coordinates                                            | Preset name or ``<x> <y>``                      |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| size                  | Component size, set width and height at once                                   | ``<w> <h>``                                     |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| visible               | Toggle component visibility                                                    | 0 - 1 (boolean)                                 |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| style                 | Customize component specific options (if available)                            | See Component ``Style Name``                    |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| scale                 | Change font scale where 100 is the default value (normalized)                  | 0 - 300 (recommended range, can be out ranged)  |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| colorMain             | Change either the font color (text) or main component color                    | See :ref:`Color Usage`                          |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| colorSecondary        | Change secondary component color                                               | See :ref:`Color Usage`                          |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| showBackGround        | Toggle background visibility                                                   | 0 - 1 (boolean)                                 |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| colorBackground       | Change the component background color                                          | See :ref:`Color Usage`                          |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| showBorder            | Toggle border visibility                                                       | 0 - 1 (boolean)                                 |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| colorBorder           | Change the component border color                                              | See :ref:`Color Usage`                          |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| styleText             | Customize font style aspect (text component only)                              | See :ref:`Style Text`                           |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| alignText             | Customize font alignment position (text component only)                        | See :ref:`Align Text`                           |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| autoAdjust            | Adjust border and background size to component content                         | 0 - 1 (boolean)                                 |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| internalLocation      | Internal rect location, set the 4 coordinates at once                          | ``<x> <y> <w> <h>``                             |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| internalPosition      | Internal rect position, set X and Y at once                                    | ``<x> <y>``                                     |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| anchorPoint           | Component anchor point                                                         | 0 - 8 (see Anchor Point)                        |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| parentAnchorPoint     | Parent component anchor point                                                  | 0 - 8 (see Anchor Point)                        |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| parentAnchorComponent | Parent component name or ``null``                                              | Component name                                  |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| barStyle              | Customize the bar options (bar component only)                                 | See Component ``Bar Style``                     |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| circleDensityPoint    | Number of points used to draw the circular bar                                 | 0 - 2                                           |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| circleStartAngle      | Starting angle of the circular bar                                             | 0 - 360                                         |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| circleEndAngle        | Ending angle of the circular bar                                               | 0 - 360                                         |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| circleThickness       | Thickness of the circular bar                                                  | 0 - 8                                           |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| feedTime              | Display duration of a feed line in milliseconds                                | 0 - 6000                                        |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| feedStayTime          | Additional display duration before the feed line fade out                      | 0 - 6000                                        |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
| feedFadeTime          | Fade in/out duration of a feed line in milliseconds                            | 0 - 6000                                        |
+-----------------------+--------------------------------------------------------------------------------+-------------------------------------------------+
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
| Shadowed          | Shadow the text by printing a bottom offsetted extra black character behind the initial text                               | 3       |
+-------------------+----------------------------------------------------------------------------------------------------------------------------+---------+
| Outlined          | Outline the text by printing a top offsetted extra colored character in front the initial text                             | 4       |
+-------------------+----------------------------------------------------------------------------------------------------------------------------+---------+
| Outlined Shadowed | Outline and Shadow the text                                                                                                | 5       |
+-------------------+----------------------------------------------------------------------------------------------------------------------------+---------+
| Shadowed More     | Bold more the shadow effect                                                                                                | 6       |
+-------------------+----------------------------------------------------------------------------------------------------------------------------+---------+

Align Text
""""""""""""""

Elements contained in component are aligned horizontaly regarding the component size bound:

+---------+--------------------------------------------------------------------------------------------------------------------------------------+---------+
| Name    | Description                                                                                                                          | Values  |
+=========+======================================================================================================================================+=========+
| Left    | Align / start drawing elements in component to the left side                                                                         | 0       |
+---------+--------------------------------------------------------------------------------------------------------------------------------------+---------+
| Center  | Center elements in component and keep equal margin on the left and on the right of the elements                                      | 1       |
+---------+--------------------------------------------------------------------------------------------------------------------------------------+---------+
| Right   | Align / end drawing elements in component to the right side                                                                          | 2       |
+---------+--------------------------------------------------------------------------------------------------------------------------------------+---------+
| Center2 | Center elements in component, align element in left justify adjusted to the longest elements and keep equal margin on left and right | 3       |
+---------+--------------------------------------------------------------------------------------------------------------------------------------+---------+

