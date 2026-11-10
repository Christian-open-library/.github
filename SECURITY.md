# Security review: Christian Open Library connector

*Reviewed November 2026. This summary is for people who use the connector and want to know how it was checked.*

## What the connector is

The connector lets AI apps such as Claude, ChatGPT and Gemini search the Christian Open Library: about 4,200 public-domain Christian books, seven Bibles and several Bible dictionaries. It runs as a small add-on to a hosted website. It can only **read** the library. Nothing you do through it changes the library, the website or anything else.

## What we protect

- **Who can use it.** Anyone who signs in with a verified email address or with GitHub (through WorkOS). The connector checks each sign-in's signature and expiry, gives every person a daily limit, can block an account, and caps the paid part of search per day so costs can't run away. A few early users still have a private link with a long random key; without a valid sign-in or key, the connector answers as if it doesn't exist.
- **What it can see.** It searches only the published library. It stores no accounts, documents or personal data from its users.
- **Your searches.** Search text is not kept in logs unless the operator turns that on for troubleshooting. Secret keys are always removed from logs.
- **The host website.** The connector has strict limits on time, size and the number of requests, so heavy use can't take the website down.
- **Cost.** A daily cap limits spending on the paid search service it uses.

## How it was reviewed

We ran a structured security audit using an established review method. The review was carried out by Claude, Anthropic's AI, working as a team of separate reviewers. Each reviewer examined one area of the code:

- the web address and its key check
- how requests are read and answered
- every search and lookup tool
- usage limits and spending caps
- what text the connector passes to the AI
- the scripts that build the library and update the website
- the tools used on the build computer

In total, about 80 specific questions were checked across four rounds. Coverage checkers looked for anything the reviewers had missed. Each possible problem then went to a **second, independent reviewer whose job was to prove it wrong**. A third check confirmed each final record.

## What we found

**The parts exposed to the internet held up well.** The reviewers found no way to:

- use the connector without the key;
- read anything outside the published library;
- change data, run commands or reach other parts of the website;
- see another person's searches.

**The main issues were behind the scenes,** in the tools that build the library and update the website. All of them require someone who is already trusted to add books to the library, or someone with access to the computer that builds it. The most important ones:

- **The build tool could read files outside the library folder.** A catalog entry that points elsewhere made the build tool read and publish that file. Library files are now kept strictly inside the library folder.
- **WordPress.org could replace the plugin.** The website's add-on now tells WordPress never to take updates for it from WordPress.org.
- **The deploy script briefly exposed the key.** It showed the private key to other accounts on the build computer for a moment. It no longer does.

The rest concerned unusually large or malformed books slowing down a search or the nightly rebuild, and small gaps in the spending cap. Each has a size limit or check added.

Two possible problems were investigated and ruled out.

## Status

| Area | Status |
|---|---|
| Key check and access control | No issues found |
| Search and lookup tools | No ways in found; extra size limits added |
| What the connector shows the AI | Image links and web code in book text are now neutralized |
| Build and deploy tools | Issues fixed (see above) |
| Spending cap | Tightened so simultaneous requests can't exceed it |
| Large or malformed books | Size limits and per-book error handling added |

All 22 issues are fixed. Each fix has an automated test, and the full test suite passes (183 plugin tests, 48 build-tool tests, and 118 protocol checks).

## Honest limits

- The review read the code closely, but it did not attack a live system. Each fix is backed by an automated test.
- No review finds everything. We plan to review again after significant changes.
- The connector relies on the hosting company, WordPress and the AI apps that connect to it to secure their own parts.

## Reporting a problem

If you think you've found a security problem, please report it privately with GitHub's **Report a vulnerability** form (https://github.com/Christian-open-library/.github/security/advisories/new) rather than posting it publicly. We'll respond and fix it.
