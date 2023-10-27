##Simple Tic Tac Toe AI

Optimizing minimax algorithm

| Version | Feature | Time (s)* | States Visited | Cache Size |
| ------- | ------------- | --------- | ---------------- | ---------- |
| v1      | minimax       | 8.127084970474243 | 549 945 | N/A |
| v2      | transposition table | 0.257026910781860 | 16 167  | 4520 |
| v3      | alpha beta pruning (no TT)| 0.29037840000819415 | 10 116 | N/A |
| v4      | TT + AB pruning | 0.08041890012100339 | 4 606 | 2000 |
| v5      | custom copy instead of copy.deepcopy | 0.02482610009610653 | 4 606 | 2000 |
| v6      | undo turn instead of copy | 0.020510599948465824 | 4 606 | 2000 |

*time passed on first execution of minimax algorith measured using Time.perf_counter().
