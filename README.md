# The Unofficial Guide

Maria Pedroza campus_life 

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->
This system is The Unofficial Guide, built on the campus_life corpus. It includes 88 short student posts covering the practical, insider details of college life that official sources leave out. It answers questions about deadlines, housing quirks, dining wait times, and financial and account details. It's built for students who want the kind of answers that usually only come from asking someone who's already been through it, rather than digging through a school website that doesn't mention them.

## Chunking Strategy

**Chunk size:** One whole post per chunk (average 317 characters across 88 posts), with a 1200-character cap as a safety net.
**Overlap:** None.

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->
campus_life posts are short (Milestone 1 showed 88 documents averaging 317 characters, longest 549) and almost always focused on a single topic. Splitting them further would risk cutting a complete thought in half for no real benefit, so I chunk by whole document instead of a fixed character window. The 1200-character cap exists only as a safety net: if a post is ever unusually long, it splits on paragraph breaks instead of mid-sentence, rather than assuming every post stays short forever.

One limitation I found: `money_jobs.txt` blends two topics in one post (on-campus jobs, and a sentence about when work starts affecting coursework), so not every chunk is purely single-topic even with this strategy.

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1**
======================================================================
Chunk 1  |  source: admin_add_drop_deadline.txt#0  |  produced by: chunker.py::split_documents
======================================================================
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.

**Chunk 2** 
======================================================================
Chunk 2  |  source: course_biol_160.txt#0  |  produced by: chunker.py::split_documents
======================================================================
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.

**Chunk 3** 
======================================================================
Chunk 3  |  source: course_hist_118_workload.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.


**Chunk 4** 
======================================================================
Chunk 4  |  source: dining_pellew_dining_hall_followup.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.

**Chunk 5** 
======================================================================
Chunk 5  |  source: housing_innisfree_hall.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
Question: Which floor in the library is best for studying?

**Answer:**
Based on the provided documents, the best floor depends on your study needs:
- The third floor is silent and enforced (*study_library_hours.txt*).
- The second floor is quiet in theory (*study_library_hours.txt*).
- The basement has the only outlets at every seat (*study_library_hours.txt*).

Sources retrieved: housing_aldridge_hall_noise.txt, study_group_rooms.txt, study_library_hours.txt

**My relevance cutoff:** 0.6 (the starter's default)

| Question | In corpus? | Best distance |
|---|---|---|
| How long does my student account stay active for after graduation? | Yes | 0.345 |
| Can I study during my on-campus job? | Yes | 0.437 |
| Which floor in the library is best for studying? | Yes | 0.449 |
| Does withdrawing from a course affect my GPA? | Yes | 0.443 |
| How many credit hours do I need to graduate? | Yes | 0.305 |
| What is the capital of Mongolia? | No | 0.825 |
| How do I write a for loop in Rust? | No | 0.896 |
| Who won the 1994 World Cup? | No | 0.886 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.844 |
| How do I change the oil in a diesel engine? | No | 0.934 |

All five in-corpus questions landed between 0.305 and 0.449; all five out-of-scope questions landed between 0.825 and 0.934 — a gap of nearly 0.4 with no overlap. I kept the starter's default cutoff of 0.6 since it sits comfortably in the middle of that gap.

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**
1. I decided one post = one chunk was the right strategy for campus_life, since Milestone 1 showed most posts were short and single-topic. I asked Claude for a replacement split_documents function implementing that, with a safety cap for unusually long posts. It wrote the function with a 1200-character cap and paragraph-based fallback splitting — I reviewed it against my own chunk-size reasoning before using it, and it re-indexed to the same 88 chunks as before, confirming no post exceeded the cap.
**2.**
2. While reviewing my Milestone 4 test question about the best library floor, I noticed the model's answer invented a detail ("rooms 210 and 211 on the second floor") that wasn't in any retrieved chunk, and separately merged an unrelated fact from a dorm-noise document (Aldridge Hall) into a claim about the library. I hadn't caught either issue on my own — Claude pointed them out and helped me rewrite the grounding instruction in generate.py to explicitly forbid inferring unstated details and combining facts across unrelated documents. Retesting confirmed both issues were fixed.

**3.** While comparing before/after run logs in unit 2, I noticed Q3's answer changed from correct to a refusal after my chunking change, but I hadn't diagnosed why. I asked Claude to help trace the cause, and together we used `app.py retrieve` to inspect the actual retrieved chunks — which showed the "third floor" content had been merged with the wrong paragraph during splitting, isolating it into a chunk that no longer ranked in the top 3. Claude helped me write up the mechanism precisely; the diagnosis itself came from reading the actual retrieved text side by side.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks discuss a single topic | 4 of 5 | 5/5* | 5/5* | 5/5* | MET |
| 5. Numeric answers stated exactly | 4 of 4 | 4/4 | 4/4 | 4/4 | MET |

\* Chunk sampling isn't run-dependent (it's not tied to the 3 model-call runs) and `app.py chunks -n 5` isn't randomized, so this number reflects the single sample discussed in Milestone 2 (5 of 5 sampled chunks single-topic; counting the known `money_jobs.txt` exception found in Unit 1, the honest fuller picture is 5 of 6). See Diagnoses for detail.

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->
Real output for each criterion is in `results/run_2026-09-29_1637_before.md` (criteria 1, 2, 3, produced by `run_eval.py::main` and `run_eval.py::check_out_of_scope`) and `results/transcript_questions_criterion5.md` (criterion 5's two supplementary questions, produced by manual runs of `app.py::cmd_ask`). Sample below:

**Criterion 1/2 example** (question: "How long does my student account stay active for after graduation?", run 1):
Your student account stays active for six months after you graduate.
Source: admin_wifi_and_accounts.txt

**Criterion 3 example** (out-of-scope question: "What is the capital of Mongolia?"):
I don't have enough information about that.
(best distance 0.825, refused before reaching the model — 0 model calls)

## Verdicts

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer | MET | All 5 test questions retrieved a chunk containing the correct answer, exceeding the 4/5 target. |
| 2 | Every answer names a source | MET | All 15 generated answers (5 questions × 3 runs) named at least one source document. |
| 3 | Gate stops out-of-corpus questions | MET | The gate refused all 5 out-of-scope questions, exceeding the 4/5 target. |
| 4 | Chunks discuss a single topic | MET | Of 5 sampled chunks (the same 5 each time, since `app.py chunks` isn't randomized), all discussed a single topic. Counting the known exception found in Unit 1 (`money_jobs.txt`, which blends jobs and coursework workload), 5 of 6 chunks checked overall discuss a single topic — still above the 4/5 target. |
| 5 | Numeric answers stated exactly | MET | All 4 numeric questions (credit hours, account duration, transcript cost, transcript delivery) stated the exact number(s) correctly across all 3 runs each (12 of 12). |

## Diagnoses

I missed nothing — all 5 criteria were MET on every run. Rather than treat this as the system being flawless, I looked honestly at whether my targets were set too low.

Criterion 1 ("retrieved chunks contain the answer, 4 of 5") turned out to be the safest target of the five: when I checked with `python app.py retrieve`, the correct source document ranked #1 for all 5 of my questions, meaning the original criterion (answer appears anywhere in top 3) was never genuinely at risk of failing. I revised it in `criteria.md` to require the answer's source to be the single top-ranked chunk, which is a meaningfully harder bar and one my system still happens to clear — but at least now the criterion is actually testing something.

## The Improvement

**What I changed:**
I added a second chunking strategy, `chunker.py::paragraph_split`, which splits each post at paragraph breaks instead of keeping the whole post as one chunk (a short heading-like first paragraph under 40 characters is merged into the next paragraph, so titles don't become their own near-empty chunks). I indexed this into a separate variant (`paragraph`) using a small script (`reindex_paragraph.py`), so both the original and new chunking exist side by side without deleting either.

**Why I picked it:**
My Unit 1 diagnosis found that `money_jobs.txt` blended two topics into one chunk (on-campus jobs, and a separate sentence about when work starts affecting coursework). Splitting by paragraph directly targets that — separating blended topics into smaller, more focused chunks.

### Run Log — After

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 2. Every answer names a source | 5 of 5 | 4/5 | 4/5 | 4/5 | MISSED |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

*(Criteria 4 and 5 were not affected by this change — chunk-topic sampling and numeric questions weren't retested against this variant, since the improvement specifically targeted retrieval for blended-topic posts.)*

**Did it help?**
Mixed — genuinely, not evasively. It helped exactly where I expected: for "Can I study during my on-campus job?", the paragraph variant retrieved a smaller, focused chunk containing only "Maximum is 20 hours a week... 10 to 12 is the point where it stops affecting coursework" — cleanly separated from the library/dining job info, and the best distance improved slightly (0.437 → 0.413).

But it broke something I didn't expect: for "Which floor in the library is best for studying?", the answer changed from a correct, sourced response ("the third floor is silent and enforced") to **"I don't have enough information to answer"** in all 3 runs. The cause: `study_library_hours.txt`'s short title ("Library hours and where to actually sit," 39 characters) got merged with the *hours* paragraph rather than the *floor* paragraph, since it's the first paragraph encountered. This left the floor-specific content in its own smaller chunk that no longer ranked in the top 3 for this question's exact wording — retrieval pulled back the title+hours chunk instead, which doesn't mention floors at all.

So the change helped one already-diagnosed weakness (topic blending) while introducing a new one (a useful chunk isolated so much it stopped being retrieved for a question it used to answer correctly). I know this because I compared the actual generated answer text, not just distances — the "after" run for Q3 explicitly refused to answer where the "before" run didn't.

## What's Still Broken

The paragraph-splitting improvement broke retrieval for "Which floor in the library is best for studying?" — the answer that used to correctly name the third floor now refuses to answer, in all 3 runs, because the relevant content got split away from the study_library_hours.txt title into a chunk that no longer ranks in the top 3 for this question's wording.

What I'd do about it: adjust the heading-merge rule in `paragraph_split` so a short title merges with whichever following paragraph is more central to the post's likely topic, not just the first one it encounters — or lower the 40-character merge threshold so titles merge with every paragraph that follows, not just the next one. I stopped here because of time — this is a real, fixable case, not a fundamental flaw in the approach, but tracking down the right merge heuristic and re-testing would take another testing cycle I didn't have time for in this unit.

## What I'd Do Differently

I'd write Criterion 4 (chunk single-topic check) to specify a real random sample rather than relying on `app.py chunks -n 5`, since that command isn't actually randomized — it returned the identical 5 chunks both times I ran it in Unit 1 and Unit 2, which meant my "sampled at random" language wasn't quite accurate to what I tested. I'd also add a criterion in Unit 1 that's specifically about consistency across chunking strategies — something like "swapping chunking strategies doesn't break previously-correct answers" — since that's exactly the kind of regression Milestone 4 surfaced, and I had no criterion written ahead of time that would have caught it as a real target to protect.