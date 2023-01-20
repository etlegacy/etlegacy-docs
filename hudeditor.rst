===================
HUD Editor
===================

Introduction
^^^^^^^^^^^^
Since the 2.81.0, ET:Legacy introduced a new way to fully customize all HUD components by using the in-game editor and using the extended json hud file.

50 components are currently customizable,

In-game editor
^^^^^^^^^^^^^^
Overview
""""""""

The in-game editor is reachable by using the menu UI ``Menu`` -> ``Options`` -> ``View`` -> ``HUD Editor`` or by typing in console the edithud command.

**Note**: The HUD editor is not available from main menu.

HUD view window
"""""""""""""""

Components selection panel
""""""""""""""""""""""""""

Parameters customization panel
""""""""""""""""""""""""""""""

Usage
"""""

New hud.dat json file
^^^^^^^^^^^^^^^^^^^^^

Overview
""""""""

Usage
"""""

Annexe
^^^^^^

Components list
"""""""""""""""

::

    crosshair
    compass
    staminabar
    breathbar
    healthbar
    weaponchargebar
    healthtext
    xptext
    ranktext
    statsdisplay
    weaponicon
    weaponammo
    fireteam
    popupmessages
    powerups
    objectives
    hudhead
    cursorhints
    weaponstability
    livesleft
    roundtimer
    reinforcement
    spawntimer
    localtime
    votetext
    spectatortext
    limbotext
    followtext
    demotext
    missilecamera
    sprinttext
    breathtext
    weaponchargetext)
    fps
    snapshot
    ping
    speed
    lagometer
    disconnect
    chat
    spectatorstatus
    pmitemsbig
    warmuptitle
    warmuptext
    objectivetext
    centerprint
    banner
    crosshairtext
    crosshairbar
    stats

Parameters list
"""""""""""""""

+--------------------+-----------------------------------------+--------------------------------------+
| Parameter          | 	Description                            | Range                                |
+====================+=========================================+======================================+
| X 	             | X coordinate                            |                                      |
+--------------------+-----------------------------------------+--------------------------------------+
| W 	             | Component Width                         |                                      |
+--------------------+-----------------------------------------+--------------------------------------+
| H 	             | Component Height                        |                                      |
+--------------------+-----------------------------------------+--------------------------------------+
| visible            |                                         |                                      |
+--------------------+-----------------------------------------+--------------------------------------+
| style              |                                         | See Style Section                    |
+--------------------+-----------------------------------------+--------------------------------------+
| scale              |                                         |                                      |
+--------------------+-----------------------------------------+--------------------------------------+
| ColorMain          |                                         |                                      |
+--------------------+-----------------------------------------+--------------------------------------+
| colorSecondary     |                                         |                                      |
+--------------------+-----------------------------------------+--------------------------------------+
| showBackGround     |                                         |                                      |
+--------------------+-----------------------------------------+--------------------------------------+
| colorBackground    |                                         |                                      |
+--------------------+-----------------------------------------+--------------------------------------+
| showBorder         |                                         |                                      |
+--------------------+-----------------------------------------+--------------------------------------+
| colorBorder        |                                         |                                      |
+--------------------+-----------------------------------------+--------------------------------------+
| styleText          |                                         |                                      |
+--------------------+-----------------------------------------+--------------------------------------+
| alignText          |                                         |                                      |
+--------------------+-----------------------------------------+--------------------------------------+
| autoAdjust         |                                         |                                      |
+--------------------+-----------------------------------------+--------------------------------------+
| styleText          |                                         |                                      |
+--------------------+-----------------------------------------+--------------------------------------+


Component Style
"""""""""""""""