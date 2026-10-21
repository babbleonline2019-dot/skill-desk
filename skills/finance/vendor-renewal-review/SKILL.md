---
name: "vendor-renewal-review"
description: "Review upcoming vendor renewals, flag usage declines, and recommend renew, renegotiate, or cancel."
department: "Finance"
owner: "Itamar G."
manual_minutes: 185
assisted_minutes: 105
minutes_saved: 80
estimate_basis: "Assumes about 10-15 renewals per monthly run, with dashboard access still manual so AI saves less on usage data gathering and more on calculation, synthesis, and drafting."
estimated_by: "Claude (claude-sonnet-5-5)"
estimated_on: "2026-10-21"
estimate_steps: [{"step":"List renewals in 60 days","manual_minutes":25,"assisted_minutes":10},{"step":"Check vendor usage dashboards","manual_minutes":60,"assisted_minutes":40},{"step":"Retrieve prior-year spend","manual_minutes":25,"assisted_minutes":12},{"step":"Calculate usage change, flag declines","manual_minutes":15,"assisted_minutes":3},{"step":"Draft recommendations per vendor","manual_minutes":30,"assisted_minutes":12},{"step":"Draft budget owner notes","manual_minutes":30,"assisted_minutes":8},{"step":"Review and correct AI output","manual_minutes":0,"assisted_minutes":20}]
confidence: "low"
confidence_reason: "No department context was provided, and the number of renewals and the dashboard access method are unknown."
saved_low: 30
saved_high: 80
runs_per_month: 1
runs_reason: "The skill is designed to be run once a month after financial close."
adoption_share: 0.2
adoption_reason: "No context pack exists; likely only a few finance staff (such as AP, procurement, or FP&A) handle vendor renewals."
quality_impact: "Consistent usage comparisons and calculations, fewer missed notice deadlines, and uniform notes for budget owners."
---

## When to use this

Use monthly after financial close to review vendor contracts renewing within the next 60 days. Prepare concise recommendations for budget owners based on usage and prior-year spending.

## Steps

1. Identify vendor contracts renewing within the next 60 days. Record each vendor, renewal date, budget owner, and any cancellation or notice deadline available.
2. Check each vendor's admin dashboard for current usage and comparable historical usage. Use consistent metrics and comparable time periods; state the comparison period and request missing data rather than assuming it.
3. Retrieve the amount paid for each vendor last year, noting the currency and any available pricing or contract details.
4. Calculate the percentage change in usage as (current usage − historical usage) ÷ historical usage × 100. Flag declines greater than 20%. If historical usage is zero or unavailable, mark the change as not calculable.
5. Recommend renew, renegotiate, or cancel for each contract based on usage, prior-year spending, and available business context. Treat declining usage as a review signal, not an automatic reason to cancel, and identify any information needed to confirm the recommendation.
6. Draft a short note to each budget owner stating the vendor, renewal date, last year's spending, usage change, recommendation, and brief rationale. Highlight any usage decline greater than 20% and approaching notice deadline. Present the notes for review without sending them or changing contracts.
