===================
ETLTV
===================

Introduction
^^^^^^^^^^^^

TO BE DONE

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
