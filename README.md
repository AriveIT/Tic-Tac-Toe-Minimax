##Simple Tic Tac Toe AI

Optimizing minimax algorithm

| Version | Added Feature | Time (s)* | States Evaluated | Cache Size |
| ------- | ------------- | --------- | ---------------- | ---------- |
| v1      | minimax       | 8.127084970474243 | 549 945 | N/A |
| v2      | caching       | 0.257026910781860 | 16 167  | 4520 |
| v3      | alpha beta pruning | 0.08060610003303736 | 3063 | 2064 |

*time passed on first execution of minimax algorith measured using Time.perf_counter().

##Known bugs
 - v3 ties 10x often to RandomAgent than v1 and v2
