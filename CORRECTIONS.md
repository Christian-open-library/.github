# Corrections log

Errors found and fixed in the books, the connector and the library's public pages, newest first.

To report one, use the [feedback form](https://github.com/Christian-open-library/.github/issues/new?template=connector-feedback.yml) (public, needs a GitHub account) or write to hello@christianopenlibrary.org.

## 11 November 2026

### Public pages

- **"Exactly as printed" was wrong.** The front page said passages were returned exactly as printed. They are returned exactly as they stand in the library's copy, and the copies have errors, most of all in scanned books. The page now says so.
- **Not every result has a year and page.** The front page and the connector's description promised both. Some sources give neither. Both now say "where the source gives them".
- **"Stores no accounts" and "private by design" said too much.** Sign-in accounts are held by WorkOS, and search words go to Voyage AI. The claims are replaced by [a page naming everyone who sees a question](PRIVACY.md).
- **The Voyage AI account is now opted out of data use.** Until today it wasn't, so Voyage's terms allowed it to keep search words and use them to improve its models.
- **"No affiliation with any church or denomination" was reworded** to what is meant: no church or denomination directs or endorses the project.
- **The security review is described more exactly.** It was carried out with Claude, Anthropic's AI. It wasn't an outside audit.
- **Monergism's editions were removed.** I asked Monergism for permission to keep 338 texts taken from its free ebooks. Monergism replied that its editions may not be placed in another library, database or AI system, so all 338 were removed from the library and the connector. A separate collection of Monergism's ebooks that had been shared with library members is no longer shared. The same works will be added again from other sources.
- **The first removal of Monergism's editions was incomplete.** It took out each work's main file but left 342 "Part" files, which hold the text of the 98 longer works, in the library members can download. They were found and removed later the same day. They were not in the connector's catalogue.
- **Most of the removed works are back, from other sources.** Of the 338 works, 126 were already in the library inside their authors' collected Works. Another 161 were added again from independent copies: EEBO-TCP, Project Gutenberg and Internet Archive scans. 51 are not back: 12 were Monergism's own compilations, and for 39 no usable independent copy was found.
- **The count of works was corrected** to about 4,400 after the removal, then to about 4,600 once the restored works were added.
- **CCEL is now credited.** CCEL confirmed that its texts may be quoted and used as long as its files are not sold.
- **Credit added for the Greek and Latin texts.** They come from the Open Greek and Latin Project under CC BY-SA 4.0. Each file and the front page now give the credit, the license and a note of what was changed.

### The connector

- **A missing book is now said plainly.** Asking for a book the library doesn't have used to return loosely related titles with a small note at the end. The result now opens with "NOT FOUND" and tells the AI not to quote the book from memory.
- **Results now say how well they match.** Each is marked exact, close, partial or loose. When nothing is close, the result opens with "NO CLOSE MATCH" or "NOT FOUND".
- **Scanned passages are now marked in search results.** Before, only the book listing said a text was a scan.

### The books

- **Reprint years were shown as publication years.** Eight works carried the year of a modern reprint. Each now has the year the work, or the translation in the file, was first published:
  - Barnes's *Notes on the New Testament*: 1949 corrected to 1832.
  - Edersheim's *Life and Times of Jesus the Messiah*: 1953 corrected to 1883.
  - Lightfoot's *Apostolic Fathers*: 1956 corrected to 1891.
  - Thomson's *Life of Dr Owen*: 1965 corrected to 1850.
  - Torrey's *Person and Work of the Holy Spirit*: 1974 corrected to 1910.
  - Van Braght's *Martyrs Mirror* (Sohm's translation): 1950 corrected to 1886.
  - MacDonald's *The Princess and Curdie*: 1934 corrected to 1883.
  - Finney's *Power From On High*: 1944 corrected to 1871, when its chapters began to appear.
- **459 works had no year and now have one.** 204 Greek and Latin texts take the year of their print edition. 219 other works take the year printed in the book itself. 36 volumes of Spurgeon's sermons take the year of the volume. About 440 works still have no year.
- **Broken characters were repaired in 40 files.** More than 2,400 dashes, quotation marks, accented letters and Greek letters had been damaged when the texts were copied, most of them in the *Treasury of Scripture Knowledge*, ten volumes of Spurgeon's sermons and Hannah Whitall Smith's *Old Testament Types and Teachings*. Each was restored from the source. 179 could not be recovered and are left as they are, 170 of them in one diagram in the *Treasury*.
