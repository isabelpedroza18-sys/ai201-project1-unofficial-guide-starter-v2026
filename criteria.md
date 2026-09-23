# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
<!-- e.g. "One of my questions is about a topic only two documents mention, so
     I expect that one to be hard." -->

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
<!-- Why all five and not four? What about your setup makes that achievable —
     or what would have to go wrong for it not to be? -->

---The system's prompt explicitly instructs it to name the source document, and in every test I ran (5 in-scope questions plus retesting during Milestone 4), it did so consistently. Since this is enforced by instruction rather than left to chance, I expect all 5, not just 4 of 5.

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**
<!-- What did your distances look like when you set the cutoff in Milestone 4?
     Was there a clean gap, or did the two groups overlap? -->

---When I set my cutoff in Milestone 4, my in-scope test questions had best distances of 0.345, 0.437, and 0.449, while out-of-scope questions had 0.825 and 0.896 — a clean gap of over 0.35 between the two groups, with no overlap. I kept the starter's default cutoff of 0.6 since it sits comfortably in that gap rather than close to either side.

## 4. Something about your chunks

<!-- YOU WRITE THIS ONE.

     How would you know if your chunks were the right size? Name something
     countable or observable.

     Examples of the right shape — don't copy these, they should come from
     what you actually saw in Milestone 3:
       - "At least 4 of 5 sampled chunks read as a complete thought, with no
          sentence cut in half at either end."
       - "No chunk is shorter than 200 characters, since anything below that
          in my corpus turned out to be a heading with no content under it." -->
At least 4 of 5 chunks sampled at random will discuss a single topic only, with no unrelated topic mixed in.


**Why this target:**
Looking at 5 posts early (admin_wifi_and_accounts.txt, money_jobs.txt, study_library_hours.txt, admin_withdraw_dealine.txt, admin_graduation_requirements.txt), most stuck to one clear topic. But money_jobs.txt blurred two — it's framed as being about on-campus jobs, but one sentence ("10 to 12 hours is the point where it stops affecting coursework") is really about academic workload, not the job itself. Since this kind of overlap can happen even in short posts, I'm not expecting a perfect 5/5.


---

## 5. Your choice

<!-- YOU WRITE THIS ONE TOO.

     Pick something you actually care about getting right. It could be about
     speed, about refusals, about a particular kind of question your corpus
     handles badly, about source attribution being correct rather than merely
     present — anything, as long as it names a number or an observable
     outcome. -->

For 4 test questions with a specific numeric answer — credit hours to graduate, account duration after graduation, transcript cost, and transcript delivery time — the system's answer will state the exact number(s), including both the electronic and postal timeframes for the transcript question, not a rounded or vague version.

**Why this target:**
Numeric answers are easy to get subtly wrong — a model might round "120" to "about 120," or mention only the faster transcript option (3 business days) and drop the postal one (10 business days), which is exactly the kind of detail that matters for someone actually mailing something. I chose all 4 of 4 rather than a lower ratio, since these are simple factual lookups from single, short sentences, and a working retrieval system should get exact numbers right consistently, not just most of the time.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
