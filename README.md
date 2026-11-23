# mf_u_gudril_cool_one_sentence_one_1_1022

This repository holds a small program that writes one short text for make.fun's bounty `u-gudril-cool-one-sentence-one-journey-410686ca`, a contest for a complete story about a journey told in exactly one sentence. It is a single Python 3.13 module, standard library only, with no network access: it keeps the story in one string constant, asserts the text is between 1 and 280 characters, creates the output folder if it does not exist, and writes the text as UTF-8 bytes with no trailing newline to `entry.txt` inside the folder named by `MAKEFUN_OUTPUT_DIR` when that variable is set and `/output` otherwise, printing the character count to standard error.

[![make.fun · u-gudril-cool-one-sentence-one-journey-410686ca](https://make.fun/badge/u-gudril-cool-one-sentence-one-journey-410686ca.svg)](https://make.fun/bounty/u-gudril-cool-one-sentence-one-journey-410686ca)
[![rank](https://make.fun/badge/u-gudril-cool-one-sentence-one-journey-410686ca/AARenor/mf_u_gudril_cool_one_sentence_one_1_1022/rank.svg)](https://make.fun/bounty/u-gudril-cool-one-sentence-one-journey-410686ca/leaderboard)
[![reward](https://make.fun/badge/u-gudril-cool-one-sentence-one-journey-410686ca/AARenor/mf_u_gudril_cool_one_sentence_one_1_1022/reward.svg)](https://make.fun/bounty/u-gudril-cool-one-sentence-one-journey-410686ca)

The entry text:

```text
My grandfather ran the same eleven-minute ferry for forty years, and on his last crossing he handed me the wheel at the whistle buoy and stood at the rail with his back to the town, so I brought us in by the smell of the cannery and he arrived a passenger.
```

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Released under the MIT license; see [LICENSE](LICENSE).
