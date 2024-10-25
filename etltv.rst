===================
ETLTV
===================

!!! UNDER CONSTRUCTION !!!

ETLTV Introduction
^^^^^^^^^^^^^^^^^^

TO BE DONE

Feature
^^^^^^^
Add ettv protocol support to etlded - ettv client can connect to etlded server and players can join and view the game.

* ettv demo recording is possible
* add cvar sv_etltv_maxslaves "Number of ettv slaves allowed to connect." - ettv_sv_maxslaves equivalent
* add cvar sv_etltv_password "Password for ettv slaves. Must be set, or no slaves will be able to connect." - ettv_password equivalent
* add cvar g_etltv_flags "Bitflag 1 and 2. 1 = prevent slaves from being kicked. 2 = grant shoutcaster status to slaves."
* removed CVAR_SERVERINFO from g_fixedphysics, g_fixedphysicsfps, g_pronedelay, g_floodProtection, sv_floodProtect, sv_userInfoFloodProtect. Server info is too long and can crash ettv slave so until etltv is a thing it needs to get shorter.

Add legacy tvgame as replacement for etpro tvgame

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
* Added `tvgamecommands` help info (/commands, excludes commands that are not available for currently running mod)
* Added possibility to intercept master server commands in lua (et_ClientCommand clientnum == -2), with this addition not natively supported mods could add support for their game commands fully in lua: client requests stats->lua sends requests to master server->intercept response->save/send over to client, or even auto updates without interaction with clients)

* Added possibility to watch tv_84 demos on client (listen server)
  * Added tv demo console command (client only) to play demo
  * Added tv ff console command (client only) to fast-forward demo by. NOTE: still cannot connect listen server as tv server although a lot of the tv server code is now compiled into client (too lazy to add DEDICATED guards and splitting a lot of the places with them is not something I like). This is also very unlikely to ever change because by design the connected tv server should be a spectator and preferably never move too.
  * Connecting tv server to a listen server is not recommended (looks buggy), other clients should be fine
  * Fixed tv server(s) and their client(s) not properly disconnecting when master server shuts down (imported ettv bug)
  * Fixed improper server shutdown on demo end if there are no more demos to play next (imported ettv bug)

* Renamed game system call
* Moved configstring initialization to `SV_InitGameVM`, this means that now it is possible to look up configstrings during `GAME_INIT`. (not possible in ettv, so anything that relies on it won't work there)
* Parsed `CS_WARMUP` and `CS_WOLFINFO` on `GAME_INIT` and `GAME_CLIENT_COMMAND`
* Added `tvg_autoAction` cvar, bit values `AA_DEMORECORD 1 AA_STATS 2`. Autorecord start demo recording the same way cg_autoaction does with client demos (with the same name schema too), only difference as of now is that demo will not be stopped during intermission (client demos are round seperated because of this). Autostats controls if tv server will periodically send commands requesting stats.
* Improved handling of spawn points, especially if game is delayed the spawnpoint can end up being very wrong (improvement over etpro tvgame)
* Fixed animation files breaking mod loading on different mods than legacy
* Extract pmove code from `bg_pmove` to `tvg_pmove`
* Fixed various pmove prediction issues on mods like ETJump or ETPro
* Overwrited master server `CS_SVCVAR` configstring
* Properly shutdown server on tv disconnect

NOTE: `sv_etltv_autorecord 1` is equal to `cl_autorecord 1` and `tvg_autoAction & 1` is equal to `cg_autoaction & 1`. So sv_etltv_autorecord records everything, while tvg_autoAction starts at the warmup countdown or GS_PLAYING (but doesn't end on itermission so whatever is after will keep being recorded. It's not impossible to change in the future if wanted.




