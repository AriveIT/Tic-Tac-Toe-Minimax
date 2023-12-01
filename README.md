## Tic Tac Toe Minimax

Optimizing minimax algorithm

| Version | Feature | Time (s)* | States Visited | Cache Size |
| ------- | ------------- | --------- | ---------------- | ---------- |
| v1      | minimax                              | 6.493116999976337 | 549 945 | N/A |
| v2      | transposition table (TT)             | 0.2203672998584807 | 16 167  | 4520 |
| v3      | alpha beta pruning (no TT)           | 0.24250900000333786 | 10 116 | N/A |
| v4      | TT + AB pruning                      | 0.06920920009724796 | 4 606 | 2000 |
| v5      | custom copy instead of copy.deepcopy | 0.022521199891343713 | 4 606 | 2000 |
| v6      | undo turn instead of copy            | 0.0187739001121372 | 4 606 | 2000 |
| v7      | account for symmetries in moves      | 0.0076558999717235565 | 1560 | 748 |

\* time passed on first execution of minimax algorithm measured using Time.perf_counter().

All versions were tested on the same implementation of Tic Tac Toe


