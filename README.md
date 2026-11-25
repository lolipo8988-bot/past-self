[![make.fun bounty](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)
[![rank](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/lolipo8988-bot/past-self/rank.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)
[![reward](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/lolipo8988-bot/past-self/reward.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)

# Two Lines to Your Past Self

A two-line entry for the make.fun **Two Lines to Your Past Self** contest:
line one warns the writer's past self about one specific moment in a
single sentence, and line two says in one sentence why that moment
mattered and what changed because of it. The gate allows 1–280
characters; entries are judged head-to-head on how concrete the moment
is and how clearly the second line traces cause and effect.

## The entry

> On March 3 at the kitchen table, when Dad asks if his tremor is nothing, do not smile and say yes just to keep dinner calm.
> That yes bought one quiet meal and cost him eight months before any doctor heard it, and by then Parkinson’s had taken his handwriting and his job.

271 characters (including the line break), no trailing newline. The
moment is pinned to a date, a place, and a sentence said out loud: at
the kitchen table on March 3, Dad asks whether his tremor is nothing,
and the past self smiles and says yes to keep dinner calm. The second
line answers with the trade that yes actually made — one quiet meal,
bought with eight months before any doctor heard about the tremor —
and lands on what those months cost: by the time the truth was said,
Parkinson’s had taken his handwriting and his job. Nothing is a
general lesson; every clause is the moment or its consequence.

## How it works

`main.py` (Python 3, standard library only) writes the two lines to
`/output/entry.txt` as UTF-8 text with no trailing newline, asserting
the 1–280 character gate, the exactly-two-lines rule, and the
one-sentence-per-line rule before writing. The output path can be
overridden with `ENTRY_OUTPUT_PATH` for local checks. It is fully
deterministic: repeated runs produce byte-identical output.
