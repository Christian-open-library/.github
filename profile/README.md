<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Christian-open-library/.github/main/profile/banner-dark.svg">
  <img alt="Christian Open Library" src="https://raw.githubusercontent.com/Christian-open-library/.github/main/profile/banner-light.svg" width="100%">
</picture>

A curated library of public-domain books in clean, searchable text, centered on the Christian tradition:

- **Theology and devotion:** the Church Fathers, the Reformers, the Puritans, Edwards, and historic creeds and confessions.
- **Commentaries and original-language help:** verse by verse, including Calvin, Matthew Henry, Gill, Poole, and Keil and Delitzsch on the Old Testament, plus Greek and Hebrew lexicons and grammars, the Expositor's Greek Testament, Trench's *Synonyms*, and the Treasury of Scripture Knowledge.
- **Sermons:** Spurgeon, Whitefield, M'Cheyne, Chalmers, and Simeon's 2,500 sermon outlines on the whole Bible.
- **Journals:** the Princeton Review and its successors (1831–1929), with articles by Charles Hodge, the Alexanders, Warfield and Machen, and the Danville Quarterly Review.
- **Poetry and fiction:** Herbert, Milton, Donne, Rossetti, George MacDonald, Chesterton, Dostoevsky, and more.
- **Philosophy:** Plato, Aristotle, the Stoics, Descartes, Spinoza, Locke, Hume, Kant, Hegel, Nietzsche, Mill, William James, and more, in older translations.
- **Classics and other traditions, for context:** Homer, Virgil, Thucydides, the Greek tragedians, Confucius, Lao Tzu, the Bhagavad-Gita, the Koran, and Maimonides.
- **Reference:** seven Bibles, classic Bible dictionaries, and The Fundamentals.

It is curated by [Matt Miller](https://github.com/mattm4444).

## What's here

| Collection | What it holds | Access |
|---|---|---|
| **The Library** | More than 4,600 public-domain and Creative Commons works, from antiquity to the 1920s, in their original editions where possible: theology, commentaries, sermons, journals, philosophy, poetry and fiction | Free, by invitation |
| **AI connector** | Search the whole library from Claude, ChatGPT, Gemini and other AI apps that support connectors, by meaning, with quotations, page citations, seven Bibles (Berean Standard Bible by default), dictionaries, and a finder for which historic writers cited any verse | Free for anyone: sign in with your email or GitHub |

**Browse every title:** [`catalog.csv`](https://github.com/Christian-open-library/.github/blob/main/catalog.csv) (author, title, year, type).

## Use the AI connector

Free for anyone; no invitation needed. Add this address to your AI app, then sign in with your email (you'll get a code) or with GitHub when it asks:

```
https://mcp.christianopenlibrary.org/mcp
```

- **Claude:** Settings → Connectors → **Add custom connector**, paste the address, then **Connect**.
- **ChatGPT** (paid plans): Settings → Apps & Connectors → turn on Developer mode → **Create**, paste the address, choose OAuth.
- **Gemini:** Settings → Connected Apps → **Add a custom app**, paste the address.

Menu names change from time to time; look for "connectors" or "MCP" in your app's settings. Each person has a fair-use daily limit.

The connector's code is open: **[read the source](https://github.com/Christian-open-library/Connector)** and the **[security review](https://github.com/Christian-open-library/Connector/blob/main/docs/security-review.md)**. It stores no accounts, documents or conversations, and it only reads public-domain and openly licensed books.

## Download the books

The books themselves are shared by invitation. **[Request access](https://github.com/Christian-open-library/.github/issues/new?template=request-library-access.yml)**, accept the invitation email from GitHub, then open the library and choose **Code → Download ZIP**, or clone it with git.

## Help the library grow

- **[Suggest a book](https://github.com/Christian-open-library/.github/issues/new?template=suggest-a-book.yml)** you've found in a public-domain source.
- **[Connector feedback](https://github.com/Christian-open-library/.github/issues/new?template=connector-feedback.yml):** tell us when the AI connector missed a book or quoted out of context. Each report becomes a test the connector has to pass.
- Members can add books directly by pull request, following the library's contributing guide.

Only free-to-share texts are accepted:

- public domain (generally published in the US before 1931);
- Creative Commons licensed.

Every addition is checked for copyright and duplicates before it goes in.

## Why you can trust it

- **Quotations are verbatim.** The connector returns passages exactly as printed, with author, title, year and, where the source has page numbers, the page, so you can check any quote against its source.
- **Every book names its source.** Each file records where its text came from and its license. Only public-domain and openly licensed works are included, and scanned books are marked as scans.
- **Original wording.** Spelling and wording are kept as printed. Where a text was cleaned up or part of a work was left out, its file says so.
- **Private by design.** The connector doesn't store your conversations, documents or accounts.
- **Open and reviewed.** The [code is public](https://github.com/Christian-open-library/Connector), and so is its [security review](https://github.com/Christian-open-library/Connector/blob/main/docs/security-review.md).
- **Independent and ad-free.** An independent project curated by Matt Miller, with no ads and no affiliation with any church or denomination.

## Support the library

The library and the AI connector are free for everyone. If they're useful to you, you can support Matt Miller's work on them. The card shows what the connector costs to run each month, and it updates as more people use it.

<a href="https://github.com/sponsors/mattm4444">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://mcp.christianopenlibrary.org/support.svg?theme=dark">
    <img alt="What the AI connector costs to run this month, and how it's covered" src="https://mcp.christianopenlibrary.org/support.svg?theme=light" width="720">
  </picture>
</a>

**[Give through GitHub Sponsors](https://github.com/sponsors/mattm4444)**, monthly or once. Gifts go to Matt personally to support his work on the library, and aren't tax-deductible.

## Credits

- **Greek and Latin texts.** The Greek and Latin texts of the Church Fathers and Philo, and Yonge's English translation of Philo, come from the [Open Greek and Latin Project](https://github.com/OpenGreekAndLatin) at the University of Leipzig ([First1KGreek](https://github.com/OpenGreekAndLatin/First1KGreek) and [csel-dev](https://github.com/OpenGreekAndLatin/csel-dev)), licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). They were converted from the project's TEI XML to Markdown, and the library's copies are shared under the same license.

## Copyright and security

- **Copyright concern?** If you believe something in the library shouldn't be here, use the **[copyright concern form](https://github.com/Christian-open-library/.github/issues/new?template=copyright-concern.yml)**. We review it and remove the material promptly.
- **Security:** the connector is read-only and was put through a structured security review. Read the [summary](https://github.com/Christian-open-library/.github/blob/main/SECURITY.md). To report a problem privately, use **Report a vulnerability** on that page's repository.

<p align="right"><sub><samp>// soli deo gloria</samp></sub></p>
