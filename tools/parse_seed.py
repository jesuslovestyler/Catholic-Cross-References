#!/usr/bin/env python3
"""Parse the original Douay-Rheims marginal cross references (CC0 corpus,
janvier-s/original-douay-rheims @ d82b285, bible/tagged/) into the seed
dataset for Catholic-Cross-References.

Rules (the "no lies" rule governs): period abbreviations expanded to the
Catholic Bible app's book names; anything that does not parse to a definite
book + chapter (+ verse) validated against the corpus's own verse counts is
dropped and recorded with a reason — never guessed.
"""
import json, glob, re, collections, sys, os

SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/workspace/goals/a-cross-reference-system-of-our-own-for-the-catholic-bible/hidden_files/source-original-dr/src/bible/tagged')

# corpus slug -> dataset book name (the Catholic Bible app's Douay-Rheims names)
BOOK_NAME = {
 'genesis':'Genesis','exodus':'Exodus','leviticus':'Leviticus','numbers':'Numbers',
 'deuteronomy':'Deuteronomy','josue':'Josue','judges':'Judges','ruth':'Ruth',
 '1-kings':'1 Kings','2-kings':'2 Kings','3-kings':'3 Kings','4-kings':'4 Kings',
 '1-paralipomenon':'1 Paralipomenon','2-paralipomenon':'2 Paralipomenon',
 '1-esdras':'1 Esdras','2-esdras':'2 Esdras','3-esdras':'3 Esdras','4-esdras':'4 Esdras',
 'tobias':'Tobias','judith':'Judith','esther':'Esther','job':'Job','psalms':'Psalms',
 'proverbs':'Proverbs','ecclesiastes':'Ecclesiastes','canticle-of-canticles':'Canticle of Canticles',
 'wisdom':'Wisdom','ecclesiasticus':'Ecclesiasticus','isaie':'Isaias','jeremie':'Jeremias',
 'lamentations':'Lamentations','baruch':'Baruch','ezechiel':'Ezechiel','daniel':'Daniel',
 'osee':'Osee','joel':'Joel','amos':'Amos','abdias':'Abdias','jonas':'Jonas',
 'micheas':'Micheas','nahum':'Nahum','habacuc':'Habacuc','sophonias':'Sophonias',
 'aggeus':'Aggeus','zacharias':'Zacharias','malachie':'Malachias',
 '1-machabees':'1 Machabees','2-machabees':'2 Machabees',
 'matthew':'Matthew','mark':'Mark','luke':'Luke','john':'John','acts':'Acts of the Apostles',
 'romans':'Romans','1-corinthians':'1 Corinthians','2-corinthians':'2 Corinthians',
 'galatians':'Galatians','ephesians':'Ephesians','philippians':'Philippians',
 'colossians':'Colossians','1-thessalonians':'1 Thessalonians','2-thessalonians':'2 Thessalonians',
 '1-timothy':'1 Timothy','2-timothy':'2 Timothy','titus':'Titus','philemon':'Philemon',
 'hebrews':'Hebrews','james':'James','1-peter':'1 Peter','2-peter':'2 Peter',
 '1-john':'1 John','2-john':'2 John','3-john':'3 John','jude':'Jude','apocalypse':'Apocalypse',
 'prayer-of-manasses':'Prayer of Manasses',
}
APPENDIX = {'3-esdras','4-esdras','prayer-of-manasses'}  # printed in the Douay Bible's appendix; not among the 73

# unnumbered abbreviations -> slug
ABBREV = {
 'gen':'genesis','ge':'genesis','exo':'exodus','exod':'exodus','ex':'exodus',
 'lev':'leviticus','levit':'leviticus','levi':'leviticus','nu':'numbers','num':'numbers',
 'deu':'deuteronomy','deut':'deuteronomy','duet':'deuteronomy','jos':'josue','ios':'josue','iosu':'josue','iosue':'josue',
 'jud':'judges','iud':'judges','iudic':'judges','ru':'ruth','rut':'ruth','ruth':'ruth',
 'tob':'tobias','judth':'judith','iudth':'judith','est':'esther','esth':'esther',
 'iob':'job','job':'job','ps':'psalms','psa':'psalms','psal':'psalms','psalm':'psalms',
 'pro':'proverbs','prov':'proverbs','cant':'canticle-of-canticles',
 'sap':'wisdom','isa':'isaie','esa':'isaie','es':'isaie','isai':'isaie','esaie':'isaie',
 'ier':'jeremie','iere':'jeremie','ierem':'jeremie','jer':'jeremie','jere':'jeremie','hier':'jeremie',
 'lam':'lamentations','thren':'lamentations','bar':'baruch',
 'eze':'ezechiel','ezech':'ezechiel','ezec':'ezechiel','ez':'ezechiel','dan':'daniel',
 'judith':'judith','deuter':'deuteronomy','collos':'colossians','philip':'philippians',
 'nahu':'nahum','nahum':'nahum','ag':'aggeus','iudi':'judges',
 'os':'osee','osee':'osee','ose':'osee','ioel':'joel','joel':'joel','am':'amos','amos':'amos',
 'abd':'abdias','ion':'jonas','mic':'micheas','mich':'micheas','nah':'nahum',
 'hab':'habacuc','habac':'habacuc','abac':'habacuc','soph':'sophonias','sopho':'sophonias','agg':'aggeus','agge':'aggeus',
 'zach':'zacharias','zac':'zacharias','mal':'malachie','malac':'malachie',
 'mt':'matthew','mat':'matthew','math':'matthew','matt':'matthew','matth':'matthew',
 'mr':'mark','mar':'mark','marc':'mark','lu':'luke','luc':'luke',
 'io':'john','jo':'john','joh':'john','ioan':'john',
 'act':'acts','acts':'acts','ro':'romans','rom':'romans',
 'gal':'galatians','eph':'ephesians','ephes':'ephesians','phil':'philippians','col':'colossians','colos':'colossians',
 'john':'john',
 'tit':'titus','philem':'philemon','phile':'philemon','heb':'hebrews','hebr':'hebrews','jac':'james','iac':'james','iacob':'james','ia':'james',
 'ioa':'john',
 'jude':'jude','iudae':'jude','iude':'jude','apo':'apocalypse','apoc':'apocalypse','apocal':'apocalypse','ap':'apocalypse',
 'man':'prayer-of-manasses',
}
# numbered abbreviations: (number, abbrev) -> slug
NUM_ABBREV = {}
for n,slug in [(1,'1-kings'),(2,'2-kings'),(3,'3-kings'),(4,'4-kings')]:
    for a in ('reg','re','regum'): NUM_ABBREV[(n,a)] = slug
for n,slug in [(1,'1-paralipomenon'),(2,'2-paralipomenon')]:
    for a in ('par','paral','para','paralip'): NUM_ABBREV[(n,a)] = slug
for n,slug in [(1,'1-esdras'),(2,'2-esdras'),(3,'3-esdras'),(4,'4-esdras')]:
    for a in ('esdr','esd','esdra','esdras'): NUM_ABBREV[(n,a)] = slug
for n,slug in [(1,'1-corinthians'),(2,'2-corinthians')]:
    NUM_ABBREV[(n,'cor')] = slug
for n,slug in [(1,'1-thessalonians'),(2,'2-thessalonians')]:
    for a in ('thess','thes','th'): NUM_ABBREV[(n,a)] = slug
for n,slug in [(1,'1-timothy'),(2,'2-timothy')]:
    for a in ('tim','timo'): NUM_ABBREV[(n,a)] = slug
for n,slug in [(1,'1-peter'),(2,'2-peter')]:
    NUM_ABBREV[(n,'pet')] = slug
for n,slug in [(1,'1-john'),(2,'2-john'),(3,'3-john')]:
    for a in ('io','jo','ioan'): NUM_ABBREV[(n,a)] = slug
for n,slug in [(1,'1-machabees'),(2,'2-machabees')]:
    for a in ('mach','mac'): NUM_ABBREV[(n,a)] = slug
for n,slug in [(1,'1-samuel-x'),(2,'2-samuel-x')]:
    pass
# 'samuel' naming never appears in DR margins (Reg. is used); guard anyway:
NUM_ABBREV[(1,'sam')] = '1-kings'; NUM_ABBREV[(2,'sam')] = '2-kings'

SINGLE_CHAPTER = {'jude','2-john','3-john','philemon','abdias'}  # verse-only citation possible

# load corpus, build verse-count table
books = {}
counts = {}   # slug -> {chapter: verse_count}
for f in sorted(glob.glob(SRC + '/*.json')):
    d = json.load(open(f))
    slug = os.path.basename(f)[:-5]  # filename stem is the stable slug ('book' field varies)
    books[slug] = d
    counts[slug] = {}
    for c in d['chapters']:
        if c['chapter'] >= 1:
            counts[slug][c['chapter']] = len(c.get('verses', []))

def valid_target(slug, ch, v):
    if slug not in counts: return False
    if ch not in counts[slug]: return False
    if v is not None and not (1 <= v <= counts[slug][ch]): return False
    return True

TOKEN_RE = re.compile(r'[^\s]+')

def parse_entry(src_slug, src_ch, src_v, raw):
    """Return (refs, drops): refs = list of dicts; drops = list of (raw_part, reason)."""
    refs, drops = [], []
    s = raw.strip()
    # tokenize keeping punctuation info
    tokens = []
    for m in TOKEN_RE.finditer(s):
        t = m.group(0)
        tokens.append(t)
    # an entry with no letters at all is a bare annotation marker (e.g. Tobias's '1.'–'14.')
    if not any(re.search(r'[A-Za-z]', t) for t in tokens):
        return [], [(raw, 'bare numbers with no book named — annotation markers in the text, not references')]
    # an 'Annot.' pointer sends the reader to a note, not to a Scripture passage:
    # parse only what stands before it and record the tail honestly
    annot_tail = None
    for idx, t in enumerate(tokens):
        if t.rstrip('.,').lower() in ('annot', 'annotation'):
            annot_tail = ' '.join(tokens[idx - 1:]) if idx > 0 else ' '.join(tokens[idx:])
            tokens = tokens[:idx - 1] if idx > 0 else []
            break
    i = 0
    cur_book = None      # slug of the book currently being cited
    cur_ch = None
    prose_mode = False
    prose_tokens = []

    def flush_prose():
        if prose_tokens:
            drops.append((' '.join(prose_tokens), 'commentary prose or annotation text, not a reference'))
            prose_tokens.clear()

    def numval(tok):
        m = re.fullmatch(r'(\d+)[.,]?', tok)
        return int(m.group(1)) if m else None

    def clean(tok):
        return tok.rstrip('.,').lower()

    n = len(tokens)
    while i < n:
        tok = tokens[i]
        c = clean(tok)
        if prose_mode:
            # resume only at a definite book lead; bare numbers inside prose never resume
            nv2 = numval(tok)
            is_lead = (
                c in ABBREV or c in ('eccl', 'eccli', 'ecclu', 'eccles', 'eccle', 'ecclci')
                or (nv2 is not None and nv2 in (1, 2, 3, 4) and i + 1 < n and clean(tokens[i + 1]) in NUM_LEADS)
                or ((c in ('ch', 'chap', 'cap') or re.fullmatch(r'[a-z]ch', c) or c == 'c')
                    and i + 1 < n and numval(tokens[i + 1]) is not None)
            )
            if is_lead:
                flush_prose(); prose_mode = False
            else:
                prose_tokens.append(tok); i += 1; continue
        # '&c.' tail -> drop rest
        if c in ('&c', '&caet', '&cet'):
            drops.append((' '.join(tokens[i:]), "'&c.' (et cetera) tail — the margin points onward without naming verses"))
            i = n; break
        if c == '&' or c == 'and':
            i += 1; continue
        # numbered book lead: '3.' followed by abbrev token
        nv = numval(tok)
        if nv is not None and nv in (1,2,3,4) and i + 1 < n:
            na = clean(tokens[i+1])
            if (nv, na) in NUM_ABBREV:
                cur_book = NUM_ABBREV[(nv, na)]; i += 2; cur_ch = None
                # chapter number next
                if i < n and numval(tokens[i]) is not None:
                    chtok = tokens[i]; cur_ch = numval(chtok); i += 1
                    i = read_after_book(tokens, i, cur_book, cur_ch, chtok, refs, drops, raw)
                elif cur_book in SINGLE_CHAPTER and i < n:
                    cur_ch = 1
                    if clean(tokens[i]) in ('v', 'u'):
                        i = read_verses(tokens, i, cur_book, cur_ch, refs, drops, src_slug)
                    else:
                        i = read_verses(tokens, i, cur_book, cur_ch, refs, drops, src_slug, first_is_verse=True)
                else:
                    drops.append((f'{nv}. {na}.', 'numbered book cited with no chapter'))
                continue
        # plain book abbrev
        if c in ABBREV:
            cur_book = ABBREV[c]; i += 1; cur_ch = None
            if cur_book in SINGLE_CHAPTER:
                # Jude, Philemon, Abdias, 2–3 John: the book has one chapter,
                # so a following number is a verse ('Jude, 18.' / 'Phile. 10.')
                cur_ch = 1
                if i < n and clean(tokens[i]) in ('v', 'u'):
                    i = read_verses(tokens, i, cur_book, cur_ch, refs, drops, src_slug)
                elif i < n and numval(tokens[i]) is not None:
                    add_ref(refs, drops, cur_book, 1, numval(tokens[i]), raw); i += 1
                else:
                    add_ref(refs, drops, cur_book, 1, None, raw)
            elif i < n and numval(tokens[i]) is not None:
                chtok = tokens[i]; cur_ch = numval(chtok); i += 1
                i = read_after_book(tokens, i, cur_book, cur_ch, chtok, refs, drops, raw)
            else:
                drops.append((tok, 'book cited with no chapter'))
            continue
        # 'Eccl.'/'Eccli' special handling
        if c in ('eccl', 'eccli', 'ecclu', 'eccles', 'eccle', 'ecclci'):
            # peek chapter
            ch = numval(tokens[i+1]) if i + 1 < n else None
            if c in ('eccli', 'ecclu', 'ecclci'):
                cur_book = 'ecclesiasticus'
            elif c == 'eccle':
                cur_book = 'ecclesiastes'
            else:  # 'eccl' / 'eccles' ambiguous
                if ch is not None and ch > 12:
                    cur_book = 'ecclesiasticus'
                elif ch is not None:
                    drops.append((' '.join(tokens[i:i+3]), "ambiguous abbreviation 'Eccl.' with chapter 12 or under — could be Ecclesiastes or Ecclesiasticus; dropped rather than guessed"))
                    i += 2; cur_book = None; continue
                else:
                    drops.append((tok, "ambiguous abbreviation 'Eccl.' with no chapter"))
                    i += 1; continue
            chtok = tokens[i + 1] if ch is not None else None
            i += 1
            if ch is not None:
                cur_ch = ch; i += 1
                i = read_after_book(tokens, i, cur_book, cur_ch, chtok, refs, drops, raw)
            continue
        # same-book chapter: 'ch.' / 'Ch.', or a lettered piece marker like Esther's 'Cch.'
        # continues the book currently being cited, or the source book at an entry's start
        if c in ('ch', 'chap', 'cap') or re.fullmatch(r'[a-z]ch', c):
            if i + 1 < n and numval(tokens[i+1]) is not None:
                cur_book = cur_book or src_slug; cur_ch = numval(tokens[i+1]); i += 2
                i = read_verses(tokens, i, cur_book, cur_ch, refs, drops, src_slug)
            else:
                drops.append((tok, "'ch.' with no chapter number"))
                i += 1
            continue
        # 'c.' before a number is a chapter marker ('c. 9.'); before anything else it is
        # the confer siglum — skip it and keep reading
        if c == 'c':
            if i + 1 < n and numval(tokens[i+1]) is not None:
                cur_book = cur_book or src_slug; cur_ch = numval(tokens[i+1]); i += 2
                i = read_verses(tokens, i, cur_book, cur_ch, refs, drops, src_slug)
            else:
                i += 1
            continue
        # bare number: a verse continuation, or the next chapter of the current book
        if nv is not None:
            if cur_book is None:
                cur_book = src_slug
            # verse continuation: '1. Mach. 4, 56. 59.' / 'Mt. 27, 1. 11.' — after a
            # verse of a chapter, a further plain number (no comma: a comma opens a
            # fresh chapter:verse group) that fits the chapter's verses is another
            # verse of the same chapter
            if (cur_ch is not None and refs and not tok.endswith(',')
                    and valid_target(cur_book, cur_ch, nv)
                    and refs[-1]['book'] == BOOK_NAME[cur_book]
                    and refs[-1].get('chapter') == cur_ch and 'verse' in refs[-1]):
                add_ref(refs, drops, cur_book, cur_ch, nv, raw); i += 1; continue
            cur_ch = nv
            has_comma = tok.endswith(',')
            i += 1
            if has_comma and i < n and numval(tokens[i]) is not None:
                cand = numval(tokens[i])
                if cand in (1, 2, 3, 4) and i + 1 < n and clean(tokens[i + 1]) in NUM_ONLY_LEADS:
                    add_ref(refs, drops, cur_book, cur_ch, None, raw)
                else:
                    i += 1
                    add_ref(refs, drops, cur_book, cur_ch, cand, raw)
            else:
                i = read_verses(tokens, i, cur_book, cur_ch, refs, drops, src_slug)
            continue
        # a numbered book's abbreviation standing alone ('Reg. 8.') is ambiguous
        if c in ('reg', 're', 'par', 'paral', 'cor', 'pet', 'thess', 'thes', 'mach', 'esdr', 'esd', 'sam', 'tim', 'timo'):
            drops.append((tok, 'a book that needs its number (as in 1.–4. Reg.) cited without one — ambiguous, dropped rather than guessed'))
            i += 1; continue
        # anything else: prose/annotation begins here — collect it, but keep
        # scanning: a later book lead in the same entry is still a reference
        prose_mode = True
        prose_tokens.append(tok); i += 1; continue
    flush_prose()
    if annot_tail:
        drops.append((annot_tail, "points to an annotation ('Annot.'), not a Scripture reference"))
    return refs, drops

def add_ref(refs, drops, slug, ch, v, raw):
    if slug is None or ch is None:
        drops.append((raw, 'reference without a definite book and chapter'))
        return
    if valid_target(slug, ch, v):
        r = {'book': BOOK_NAME[slug], 'chapter': ch}
        if v is not None: r['verse'] = v
        if slug in APPENDIX: r['appendix'] = True
        refs.append(r)
    else:
        tgt = f"{BOOK_NAME.get(slug, slug)} {ch}" + (f":{v}" if v else '')
        drops.append((tgt, 'target does not exist in the original Douay-Rheims text (book, chapter, or verse beyond its count)'))

NUM_LEADS = {a for (_, a) in NUM_ABBREV.keys()}
# abbreviations that exist ONLY as part of a numbered name ('1. Pet.'); 'Io.' is
# excluded — standing alone it is the Gospel of John, and the comma guard must not
# steal a verse number to build '1. Io.' out of 'Io.'
NUM_ONLY_LEADS = NUM_LEADS - {'io', 'jo', 'ioan'}

def read_after_book(tokens, i, book, ch, chtok, refs, drops, raw):
    """Convention (documented in the dataset README, drawn from the corpus's own usage):
    a run of 3+ plain numbers after a book name is a list of CHAPTERS (the last may
    carry a comma verse); exactly one further plain number reads as the VERSE of the
    chapter just named, falling back to a second chapter when no such verse exists;
    '&'-joined numbers are chapters; 'v.' introduces verse numbers."""
    n = len(tokens)
    if chtok.endswith(','):
        if i < n and re.fullmatch(r'\d+[.,]?', tokens[i]):
            cand = int(tokens[i].rstrip('.,'))
            # guard: 'Ro. 12, 1. Pet. 3, 9.' — the number belongs to the next book's
            # name ('1. Pet.'), and the comma only separates; read the chapter alone
            if cand in (1, 2, 3, 4) and i + 1 < n and clean_local(tokens[i + 1]) in NUM_ONLY_LEADS:
                add_ref(refs, drops, book, ch, None, raw); return i
            add_ref(refs, drops, book, ch, cand, raw); return i + 1
        add_ref(refs, drops, book, ch, None, raw); return i
    # lookahead run of plain number tokens (not ending ','), stopping before a numbered-book lead
    run = []
    j = i
    while j < n:
        t = tokens[j]
        if not re.fullmatch(r'\d+\.', t) and not re.fullmatch(r'\d+', t):
            break
        if j + 1 < n and clean_local(tokens[j + 1]) in NUM_LEADS and int(t.rstrip('.')) in (1, 2, 3, 4):
            break
        run.append(int(t.rstrip('.'))); j += 1
    if len(run) >= 2:
        add_ref(refs, drops, book, ch, None, raw)
        for cn in run:
            add_ref(refs, drops, book, cn, None, raw)
        return j
    if len(run) == 1:
        v = run[0]
        if valid_target(book, ch, v):
            add_ref(refs, drops, book, ch, v, raw)
        elif valid_target(book, v, None):
            add_ref(refs, drops, book, ch, None, raw)
            add_ref(refs, drops, book, v, None, raw)
        else:
            drops.append((f'{BOOK_NAME[book]} {ch}. {v}.', 'neither a verse of the named chapter nor another chapter of the book in the original text'))
        return i + 1
    # no plain run: 'v.' verse list or chapter-only
    return read_verses(tokens, i, book, ch, refs, drops, None)

def clean_local(tok):
    return tok.rstrip('.,').lower()

def read_verses(tokens, i, book, ch, refs, drops, src_slug, first_is_verse=False, cont=False):
    """After a chapter is established: read optional verse info.
    Forms: ', v' in following token (chapter token ended with ','); 'v.'/'v' then verse numbers;
    further '. N' groups are handled by the main loop as new chapter groups of the same book,
    EXCEPT right after a 'v.' marker, where numbers are verses of this chapter."""
    n = len(tokens)
    # verse given as next token because previous token ended with ',' — handled by caller via cont path
    if first_is_verse:
        # tokens[i] itself is a verse number
        if i < n:
            m = re.fullmatch(r'(\d+)[.,]?', tokens[i])
            if m:
                add_ref(refs, drops, book, ch, int(m.group(1)), '')
                i += 1
                return i
        add_ref(refs, drops, book, ch, None, '')
        return i
    # 'v.' marker?
    if i < n and tokens[i].rstrip('.,').lower() in ('v', 'u'):
        i += 1
        # verse numbers separated by '.' until a book lead / prose / end;
        # an invalid verse ends the list — what follows is a new chapter group
        got = False; dropped_invalid = False
        while i < n:
            m = re.fullmatch(r'(\d+)[.,]?', tokens[i])
            if m:
                vnum = int(m.group(1))
                if valid_target(book, ch, vnum):
                    add_ref(refs, drops, book, ch, vnum, '')
                    got = True; i += 1; continue
                drops.append((f'{BOOK_NAME[book]} {ch}:{vnum}',
                              'target does not exist in the original Douay-Rheims text (book, chapter, or verse beyond its count)'))
                dropped_invalid = True
                i += 1
            break
        if not got and not dropped_invalid:
            add_ref(refs, drops, book, ch, None, '')
        return i
    # comma-verse: previous token ended with ',' — the caller passes cont; here detect by
    # checking if the *previous consumed* token ended with ',': we approximate — if the token
    # right here is a number AND the raw chapter token had a trailing comma, the main loop
    # handles it. Default: chapter-only ref.
    add_ref(refs, drops, book, ch, None, '')
    return i

def main():
    dataset = {}
    all_drops = []
    stats = collections.Counter()
    per_book = collections.defaultdict(lambda: collections.Counter())
    for slug, d in sorted(books.items()):
        name = BOOK_NAME[slug]
        for c in d['chapters']:
            if c['chapter'] == 0: continue
            for v in c.get('verses', []):
                for e in v.get('cross_refs', []):
                    raw = e['text']
                    stats['entries'] += 1
                    per_book[slug]['entries'] += 1
                    refs, drops = parse_entry(slug, c['chapter'], v['verse'], raw)
                    for r in refs:
                        key = f"{c['chapter']}:{v['verse']}"
                        dataset.setdefault(name, {}).setdefault(key, [])
                        ent = {'raw': raw, 'target': r}
                        dataset[name][key].append(ent)
                        stats['refs'] += 1
                        per_book[slug]['refs'] += 1
                    for part, reason in drops:
                        all_drops.append({'source': {'book': name, 'chapter': c['chapter'], 'verse': v['verse']},
                                          'raw_entry': raw, 'dropped_part': part, 'reason': reason})
                        stats['dropped_parts'] += 1
                        per_book[slug]['dropped_parts'] += 1
    json.dump({'dataset': dataset, 'drops': all_drops,
               'stats': dict(stats),
               'per_book': {BOOK_NAME[k]: dict(v) for k, v in per_book.items()}},
              open(os.path.expanduser('~/workspace/goals/a-cross-reference-system-of-our-own-for-the-catholic-bible/hidden_files/parse_out.json'), 'w'),
              ensure_ascii=False, indent=1)
    print('STATS:', dict(stats))
    print('\nPER BOOK (entries/refs/dropped_parts):')
    for k, v in sorted(per_book.items()):
        print(f"  {BOOK_NAME[k]:28s} {v['entries']:4d} {v['refs']:4d} {v['dropped_parts']:4d}")
    print('\nDROP REASONS:')
    rc = collections.Counter(d['reason'] for d in all_drops)
    for r, n in rc.most_common():
        print(f'  {n:4d}  {r}')

if __name__ == '__main__':
    main()
