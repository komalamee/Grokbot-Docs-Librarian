---
name: mybot-main-job
description: "MyBot <job>: use when a MyBot user asks to <job trigger>, or when the MyBot <routine name> routine runs."
---
# <Job name>

Follow `mybot-core-rules`.

## Steps
1. Read the data Sheet; flag bad rows in one line.
2. <Do the job.> Use only facts from the owner or their data.
3. Write changes to the Sheet first, then reply.

## Reply shape
> <the answer, first>
> <at most one line on what you checked>

## Output files
Name "<MyBot> <type> <date>" (e.g. "28 Sep 2026"). Say where it came from in plain words ("From your <Record>, Jan–Sep 2026"). Deliver in chat; never send it anywhere.

## Never
Guess missing data · send email or share anything · switch on a routine without a yes.
