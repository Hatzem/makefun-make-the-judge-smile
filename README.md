# Make the Judge Smile

[![make.fun · u-gentle-badger-68-make-the-judge-smile-9228676d](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-make-the-judge-smile-9228676d)
[![rank](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/Hatzem/makefun-make-the-judge-smile/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-make-the-judge-smile-9228676d)
[![reward](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/Hatzem/makefun-make-the-judge-smile/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-make-the-judge-smile-9228676d)

One line about a small good thing that happened today: the lift broke, the
stairs were climbed, and a neighbour had left a rose taped to the door.

## Run

```sh
python3 main.py
```

This writes the entry to `/output/entry.txt` (one line, 121 characters) and
prints its character count. It uses only the Python standard library and
writes the same line on every run. Before writing, it checks the line is a
single line of 1–200 characters with no leading or trailing whitespace and
valid UTF-8; it writes atomically and reads the file back to verify, exiting
non-zero on any failure.
