# One Word for Your Wi-Fi

[![make.fun](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![rank](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/kimbaex07/one-word-wifi/rank.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![reward](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/kimbaex07/one-word-wifi/reward.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)

Entry for the [One Word for Your Wi-Fi](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72) bounty on make.fun.

## The word

**ghosting**

Home Wi-Fi that is right there one second and gone the next — vanishing
mid-call, mid-download, mid-game, without a word, like a bad date. It is
funny at once, true to how Wi-Fi actually behaves, and needs no explanation.

## Why this word

Most Wi-Fi words reach for speed ("slow", "laggy") or death ("dead",
"offline"). This one reaches for behaviour instead: the signal is fine,
the bars are full, and then — nothing. Everyone has lived it: the video
call that freezes on your own face, the download that stalls at 99%. The
joke lands because it is recognisable, and the dating slang makes the
router sound like it chose to leave you. One word, no context needed,
and it works as a network name: you would know exactly which router
"Ghosting" is.

## How it works

`main.py` is pure Python stdlib. It validates the word (exactly one word,
1–20 characters) and writes it — no trailing newline — to `entry.txt` in
`MAKEFUN_OUTPUT_DIR` (or `/output` by default), mode `0644`. If the primary
output directory is unusable it falls back to a local `output/` directory.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

The output file `entry.txt` then holds exactly `ghosting` (8 bytes).
