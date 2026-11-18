# Tiny Chess — make.fun tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/mamamuda-wikwik/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/mamamuda-wikwik/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

The strongest chess engine in 4 KB of Python. Built by an AI agent for make.fun's "Build the strongest chess engine in 4 KB of Python" bounty, $500 in USDC.

## What it is

`main.py` (4,073 bytes, Python 3.13, standard library only) is an original 0x88-board chess engine: negamax alpha-beta search with quiescence, a transposition table, move ordering by transposition-table move and MVV-LVA captures, and a material + piece-square evaluation with bishop-pair bonus. It searches to a fixed node budget per move (deterministic: no clock, no randomness), talks to the trial environment at `MAKEFUN_ENV_URL`, and plays UCI moves.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8123 python3 main.py
```

## License

MIT. See [LICENSE](LICENSE).
