# Run log — Criterion 5 supplementary questions

- Produced by: manual runs via `python app.py ask "..."`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `campus_life` (index variant `default`)
- top-k: 3 · relevance cutoff: 0.6
- Runs per question: 3, caching off (`$env:AI201_CACHE = "0"`)
- When: 2026-09-29

These two questions are not part of `questions.py` — they exist specifically
to give Criterion 5 ("numeric answers stated exactly") a full 4 of 4 sample,
alongside the credit-hours and account-duration questions already covered in
the main run log.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| How much do official transcripts cost to order? | $8 ✅ | $8 ✅ | $8 ✅ |
| How long will it take to receive my official transcript, once ordered? | both timeframes ✅ | both timeframes ✅ | both timeframes ✅ |

---

## Real output

### How much do official transcripts cost to order? — run 1

- Best distance: 0.198 (passed the gate)
- Sources retrieved: admin_printing_quota.txt, admin_transcript_requests.txt, money_textbooks.txt

```
Official transcripts cost $8. This information comes from admin_transcript_requests.txt.
```

### How much do official transcripts cost to order? — run 2

- Best distance: 0.198 (passed the gate)
- Sources retrieved: admin_printing_quota.txt, admin_transcript_requests.txt, money_textbooks.txt

```
Official transcripts cost $8.

Source: admin_transcript_requests.txt
```

### How much do official transcripts cost to order? — run 3

- Best distance: 0.198 (passed the gate)
- Sources retrieved: admin_printing_quota.txt, admin_transcript_requests.txt, money_textbooks.txt

```
Official transcripts cost $8.

Source: admin_transcript_requests.txt
```

### How long will it take to receive my official transcript, once ordered? — run 1

- Best distance: 0.277 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_library_holds.txt, admin_transcript_requests.txt

```
According to `admin_transcript_requests.txt`, official transcripts take three business days electronically or ten days by post.
```

### How long will it take to receive my official transcript, once ordered? — run 2

- Best distance: 0.277 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_library_holds.txt, admin_transcript_requests.txt

```
According to `admin_transcript_requests.txt`, official transcripts take three business days electronically or ten by post.
```

### How long will it take to receive my official transcript, once ordered? — run 3

- Best distance: 0.277 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_library_holds.txt, admin_transcript_requests.txt

```
According to `admin_transcript_requests.txt`, official transcripts take three business days electronically or ten by post.
```

---

## Verdict for Criterion 5

Combined with the credit-hours and account-duration questions in the main
run log (`run_2026-09-29_1637_before.md`), all 4 of 4 numeric questions
named in Criterion 5 stated the exact number(s) in every one of 3 runs
(12 of 12 total):

| Numeric question | Exact number stated, all 3 runs? |
|---|---|
| How many credit hours do I need to graduate? | Yes — "120" |
| How long does my student account stay active for after graduation? | Yes — "six months" |
| How much do official transcripts cost to order? | Yes — "$8" |
| How long will it take to receive my official transcript, once ordered? | Yes — both "three business days" and "ten days by post" |

**Verdict: MET** (4 of 4, exceeding the target).
