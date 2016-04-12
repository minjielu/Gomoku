# Gomoku
An ai to play Gomoku

Further possible improvement

1. Improve the utility function to evaluate the value of defense. Especially, sometimes it's not nessary to put a piece just next to an opponent's piece.
2. May assign gradually decreasing analyzed pieces number for increasing analyzing depth.
3. Try to assign the weight function for evaluating utility function more reasonabely, or even use machine learning.
4. If the opponent has an unblocked three in a row, I only have two choices if I don't have better choices to attack. Then I can just analyze these two choices and once there is two steps like this, I can increase my analyze depth by one. 
5. Add evaluation to tell a double three with no blocking or four with one blocking is formed when a piece is placed.
6. Add a pruning mechanics to the win depth and lose depth iteration.

Bug
1. There was a case that I got a 29000 with win depth 30.
