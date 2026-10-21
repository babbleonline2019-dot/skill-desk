---
name: "vendor-renewal-review2"
description: "Review upcoming vendor renewals, flag usage declines, and recommend renew, renegotiate, or cancel to budget owners."
department: "Finance"
owner: "Itamar G."
manual_minutes: 180
assisted_minutes: 106
minutes_saved: 74
estimate_basis: "Assumes about 10-15 vendor renewals per cycle, with dashboard access still requiring manual retrieval and a human checking all figures and recommendations before sending; savings are conservative because data retrieval is only partly sped up."
estimated_by: "Claude (claude-sonnet-5-5)"
estimated_on: "2026-10-21"
estimate_steps: [{"step":"Identify renewals in 60 days","manual_minutes":25,"assisted_minutes":12},{"step":"Pull usage data from dashboards","manual_minutes":45,"assisted_minutes":30},{"step":"Retrieve prior-year spend and terms","manual_minutes":30,"assisted_minutes":18},{"step":"Calculate usage decline and flag","manual_minutes":15,"assisted_minutes":4},{"step":"Draft renew/renegotiate/cancel recommendations","manual_minutes":30,"assisted_minutes":12},{"step":"Draft budget-owner notes","manual_minutes":35,"assisted_minutes":10},{"step":"Review and correct AI output","manual_minutes":0,"assisted_minutes":20}]
confidence: "low"
confidence_reason: "There is no department context pack, and the number of renewals per month and the dashboard access are unknown."
saved_low: 45
saved_high: 85
runs_per_month: 1
runs_reason: "The skill is designed for a monthly review after financial close."
adoption_share: 0.25
adoption_reason: "Only a few finance staff, such as those handling procurement, AP, or FP&A, own vendor renewal reviews; no context pack suggests broader involvement."
quality_impact: "Consistent usage-decline flagging and notice-deadline tracking reduce missed deadlines and unplanned auto-renewals."
---

## When to use this

Use monthly after financial close to review vendor contracts renewing within the next 60 days. Prepare budget-owner recommendations based on usage trends and prior-year spending.

## Steps

1. Confirm the review date and identify vendor contracts renewing within the next 60 days. Record each vendor, renewal date, budget owner, and any cancellation or notice deadline.
2. Retrieve usage data from the relevant admin dashboards. Compare current usage with a comparable prior period, state the periods and metrics used, and flag missing data rather than estimating it.
3. Retrieve what was paid for each vendor last year and note any available renewal pricing or changes in contract terms.
4. Calculate the percentage decline in usage as (prior usage − current usage) / prior usage × 100. Flag declines greater than 20%; if prior usage is zero or unavailable, mark the comparison as not calculable.
5. Recommend renew, renegotiate, or cancel for each contract based on usage, spending, and available business context. Treat a usage decline as a review signal rather than an automatic reason to cancel, and identify any information needed to support the recommendation.
6. Draft a short note to each budget owner stating the vendor, renewal date, relevant notice deadline, prior-year spending, usage trend, recommendation, and supporting rationale. Highlight time-sensitive decisions and request approval before any contractual action.
