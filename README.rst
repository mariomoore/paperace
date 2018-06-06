========
PapeRace
========

Computer implementation of the game, which could be played on a piece of
checkered paper.


Description
===========

This is my first game written in Python. Keep that in mind and be forgiving,
please ;)

The goal of the game is to beat one lap on the racetrack by placing dots at
the intersection of the grids. The player should move clockwise. The first dot
can be placed at a distance of one grille (directly on the right or diagonally).
Consider this movement as a vector [x, y], where 'x' is a component of
the right/left movement, and 'y' is a component of the up and down motion. Each
next move should be the same as the previous one (same motion vector), but each
component can be freely modified by + 1/-1. In other words, you can move to
the field by distance [x, y] from the current position OR to one of the 8
adjacent fields. This simulates the acceleration/deceleration of the vehicle
and torsion. The player loses when he is out of the track or out of the game
window.
.. image:: src\paperace\plansza\plansza.png

Features
========

- The game is inteded for 1-6 human players
- At the beginning of each race the player's position on the red starting line is random
- In each race the player's color is random
- The color of the current player is marked with a border with the same color around the racetrack


Note
====

This project has been set up using PyScaffold 3.0.3. For details and usage
information on PyScaffold see http://pyscaffold.org/.
