# Tic-Tac-Toe AI

Classic tic tac toe game that has a reinforcement learning model that learns how to play. You can train the model, against a player that plays randomly, a human player, or itself (robot wars). 

## Getting started

1. Have Python 3.7.3. 
1. Make sure to install modules from `requirements.txt`
1. Run with `python main.py` 

For now, if you want to change the type of players involved, you have to explicitly change it in the code. You can find all the implementations of the player entity under `engine/player`.
The `.save` files represent the model's learning progress. If you delete them you have to train the model again. The progress is saved again every 10000 iterations. 
