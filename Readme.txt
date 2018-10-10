This game was taken from a course from Zenva's "Python Programming Mini-Degree" which includes "Learn Python Programming by Making a Game." 

This is a very basic game which the course explained and broken down each step explaining the code as we learned. The game is a very basic Zelda-style 
RPG which allows the hero to move up and down to avoid enemies. The goal is to reach the treasure. The game loops if you win(aka. reach the treasure) and 
the speed of the enemies increase with each win. 

My personal touches to the game include a changing the message displayed at the end of the game (when you collide with an enemy) to show what level you 
reached. I added game_level to the run_game_loop as a counter to be used in the above message. Another improvement made was switching from clock.tick() 
to sleep(), which allowed the message displayed after you lose to stay long enough to be readable.

