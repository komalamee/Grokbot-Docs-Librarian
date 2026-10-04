# Listing: The Librarian

**DRAFT: the wording still needs the owner's approval.** Nothing here is final, and nothing goes to the marketplace until the bot has been tested and the owner has said yes.

## Name
The Librarian   (one spelling everywhere)

## One-line pitch
A library for your contracts, policies and any long document you might need to look back at.

## What it does
- **Files straight from your email.** It finds your contracts, policies and long documents and files them as they arrive.
- **Indexing.** It keeps a catalog of everything it has filed, with the type, provider, key dates and a link back to each one, in a Google Sheet you own.
- **Tracks your renewals.** When something is 30 days or less from renewing or ending, it tells you once and asks whether you want to renew or cancel.
- **Answers from your documents.** Ask what a policy or contract says, and you get the answer with the exact clause quoted and a link to the document.

## Routines you can switch on
An inbox check for new documents (daily at 09:00 your time is the suggestion; you pick the frequency), a renewal alert for anything 30 days or less away, and a look-ahead on the 1st of the month. All three start off, each run uses tokens, and it asks which ones you want. Say "stop" any time.

## Who it's for
Anyone who would rather not file things away but wants them filed, organised, and ready to be asked questions like a database.

## What it connects to
Gmail (read access) to find your documents and spot new sign-ups, and to draft emails that only you send. Google Sheets (edit access) for the index. Google Drive (edit access) only if you want your files copied there. It can also save them to a folder on your own computer, asking your approval there each time, or to another service you name if that service's connection can save files. Google Calendar (edit access) only if you want renewal dates added. Each is offered when it's needed.

It keeps a private text copy of your documents on its own computer so answers are quick and use fewer tokens. It's never shared.

It can't read a document behind a DocuSign link, a password-protected file or a member-only portal. It files what the covering email says, tells you which ones it couldn't open, and adds any of them if you send it the file.

## Try saying   (a bot template can't carry example prompts, so these also go to whoever writes the launch posts)
1. "Am I covered for car hire excess in Portugal?"
2. "Talk me through exactly what car rental insurance I've got across all my credit cards."
3. "What do I need to know about my travel insurance policy?"
4. "What's coming up for renewal next month?"

## Made by
Komal Amin

<!-- No disclaimer: this bot carries none anywhere. Don't add one. -->
<!-- Check before publishing: every line maps to a behaviour tested in proof/. No embellishment, no invented detail, no prices, install counts, testimonials or outcome promises. -->
