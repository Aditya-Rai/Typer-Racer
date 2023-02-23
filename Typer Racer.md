# Typer Racer
## Working of the game

- Taking Name and email id of the user that will play the game
- A random paragraph is generated which approximate size can be controlled, e.g. how many sentences to include in the paragraph
- The game does not start until the player starts typing in the textarea provided, once the user starts typing the 60 secodns counter starts.
- If the player types the correct character as the paragraph shown, the color of the paragraph turns green and if the character is wrong, from that point the color does not change thus making the player realize that the player is typing wrong characters.
- If the player submit the game by own, the result is shown, else when the timer is over the player is shown the result based on the amount of words the player was able to type in 60 secodns.
- Also the name and the email field is compulsory to type else the player cannot submit the game.
- After submitting the game the player can see the WPM, Accuracy and the Position or Rank as compared to all the participating players. 
- The player can also see the Leaderboard which has the top 10 players according to their WPM in descending order.


### How game was developed 

##### Tech Stack
1. Python - [All the logic implementation is done using python]
2. HTML, CSS, Bootstrap, JS [For making the Frontend and using Javascript for eventlisting]
3. Flask framework

##### Folders and Files
- static contains
1. logo.jpeg [Logo used in the website]
2. styles.css [Css file for designing]
3. top_players.csv [Initially this file is not present untill we run the program once the program is executed the file is generated automatically]

- templates cotanis
1. index.html [Landing page]
2. sumbit.html [Page that is shown when the user submits the game]

- app.py [The main flask file that we need to run indorder to run the app]
- data.csv [This file contains data of all the players playing the game, this is also not present intitally, this is automatically generated when the game is played atleast once]


##### How to run the app
- python3 app.py 


## Installations

1. numpy
```
pip install numpy
```

2. pandas
```
pip install numpy
```
3. Flask
```
pip install flask
```
4. requests
```
pip install requests
```
5. DocumentGenerator
```
pip install essential_generators
```