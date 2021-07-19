===============================
Appendix: Bayesian Skill Rating
===============================

Background of the `Bayesian <https://en.wikipedia.org/wiki/Bayesian>`_ skill rating system implementation.

Background
==========

* Implement a new, proved metric that can be used to compare skill of players over time
* Get rid of XP save (not XPs!) and all of its unwanted side effects
* Provide a solid base upon which some nice features could be built later on

Measure players' skill
----------------------

As FPS require skills in multiple areas like reflex, planning, tactical analysis or teamwork, with the relative importance of these skills depending on the map, game mode, player roles or team compositions, a **skill rating** could be defined as a metric measuring *"all the parameters of a player that help his team to win"*. This can be measured by a probabilistic, Bayesian approach by simply looking at the output of a game instead of the various in-game micro-parameters (such as accuracy, number of kill, etc.), which are vastly limited to define what the skill of a player is.

One another important reason why a skill rating system should only consider match results to compute the skill is that accounting for extra information given by in-game parameters might be abused by players. This can be very detrimental to team-based games, where players would try to maximize statistics that boost their skill (e.g. their own number of kills or awards) instead of doing what is best for their team to win.

To give an example, let's consider the following: Which is the better player, the rambo medic that kills these 20 random enemies that are easy targets, or that one guy that smartly avoid fight but actually steals and retrieves the objective to win the map? The former contributes a bit to the team, but it is the latter that makes the decisive move. Any system based on in-game parameters (such as number of kills) would give lot of credits to the first player and only a few to the second one, but it is them that did the most important part of the job. By looking at only the outcome, and with the laws of probability, it is the real ability of making the team win that is measured on the long term. Such a skill rating also cannot be "farmed" with specific actions, but requires players to do their best to help the team to increase.

In addition, in-game ranks are tied to the Skill Rating value when the system is enabled. Ranks thus provide a quick way to display the actual skill of players. When Skill Rating is disabled, the ranks will behave as they normally do by being tied to XPs.

Get rid of XP save side effects
-------------------------------

ET implements XPs, which measure player' scores based on specific actions (kills, construction, revive, ..) and are also used to control the various skill levels, similarly to a RPG. However, XPs don't give any indication of the real global performance of a player. As *XP Save* (which isn't part of the original game) is usually enabled on servers, XPs merely only give a hint about the time the player has played on a specific server. Saving XPs also create some imbalance by enabling abilities of skill levels permanently (such as adrenaline for medics) which have never been accounted for in the original game balance, where XPs were reset at the end of matches or the end of campaigns.

Foundation for the future
-------------------------

Beside rating individual players, a Bayesian skill rating system can be useful for:

* predicting the outcome of matches in a multiplayer game
* rating the "match quality" during a given map, and
* keeping the teams balanced to, in theory, keep the gameplay entertaining

Also, it can be used to:

* track player ratings across multiple servers world-wide with a master server (global leaderboard)
* recommend servers to players based on the difficulty level of each server (difficulty matching)

Additionally, analysis of collected statistics can give insights that lead to improvements in gameplay by:

* allowing server administrators to more fairly balance matches
* allowing level and map designers to either create more balanced maps, or recommend more appropriate time limits to create more balanced maps

Objectives
==========

As a first step, a possible implementation should focus on giving useful information:

* skill rating
* match quality rating
* outcome prediction
* analysis of maps gameplay

Once this is working in a satisfying way, additional features could be build upon to provide the following:

* team balancing
* centralized leaderboard
* matchmaking with players of similar skills

Existing implementations
========================

.. note::
    * The `Bradley-Terry model <https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model>`_ model uses the `Logistic distribution <https://en.wikipedia.org/wiki/Logistic_distribution>`_, while the `Thurstone-Mosteller <https://en.wikipedia.org/wiki/Thurstonian_model>`_ model uses the `Normal distribution <https://en.wikipedia.org/wiki/Normal_distribution>`_.
    * The `Logistic distribution <https://en.wikipedia.org/wiki/Logistic_distribution>`_ seems to model real life data better than the `Normal distribution <https://en.wikipedia.org/wiki/Normal_distribution>`_ (according to Chess players), but they are actually pretty `similar <https://en.wikipedia.org/wiki/Logit#Comparison_with_probit>`_.


Elo
---

`Elo <https://en.wikipedia.org/wiki/Elo_rating_system>`_ is possibly the most prominent rating system in use today.

.. important::
    **References**: `Elo rating system <https://en.wikipedia.org/wiki/Elo_rating_system>`_.

**Overview**

* A player's Elo rating is represented by a number which increases or decreases based upon the outcome of games between rated players.
* After every game, the winning player takes points from the losing one. The difference between the ratings of the winner and loser determines the total number of points gained or lost after a game.
* In a series of games between a high-rated player and a low-rated player, the high-rated player is expected to score more wins. If the high-rated player wins, then only a few rating points will be taken from the low-rated player. However, if the lower rated player scores an upset win, many rating points will be transferred. The lower rated player will also gain a few points from the higher rated player in the event of a draw.
* This rating system is self-correcting. A player whose rating is too low should, in the long run, do better than the rating system predicts, and thus gain rating points until the rating reflects their true playing strength.

**Limitations**

Though the Elo ranking systems has been successful, it is designed for two-player games.

Glicko
------

The `Glicko <https://en.wikipedia.org/wiki/Glicko_rating_system>`_ updating system improves over Elo by incorporating the variability in parameter estimates.

.. important::
    **Type**: Bradley-Terry model

    **References**: `Glicko Ratings <http://www.glicko.net/glicko.html>`_.

    * `Glicko rating system <http://www.glicko.net/glicko/glicko.pdf>`_
    * `Glicko-2 rating system <http://www.glicko.net/glicko/glicko2.pdf>`_

**Overview**

Prior to a rating period, a player's skill (θ) is assumed to follow a Gaussian distribution which can be characterized by two numbers:

* the average skill of the player (μ)
* the degree of uncertainty in the player's skill (σ)

Glicko models the game outcomes by the `Bradley-Terry model <https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model>`_ and updates players' skills after a rating period.
Glicko performs best when the number of games per player is around 5-10 in a rating period.

The Glicko-2 rating system improves upon the Glicko rating system and further introduces the *rating volatility*, which indicates the degree of expected fluctuation in a player's rating.

**Limitations**

Similarly to Elo, the Glicko ranking system has been successful, but they are designed for two-player games.

ETPub skill rating
------------------

ETPub implements such a metric with its "Player Rating", giving a normalized skill score.

.. important::
    **Type**: Single layer neural network using Bradley-Terry model (Logistic distribution)

    **References**: `Improving Machine Learning Through Oracle Learning <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.1028.1703&rep=rep1&type=pdf>`_. In particular:
    
    * Chapter 7: "A Bradley-Terry Artificial Neural Network Model for Individual Ratings in Group Competitions"
    * Chapter 8: "Hierarchical Models for Estimating Individual Ratings from Group Competitions"

**Overview**

The base abilities of the model is useful to determine player ratings by:

* allowing for weighting individuals
* dealing with rating uncertainty
* preventing rating inflation

It is extended to take into account:

* the map-side effect
* the effects of time on gameplay
* the server difficulty

The model allows for real time win performance prediction.

.. notes:
   **Map-side effect**:

   * most maps were designed such that one side has a major advantage.
   
   **Time effect**:
   
   * can be used for real time determination of match outcome probability, not actually useful to determine the outcome prior to the match.
   
   **Server difficulty**:
   
   * allow players performance comparison across servers more effectively
   * gives us a measure of how difficult each server is, as this parameter can also be interpreted as the rating increase a given side expects for each additional player on that side. Servers where having additional players will not make up for the skill of the players are more difficult than those where a few extra players alone can decide the winner.

**Limitations and possible improvements**

Parameters:

    * **Rating uncertainty**: the downside to this method of modeling uncertainty is that is does not allow for a later change in an individuals rating due to long periods of inactivity or due to improving rating over time. This could be implemented with a form of certainty decay that lowered an individual's certainty value over time (see Glicko-2 rating volatility).
    * **Map side**: a similar measure of uncertainty could be applied to the field-group parameters.
    * **Server difficulty**: the accuracy of server difficulty comparison is affected by how often players move between servers.

All associations are assumed to be additive and linear:

    * They are additive in the sense that the skill of a given team is proportional to the sum of the skill of the players in that team. It does not take into account higher-level interactions between the players.
    * It is linear because the effects of time and the number of players per team is assumed to affect the model in a linear fashion.

Two approaches to improving the robustness of the current model include:

    * Extending the current single-layer ANN to a multi-layer ANN
    * Constructing a higher-level statistical model that allows for these additional complexities

**Evaluation**

    * The model accuracy is tested against predicting the matches used to estimate the model parameters. The data set used consisted of 4,675 matches, 5,145 players, and 14 matches on average per player. The results show the accuracy to be 72.5%, but this result does not seem to have been cross validated.

**Bug**

   * In the latest implementation of etpub, there is a bug concerning the time played in each team values (`mapAxisTime`/`mapAlliesTime`). This value is not computed when players are in limbo (most likely due to an unrelated change that was later implemented), so the more a player spend in limbo, the less accurate these values are.
   * Consequently, the PRW can't be accurate either. This bug is also still present in the latest release of the Silent mod. It's been reported to the Silent team, but they didn't fix the issue.

TrueSkill
---------
The TrueSkill system is a more modern algorithm that has been developed by MicroSoft for its XBox matching service. It has the advantage over the ETPub PR that it starts very low and increases over time (like XPs), before stabilizing when the skill rating is accurate (like the ETPub PR).

.. important::
    **Type**: Bayesian network using Thurstone-Mosteller model (Normal distribution)

    **References**:
    
    * `TrueSkill™ Ranking System <http://research.microsoft.com/en-us/projects/trueskill/>`_
    * `TrueSkill™ Ranking System: Details <http://research.microsoft.com/en-us/projects/trueskill/details.aspx>`_
    * `TrueSkill™ Ranking System: FAQ <http://research.microsoft.com/en-us/projects/trueskill/faq.aspx>`_
    * `Computing Your Skill <http://www.moserware.com/2010/03/computing-your-skill.html>`_

    **Reports**:

    * `TrueSkill(TM): A Bayesian Skill Rating System <http://research.microsoft.com/pubs/67956/NIPS2006_0688.pdf>`_
    * `The Math Behind TrueSkill <http://www.moserware.com/assets/computing-your-skill/The%20Math%20Behind%20TrueSkill.pdf>`_
    * `On Gaussian Expectation Propagation <http://research.microsoft.com/pubs/74554/EP.pdf>`_
    * `TrueSkill2: An improved Bayesian skill rating system <https://www.microsoft.com/en-us/research/uploads/prod/2018/03/trueskill2.pdf>`_

**Overview**

* Allow multi players comparison
* Allow multi teams comparison
* Allow draw
* Allow partial play
* Allow partial update
* Allow uncertainty over time
* Allow match quality evaluation
* Allow win probability prediction

**Limitations and possible improvements**

* No map-side effect parameter
* No time effect parameter

TrueSkill can be expanded to take both of these parameters into account. They can be modeled with another Gaussian in the team performance factor.

**Evaluation**

The prediction error (fraction of teams that were predicted in the wrong order before the game) has been evaluated.

* However. this measure is difficult to interpret because of the interplay of ranking and matchmaking: depending on the (unknown) true skills of all players, the smallest achievable prediction error could be as big as 50%.
* In order to compensate for this latent, unknown variable, a competition wa arranged between ELO and TrueSkill: each system was let predict which games it considered most tightly matched and presented them to the other algorithm. The algorithm that predicts more game outcomes correctly has a better ability to identify tight matches.
* For TrueSkillthe matchmaking criterion was used and for Elo the difference in Elo scores, s1 - s2, was used.

The Halo 2 Beta Dataset (v1.1) has been used to evaluate the model. It consists of various matches outcome, including small teams games (up to 4 players in 2 teams, 27539 games for 4992 player) and large teams games (up to 8 players in 2 teams, 1199 games for 2576 players).

From this dataset:

* 80% has been used for data of training
* 10% has been used for testing
* 10% has been used for cross-validation

Prediction errors has been shown to be 37.17% (or 62.83% accuracy) for small team and 29.94% (or 70.06%) for large teams. TrueSkill proved to be significantly better at predicting the tight matches than Elo (buffed for team ranking).

**Convergence**

* The algorithm converges, for 2 teams with 8 players per team, after 91 games (average number of games per gamer that the system ideally needs to identify the skill level).
* This is quite slow to determine the skill rating
* But this slowness is good as a replacement of XP save!

TrueSkill extensions
--------------------

.. important:: References:
    
    * `TrueSkill extension accommodating score-based match outcomes <https://github.com/rmarquis/ecml2mlj/blob/master/doc/sbsl_ecml_camera_ready_complete_version.pdf>`_ (`website <https://code.google.com/p/ecml2mlj/>`_)
    * `TrueSkill extension accommodating score-based match outcomes and home field advantage <https://github.com/rmarquis/ecml2mlj/blob/master/doc/sbsl_mlj.pdf>`_ (`website <https://code.google.com/p/ecml2mlj/>`_)

Various references
------------------

* `Microsoft TrueSkill and the Art of Gaming Statistics <http://www.peachpit.com/articles/article.aspx?p=443596>`_, short introduction
* `A Bayesian approximation method for online ranking: Approximate Bayesian network using Bradly-Terry model <https://www.csie.ntu.edu.tw/~cjlin/papers/online_ranking/online_journal.pdf>`_
* `Analysis of paired comparison data using Bradley-Terry models with applications to football data <https://haziqj.ml/files/haziq-msc-thesis.pdf>`_
* `Model-Based Machine Learning, Chapter 3: Meeting Your Match <http://www.mbmlbook.com/TrueSkill.html>`_, deeper explanation
* `Beyond Skill Rating: Advanced Matchmaking in Ghost Recon Online <http://www.iro.umontreal.ca/~lisa/pointeurs/gro-matchmaking-ieee.pdf>`_
* `Model-based machine learning <http://rsta.royalsocietypublishing.org/content/371/1984/20120222>`_
* `Why We Should Never Go Back to 1-50.. or The Death of the Halo Black Market <http://forums.bungie.org/halo/archive35.pl?read=1054300>`_, interesting point of view on the effect of the ranking algorithm of the players behavior
* `Rating systems with multiple factors <http://homepages.inf.ed.ac.uk/imurray2/projects/2011_marius_stanescu_msc.pdf>`_
* `A rating system for asymmetric multiplayer games <https://www.snellman.net/blog/archive/2015-11-18-rating-system-for-asymmetric-multiplayer-games/>`_
* `TrueSkill Through Time: Revisiting the History of Chess <https://www.microsoft.com/en-us/research/wp-content/uploads/2008/01/NIPS2007_0931.pdf>`_
* `Whole-History Rating: A Bayesian Rating System for Players of Time-Varying Strength <https://www.remi-coulom.fr/WHR/WHR.pdf>`_
* `Beyond skill-based rating systems: analyzing and evaluating player performance <https://www.researchgate.net/publication/319926061_Beyond_skill-based_rating_systems_analyzing_and_evaluating_player_performance>`_, interesting read for the idea of rewarding players in the losing team, but misses the point of only looking at match outcome
* `Application and Further Development of TrueSkill Ranking in Sports <https://uu.diva-portal.org/smash/get/diva2:1322103/FULLTEXT01.pdf>`_
* `VALORANT Ranks and Competitive Matchmaking <https://beta.playvalorant.com/en-us/news/dev/valorant-ranks-and-competitive-matchmaking/>`_, very basic overview of an implementation in a modern competitve game

Implementation
==============

We'll implement TrueSkill, for the following reasons:

* Although the ETPub algorithm includes the extra map and time parameters, it severely suffers from a fixed rating uncertainty that TrueSkill actually manages properly.
* TrueSkill is also quite simple to implement and fast to compute in ET context, as the game doesn't require more than 2 teams (no complex Belief Propagation required) and doesn't have draw either.
* We also extend TrueSkill for map-side and time parameters to improve it.

**Overview of work required**

* Implement rating database management
* Take time of clients that have disconnected before the end of the game into account
* Take time of clients that have disconnected then reconnected into account
* Extend algorithm with field parameter
* Extend algorithm with time parameter
* Extend win probability with field parameter
* Extend win probability with time parameter
* Add cvar in default config file
* Implements useful commands (/rating, /allrating, ..)

See also the `related tracker issue <https://github.com/etlegacy/etlegacy/issues/403>`_ for implementation details.

**Language**

Although a Lua implementation is available (FAF), a C implementation would allow tigher integration in the mod and ease future features development.

* Implement the base algorithm directly in C
* Implement players database management tighly with our embedded engine database system. Some balancing commands can be integrated to our Lua administration suite.
* What about map data collection? The mapvoting gametype already exist in C in the code, but it is based on a file format instead of DB. Let's keep thing separate for now.

**Algorithm**

Factor 1: What Do We Already Know About Your Skill?
    * previous skill level (μ, σ) from somewhere (e.g. a player database)
    * add some uncertainty (τ) to your skill's standard deviation to keep game dynamics interesting

Factor 2: How Are You Going To Perform?
    * add in beta (β)

Factor 3: How is Your Team Going to Perform?
    * computing the performance of a team as a whole
    * team's performance is the sum of each team member's performance
    * weight each team member's contribution by the amount of time that they played

Factor 4: How'd Your Team Compare?
    * compare team performances in pairs
    * subtracting team performances to come up with pairwise differences

Factor 5: How Should We Interpret the Team Differences?
    * comparison factor based on the team performance differences
    * comparison depends on whether the pairwise difference was considered a "win" or a "draw."
    * we imagine that there is a buffer of space called a "draw margin" (ε) where performances are equivalent

Others
    * add partial play support
    * add map side extension

**Extension**

We actually extend TrueSkill for map side (field advantage) effect parameter:

* Additional Gaussian can be used in the team performance factor
* A cvar option enables this extension

Approximate the map field advantage with a discrete `Bernouilly distribution <https://en.wikipedia.org/wiki/Bernoulli_distribution>`_:

* `p = probability` of a team winning on a certain map (`0 < p < 1`)
* `mean = p`
* `var = p * (1-p)`

Both map side and map time parameters are taken into account here, as the length of the map determines who is more likely to win.

Notes:

* Scaling of mean and var should be done by a factor of `2 * MU`
* Number of required match before p is valid should be defined. For the more general `binomial distribution <https://en.wikipedia.org/wiki/Binomial_distribution>`_ `B(n,p)` with `n = matches` and `p = prob`, `mean = np`, `var = np(1-p)`, and the normal approximation is `N(np, np(1-p))` with `n > 20` and `p not near 0 or 1`.
* See `Binomial proportion confidence interval <https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval>`_ and `g_playerRating_mapPad` from etpub to stabilize the map bias mean early.

**Team balance**

Balance team using the match quality equation. See:

* `About TrueSkill and game-quality optimization <https://forums.faforever.com/viewtopic.php?f=41&t=12862>`_
* `Heap's algorithm <https://en.wikipedia.org/wiki/Heap%27s_algorithm>`_
* `Permutations of combinations of two groups <https://stackoverflow.com/questions/29831862/permutations-of-combinations-of-two-groups>`_

Frequently Asked Questions
==========================

Anwers to common questions about the implemented Bayesian skill rating system.

General
-------

* What is the Skill rating system?

 It is an implementation of the `TrueSkill <https://en.wikipedia.org/wiki/TrueSkill>`_ statistical ranking system developed by Microsoft for its video game matchmaking on Xbox Live.

* How does this compare to the popular Elo?

`Elo <https://en.wikipedia.org/wiki/Elo_rating_system>`_ is a simple rating system that models the relative strength (or skill) of players by a single number.
`Glicko <https://en.wikipedia.org/wiki/Glicko_rating_system>`_ is more elaborated system models the strength `Mu` and additionally the uncertainty `Sigma` of that value.
TrueSkill is a generalization of Glicko for multiple teams and multiple players games, and the Skill Rating system expands on it to fit Legacy matches even better.

* What does the rating value represent?

The Skill Rating value is modeled as `SR = Mu - 3 * Sigma`, and represents the conservative relative skill of a player in a specific pool of players. In other words, it's a conservative way to say "the player skill is 99.7% likely to be better than this value" and can't be absolutely compared across servers.

* New players have a rating of zero. Does this mean the system believe they are noob?

No, every player starts with an average rating `Mu = 25` with a defined uncertainty of `Sigma = 25/3`, which means every new player SR is displayed as zero despite being evaluated as "average" under the hood.

* Why not using kills or in-game actions to rate players?

As FPS require skills in multiple areas like reflex, planning, tactical analysis or teamwork, with the relative importance of these skills depending on the map, game mode, player roles or team compositions. A **skill rating** could be defined as a metric measuring *"all the parameters of a player that help his team to win"* rather than the various in-game micro-parameters (such as accuracy, number of kills, etc.), which are vastly limited to define what the skill of a player is. Over the long term, the skill of a player can be measured more accurately by simply looking at the result of a game.

Another important reason why a skill rating system should only consider match results to compute the skill is that accounting for extra information given by in-game parameters might be abused by players. This can be very detrimental to team-based games, where players would try to maximize statistics that boost their skill (e.g. their own number of kills or awards) instead of doing what is best in a specific situation to help their team win.

* Why is TrueSkill adapted to public servers?

Public servers don't have many constraints. Players can join, leave a match at any time, switch team at any moment, or join the team with the most players at their own discretion. All of these aspects are taken into account by the SR algorithm.

* What is the map bias?

The vast majority of the maps played are asymmetric, and as such are easier for one side compared to the other. While this aspect isn't modelled in the original TrueSkill system, it is taken into account into the implemented SR system as an additional parameter.

* What is taken into account while calculating SR?

The mean and uncertainty values of a player skill, the skill of their teammates and enemy players, the difference of strength of each team, the time played in each team, the bias of the map played.

What if...
----------

* What if players change team to be on the winning team instead?

The relative strength of teams is taken into account. Winning a game in a team that is evaluated as much stronger than the other will indeed result in an increase of SR of the player, but that increase will be very minimal and can be as low as thousandths of a more balanced game.

* What happens if I am playing only with noobs, which make me lose ever time. I cannot get a strong rating, despite being better than them!

Again, the relative strength of teams is taken into account. Losing a game in a team that is evaluated as much weaker than the other will indeed result in an decrease of SR of the player, but that decrease will be very minimal and can be as low as thousandths of a more balanced game.

* What happens if players switch team to the winning team before the end of the map?

The time played in both team is taken into account. Switching team at the last moment will not result in a significant increase of rating, and in fact will likely still result in a significant decrease of rating.

* What happens if players disconnect from the current match?

The time played by each player, even those that left before the end of the match, is taken into account in the SR calculation. Their SR will also be adjusted accordingly.

* What happens if players disconnect and reconnect to the same match?

The time played prior disconnection will be taken into account. Their SR will be adjusted accordingly.

* How does one cheat the system?

By trying to do their best to help their team win a game.

Tell me more...
---------------

* The win percentage indicated team A would win, but team actually B won. Explain!

The win percentage is a real time calculation of the expected outcome of a game, based on the above mentioned parameters. It can't predict the future accurately, but is somewhat good at giving a prediction that is better than flipping a coin. For reference, accuracy data taken on millions of Halo games reveals that the win percentage is accurate in about ~70% of times.

* I'm playing alone on an empty server, and the win percentage indicate 50%. Explain!

Some crash-inducing mathematical weirdness occurs when dividing by zero. As such, the algorithm assumes that at least one player is present in each team, which shouldn't be a big problem in a multiplayer game.

* How does one make advantage of the system to boost his rating?

As the relative strength of teams is taken into account, an "easy" way to get a significant SR increase is to play in the weaker team and beat the odds.

* The Scoreboard has most strong players in one team, yet the scoreboard set the winning percentage to the weak team. Explain!

The winning percentage isn't a measure taken for a specific time only, but takes the time played prior to it. As such, if most strong players are in a weaker team, it means they switched team at some point during the match.

* How long does it take for the rating to converge toward an accurate value?

It depends on the number of players, their existing relative SR and the size of teams during matches. As a rule of thumb, the more players on a server and the more experienced they are, the faster your SR will converge.

* Why use shuffle by SR instead of XP shuffle?

XP shuffle is based on the ongoing match or campaign, and is based on micro-parameters that might not be relevant for determining who is better skilled. SR is based on long term data of game outcomes and as such is a better way to balance team.

* The maps are always favoring a side. What about this?

The map bias is taken into account in the SR calculation. As such, playing one side or the other isn't a determinant factor to increase SR.

* How is the map bias computed?

It is modeled as an extra parameter evaluating home field advantage using past outcome on that specific map. 

* What influence do bots have on map bias (is this good for bias calculation)?

Since bots are equally stupid, they actually do help in evaluating the map bias. 

Advanced questions
------------------

* Why using TrueSKill and not using the system implemented in ETPub?

Simply said, TrueSkill is a more modern approach of the model used by ETPub. Specifically, it is less prone to rating uncertainty becoming stuck over time, and its conservative estimation that is slowly increasing provides a better alternative to replace XPs save in the eyes of players.

* What are the differences between TrueSkill and the system implemented in Legacy mod?

What the ETPub system did better than TrueSkill is in modeling the effect of asymmetric maps, which is completely absent in the original TrueSkill. The implementation extends the algorithm to take into account this map bias in each match.

* What are the actual limitations of the system?

The system does several simplification by assuming associations to be additive and linear, such as team performance, which could be improved upon.
The evaluated SR also doesn't take long periods of inactivity into account, as player performance should be expected to be lower than it was estimated previously. While some random noise is added in order to prevent the SR to converge so much that it wouldn't change anymore, certainty decay might be another possibility of improving the system.

* Why aren't you calling this system "TrueSkill"?

TrueSkill is trademarked by Microsoft. While the algorithm is also patented in the US, software patents are however excluded from patentability in Europe (where all the core members of ET:Legacy team are located), not to mention there is very little that isn't actually pure Bayesian statistics. Also, the ET: Legacy project is not commercially driven.

* Will this system be used for match making?

It could be used as a basis for an upcoming matchmaking feature. However, such feature first and foremost depends on the availability of a wide pool of players, which might not be big enough anymore to ensure it works reliably.

* Can you give me resources to learn more about the system?

See the `Existing implementations` section for resources, articles and the different papers used in the SR implementation in Legacy mod.
