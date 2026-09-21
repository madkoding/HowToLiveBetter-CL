---
name: adapting-evidence-based-life-guides
description: Adapt cost-benefit life guides to your country and culture.
version: 1.0.0
author: madkoding, Hermes Agent
license: Unlicense
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [research, localization, evidence-based, public-health, legal, methodology]
    related_skills: [grounded-citations, competitor-news-monitor]
---

# Adapting Evidence-Based Life Guides to a Local Culture

Takes a cost/benefit-ranked life guide (longevity, money, law, work, family, bureaucracy) and
rebuilds it for a target country: keeps the international evidence, replaces the entire legal,
institutional and economic layer with locally verified facts, and enforces a fixed item format
so every claim carries a cost, a benefit, an evidence grade and a primary source.

Use this when a guide written for one country (e.g. China, the US) must become usable — and
trustworthy — for readers in another. **It is not a translation task.** Translation preserves
facts that are false in the target country; this method deletes and replaces them.

## When to Use

- Adapting a country-specific advice corpus (health, money, law, benefits, bureaucracy) to
  another country.
- Building or extending an evidence-ranked guide where every item must state cost, benefit and
  source quality.
- Auditing an existing localized guide for invented numbers, dead institutional references, or
  sources that do not say what the item claims.

Don't use for: translating marketing copy or UI strings; summarizing research (that's a
literature task); anything where the reader doesn't need a decision-ready cost/benefit.

## Prerequisites

- The source corpus as plain markdown, one file per chapter, items marked with a consistent
  heading pattern (`### N. Title`).
- Read/write file access and a shell for the verification scripts (`python3`, stdlib only).
- **No web access = stop.** Every localized fact must be read from its official source in this
  session. Adapting from memory is how invented numbers get published.

## The Method: Seven Layers

Work top to bottom. Layers 1–3 are what make the output trustworthy; 4–7 are what make it usable.

### 1. Split the corpus by evidence portability, before touching a word

Classify every source item into one of three buckets. This decision, not the writing, is the
project:

| Bucket | What it is | What you do |
|---|---|---|
| **Universal evidence** | RCTs, meta-analyses, cohorts on human physiology and physics: smoking, blood pressure, exercise, sleep, seat belts, helmets, drowning, vaccines | **Keep the study and its numbers verbatim.** Add the local statistic if one exists. Never recompute. |
| **Country-specific norm** | Laws, agencies, benefit amounts, deadlines, phone numbers, procedures, prices | **Delete and replace** with the target country's equivalent, verified against the primary source. |
| **Culturally relative** | Marriage customs, family obligations, betrothal gifts, deference to authority, what counts as polite | **Re-evaluate from scratch.** Often the item inverts. |

A guide that skips step 1 and "translates" produces the worst outcome: confident advice citing
a foreign statute that does not exist locally, with a real-looking number attached.

### 2. Build the substitution table for the target country

One row per source-country institution, with the local equivalent — or `none`, which means the
item gets deleted rather than force-fitted. Fill it by hand, with links, before writing prose.
This table is the project's spine: every writer works from it, and it is the first thing a
reviewer checks.

Worked example (China → Chile, from the reference implementation):

| Source institution | Target equivalent | Notes |
|---|---|---|
| National medical insurance | Fonasa / Isapre, A–D income tiers, GES/AUGE plan | Different cost structure entirely |
| Unemployment insurance | Seguro de cesantía (AFC) + severance | Two separate mechanisms, not one |
| Labour arbitration | Labour Inspectorate → Labour Courts | Monitorio procedure below a wage threshold |
| Household registration (hukou) | *none* | Delete all items that depend on it |
| Work-injury scheme | Ley 16.744 mutual insurers, mandatory employer coverage | DIAT/DIEP forms, distinct disability ratings |
| Betrothal gift law | *none* — but marital property regimes, union agreements and economic compensation exist | Different legal object; do not pretend equivalence |

Two failure modes to watch: **same-sounding, different reality** (a "public option" that works
nothing like the source's) and **near-equivalent with a trap** (a benefit that exists but has a
threshold, waiting period or means test the source item never mentions). State the trap in
`Notas`; a benefit described without its conditions is a false promise.

### 3. Re-anchor the numbers

- Keep every international effect size exactly as published, with its confidence interval.
- Add the local prevalence/incidence statistic when an official body publishes one.
- Local money: nominal currency **with the year** ("$529.000 CLP, 2026"). A bare amount rots.
- Legal: quote the article verbatim in the source line; the body says what to *do*.
- Time: distinguish business days from calendar days. Always.
- **No local figure found → mark it explicitly** (see Verification) and log it. Never substitute
  a plausible value, a foreign value, or a value from memory.

### 4. Enforce one item format

Every item gets the same fields, in the same order, plus a machine-readable cost tag in an HTML
comment (invisible on GitHub, parsed by the search page). Full spec:
`references/item-format.md`. The load-bearing parts:

- A **plain-language line** that restates the benefit for a non-statistician, using only numbers
  already present elsewhere in the item, and none of the statistics vocabulary (`RR`, `HR`,
  `OR`, `CI`, `cohort`, `meta-analysis`). This is the line most readers actually use; treat
  violations as errors, not style notes.
- A **benefit grade assigned mechanically** from a published threshold table, not by feel:
  mortality reduction ≥20% = high, 10–20% = medium, <10% = low; money in millions = high, etc.
  Mechanical assignment is what keeps ranking honest across 500 items written by different hands.
- **Cross-dimension scores are never compared or summed** (a mortality gain is not "worth" a
  money gain). Say so in the guide's own rules; it prevents fabricated trade-offs later.

### 5. Localize the tone, not just the language

Target a register a reader in that country would recognize as serious but not foreign. Keep
localisms that are *the actual name of a thing* (agency names, forms, colloquial names for
public benefits) and strip localisms used as decoration. Drop exclamation marks, moralizing, and
"you should"; show cost and benefit and let the reader decide. Full rules:
`references/cultural-adaptation.md`.

### 6. Drop what has no local referent

An item whose premise does not exist locally is deleted, not annotated. A guide with 300 verified
items outranks one with 500 where a fifth point at institutions that do not exist. Resist filling
volume — volume is the failure mode, not the goal.

### 7. Ship the machinery, not just the prose

A single searchable page over all items, generated from the markdown, filtered by evidence grade
and by the cost dimensions. Data comes from the markdown, so fixing the text fixes the page.
Without it, nobody can find the item that applies to them and the corpus is dead weight.

## Procedure

1. **Inventory the source.** Count items per chapter; extract one item to see the real schema
   (headings, tags, field names). Completion: a per-chapter item count that sums to the stated
   total.
2. **Write the adaptation contract** as the repo's first file: bucket rules, substitution table,
   item format, grading, sourcing rules, hard prohibitions, and the local "unverified" marker.
   Completion: a writer can produce a compliant item using only this file.
3. **Research in parallel, by domain, against primary sources only.** One researcher per domain
   (health, money, law, labour, emergencies, family, housing, bureaucracy, education). Demand
   per datum: claim, exact number, URL, source version/date, and a short verbatim quote where
   the number is load-bearing. Forbid press, blogs, law-firm posts and aggregators as sources.
   Completion: every researcher returns a file with cited data, and a list of what it could not
   verify.
4. **Write chapters** from the research files, using the item format. Rewrite items whose premise
   vanished; keep the universal-evidence ones as-is. Completion: every chapter parses under the
   validator with zero errors.
5. **Verify with tooling**, then verify the tooling's blind spots by hand:
   - structural checks: field presence, tag vocabulary, evidence grade, URL presence, the
     plain-language line's vocabulary and number set;
   - a URL sweep (report 4xx/5xx, tolerate 403/429 as warnings);
   - counts reconciled against the README;
   - **a human read of the top-ranked items in each chapter** — automated checks cannot tell
     whether a cited statute says what the item claims.
6. **Cross-check the local numbers** against the source's own version history. Benefit amounts,
   phone numbers and fees change on a legislative calendar; a figure without a date is a defect.
7. **Publish** with the license, the adaptation contract, the verification log, and the search
   page. Completion: a fresh reader can go from a symptom, a problem or a form name to one
   specific cited item.

## Quick Reference

```bash
python3 scripts/verificar.py            # format, tags, fields, grade, counts
python3 scripts/verificar.py --urls     # also probe every cited link
python3 scripts/verificar.py --json     # machine-readable audit
python3 scripts/construir.py            # build the search page's data from the markdown
```

## Pitfalls

1. **Translating a statute.** A translated foreign law is a fabricated law. Replace it or delete
   the item; there is no third option.
2. **Porting a country-specific number.** A prevalence figure, a benefit amount, a fine, a
   deadline — if it describes the source country, it is wrong locally even if the source is
   impeccable.
3. **Trusting an aggregator.** Sites that summarize public procedures are the most convincing and
   least reliable source available. Use the issuing body's own text.
4. **The confident summary.** A press article reporting "the new law says X" without the article
   number is a lead, not a source. Chase the text.
5. **A stale page on an official domain.** The worst source is an official body's own page that
   was never updated — an agency still publishing the old count or the superseded deadline. Being
   on a government domain is not evidence of being current. Check the version date, and where two
   official pages disagree, publish the discrepancy and say which one is current instead of
   silently picking one.
6. **A cross-reference to an item that does not exist.** "The red line is in chapter 09" is worse
   than no pointer at all: the reader looks, finds nothing, and stops trusting the rest. Verify
   every internal reference against the target chapter's actual item list.
7. **Inventing a plausible number to fill a gap.** The single most damaging failure, because it
   is undetectable in review and destroys the whole corpus's credibility. Mark it and log it.
8. **Statistics leaking into the plain-language line.** `RR 0,80 (IC 0,77–0,83)` in that line
   loses the reader the item was written for.
9. **Grading by gut.** Without mechanical thresholds, rankings drift and the "highest value
   first" ordering becomes fiction.
10. **Benefit without conditions.** A means test, waiting period or minimum contribution omitted
    from an item turns advice into a trap.
11. **Preserving item count as a goal.** Adapting by volume produces padding; the correct number
    is however many items survive verification.
12. **A country-specific phone number or agency name left in the source language.** Instantly
    visible to locals and fatal to trust.
13. **A validator that cries wolf.** A checker with false positives gets ignored, and an ignored
    checker is worse than none. Match forbidden terms on word boundaries (`\bOR\b`), never as bare
    substrings — `or:` fires on "mayor:", "menor:", "superior:". After fixing one, test both
    directions: the legitimate text must pass and the real violation must still fail.
14. **Verifying links in series.** A corpus of hundreds of URLs times out before finishing. Probe
    in parallel with a disk cache; treat 403/429 as warnings (official sites block bots or have a
    broken certificate chain while opening fine in a browser); retry 5xx once before believing it;
    and send DOI lookups to a citation API that returns the real title, which is how a fabricated
    DOI gets caught.
15. **Trusting a writer's self-report.** Have a second pass audit finished chapters against their
    sources. On the reference implementation that pass found mis-attributed articles, a
    recommendation its own sources did not support, and a study paraphrased more strongly than the
    paper allowed.

## Verification

Before publishing, all of these must hold:

- [ ] Every item carries the cost tag with values from the allowed vocabulary; the search page
      parses the corpus without a fallback error.
- [ ] Every item has cost, plain-language, benefit, evidence grade and at least one URL.
- [ ] No `RR`/`HR`/`OR`/`CI` vocabulary and no new numbers in the plain-language line.
- [ ] Every evidence grade is A, B or C; anything marked disputed lists the counter-evidence.
- [ ] Every unverifiable datum is marked with the project's marker and logged in the verification
      directory — the marker count matches the log.
- [ ] The item total in the README equals the number of items in the corpus.
- [ ] The substitution table has no rows left pointing at the source country's institutions.
- [ ] Spot-checked items: the cited source actually contains the claimed number (read it, do not
      assume the URL resolves to the right place).
- [ ] The guide states, in its own rules, that cross-dimension scores are not comparable, and
      that it is not medical, legal or financial advice.

See `references/verification.md` for the full protocol and `references/worked-example-chile.md`
for the reference implementation (China → Chile, 32 chapters).
