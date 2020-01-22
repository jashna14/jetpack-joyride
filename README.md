# SAVE THE YODA(Inspired by Jetpack-Joyride) - "Terminal-based version"

## About :-
```
Jetpack Joyride is a 2011 side-scrolling endless runner action video game created by Halfbrick Studios. The game features the same protagonist from Monster Dash, Barry Steakfries, who the player controls as he steals a jet pack from a top-secret laboratory. The game has been met with very favorable reviews, and has won numerous awards. 
This is a terminal version of the 'Jetpack-Joyride' game. It exhibits Object-Oriented Programming concepts like encapsulation, inheritance, abstraction and polymorphism.
```
## Pre-requisites :-
```
In order to play this game, python3 should be installed install on your system and colorama should be installed. Step to install are given for linux.
```
### Installation [For linux] :-
```
foo@bar:~$ sudo apt-get update
foo@bar:~$ sudo apt-get install python3
foo@bar:~$ pip3 install colorama
```

## Instructions To Play 

* Run the following command to start the game.

    ```
    foo@bar:~$ python3 run.py
    ```

* Use 'w', 'a' and 'd' to control player.

* Use 's' to fire bullets.

* Use 'Space' to activate shield around player.

## About this game
```
Din is a mandalorian living in the post-empire era. He is one of the last remaining members of his clan in the galaxy and is currently on a mission for the Guild. He needs to rescue The Child, who strikingly resembles Master Yoda, a legendary Jedi grandmaster. But there are lots of enemies and obstacles in his way, trying to prevent Din from saving Baby Yoda. Din is wearing classic mandalorian armour andhas a jetpack as well as a blaster with unlimited bullets. We’ve got to help him fight his way through and rescue Baby Yoda.
This game consists of one level. You will see that this game is quite a replica of the original game. You win when you defeat the **Boss enemy**. Rest of the details are stated below explicitly for each element of the game.
```

### Mandolian

* He is the main player of the game.

* Has 5 lives. Mandolian is respawned always at the current position  of him.

* Can activate shield to protect itself from obstacles

* Can fire bullets.

### Grid

* background keeps changing

* Has Floor and Roof 

### Beams

* There are three types of beams :-
1) Horizontal beam
2) Vertical beam
3) Diagonal beam

* comes randomly at any point

* Mandolian loses a life on colliding with a beam

* Can be destroyed by a bullet fired by Mandolian

#### Magnet

* Comes randomly at any point

* Constantly attracts Mandolian towards it if it is in certain range

* Can't be destroyed

### Boss_enemy

* Comes at end of the game

* It is the Hardest enemy to defeat

* Fires iceballs that looks similar like bullets

* Adjust its position in accordance with Mandolian's y-coordinate

* Has 5 lives

* Once Mandolian defeats him, game is over

### Iceball

* Fired by Boss_enemy

* Mandolian loses a life on colliding with a iceball

* Are fired at every 0.5 seconds

### Shield

* Used to shield Mandolian from obstacles and iceballs

* refills at every 60 unit time

* Once occupied, it lasts for 10 unit time

* If Mandolian collides with obstacle or iceball, shield disappears saving one life of Mandolian

* can be occupied by pressing 'Space' if shieldmode is True


### Speed_booster

* Comes randomly at any point 

* Game speed increases on collecting it

* Once occupied, it lasts for 10 unit time


### Score 

* Increases on destroying beams, collecting coins and beating the Boss-enemy


### SPECIAL FEATURES 

* Different colors are given to different components of the game
* Sound has been added
* ASCII Art has been used
