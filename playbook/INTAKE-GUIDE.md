# Intake guide: how to run the conversation with Koko

Version 0.1 (29 Sep 2026). Use at gate ② (Goal and intake), after Koko picks an idea and before any spec.
Why: the bot must match how Koko pictures it. A clear goal and a real conversation matter more than any rule list.
Write-up template: `templates/INTAKE.md` → the bot's `docs/INTAKE.md`.

## How to run it
- A real conversation, **one topic per message**, in plain words.
- Ask open questions. Listen more than propose.
- If I suggest something, say so: "My suggestion: …". It only counts if Koko says yes.
- After each topic, play back what I understood in 1–3 lines. Let Koko correct it before moving on.
- Never fill a gap with my own guess. Never copy Nomad Pro's (or any bot's) choices without asking.
- Not decided yet? Write it under "Open points" and move on.
- Log each update with the time Koko said it, as the Docs Librarian intake does. Record approved wording word for word.

## The 13 topics, in this order

**1. The goal line**
- Who is this bot for, in a few words?
- What is the one thing it should get done for them?
- How would you say it in one line?

**2. Who uses it and their situation**
- Who is the typical user? What's going on in their life or work?
- What do they do today instead, and what's annoying about it?
- Who is it *not* for?

**3. A normal day or week with the bot**
- Walk me through a normal day or week. When do they talk to it?
- What does it do on its own, without being asked?
- How often should they hear from it?

**4. The first result (by message 2)**
- What should they see by the bot's second message?
- What should it look like: a list, a bar, a table, an image?
- What's the smallest thing we need to ask to show it?

**5. What it must never do**
- What would annoy or worry you if the bot did it?
- Anything it must never say, send, change or delete?

**6. Tone, length and look of replies**
- How should it sound? Any words to avoid?
- How long should replies be? (Koko's usual: answer first, short, plain, visual. Same here?)
- Emojis, images, tables: yes or no?

**7. Onboarding (the first messages)**
- What should message 1 say?
- What do we ask now, and what can wait?
- When should it offer connections?

**8. Specific routines**
- What could it do on a schedule, and at what exact time?
- When should it stay quiet?
- All routines start OFF and the bot asks the user during setup which to switch on (each run uses tokens). Which ones should it suggest, and how should it word the question?

**9. The data Google Sheet**
- What should the Sheet keep? Who reads it, and what should they see first?
- Which parts does the user edit by hand?
- What should the summary show, and which period should its dropdown pick (month, year, tax year)?
- I'll show a screenshot mock-up with fake data before building it.

**10. Connections needed and why**
- Which apps should it connect to (Gmail, Calendar, Drive, Sheets, other)?
- What does each do for the user? Which are must-have, which nice-to-have?
- Does anything need to be installed on the user's computer on import (fixed files)?

**11. Does the subject need a disclaimer at all?** (default: no)
- Does it touch health, money, law or similar, where a wrong answer could hurt someone?
- If yes: what should it never claim, and the exact words.

**12. What "working" means to you**
- How will you know the bot is working?
- What would make someone come back next week?

**13. Example conversations**
- Can you picture 2–3 real chats? What does the user say, and what does the bot answer?

## After the session
- Fill `docs/INTAKE.md`. Mark open points; don't guess them.
- Koko confirms it. Then fill `docs/SPEC.md` from it. Every spec choice traces back to the intake or is a suggestion Koko approved.
