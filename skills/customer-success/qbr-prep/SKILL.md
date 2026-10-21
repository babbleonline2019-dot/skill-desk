---
name: "qbr-prep"
description: "Prep the quarterly business review deck for an account."
department: "Customer Success"
owner: "Nilay Shah"
manual_minutes: 125
assisted_minutes: 49
minutes_saved: 76
estimate_basis: "Assumes a CSM working on a single mid-size account with data in standard tools (analytics, support desk), where the AI can access or ingest exports, and the assisted time includes checking numbers and tailoring slides to the customer."
estimated_by: "Claude (claude-sonnet-5-5)"
estimated_on: "2026-10-21"
estimate_steps: [{"step":"Pull 90-day usage","manual_minutes":30,"assisted_minutes":12},{"step":"Summarize tickets/escalations","manual_minutes":35,"assisted_minutes":12},{"step":"Draft three slides","manual_minutes":60,"assisted_minutes":25}]
confidence: "medium"
confidence_reason: "Task scope is clear, but time varies with data access, account size, and how much AI can pull directly versus needing manual exports."
---

## When to use this

Two weeks before a QBR, when the CSM needs a first draft of the deck.

## Steps

1. Pull the account's usage from the last 90 days.
2. Summarize support tickets and any escalations.
3. Write three slides: what's going well, what's at risk, and what we propose for next quarter.
