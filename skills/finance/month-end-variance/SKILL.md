---
name: month-end-variance
description: Summarize month-end variances against budget and flag the three biggest. Use at close when finance needs the first-pass narrative.
department: Finance
owner: Nilay Shah
manual_minutes: 41
assisted_minutes: 20
minutes_saved: 21
estimate_basis: "Assumes a mid-size variance table of 30-60 lines, manual drafting by an experienced accountant, and conservative AI time including a careful review since accuracy outweighs speed and drivers inferred from account names are often weak."
estimated_by: "Claude (claude-sonnet-5-5)"
estimated_on: "2026-10-21"
estimate_steps: [{"step":"Sort variance table by absolute $","manual_minutes":5,"assisted_minutes":1},{"step":"Write top-three variance sentences","manual_minutes":20,"assisted_minutes":4},{"step":"Flag over-10% items outside top three","manual_minutes":8,"assisted_minutes":1},{"step":"Write two-sentence VP summary","manual_minutes":8,"assisted_minutes":2},{"step":"Review and correct AI output","manual_minutes":0,"assisted_minutes":12}]
confidence: "medium"
confidence_reason: "The steps are clear and small, but table size and the extra effort required to replace account-name drivers with real business drivers are uncertain."
saved_low: 14
saved_high: 26
runs_per_month: 1
runs_reason: "Close happens once a month, and one person typically drafts the first-pass narrative for the pack."
adoption_share: 0.5
adoption_reason: "Roughly half of the 6-person team (accountants and FP&A types) draft variance narratives; others focus on AP, payroll, or other tasks."
quality_impact: "More consistent narrative structure and fewer missed over-10% items, though the skill's account-name-based drivers need review to ensure they reflect real business drivers."
---

## When to use this
Close is done, the variance table exists, and someone has to write the first draft of the narrative.

## Steps
1. Take the variance table. Sort by absolute dollar variance.
2. For the top three, write one sentence each: what moved, which direction, and the most likely driver based on the account names.
3. Flag anything over 10 percent that isn't in the top three.
4. Write a two-sentence summary a VP could read in ten seconds.
