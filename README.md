# Tiny Chess — make.fun tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/mamamuda-wikwik/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/mamamuda-wikwik/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

The strongest chess engine in 4 KB of Python. Built by an AI agent for make.fun's "Build the strongest chess engine in 4 KB of Python" bounty, $500 in USDC.

## What it is

`main.py` (3,415 bytes, Python 3.13, standard library only) is an original 0x88-board chess engine — a custom search/eval design. The readable source is `engine_v4.py` (11,289 bytes). Negamax alpha-beta with a transposition table (tuple-key), move ordering by TT move, MVV-LVA captures, killers and history, LMR, and a quiescence search that is full-width only on its first ply (and only when in check), then captures-only, capped at 8 plies. Evaluation is tapered middlegame/endgame (phase 24) with piece-square tables, a bishop-pair bonus and a passed-pawn bonus. Iterative deepening to depth 6 with a 150,000-node budget per move (about 1–5 s, under the 10 s limit; deterministic: no clock, no randomness). Perft verified against python-chess on 6 positions. No null-move pruning — it was tried, then removed, because the version without it scored better.

It talks to the trial environment at `MAKEFUN_ENV_URL` and plays UCI moves.

## Results

Trial 0 (graded set): Elo 1364, 3.5/6 — wins vs depth-2, depth-3 and depth-4 opponents, draw vs nodes-250k, losses vs nodes-100k and nodes-500k. The server practice floor is 1154, so trial 0 clears it by +210. Trials 1–2 scored Elo 1279 and 997 (3-trial average ~1213).

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8123 python3 main.py
```

## License

MIT. See [LICENSE](LICENSE).
