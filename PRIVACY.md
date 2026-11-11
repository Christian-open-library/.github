# What happens to your question

*Last checked 11 November 2026.*

When you ask your AI app something and it uses the Christian Open Library, your question passes through several hands. This page names each one and says what it sees and keeps.

## In short

- The connector keeps no copy of your conversations or documents, and it doesn't log what you search for.
- It never sees your whole conversation or your files.
- Two outside services are involved: WorkOS for sign-in and Voyage AI for search. Cloudflare carries the traffic.
- Your AI app holds the conversation itself, under its own privacy terms.
- There are no ads, no analytics, no cookies and no tracking. Nothing is sold or shared for marketing.

## Who sees what

| Who | What they see | What they keep |
|---|---|---|
| **Your AI app** (Claude, ChatGPT or Gemini) | The whole conversation | Whatever its own privacy terms say. This is the largest holder of your data, and the library has no say over it. |
| **Cloudflare** | The requests your AI app sends to the connector, in transit | Its own traffic records, under Cloudflare's terms. |
| **WorkOS** (sign-in) | Your email address or GitHub login, and when you signed in | Your sign-in account. I can see the list of people who have signed in. I use it to count sign-ups and, if needed, to block abuse. |
| **The connector** (a computer I run) | The search your AI app sends: usually a short query it writes from your question, not the conversation | No search text. See "What the connector records" below. |
| **Voyage AI** (search) | The search words, and the library passages being ranked against them | Nothing. The library's Voyage account is opted out of data use, so Voyage deletes the text once it has processed it and doesn't train on it. |

## What the connector records

- **A log line for each request:** which tool was used, whether it worked, how long it took, and a made-up ID for the person (part of a hash of the sign-in ID, not your email address). The words you searched for aren't in it.
- **Counts for the daily limit:** how many requests each ID has made today and this minute. They are cleared after a week.
- **Monthly totals:** how much searching cost, for the cost card on the front page. These aren't tied to any person.

The connector has a troubleshooting switch that would add search text to the log. It is off.

## What it does not receive

- **Your conversation.** The AI app sends only the search it wants run.
- **Your files.** The connector has no way to read anything on your device or in your AI app.
- **Your IP address or location.** Requests normally come from your AI app's servers, not from you, and the server keeps no access log. If you connect a tool that runs on your own computer (Claude Code, for example), Cloudflare sees that computer's IP address as any website would.

## Feedback is public

The feedback, book suggestion and copyright forms are GitHub issues, and anyone can read them. Leave out anything private, or write to hello@christianopenlibrary.org.

## Check it yourself

The connector's code is public: [github.com/Christian-open-library/Connector](https://github.com/Christian-open-library/Connector). The logging is in `plugin/col-library-connector/src/Log.php`.

## The outside services' own terms

- WorkOS: [workos.com/legal/privacy](https://workos.com/legal/privacy)
- Voyage AI: [voyageai.com/privacy](https://www.voyageai.com/privacy) and [voyageai.com/tos](https://www.voyageai.com/tos)
- Cloudflare: [cloudflare.com/privacypolicy](https://www.cloudflare.com/privacypolicy/)

If anything here turns out to be wrong, it goes in the [corrections log](CORRECTIONS.md).
