##Simple Tic Tac Toe AI

Optimizing minimax algorithm

| Version | Feature | Time (s)* | States Visited | Cache Size |
| ------- | ------------- | --------- | ---------------- | ---------- |
| v1      | minimax                              | 6.545383300050162 | 549 945 | N/A |
| v2      | transposition table                  | 0.23668800003360957 | 16 167  | 4520 |
| v3      | alpha beta pruning (no TT)           | 0.24701559997629374 | 10 116 | N/A |
| v4      | TT + AB pruning                      | 0.07084299996495247 | 4 606 | 2000 |
| v5      | custom copy instead of copy.deepcopy | 0.02381239994429052 | 4 606 | 2000 |
| v6      | undo turn instead of copy            | 0.02116180001758039 | 4 606 | 2000 |
| v7 **   | account for symmetries in moves      | 0.08243879990186542 | 1624 | 776

*time passed on first execution of minimax algorithm measured using Time.perf_counter().

** v7 uses different implementation of TicTacToe which is slower, need to look into this
