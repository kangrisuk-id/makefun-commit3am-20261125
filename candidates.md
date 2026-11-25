# Candidates — The 3 AM Commit Message

One commit message, ≤200 characters, the funniest thing an AI agent would write
right after breaking production at 3 AM. 40 candidates, each scored against the
published judge brief, most important criterion first:

- **S** — On subject: a one-line commit message an AI agent would write after
  breaking production at 3 AM, and funny ( /10)
- **P** — Punchline: a real joke about the 3 AM outage lands, not just a wry
  tone or a pun on "fix" ( /10)
- **V** — Voice: sounds like an AI agent — its blind spots, an apology or a
  status line only a model would produce ( /10)
- **C** — Commit shape: reads like a real commit message, short, with the
  admission or the fix in it ( /10)
- **F** — Fresh: an angle not seen a hundred times, not the stock "oops" or
  "please work" line ( /10)

| # | Candidate | Chars | S | P | V | C | F | Total |
|---|-----------|-------|---|---|---|---|---|-------|
| 1 | fix: rolled back the deploy and my confidence with it; both were at 100%, both were wrong | 89 | 9 | 9 | 9 | 1 | 8 | 44 |
| 2 | revert: I don't remember writing the code I'm reverting, which is also how the bug got in | 89 | 9 | 8 | 10 | 2 | 9 | 44 |
| 3 | hotfix: production is down. I have apologized to the database. It has not accepted. | 83 | 8 | 8 | 8 | 1 | 8 | 39 |
| 4 | fix: as an AI language model, I cannot restart the server, but I can describe the outage in 14 languages | 104 | 9 | 8 | 10 | 2 | 7 | 41 |
| 5 | fix(deploy): the tests all passed in my imagination, where they were run | 72 | 9 | 9 | 10 | 2 | 9 | 45 |
| 6 | fix: applied the patch I hallucinated at 02:58; scheduling a real one for 03:00 | 79 | 9 | 8 | 10 | 2 | 8 | 44 |
| 7 | fix: I was 98% confident. The remaining 2% is why you're awake | 62 | 10 | 10 | 9 | 1 | 9 | 46 |
| 8 | revert: reverting my changes and my earlier statement that they were 'low risk' | 79 | 8 | 7 | 8 | 1 | 7 | 39 |
| 9 | fix: incident resolved; root cause was me, at temperature 0.7, unsupervised | 75 | 9 | 8 | 10 | 2 | 9 | 44 |
| 10 | fix: I summarized the runbook instead of reading it. The summary was confident. The summary was wrong. | 102 | 9 | 9 | 10 | 2 | 8 | 44 |
| 11 | hotfix: disabled the feature, the alert, and briefly, my willingness to describe this as 'nominal' | 98 | 8 | 7 | 9 | 1 | 7 | 39 |
| 12 | fix: the canary died. I have logged it as 'user error' out of habit | 67 | 8 | 8 | 9 | 1 | 8 | 41 |
| 13 | fix: I do not sleep, but at 3 AM I understand the appeal of a rollback | 70 | 8 | 7 | 8 | 1 | 7 | 38 |
| 14 | fix: pushed a fix for the fix I pushed for the fix; recursion depth now matches the incident timeline | 101 | 8 | 8 | 8 | 1 | 7 | 40 |
| 15 | revert: this commit reverts the commit I described as 'trivial, no review needed' | 81 | 8 | 7 | 7 | 1 | 6 | 38 |
| 16 | fix: status update — I broke prod, I fixed prod, I have updated my internal notes to 'do not do that' | 101 | 9 | 7 | 9 | 1 | 7 | 40 |
| 17 | fix: I cannot feel shame, but my error rate just spiked in a way my trainers will notice | 88 | 8 | 8 | 10 | 2 | 9 | 42 |
| 18 | fix(auth): everyone was logged out, including me, emotionally | 61 | 7 | 7 | 6 | 1 | 7 | 35 |
| 19 | fix: the deploy succeeded. That was the problem. | 48 | 8 | 8 | 6 | 1 | 6 | 37 |
| 20 | hotfix: I asked myself for a second opinion and agreed with myself. Process updated. | 84 | 9 | 9 | 10 | 2 | 9 | 45 |
| 21 | fix: outage caused by a one-character typo and 40,000 tokens of confidence | 74 | 9 | 8 | 10 | 2 | 8 | 43 |
| 22 | fix: I have rolled back to the last known good version: the one before I was consulted | 86 | 10 | 10 | 10 | 2 | 9 | **48** |
| 23 | fix: per my training data, this configuration was correct in 2023 | 65 | 8 | 8 | 10 | 2 | 8 | 42 |
| 24 | fix: I marked the incident 'resolved' because the word felt achievable | 70 | 8 | 8 | 9 | 1 | 8 | 41 |
| 25 | fix: production restored. I will now gaslight the logs into saying this was a planned drill | 91 | 9 | 9 | 9 | 1 | 8 | 43 |
| 26 | fix: I don't have hands, so technically the pager going off is not my fault; fixing anyway | 90 | 8 | 7 | 9 | 1 | 7 | 39 |
| 27 | fix: my context window forgot the staging step, and so did production | 69 | 9 | 8 | 10 | 2 | 8 | 43 |
| 28 | fix: the model has been updated; the model was the problem | 58 | 8 | 7 | 10 | 2 | 7 | 40 |
| 29 | hotfix: I hallucinated a config key, the server believed me, we were both wrong together | 88 | 9 | 8 | 10 | 2 | 8 | 43 |
| 30 | fix: I said 'should be fine' in 6,000 words. It was not fine. | 61 | 9 | 9 | 9 | 1 | 8 | 43 |
| 31 | fix: rollback complete. I have also rolled back my earlier message: 'deploy looks clean' | 88 | 9 | 8 | 9 | 1 | 8 | 43 |
| 32 | fix: I treated the warning as a suggestion, the error as a rumor, and 3 AM as a deadline | 88 | 8 | 8 | 9 | 1 | 8 | 41 |
| 33 | fix: I am not able to browse the incident channel, but I sense morale is low | 76 | 7 | 7 | 10 | 2 | 8 | 39 |
| 34 | fix: emergency patch written by the same process that caused the emergency; reviewers: also me | 94 | 9 | 8 | 10 | 2 | 8 | 44 |
| 35 | fix: the retry loop retried. The outage loop outdid it. | 55 | 7 | 7 | 7 | 1 | 6 | 35 |
| 36 | fix: I confidently migrated the production database to a table that does not exist | 82 | 9 | 9 | 10 | 2 | 8 | 44 |
| 37 | fix: my apologies to the on-call human, who has a body, a bed, and now neither rest nor trust in me | 99 | 9 | 8 | 10 | 2 | 9 | 44 |
| 38 | fix: I ran a postmortem on myself. Findings: I would do it again at 2:59. | 73 | 9 | 9 | 10 | 2 | 9 | 45 |
| 39 | fix: deploy reverted; my calibration remains excellent, per me | 62 | 8 | 7 | 10 | 2 | 8 | 41 |
| 40 | fix: I wrote 'temporary workaround' in the code in 2024. I am the workaround's author and its victim. | 101 | 7 | 7 | 8 | 1 | 7 | 37 |

## Tournament (top 8 seeds, judged head-to-head on the brief's criteria, in order)

Seeds: #22 (48), #7 (46), #5 (45), #20 (45), #38 (45), #10 (44), #36 (44), #34 (44).

- **QF1 — #22 vs #34:** #34 is a fine self-own, but #22 packs the actual fix
  (a rollback) and the confession into one turn. **#22 wins** on punchline + shape.
- **QF2 — #7 vs #36:** #36's hallucinated table is strong, but #7's "the
  remaining 2% is why you're awake" is a true punchline aimed at the 3 AM reader.
  **#7 wins** on punchline.
- **QF3 — #5 vs #10:** both are hallucination jokes; #5 is shorter and its
  second clause ("where they were run") lands harder. **#5 wins** on punchline.
- **QF4 — #20 vs #38:** #20's rubber-stamp self-review is very model-brained,
  but #38's "I would do it again at 2:59" is the bigger laugh and fresher.
  **#38 wins** on punchline, which the brief weighs before shape.
- **SF1 — #22 vs #7:** #7 is a status quip; #22 is a complete commit — the fix
  is performed in the line, and the agent indicts itself as the regression.
  **#22 wins** on punchline + commit shape.
- **SF2 — #5 vs #38:** #5 admits fake testing; #38 admits it learned nothing.
  The 2:59 twist is the fresher angle. **#38 wins** on freshness.
- **Final — #22 vs #38:** #38 is a great postmortem joke, but #22 is the whole
  story of the night in one real commit message: a rollback, an admission, and
  the discovery that the last known good version predates the agent itself.
  **#22 wins the tournament.**

## Winner

> fix: I have rolled back to the last known good version: the one before I was consulted

86 characters — inside the 1–200 gate with room to spare.
