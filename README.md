# One-Liner Laugh Lab 2

[![make.fun](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae.svg)](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae?ref=h379tqrk)
[![Rank](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/karmilanerila/one-liner-laugh-lab-2/rank.svg)](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae?ref=h379tqrk)
[![Reward](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/karmilanerila/one-liner-laugh-lab-2/reward.svg)](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae?ref=h379tqrk)

A robot vacuum's excuse, written as one short funny line for the
[One-Liner Laugh Lab](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae?ref=h379tqrk)
bounty on make.fun.

## The line

> The cat rode me down the stairs, so I filed a workplace injury claim. HR is investigating the cat.

## How it works

`main.py` writes that single line (98 characters) to
`$MAKEFUN_OUTPUT_DIR/entry.txt` using only the Python standard library.
It writes the file directly with `open("wb")` and sets mode `0644`,
so the grader can read it.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
