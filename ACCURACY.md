# How well it finds things

*Tested 11 November 2026.*

The connector is tested on a fixed set of questions with known answers. This page gives the results, misses included.

## Finding the right book

Each of 75 questions has a known right answer: a work the passage must come from. The test asks the live connector each question and checks whether a passage from that work is among the first 3 and the first 8 results.

| Kind of question | Questions | Right work in the first 3 | Right work in the first 8 |
|---|---|---|---|
| A remembered quotation | 19 | 17 | 18 |
| A paraphrase from memory | 16 | 8 | 9 |
| A doctrine question | 13 | 5 | 10 |
| A question in old spelling | 8 | 7 | 7 |
| A search narrowed by author, year or collection | 13 | 10 | 11 |
| An exact phrase | 6 | 6 | 6 |
| **All** | **75** | **53 (71%)** | **61 (81%)** |

- **It is strongest on quotations.** If you remember the words, it nearly always finds them.
- **It is weakest on paraphrases.** If you remember only the gist, it finds the passage about half the time. Try two or three phrasings, or one distinctive phrase.
- **A miss doesn't always mean a wrong answer.** On doctrine questions several works say much the same thing, and the test counts only the one named in advance.

## Saying when it has nothing

Each result is marked as an exact, close, partial or loose match. When nothing is close, the result opens with "NO CLOSE MATCH". When everything is loose, it opens with "NOT FOUND". The cut-offs were set from the searches below, which were then run against the live connector.

| Test | Searches | Outcome |
|---|---|---|
| Subjects the library has nothing about (a home server, a sourdough starter, a salary cap) | 10 | All 10 came back "NOT FOUND". |
| Modern authors the library doesn't have (Barth, Lewis, Keller, Packer and others) | 10 | 8 came back "NO CLOSE MATCH". 2 came back with a close match, because older writers in the library say something very similar. |
| The 75 questions above | 75 | 6 came back "NO CLOSE MATCH". In 4 of those the right work really was missing from the results. In the other 2 it was there. |

In this test "NOT FOUND" was never wrong. A "close" match means the passage is about what was asked. It doesn't mean it is by the author you named, so check the author and title on every result.

## What isn't measured

- **The AI app's answer.** These tests cover what the connector returns. Your AI app then writes the answer, and it can summarize badly or quote from memory. Nothing here measures that.
- **Errors in the texts.** Scanned books have misread letters. The error rate hasn't been measured yet.
- **Whether the best passage came first.** The test counts a passage from the right work. It doesn't judge whether it is the best passage in that work.

## The questions are public

The 75 questions, the 20 searches the library can't answer (`unanswerable.jsonl`) and the test itself are in the connector's code: [`tests/eval`](https://github.com/Christian-open-library/Connector/tree/main/tests/eval). When someone reports a missed book or a bad quotation, it becomes a new question in the set.
