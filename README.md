# Catholic Cross References

A cross-reference system for the Catholic Bible, built in the open and given to the Church as public domain — anyone may use it freely, for anything, forever.

Modern Catholic Bibles are nearly bare of cross references in the seven books the whole Church read as Scripture for fifteen centuries — Tobit, Judith, Wisdom, Sirach (Ecclesiasticus), Baruch, and 1–2 Maccabees — and in the added chapters of Esther and Daniel. The big reference collections used by most Bible apps cover only the 66 books of the Protestant canon. This project exists to close that gap: first by recovering the references the Catholic Bible's own oldest English translation printed in its margins, then by building a new, carefully checked apparatus of our own on top of them, book by book.

It already feeds the free [Catholic Bible app](https://jesuslovestyler.github.io/Catholic-Bible/) (Douay-Rheims, Challoner revision), where the seed below now serves the deuterocanon books and added chapters beside the Treasury of Scripture Knowledge.

## Version 0.6.0 — beyond the deuterocanon: Genesis

The same work now extends into the rest of the canon, beginning where the Bible begins. **Genesis — 122 new references** (68 allusion, 43 parallel, 11 theme — and no quotations, honestly: every pair that would grade as a strict quotation of Genesis, like Romans 4:3 and Matthew 19:5, is already carried by the seed or by the deuterocanon layer). `our-references.json` now holds **502 references** (180 parallel, 275 allusion, 11 quotation, 36 theme).

Seventy-six entries are sourced at Genesis itself and forty-six at later verses looking back, touching 34 of its 50 chapters; the chapters left untouched are either already served by the seed or offer no verifiable verbal link, and the draft's set-asides are recorded with their reasons. Among the threads: John opening his Gospel with Genesis' first words ("In the beginning"); the oath of Genesis 22 taken up again and again — pleaded back to God in Exodus 32:13, and heard behind Romans 8:32, where the Father "spared not even his own Son," answering the verse where Abraham did not spare his; the garden's restoration traced through Isaias 51:3 and Ezechiel to the river and the tree of life in Apocalypse 21–22; Sodom expounded by the prophets, including Ezechiel 16:49's own account of her sin; and the seams where Genesis hands its story to Exodus — the seventy souls of 46:8 becoming Exodus 1:1, Israel's increase in 47:27 becoming Exodus 1:7, and Joseph's charge about his bones (50:24) kept in Exodus 13:19 and Josue 24:32.

## Version 0.5.0 — the deuterocanon complete

The last four works are in, and `our-references.json` now holds **380 references** (137 parallel, 207 allusion, 11 quotation, 25 theme) covering the whole deuterocanon — the part of the Catholic Bible where cross references were scarcest:

- **Baruch — 44 references**, and not one of them a parallel: Baruch is prayer and poetry reworking earlier texts, so its links are verbal. Its confession is Daniel 9 taken up sentence by sentence (one true quotation at 1:15); its comfort of Jerusalem runs to Isaiah 40, 52, 60, and 61; its wisdom hymn asks Moses' and Job's own questions about where wisdom is found, and 3:38 — "he was seen upon the earth, and was conversant with men" — is set beside John 1:14 as allusion. The Epistle of Jeremias (ch. 6) is tied into the idol passages of Isaiah, Jeremias 10, and the Psalms.
- **1 and 2 Machabees — 31 references.** The abomination of desolation (1 Mach 1:57) stands between Daniel 11 and Matthew 24; Mathathias's testament is routed to the halves of the fathers' stories the old margins missed; and 2 Machabees 7 meets Hebrews 11:35 twice — the brethren who were racked for a better resurrection, and their mother, at the head of the women who received their dead. Judas's offering for the dead is set beside 1 Corinthians 15:29 as **theme**, on the argument both passages share, and the dataset grades it no higher.
- **The additions to Esther — 16 references**, and none into the New Testament: Esther is never quoted there, and nothing was forced. The dream interprets itself (the little fountain that becomes a river is Esther); Esther's prayer pairs with Judith's on shared words; and the king's heart turned to mildness (15:11) is Proverbs 21:1 at work. One famous line was checked and refused: "our inheritance is turned to strangers" is Lamentations 5:2 — as printed, it is not in Esther's prayer.
- **The additions to Daniel — 37 references.** The Song of the Three is mapped onto Psalm 148 item by item; Azarias's prayer pleads God's oath to Abraham in nearly God's own words (3:36); Susanna's chapter proves to be a small legal web woven from Deuteronomy 19; Bel joins the idol passages of Isaiah 46 and Baruch 6; and Habacuc, carried by the hair to feed Daniel in the den, is set beside Elias's carrying in 3 Kings and Philip's in Acts 8.

## Version 0.4.0 — Tobias and Judith

Two smaller books added to `our-references.json`, which now holds **252 references** (105 parallel, 128 allusion, 6 quotation, 13 theme):

- **Tobias — 32 references.** The old margins nearly skipped this book (one real reference in the whole of it), so its layer is mostly new ground: Raphael, "one of the seven, which assist before our Lord," tied to the seven angels of Apocalypse 8 and to Gabriel's own introduction in Luke 1; Tobit's instruction in chapter 4 — alms laying up a good treasure, the hire paid the same day, the rule of doing to no man what you hate — beside Matthew 6, James 5, and the golden rule; Tobias's song in chapter 13, which takes up Anna's sentence from 1 Kings 2 and runs on to Isaiah 60 and the sapphires of Apocalypse 21. Sarah's seven husbands are set beside the Sadducees' question as **parallel, not allusion** — the sevens match, the situations differ, and the dataset says so.
- **Judith — 35 references.** The Jael thread is woven whole: the deliverance "by the hand of a woman" (Judges 4:9) behind Judith 13, Deborah's "blessed among women" (Judges 5:24) behind Ozias's blessing of Judith "above all women upon the earth," and that blessing beside Elizabeth's in Luke 1:42. Her canticle quotes the Psalms outright (13:21; 16:17), and her rebuke of the elders in chapter 8 reaches both the desert serpents of Numbers 21 and Paul's warning from them in 1 Corinthians 10 — from a single verse.

## Version 0.3.0 — Ecclesiasticus

The second book of our own references is **Ecclesiasticus** (Sirach), added to `our-references.json` — which now holds **185 references** (93 parallel, 83 allusion, 1 quotation, 8 theme) across the two books:

- **85 new references** for Ecclesiasticus: the praise of the fathers (chapters 44–50) mapped person by person to the accounts it retells; the yoke of chapter 51 taken up in Matthew 11 ("submit your neck to the yoke" — "Take up my yoke upon you"); the forgiveness rule of chapter 28 in Matthew 6 and Mark 11; five threads into James; and Sirach's own roots in Deuteronomy 30, Jeremias's potter, and the creation hymn
- Fifty further candidates were set aside and recorded — most already carried by the seed (Sirach's old margins were the seed's densest), the rest unproven from the text: chapter 50's Simon the high priest, who has no earlier account to point to, is left honestly unlinked
- One discipline note: Sirach's numbering in the original Douay-Rheims differs in places from modern editions (the yoke stands at 51:34–35, not 51:26–27); this dataset follows the text as printed

## Version 0.2.0 — our own references begin: Wisdom

On top of the seed, this project is now building its own cross references, book by book. The first book is **Wisdom**, in `our-references.json`:

- **100 references** at 80 verses, in both directions — Wisdom pointing to the rest of Scripture, and the rest of Scripture (Romans 1:20, Hebrews 1:3) pointing to Wisdom
- By kind: **47 parallel, 48 allusion, 1 quotation, 4 theme**
- The history spine of Wisdom 10–19 is mapped verse by verse to the Genesis, Exodus, and Numbers passages it retells; the New Testament layer runs from the just man of Wisdom 2 behind the Passion, through Wisdom 13–15 answering in Romans 1 and 9, to God's armor in Wisdom 5 reappearing in Ephesians 6
- Every reference carries its **evidence**: the short quotations from both passages on which the link rests, so any reader can check it against the text. Candidates that could not be proven from the words on the page were set aside, not stretched — including the famous near-miss of Wisdom 18:15 and John 1:14, which share the word "word" and nothing more.

## Version 0.1.0 — the seed

The seed is the cross-reference apparatus printed in the margins of the **original Douay-Rheims Bible** — the New Testament at Rheims in 1582 and the Old Testament at Douay in 1609–1610 — parsed into structured data.

- **1,984** marginal entries read
- **2,813** references kept, at **1,889** verses in **65** books
- **85** entry parts set aside, every one recorded with its reason in `dropped-entries.json`

The seed data comes from the [Original Douay-Rheims project](https://thedouayrheims.com), whose transcription of the original Bible (text and marginal apparatus) is released **CC0 1.0 / public domain** — corpus: `janvier-s/original-douay-rheims`, commit `d82b285`, folder `bible/tagged/`. This repository's own work is under the **Unlicense** (see `LICENSE`): public domain as nearly as the law allows.

### Files

- `cross-references.json` — the seed dataset. References are keyed by book (Douay-Rheims names and numbering, Psalms in Vulgate numbering), then by `"chapter:verse"`. Each entry keeps the margin's printed string (`raw`) beside its parsed `targets`, so every line can be traced back to the page it came from. A target with no verse (e.g. `"Genesis 22"`) cites the whole chapter, as the margin printed it.
- `our-references.json` — this project's own references, built on top of the seed (see the 0.2.0 section above). Same keying; each reference is labeled by kind and carries the quoted evidence from both passages.
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

The seed is a beginning, not the harvest — four-century-old margins were sparing. On top of it, this project is building **our own cross references**, book by book, starting with the deuterocanon and the added chapters where the need is greatest. The deuterocanon is complete (0.2.0–0.5.0, above) — the ground where the need was greatest is covered first, as planned. From there the same patient work has begun extending, book by book, across the rest of the canon, starting with Genesis (0.6.0, above); and this layer will in due course flow into the Catholic Bible app beside the seed, so a reader of Tobias or Judith or 2 Machabees finds these threads at the foot of the page. Every added reference will be checked against both passages it joins, and labeled by kind — quotation, allusion, parallel account, or shared theme — and the dataset and the app will name their sources honestly as the work grows. Sources are public domain only: the biblical texts themselves (Sirach 44–50 and Wisdom 10 are built-in spines of parallels), public-domain commentaries and Fathers, and the seed above. No modern copyrighted apparatus is copied.

*Soli Deo gloria.*
