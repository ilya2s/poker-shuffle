# Poker Shuffle
Poker Shuffle is a solitaire poker game where the player draws 25 cards one at a time and places them on a 5x5 grid to form poker hands, aiming to maximize the total point value.

## Gameplay
- Draw cards one at a time by clicking on the deck.
- Place cards on the 5x5 grid by clicking on a blank square.
- Move cards around the grid by selecting a card and clicking on a different blank square.
- The game ends when the 25th card is placed and the final score is displayed.

![image](https://user-images.githubusercontent.com/42526358/213894182-1e127670-9807-4057-8ba3-ed04e881eddf.png)

## Scoring
- Different poker hands, such as flush, full house, and straight flush, have point values assigned to them.
- Hands are scored for each row and column, and the total score is displayed at the bottom right of the grid.
- The player's goal is to maximize the total point value by forming the best possible hands.

## Images
- Card images are in SVG format and are accessed from the codeboot.org server.
- A silhouette of a card is used to represent blank spaces on the grid.

## Technical details
- The game was developed using Python and codeBoot, a framework that allows for modifying the DOM and handling events.
- The game doesn't require writing HTML or CSS as all the code, including HTML and CSS, is in the tp2.py file.
- The game can be launched by executing the init() function in the tp2.py file.
- The HTML and CSS for the game were generated using Python, with the help of functions, loops or map to avoid repetition of code.
- The game utilizes onclick events and the DOM to handle user input.
