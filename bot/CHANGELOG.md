# Changelog: Docs Librarian

One entry per version. Repo tag = marketplace card version. Add the listing URL right after Koko presses Publish.

## v0.1.0 (not published) · 29 Sep 2026
- Made from grokbot-template v0.1.
- Repo set up: `bot-skeleton/` became `bot/`, `mybot` / `MyBot` became `docs-librarian` / `Docs Librarian`.
- `docs/INTAKE.md` and `docs/SPEC.md` added unchanged, as agreed with Koko.
- `bot.json`: profile from the agreed goal line, the four connections from SPEC §10, general memories.
- `routines.json`: the three routines from SPEC §9, every one `"enabled": false`.
- Skills written from the spec, replacing the setup placeholders: `docs-librarian-getting-started` (SPEC §4 and the approved messages in Appendix A), `docs-librarian-core-rules` (§7, §11), `docs-librarian-library` (§3 to §7) and `docs-librarian-renewals` (§8).
- Routine job text rewritten from SPEC §6, §8 and §9; all three stay `"enabled": false`.
- Fixed files: `index-sheet-layout.json` (§5) and `folder-set.json` (§4). The repo is public now, so both are fetched at setup from raw URLs on `main` rather than embedded; `MANIFEST.md` lists each one and the skill that uses it.
- `listing/LISTING.md`: a draft from the spec for the owner to approve.
- `bot.json`: memories rewritten from the spec. `banned.txt` mirrors the core-rules list, drawn from §11.
- Build and scan run clean; `args/create_bot_share_json.args.json` is a pre-test build, not a release.
