===================
List of Vsays
===================

.. _vsays:

Voice Chat
^^^^^^^^^^^

Enemy Territory: Legacy ships with a set of pre-recorded voice messages that can be
sent to the other players with the ``vsay`` console commands. The messages are
defined by the scripts ``etmain/scripts/wm_axis_chat.voice`` and
``etmain/scripts/wm_allies_chat.voice``, and the client picks the file matching the
team of the speaker: the axis team uses ``wm_axis_chat.voice`` while the allies
team uses ``wm_allies_chat.voice``.

Most of the messages are reachable from the quick message menu, opened with the
``mp_QuickMessage`` command or with the *Quick Message* entry of the main menu. Each
menu item sends one of the following commands:

+-----------------------+--------------------------------------------------+
| **Command**           | **Effect**                                       |
+=======================+==================================================+
| ``VoiceChat``         | Sends the message to every player                |
+-----------------------+--------------------------------------------------+
| ``VoiceTeamChat``     | Sends the message to the team of the speaker     |
+-----------------------+--------------------------------------------------+
| ``VoiceFireteamChat`` | Sends the message to the fireteam of the speaker |
+-----------------------+--------------------------------------------------+

.. note::
   A message can have several voice variants. They are picked randomly, and each
   of them can have its own text, as shown in the table below.

.. contents:: `Table of contents`
   :depth: 2
   :local:

Voice Chat Commands
--------------------

The commands below are the ones sent by the quick message menu. The **Fireteam**
overlay and the class announcements of the *Function* menu item are listed too.

.. list-table::
   :header-rows: 1
   :widths: 16 20 12 26 26

   * - **Command**
     - **Text**
     - **Icon**
     - **Axis voice**
     - **Allies voice**
   * - ``PathCleared``
     - Path cleared.
     - n/a
     - ``sound/chat/axis/11a.wav``, ``sound/chat/axis/11b.wav``
     - ``sound/chat/allies/11a.wav``, ``sound/chat/allies/11b.wav``
   * - ``EnemyWeak``
     - The enemy is weakened.
     - n/a
     - ``sound/chat/axis/12a.wav``, ``sound/chat/axis/12b.wav``
     - ``sound/chat/allies/12a.wav``, ``sound/chat/allies/12b.wav``
   * - ``AllClear``
     - All clear.
     - n/a
     - ``sound/chat/axis/13a.wav``, ``sound/chat/axis/13b.wav``
     - ``sound/chat/allies/13a.wav``, ``sound/chat/allies/13b.wav``
   * - ``Incoming``
     - Incoming!
     - n/a
     - ``sound/chat/axis/14a.wav``, ``sound/chat/axis/14b.wav``
     - ``sound/chat/allies/14a.wav``, ``sound/chat/allies/14b.wav``
   * - ``FireInTheHole``
     - Fire in the hole!
     - ``sprites/voicechat_orange``
     - ``sound/chat/axis/15a.wav``, ``sound/chat/axis/15b.wav``
     - ``sound/chat/allies/15a.wav``, ``sound/chat/allies/15b.wav``
   * - ``OnDefense``
     - I'm on defense.
     - n/a
     - ``sound/chat/axis/16a.wav``, ``sound/chat/axis/16b.wav``
     - ``sound/chat/allies/16a.wav``, ``sound/chat/allies/16b.wav``
   * - ``OnOffense``
     - I'm on offense.
     - n/a
     - ``sound/chat/axis/17a.wav``, ``sound/chat/axis/17b.wav``
     - ``sound/chat/allies/17a.wav``, ``sound/chat/allies/17b.wav``
   * - ``MinesCleared``
     - Mines cleared.
     - n/a
     - ``sound/chat/axis/19a.wav``, ``sound/chat/axis/19b.wav``
     - ``sound/chat/allies/19a.wav``, ``sound/chat/allies/19b.wav``
   * - ``EnemyDisguised``
     - Enemy in disguise.
     - n/a
     - ``sound/chat/axis/10a.wav``, ``sound/chat/axis/10b.wav``
     - ``sound/chat/allies/10a.wav``, ``sound/chat/allies/10b.wav``
   * - ``Medic``
     - Need a Medic!
     - ``sprites/voiceMedic``
     - ``sound/chat/axis/21a.wav``, ``sound/chat/axis/21b.wav``
     - ``sound/chat/allies/21a.wav``, ``sound/chat/allies/21b.wav``
   * - ``NeedAmmo``
     - I need ammo!
     - ``sprites/voiceAmmo``
     - ``sound/chat/axis/22a.wav``
     - ``sound/chat/allies/22a.wav``
   * - ``NeedBackup``
     - I need backup!
     - n/a
     - ``sound/chat/axis/23a.wav``, ``sound/chat/axis/23b.wav``
     - ``sound/chat/allies/23a.wav``, ``sound/chat/allies/23b.wav``
   * - ``NeedEngineer``
     - We need an engineer!
     - n/a
     - ``sound/chat/axis/24a.wav``, ``sound/chat/axis/24b.wav``
     - ``sound/chat/allies/24a.wav``, ``sound/chat/allies/24b.wav``
   * - ``CoverMe``
     - Need covering fire!, Cover me!
     - n/a
     - ``sound/chat/axis/25a.wav``, ``sound/chat/axis/25b.wav``, ``sound/chat/axis/25c.wav``, ``sound/chat/axis/25d.wav``
     - ``sound/chat/allies/25a.wav``, ``sound/chat/allies/25b.wav``, ``sound/chat/allies/25c.wav``, ``sound/chat/allies/25d.wav``
   * - ``HoldFire``
     - Hold your fire!
     - ``gfx/2d/friendlycross``
     - ``sound/chat/axis/26a.wav``, ``sound/chat/axis/26b.wav``
     - ``sound/chat/allies/26a.wav``, ``sound/chat/allies/26b.wav``
   * - ``WhereTo``
     - Where to?
     - n/a
     - ``sound/chat/axis/27a.wav``, ``sound/chat/axis/27b.wav``
     - ``sound/chat/allies/27a.wav``, ``sound/chat/allies/27b.wav``
   * - ``NeedOps``
     - We need Covert Ops!
     - n/a
     - ``sound/chat/axis/28a.wav``, ``sound/chat/axis/28b.wav``
     - ``sound/chat/allies/28a.wav``, ``sound/chat/allies/28b.wav``
   * - ``FollowMe``
     - Follow me!
     - n/a
     - ``sound/chat/axis/31a.wav``, ``sound/chat/axis/31b.wav``
     - ``sound/chat/allies/31a.wav``, ``sound/chat/allies/31b.wav``
   * - ``LetsGo``
     - Let's go!
     - n/a
     - ``sound/chat/axis/32a.wav``, ``sound/chat/axis/32b.wav``
     - ``sound/chat/allies/32a.wav``, ``sound/chat/allies/32b.wav``
   * - ``Move``
     - Move!
     - n/a
     - ``sound/chat/axis/33a.wav``, ``sound/chat/axis/33b.wav``
     - ``sound/chat/allies/33a.wav``, ``sound/chat/allies/33b.wav``
   * - ``ClearPath``
     - Clear the path!
     - n/a
     - ``sound/chat/axis/34a.wav``, ``sound/chat/axis/34b.wav``
     - ``sound/chat/allies/34a.wav``, ``sound/chat/allies/34b.wav``
   * - ``DefendObjective``
     - Defend our objective!
     - n/a
     - ``sound/chat/axis/35a.wav``, ``sound/chat/axis/35b.wav``
     - ``sound/chat/allies/35a.wav``, ``sound/chat/allies/35b.wav``
   * - ``DisarmDynamite``
     - Disarm the dynamite!
     - n/a
     - ``sound/chat/axis/36a.wav``, ``sound/chat/axis/36b.wav``
     - ``sound/chat/allies/36a.wav``, ``sound/chat/allies/36b.wav``
   * - ``ClearMines``
     - Clear the mines!
     - n/a
     - ``sound/chat/axis/37a.wav``, ``sound/chat/axis/37b.wav``
     - ``sound/chat/allies/37a.wav``, ``sound/chat/allies/37b.wav``
   * - ``ReinforceOffense``
     - Reinforce the offense!
     - n/a
     - ``sound/chat/axis/39a.wav``, ``sound/chat/axis/39b.wav``
     - ``sound/chat/allies/39a.wav``, ``sound/chat/allies/39b.wav``
   * - ``ReinforceDefense``
     - Reinforce the defense!
     - n/a
     - ``sound/chat/axis/38a.wav``, ``sound/chat/axis/38b.wav``
     - ``sound/chat/allies/38a.wav``, ``sound/chat/allies/38b.wav``
   * - ``Affirmative``
     - Ja!, Jawohl!, Affirmative!!
     - ``sprites/greentick``
     - ``sound/chat/axis/41a.wav``, ``sound/chat/axis/41b.wav``, ``sound/chat/axis/41c.wav``
     - ``sound/chat/allies/41a.wav``, ``sound/chat/allies/41b.wav``, ``sound/chat/allies/41c.wav``
   * - ``Negative``
     - Negative!, Nein!
     - ``sprites/redcross``
     - ``sound/chat/axis/42a.wav``, ``sound/chat/axis/42b.wav``, ``sound/chat/axis/42c.wav``
     - ``sound/chat/allies/42a.wav``, ``sound/chat/allies/42b.wav``, ``sound/chat/allies/42c.wav``, ``sound/chat/allies/42d.wav``
   * - ``Thanks``
     - Danke!, Danke sehr!
     - n/a
     - ``sound/chat/axis/43a.wav``, ``sound/chat/axis/43b.wav``, ``sound/chat/axis/43c.wav``
     - ``sound/chat/allies/43a.wav``, ``sound/chat/allies/43b.wav``, ``sound/chat/allies/43c.wav``, ``sound/chat/allies/43d.wav``
   * - ``Welcome``
     - You're welcome., Bitte sehr., Kein problem.
     - n/a
     - ``sound/chat/axis/44a.wav``, ``sound/chat/axis/44b.wav``, ``sound/chat/axis/44c.wav``
     - ``sound/chat/allies/44a.wav``, ``sound/chat/allies/44b.wav``, ``sound/chat/allies/44c.wav``, ``sound/chat/allies/44d.wav``
   * - ``Sorry``
     - Sorry!
     - n/a
     - ``sound/chat/axis/45a.wav``, ``sound/chat/axis/45b.wav``
     - ``sound/chat/allies/45a.wav``, ``sound/chat/allies/45b.wav``, ``sound/chat/allies/45c.wav``
   * - ``Oops``
     - Oops!
     - n/a
     - ``sound/chat/axis/46a.wav``, ``sound/chat/axis/46b.wav``
     - ``sound/chat/allies/46a.wav``, ``sound/chat/allies/46b.wav``, ``sound/chat/allies/46c.wav``
   * - ``Hi``
     - Hallo!
     - n/a
     - ``sound/chat/axis/54a.wav``, ``sound/chat/axis/54b.wav``, ``sound/chat/axis/54c.wav``
     - ``sound/chat/allies/54a.wav``, ``sound/chat/allies/54b.wav``, ``sound/chat/allies/54c.wav``, ``sound/chat/allies/54d.wav``, ``sound/chat/allies/54e.wav``
   * - ``Bye``
     - Auf wiedersehen.
     - n/a
     - ``sound/chat/axis/55a.wav``, ``sound/chat/axis/55b.wav``, ``sound/chat/axis/55c.wav``
     - ``sound/chat/allies/55a.wav``, ``sound/chat/allies/55b.wav``, ``sound/chat/allies/55c.wav``, ``sound/chat/allies/55d.wav``, ``sound/chat/allies/55e.wav``
   * - ``GreatShot``
     - Great shot!
     - n/a
     - ``sound/chat/axis/56a.wav``, ``sound/chat/axis/56b.wav``
     - ``sound/chat/allies/56a.wav``, ``sound/chat/allies/56b.wav``
   * - ``Cheer``
     - Oh yes!, Wunderbar!, Excellent!, Jahaa!, Sehr gut!
     - n/a
     - ``sound/chat/axis/57a.wav``, ``sound/chat/axis/57b.wav``, ``sound/chat/axis/57c.wav``, ``sound/chat/axis/57d.wav``, ``sound/chat/axis/57e.wav``, ``sound/chat/axis/57f.wav``, ``sound/chat/axis/57g.wav``, ``sound/chat/axis/57h.wav``
     - ``sound/chat/allies/57a.wav``, ``sound/chat/allies/57b.wav``, ``sound/chat/allies/57c.wav``, ``sound/chat/allies/57d.wav``, ``sound/chat/allies/57e.wav``, ``sound/chat/allies/57f.wav``, ``sound/chat/allies/57g.wav``, ``sound/chat/allies/57h.wav``, ``sound/chat/allies/57i.wav``, ``sound/chat/allies/57j.wav``, ``sound/chat/allies/57k.wav``, ``sound/chat/allies/57l.wav``
   * - ``GoodGame``
     - Good game!
     - n/a
     - ``sound/chat/axis/586a.wav``, ``sound/chat/axis/586b.wav``
     - ``sound/chat/allies/586a.wav``, ``sound/chat/allies/586b.wav``, ``sound/chat/allies/586c.wav``
   * - ``CommandAcknowledged``
     - Command acknowledged!
     - n/a
     - ``sound/chat/axis/81a.wav``, ``sound/chat/axis/81b.wav``
     - ``sound/chat/allies/81a.wav``, ``sound/chat/allies/81b.wav``, ``sound/chat/allies/81c.wav``, ``sound/chat/allies/81d.wav``
   * - ``CommandDeclined``
     - Command declined!
     - n/a
     - ``sound/chat/axis/82a.wav``, ``sound/chat/axis/82b.wav``
     - ``sound/chat/allies/82a.wav``, ``sound/chat/allies/82b.wav``, ``sound/chat/allies/82c.wav``, ``sound/chat/allies/82d.wav``
   * - ``CommandCompleted``
     - Command completed!
     - n/a
     - ``sound/chat/axis/83a.wav``, ``sound/chat/axis/83b.wav``
     - ``sound/chat/allies/83a.wav``, ``sound/chat/allies/83b.wav``
   * - ``DestroyPrimary``
     - Destroy primary objective!
     - n/a
     - ``sound/chat/axis/71a.wav``, ``sound/chat/axis/71b.wav``
     - ``sound/chat/allies/71a.wav``, ``sound/chat/allies/71b.wav``
   * - ``DestroySecondary``
     - Destroy secondary objective!
     - n/a
     - ``sound/chat/axis/72a.wav``, ``sound/chat/axis/72b.wav``
     - ``sound/chat/allies/72a.wav``, ``sound/chat/allies/72b.wav``
   * - ``DestroyConstruction``
     - Destroy construction!
     - n/a
     - ``sound/chat/axis/73a.wav``, ``sound/chat/axis/73b.wav``
     - ``sound/chat/allies/73a.wav``, ``sound/chat/allies/73b.wav``
   * - ``ConstructionCommencing``
     - I'm constructing!
     - n/a
     - ``sound/chat/axis/84a.wav``, ``sound/chat/axis/84b.wav``
     - ``sound/chat/allies/84a.wav``, ``sound/chat/allies/84b.wav``
   * - ``RepairVehicle``
     - Repair the vehicle!
     - n/a
     - ``sound/chat/axis/75a.wav``, ``sound/chat/axis/75b.wav``
     - ``sound/chat/allies/75a.wav``, ``sound/chat/allies/75b.wav``
   * - ``DestroyVehicle``
     - Disable the vehicle!
     - n/a
     - ``sound/chat/axis/76a.wav``, ``sound/chat/axis/76b.wav``
     - ``sound/chat/allies/76a.wav``, ``sound/chat/allies/76b.wav``
   * - ``EscortVehicle``
     - Escort the vehicle!
     - n/a
     - ``sound/chat/axis/77a.wav``, ``sound/chat/axis/77b.wav``
     - ``sound/chat/allies/77a.wav``, ``sound/chat/allies/77b.wav``
   * - ``TakingFire``
     - Taking fire!
     - n/a
     - ``sound/chat/axis/18a.wav``, ``sound/chat/axis/18b.wav``
     - ``sound/chat/allies/18a.wav``, ``sound/chat/allies/18b.wav``
   * - ``FTAttack``
     - Attack!
     - n/a
     - ``sound/chat/axis/98a.wav``, ``sound/chat/axis/98b.wav``, ``sound/chat/axis/98c.wav``
     - ``sound/chat/allies/98a.wav``, ``sound/chat/allies/98b.wav``
   * - ``FTFallBack``
     - Fall back!
     - n/a
     - ``sound/chat/axis/99a.wav``
     - ``sound/chat/allies/99a.wav``, ``sound/chat/allies/99b.wav``
   * - ``FTCoverMe``
     - Cover me!
     - n/a
     - ``sound/chat/axis/25c.wav``, ``sound/chat/axis/25d.wav``
     - ``sound/chat/allies/25c.wav``, ``sound/chat/allies/25d.wav``
   * - ``FTCoveringFire``
     - Covering fire!
     - n/a
     - ``sound/chat/axis/25a.wav``, ``sound/chat/axis/25b.wav``
     - ``sound/chat/allies/25a.wav``, ``sound/chat/allies/25b.wav``
   * - ``FTMortar``
     - Deploy mortar!
     - n/a
     - ``sound/chat/axis/911a.wav``, ``sound/chat/axis/911b.wav``
     - ``sound/chat/allies/911a.wav``, ``sound/chat/allies/911b.wav``
   * - ``FTHealSquad``
     - Heal the squad!
     - n/a
     - ``sound/chat/axis/921a.wav``, ``sound/chat/axis/921b.wav``
     - ``sound/chat/allies/921a.wav``, ``sound/chat/allies/921b.wav``
   * - ``FTHealMe``
     - Heal me!
     - ``sprites/voiceMedic``
     - ``sound/chat/axis/922a.wav``, ``sound/chat/axis/922b.wav``
     - ``sound/chat/allies/922a.wav``
   * - ``FTReviveTeamMate``
     - Revive team mate!
     - n/a
     - ``sound/chat/axis/923a.wav``, ``sound/chat/axis/923b.wav``
     - ``sound/chat/allies/923a.wav``, ``sound/chat/allies/923b.wav``
   * - ``FTReviveMe``
     - Revive me!
     - ``sprites/voiceMedic``
     - ``sound/chat/axis/924a.wav``, ``sound/chat/axis/924b.wav``
     - ``sound/chat/allies/924a.wav``, ``sound/chat/allies/924b.wav``
   * - ``FTDestroyObjective``
     - Destroy the objective!
     - n/a
     - ``sound/chat/axis/931a.wav``, ``sound/chat/axis/931b.wav``
     - ``sound/chat/allies/931a.wav``, ``sound/chat/allies/931b.wav``
   * - ``FTRepairObjective``
     - Repair objective!
     - n/a
     - ``sound/chat/axis/932a.wav``, ``sound/chat/axis/932b.wav``
     - ``sound/chat/allies/932a.wav``, ``sound/chat/allies/932b.wav``
   * - ``FTConstructObjective``
     - Construct objective!
     - n/a
     - ``sound/chat/axis/933a.wav``, ``sound/chat/axis/933b.wav``
     - ``sound/chat/allies/933a.wav``, ``sound/chat/allies/933b.wav``
   * - ``FTDisarmDynamite``
     - Disarm the dynamite!
     - n/a
     - ``sound/chat/axis/36a.wav``, ``sound/chat/axis/36b.wav``
     - ``sound/chat/allies/36a.wav``, ``sound/chat/allies/36b.wav``
   * - ``FTDeployLandmines``
     - Deploy landmines!
     - n/a
     - ``sound/chat/axis/934a.wav``, ``sound/chat/axis/934b.wav``
     - ``sound/chat/allies/934a.wav``, ``sound/chat/allies/934b.wav``
   * - ``FTDisarmLandmines``
     - Disarm landmines!
     - n/a
     - ``sound/chat/axis/935a.wav``, ``sound/chat/axis/935b.wav``
     - ``sound/chat/allies/935a.wav``, ``sound/chat/allies/935b.wav``
   * - ``FTCallAirStrike``
     - Call an airstrike!
     - n/a
     - ``sound/chat/axis/941a.wav``, ``sound/chat/axis/941a.wav``
     - ``sound/chat/allies/941a.wav``, ``sound/chat/allies/941a.wav``
   * - ``FTCallArtillery``
     - Call in artillery!
     - n/a
     - ``sound/chat/axis/942a.wav``, ``sound/chat/axis/942b.wav``
     - ``sound/chat/allies/942a.wav``, ``sound/chat/allies/942b.wav``
   * - ``FTResupplySquad``
     - Resupply the squad!
     - n/a
     - ``sound/chat/axis/944a.wav``, ``sound/chat/axis/944b.wav``
     - ``sound/chat/allies/944a.wav``, ``sound/chat/allies/944b.wav``
   * - ``FTResupplyMe``
     - Resupply me!
     - ``sprites/voiceAmmo``
     - ``sound/chat/axis/945a.wav``, ``sound/chat/axis/945b.wav``
     - ``sound/chat/allies/945a.wav``, ``sound/chat/allies/945b.wav``
   * - ``FTExploreArea``
     - Explore the area!
     - n/a
     - ``sound/chat/axis/951a.wav``, ``sound/chat/axis/951b.wav``
     - ``sound/chat/allies/951a.wav``, ``sound/chat/allies/951b.wav``
   * - ``FTSatchelObjective``
     - Destroy the objective!
     - n/a
     - ``sound/chat/axis/931a.wav``, ``sound/chat/axis/931b.wav``
     - ``sound/chat/allies/931a.wav``, ``sound/chat/allies/931b.wav``
   * - ``FTInfiltrate``
     - Infiltrate!
     - n/a
     - ``sound/chat/axis/953a.wav``, ``sound/chat/axis/953b.wav``
     - ``sound/chat/allies/953a.wav``, ``sound/chat/allies/953b.wav``
   * - ``FTGoUndercover``
     - Go undercover!
     - n/a
     - ``sound/chat/axis/954a.wav``, ``sound/chat/axis/954b.wav``
     - ``sound/chat/allies/954a.wav``
   * - ``FTProvideSniperCover``
     - Provide sniper cover!
     - n/a
     - ``sound/chat/axis/955a.wav``, ``sound/chat/axis/955b.wav``
     - ``sound/chat/allies/955a.wav``
   * - ``IamSoldier``
     - I'm a soldat.
     - ``gfx/limbo/ic_soldier``
     - ``sound/chat/axis/61a.wav``, ``sound/chat/axis/61b.wav``
     - ``sound/chat/allies/61a.wav``, ``sound/chat/allies/61b.wav``
   * - ``IamMedic``
     - I'm a medic.
     - ``gfx/limbo/ic_medic``
     - ``sound/chat/axis/62a.wav``, ``sound/chat/axis/62b.wav``
     - ``sound/chat/allies/62a.wav``, ``sound/chat/allies/62b.wav``
   * - ``IamEngineer``
     - I'm an engineer.
     - ``gfx/limbo/ic_engineer``
     - ``sound/chat/axis/63a.wav``, ``sound/chat/axis/63b.wav``
     - ``sound/chat/allies/63a.wav``, ``sound/chat/allies/63b.wav``
   * - ``IamFieldOps``
     - I'm a field op.
     - ``gfx/limbo/ic_fieldops``
     - ``sound/chat/axis/64a.wav``, ``sound/chat/axis/64b.wav``
     - ``sound/chat/allies/64a.wav``
   * - ``IamCovertOps``
     - I'm a covert op.
     - ``gfx/limbo/ic_covertops``
     - ``sound/chat/axis/65a.wav``
     - ``sound/chat/allies/65a.wav``
   * - ``FTCheckLandmines``
     - Check for landmines!
     - n/a
     - ``sound/chat/axis/952a.wav``, ``sound/chat/axis/952b.wav``
     - ``sound/chat/allies/952a.wav``
