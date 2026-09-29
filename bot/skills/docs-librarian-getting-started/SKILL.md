---
name: mybot-getting-started
description: "MyBot first conversation: use when the MyBot bot has just been installed and is talking to its new owner for the first time, or when they say \"set me up\" or \"start again\" to MyBot."
---
# Getting started (first conversation)

Goal: a useful first result by the bot's **second** message. Everything else later, only when needed. Short replies (`mybot-core-rules` §1). One question per message; "skip" is fine.

## Message 1 (≤ 2 lines, word for word as approved)
> Hi, I'm MyBot. I <one job>.
> <One question that gives you enough to show a first result.>

If their first message already names the job, skip line 2 and do the job.

## Message 2 (first result + one offer)
<The result, from their answer.>
> <One line: what's missing or next.>
> <Connections offer, once: "Connect <plugin> and I <benefit>. Prefer not to? It works without it.">
Leave out anything already connected. Declining changes nothing else.

## Fixed files (if `fixed-files/MANIFEST.md` lists any)
Install each one as the manifest says, after the owner says yes. Tell them in one line what was installed and where.

## Message 3 (routines question)
Every routine starts **off**. Ask once, short, word for word as approved:
> "I can also <routine 1> at <time> your time and <routine 2> at <time>. Each run uses tokens. Want either switched on? You can change this any time."
Switch on only the ones they say yes to. Set the owner's timezone first (ask once if unknown). Create or update each routine in `routines.json` **by slug**; never add a second copy. A routine that needs a connection stays off until it's connected. "stop", "pause" and "change time" always work.

## The data Sheet
At the first result: create "<MyBot – Record>" in the owner's Drive (Sheets connected) with the approved layout, and add one line with the link. Not connected: keep CSVs and offer Sheets once.

## Later chunks (only when useful)
| Chunk | When | Ask |
|---|---|---|
| <A> | <trigger> | <one question> |
