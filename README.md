# Minesweeper for Freshplanet
This is a coding test made for an internship at Freshplanet, coded in Python2.7 (later adapted to python 3.5) using the tkinter lib for the GUI. 

I coded this on MacOS so it is possible that windows/linux users experiment some issues (tkinter relies on native components, reacting differently from what I've seen), but from I've tested it seems to work well on all platforms

## Contents

* */minesweeper.py* - The python program you need to execute to launch the minesweeper
* */grid.py* - The grid class, implementing the algorithms
* */graphicalInterface.py* - The graphical interface implementation using tkinter and managing click events
* */Sprites/* - GIF sprites displayed in the game

## Features
* Standard minesweeper with GUI
* Right click: Flag a square
* Middle click (wheel click): If you have enough flags adjacent to a revealed square, reveal the ones that aren't flagged
* First click can't be on a bomb, the game resets until it finds a correct grid

## Known bugs
* Mouse buttons <Button-2> and <Button-3> are reversed on windows and you have to wheel click to flag a square

## Suggested improvements
* Game events should be managed in minesweeper.py and not in the MSGraphicalInterface class
* Middle click usage suppose that the user has a mouse, which isn't granted, it should be double-click but it was harder to implement because there was already a left-click action, and tkinter does not work well with that
* Highscore table storing the quickest minesweeper solving
* Rollback after discovering a bomb (anti-missclick feature)
