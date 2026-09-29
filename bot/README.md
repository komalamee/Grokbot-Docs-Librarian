# <Bot name> (Grok Bot template)

<one line, from the agreed goal line> · Live link: not published yet · Current version: none

| Folder / file | What |
|---|---|
| `bot.json` | Profile, connections (`pluginId` strings), memories, getting-started skill |
| `routines.json` | The one source for routines. Every routine `"enabled": false` |
| `skills/` | `mybot-getting-started`, `mybot-core-rules`, `mybot-main-job` (rename `mybot`) |
| `fixed-files/` | Files that install on the user's side on import, listed in `MANIFEST.md` |
| `docs/` | `INTAKE.md`, `SPEC.md`, `RETEST.md`, comparisons, website handoff |
| `listing/` | Marketplace listing copy and images |
| `proof/` | Screenshots and test-run evidence for each release |
| `samples/` | Fake data only: Sheet mock-ups, sample files |
| `args/` | Generated share args (by `build.py`; never hand-edited) |
| `build.py` · `banned_scan.py` · `banned.txt` | Build with hard checks; banned-word and private-data scan |

Build: `python3 build.py --private-terms ../private-terms.txt` (add `--check-live <live skills folder>` before release).
Scan: `python3 banned_scan.py skills listing args --banned banned.txt --private-terms ../private-terms.txt`.
