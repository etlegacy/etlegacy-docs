===================
ETLTV
===================

!!! UNDER CONSTRUCTION !!!

Introduction
^^^^^^^^^^^^

TO BE DONE

Feature
^^^^^^^
Add ettv protocol support to etlded - ettv client can connect to etlded server and players can join and view the game.

* ettv demo recording is possible
* add cvar sv_etltv_maxslaves "Number of ettv slaves allowed to connect." - ettv_sv_maxslaves equivalent
* add cvar sv_etltv_password "Password for ettv slaves. Must be set, or no slaves will be able to connect." - ettv_password equivalent
* add cvar g_etltv_flags "Bitflag 1 and 2. 1 = prevent slaves from being kicked. 2 = grant shoutcaster status to slaves."
* removed CVAR_SERVERINFO from g_fixedphysics, g_fixedphysicsfps, g_pronedelay, g_floodProtection, sv_floodProtect, sv_userInfoFloodProtect. Server info is too long and can crash ettv slave so until etltv is a thing it needs to get shorter.

Add legacy tvgame as replacment for etpro tvgame

* players can join ettv server connected to etlded server and watch and chat about the game
* most commands supported with some flood protection in place - up to change in the future still
* slave server support for 64 player server max right now (it's not realy an issue I believe but it's low priority for me)
* ignore/unignore commands not added right now but can turn on/off chat with /tvchat
* /players and /viewers commands
* /follow [id/name] or just classic legacy mod following (minus aim and follow whoever is under crosshair)
* rcon and ref for muting/kicking viewers
* LUA is "in" but disabled

Add possibility for etlded to act as a client (ettv)

* add possibility for etlded to act as a client
* add command tv connect <ip> <masterpassword> (sv_etltv_maxslaves and sv_etltv_password must be set on master server)
* add command tv disconnect
* add command record <name> (optional) for recording tv demos
* add command stoprecord for stopping recording
* add command demo <name> for demo playback
* add command ff <seconds> command - fastforwarding demo (works similiar to timescale) stops on map_restart or can stop it with ff 0
* add cvar sv_etltv_autorecord <0/1> automatically record tv demos
* add cvar sv_etltv_autoplay <0/1> automatically play demos (only on specifically named demos from autorecording, fe. demo0001->demo0002 etc.)
* add cvar sv_etltv_clientname etltv client name
* demos are recorded into tvdemos folder with extension tv_84
* etpro tv demos are playable, best is to use ettv tvgame and start etlded with +fs_game etpro (put etpro tvgame into etpro mod folder). Need 2.6b client in order to watch
* slave server will not download missing files from master server, so need to make sure it has every pk3 it needs
* only available for dedicated server

Add automatic feed delay to etltv

* add cvar sv_etltv_delay <seconds> - setable only on etlded init, delays feed from master server
* add cvar sv_etltv_shownet - for network debugging
* disabled /scores command in tvgame because it can easily lag the server
* add parseEntitiesNum check to etlded for snapshot generation - current check doesn't seem to work at all (svs.nextSnapshotEntities), server will send on its own uncompressed snapshot if it detects that client will go over MAX_PARSE_ENTITIES
* add optional privatepassword argument to tv connect command. tv connect server masterpassword privatepassword
* add cvar sv_etltv_queue_ms (read only) for storing the amount of time till the game will start (backward compatible with etpro)
* various other general improvments to etltv
* players can connect to delayed slave server even before the game starts just like on ettv

> 2.82

* add 64+ players server support

Notes:
* setting sv_maxclients higher than 64 might require setting higher com_hunkMegs.
* legacy cgame doesn't support higher than 64 sv_maxclients, notably CG_ParseFireteams uses cgs.maxclients which will break the game if it goes over 64.
* legacy ui doesn't support showing higher than 64 sv_maxclients servers in the browser, unless ui_serverBrowserSettings 4 is set on game init.

> 2.82.1

* Added chaining support to ETLTV

* Added gamenametv server info cvar so it is possible to tell apart standard mod from tvmod
* Made etltv register server info cvars on it's own (any mod will now show it's own server info cvars)
* Removed unused and unnecessary cvars and rename some from g_* to tvg_*
* Fixed server info cvars not being updated beside during server spawn
* Fixed only legacy mod working using tvgame (broke after some update)
* Removed tvg_character.c and other no longer necessary code
* Fixed viewers playerstate clientNum being updated to incorrect value in TVG_ClientUserinfoChanged (interfered with correct snapshot generation)
* Implemented cvar tvg_inactivity <seconds> - kicks viewers after specified amount of time of inactivity (following a player counts as activity)
* Added a way to recognize currently run mod inside tvgame (as of right now Legacy, ETJump, ETPro)
* Added mod specific game commands auto updates and exlcuded ETJump from some that are related to weapon stats
* Added handling for two ETJump game commands GUID_REQUEST and HAS_TIMERUN (just ignored)
* Added handling for old IMPKD game command (ETMain and possibly most other mods still use it)

> 2.8X.X

* Added lua support to ETLTV. Main differences from legacy mod for scripts:
  * Removed some hooks and functions that are not relevant to tvgame
  * Added et.gentity_get access to master server entityState_t and entityShared_t structs
  * Added et.level_get added access to level_locals_t struct
  * Added et.ps_get access to master server players playerState_t struct
  * Added et.gclient_get access to viewers gclient_t struct
  * Added et.client_set access to viewers gclient_t struct
  * Only viewers struct is writeable (at least as of now)
  * Removed and add a bunch of accessible fields
  * Added et.TeleportPlayer( clientnum, vec3_t origin, vec3_t angles )
  * Added clientnum = et.MasterClientNumberFromString( string ) searches through master clients for one partial match with string

NOTE: lua works only for sv_pure 0 slave server because otherwise lua scripts cannot be read (in short because of extension whitelist in file system, might be not possible to properly fix)

* Fixed incorrect mods type in tvcmd_reference_t
* Refactored some if statements
* Removeed `g_mdx.c` from build
* Removed not needed or "incompatible" code
* Init r.ownerNum to ENTITYNUM_NONE for player entities
* Fixed and added `SpectatorAttackFollow` trace
* Removed CVAR_SERVERINFO flag from g_fixedphysics, g_fixedphysicsfps and g_pronedelay cvars
* `G_ETTV` gameexport is now only kept for ETTV compatibility


