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

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
