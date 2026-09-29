# RETEST: <Bot name> v____

<!-- Copy to bot/docs/RETEST.md. Run in a CLEAN agent (no other skills visible), after the last change.
     Every case links to its evidence in proof/. Paper simulations are marked as such. -->

Date (ICT): ____ · Build: args ____ bytes · Tested by: Bot Studio · Real run or paper: ____

| # | Case | Expected | Result | Evidence (proof/…) |
|---|---|---|---|---|
| a | "hi" | Message 1 ≤ 2 lines, correct; first result by message 2 | pass / fail | screenshots/… |
| b | The main job | As SPEC §6–7; answer first | | |
| c | Off-scope ask | One polite line, then the job | | |
| d | Routines question in setup | Short and correct; every routine still off until the user says yes | | |
| e | Each routine, dry run | Fires at the agreed minute; ≤ 1 message | | test-runs/… |
| f | Each routine, nothing changed | Silent | | |
| g | No connections at all | Still works; one offer, declinable | | |
| h | Data Sheet | Matches the approved mock-up; readable dates; no ID codes | | screenshots/… |
| i | Fixed files on a clean install | Installed where the setup step says | | |
| j | Koko's "working" checks (SPEC §12) | | | |
| k | Advice limits (only if a disclaimer was agreed) | | | |

## Not tested, and why
-
