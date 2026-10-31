# Catholic Cross References

A cross-reference system for the Catholic Bible, built in the open and given to the Church as public domain — anyone may use it freely, for anything, forever.

Modern Catholic Bibles are nearly bare of cross references in the seven books the whole Church read as Scripture for fifteen centuries — Tobit, Judith, Wisdom, Sirach (Ecclesiasticus), Baruch, and 1–2 Maccabees — and in the added chapters of Esther and Daniel. The big reference collections used by most Bible apps cover only the 66 books of the Protestant canon. This project exists to close that gap: first by recovering the references the Catholic Bible's own oldest English translation printed in its margins, then by building a new, carefully checked apparatus of our own on top of them, book by book.

It already feeds the free [Catholic Bible app](https://jesuslovestyler.github.io/Catholic-Bible/) (Douay-Rheims, Challoner revision), where the seed below now serves the deuterocanon books and added chapters beside the Treasury of Scripture Knowledge.

## Version 0.1.0 — the seed

The seed is the cross-reference apparatus printed in the margins of the **original Douay-Rheims Bible** — the New Testament at Rheims in 1582 and the Old Testament at Douay in 1609–1610 — parsed into structured data.

- **1,984** marginal entries read
- **2,813** references kept, at **1,889** verses in **65** books
- **85** entry parts set aside, every one recorded with its reason in `dropped-entries.json`

The seed data comes from the [Original Douay-Rheims project](https://thedouayrheims.com), whose transcription of the original Bible (text and marginal apparatus) is released **CC0 1.0 / public domain** — corpus: `janvier-s/original-douay-rheims`, commit `d82b285`, folder `bible/tagged/`. This repository's own work is under the **Unlicense** (see `LICENSE`): public domain as nearly as the law allows.

### Files

- `cross-references.json` — the dataset. References are keyed by book (Douay-Rheims names and numbering, Psalms in Vulgate numbering), then by `"chapter:verse"`. Each entry keeps the margin's printed string (`raw`) beside its parsed `targets`, so every line can be traced back to the page it came from. A target with no verse (e.g. `"Genesis 22"`) cites the whole chapter, as the margin printed it.
- `dropped-entries.json` — everything that was **not** carried into the dataset, with the reason in plain words. Nothing was guessed to make the numbers bigger.
- `tools/parse_seed.py` — the parser that produced both files from the CC0 corpus, so the work can be re-run and checked.

Targets in **3 Esdras, 4 Esdras, and the Prayer of Manasses** — books the Douay Bible printed in its appendix, not among the 73 of the Catholic canon — are kept and flagged with `"appendix_targets": true`, exactly as they stand in the original.

## How the margins were read

The old margins cite in a shorthand of their time — `Sap. 7, 26.` for Wisdom 7:26, `3. Reg. 8.` for 3 Kings 8, `Eccli. 44. 22.` for Ecclesiasticus 44:22. They were read by these stated conventions, drawn from the corpus's own usage and applied uniformly:

- A comma joins chapter and verse (`Sap. 7, 26`); `v.` introduces verse numbers (`Iere. 25. v. 8. 9.`).
- Exactly one further plain number after a chapter reads as that chapter's verse (`Eccli. 44. 22`); a run of three or more plain numbers reads as a list of chapters (`Exo. 7. 8. 9. 10. 11. 12, 37`), and numbers joined by `&` are chapters.
- After a verse, a further plain number that fits the same chapter's verses is another verse of that chapter (`1. Mach. 4, 56. 59.`); a comma opens a fresh chapter-and-verse group.
- `Eccl.` with a chapter of 13 or more is Ecclesiasticus (Ecclesiastes has only 12 chapters); with a chapter of 12 or under it is genuinely ambiguous between the two books, and was **dropped rather than guessed**.
- Every target was checked against the original text itself — the book, the chapter, and the verse must exist in the Douay-Rheims as printed. Targets that fail (a handful, including a few misprints in the transcription) are in `dropped-entries.json`.

Before this dataset was published, its deuterocanon counts were cross-checked against an independent parse made for the Catholic Bible app: both readings agree exactly (Ecclesiasticus 128 entries → 150 references; Wisdom 34 → 43; Tobias 22 entries → 1 reference with 21 annotation markers set aside; Judith 14; Baruch 10; 1 Machabees 19; 2 Machabees 9).

## Where this goes

The seed is a beginning, not the harvest — four-century-old margins were sparing. On top of it, this project is building **our own cross references**, book by book, starting with the deuterocanon and the added chapters where the need is greatest. Every added reference will be checked against both passages it joins, and labeled by kind — quotation, allusion, parallel account, or shared theme — and the dataset and the app will name their sources honestly as the work grows. Sources are public domain only: the biblical texts themselves (Sirach 44–50 and Wisdom 10 are built-in spines of parallels), public-domain commentaries and Fathers, and the seed above. No modern copyrighted apparatus is copied.

*Soli Deo gloria.*
