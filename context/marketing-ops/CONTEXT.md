---
department: Marketing Ops
owner: Nilay Shah
systems: Salesforce, HubSpot, Slack
---

## How this team works
Marketing Ops runs the ABM program for merchant accounts. Every week the team picks target accounts, builds a personalized landing page for each, and hands them to sales. Speed matters more than polish on the first draft; design reviews before anything goes live.

## Systems and how to use them
### Salesforce (via the Salesforce MCP)
- Target accounts are Accounts where ABM_Tier__c is 1 or 2. Ignore Tier 3.
- Use the Account Owner, not the Opportunity Owner, as the sales contact.
- Marketing has read-only access to pipeline. Never write to Opportunity fields.
- Industry lives in Merchant_Category__c, not the standard Industry field.

### HubSpot
- Landing pages are created as drafts in the "ABM 2026" folder. Never publish directly.
- Every page needs the UTM campaign "abm-q4".

### Slack
- Post finished drafts to #abm-pages and tag the account's sales owner.

## Glossary
- Tier 1: top 50 strategic merchant accounts, fully personalized pages.
- Tier 2: next 200 accounts, industry-level personalization.
- MQL: a contact who visited an ABM page and booked a demo.

## Things new hires get wrong
- Writing copy about consumer cash back. ABM pages talk to merchants about incremental revenue, not to consumers.
- Using the Opportunity Owner as the sales contact.
- Publishing pages without design review.
