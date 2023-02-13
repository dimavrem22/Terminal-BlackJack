<h2>How to run program:</h2>
- The program only uses the 'random' library from python. No need to install other dependencies. <br/>
- Navigate to submission directory in your terminal. <br/>
- Ensure that 'blackjack.py' have executable permissions. <br/>
- To run game, use the './blackjack.py' command.  <br/><br/>

<h2>Assumptions and choices:</h2>
None. I understood the assignment.  <br/><br/>

<h2>What I did well:</h2>
- Good choice of data structures used to represent the game state. <br/>
- The code is broken down into many helper functions which makes it easy to test. <br/> 
- The code is well commented allowing for readers to follow along fairly easily. <br/><br/>

<h2>Design and Algorithm Choices:</h2>
- The card deck is represented as a list of strings. 
- There is a function which maps the card string onto a value. <br/> 
- The card deck is randomized prior to the start of the game and each time a card is drawn, I pop the first value in the list. <br/> 
- The dealer's and player's hands are representated as lists of strings. <br/> 
- On each card draw, the score of player's and/or dealer's hands are reevaluated and the result is stored in a variable. <br/> 
- The logic of the game begins with card shuffling and dealing of cards. There is a loop to represent player's actions while they hit, until they bust, stand, or get blackjack. If the game did not end after the player's turn, we loop through the dealer's turn until the dealer reaches 17+ score, busts, or gets blackjack. If neither player busted or got blackjack, there is a function which takes the state of the game and determines the winner or tie. <br/> 
- When evaluating the hand score including aces, we test 2 scenarios. Since no more than 1 ace can have a value of 11, we calculate the hand score with 1 ace as 1/11 and the remaider as 1. If the higher score is less than or equal to 21, we use that one. Otherwise we use the smaller number. <br/> <br/>

<h2>Tradeoffs:</h2>
The main tradeoff was the decision between implementing the game in a scripting manner vs closely following Object Oriented Design principles. For the sake of time, I decided that the game was simple enough to avoid representations of game state using rigid classes, however, this makes it more difficult to reuse this code for implementing variations of the game. <br/><br/>

<h2>Future Improvements:</h2>
Given more time, I would make the game function more modular. I would separate the player's moves, and dealer's moves into separate functions. This would make it easier to test the game logic with autiomated tests. Additionally, I would create a class to represent the game state following principles of OOP. This would help maintain all of the game related variables in a more organized manner allowing for smoother adjustmenets in the future if the rules of the game were to change, or if we wanted to add layers of complexity. <br/><br/>
I would also allow the player an option to continue playing after one round of the game is over. Perhaps, keep a score between the player and the dealer. <br/><br/>

<h2>Manual Tests:</h2>
I played the game myself at every step of the development process. This way, noticed that my implementation way flawed when the player was dealt a blackjack with the first 2 cards, but was still given a choice to stand or hit. I had to modify the player's turn loop in order to check for blackjack or busts prior to making nay decisions. <br/><br/>

<h2>Automated Tests:</h2>
- Navigate to submission directory in your terminal. <br/>
- Ensure that 'tests.py' have executable permissions. <br/>
- To run automated tests, run './tests.py'. <br/><br/>
