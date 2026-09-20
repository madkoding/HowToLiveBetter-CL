# adapting-evidence-based-life-guides

A portable skill (agent instructions) for taking a cost/benefit-ranked life guide written for one
country and rebuilding it for another — properly, with verified local sources instead of translated
foreign facts.

It was extracted from the Chilean adaptation of
[dlgrv/HowToLiveBetter](https://github.com/dlgrv/HowToLiveBetter) (528 items, China-specific laws,
agencies and prices) into **HowToLiveBetter-CL**. The method is country-agnostic: replace China →
Chile with any pair.

## What it does

Turns "translate this guide" — a task that produces confident, wrong advice — into a repeatable
seven-layer method:

1. **Split the corpus by evidence portability** — international RCTs and cohorts stay verbatim;
   laws, agencies, benefits and prices get deleted and replaced; culturally relative items get
   re-evaluated from scratch.
2. **Build a substitution table** before writing prose — one row per source-country institution
   with the local equivalent, or `none` (which means the item is deleted, not force-fitted).
3. **Re-anchor the numbers** — keep effect sizes with their intervals, add local official
   statistics, date every money figure, never invent a missing one.
4. **Enforce one item format** — cost, plain-language translation, raw benefit, evidence grade,
   primary source, and a machine-readable cost tag the search page parses.
5. **Localize register, not just language** — keep the names of real local institutions, strip
   decorative localisms, drop moralizing.
6. **Delete what has no local referent** — 300 verified items beat 500 with a fifth pointing at
   institutions that don't exist.
7. **Ship the machinery** — a generated search page over all items, filtered by evidence grade and
   cost dimensions.

## Contents

```
SKILL.md                              the method: when to use, prerequisites, 7 layers, procedure,
                                      quick reference, 10 pitfalls, release verification list
references/item-format.md             field-by-field item spec, cost-tag vocabulary, mechanical
                                      benefit grading thresholds, plain-language-line rules
references/cultural-adaptation.md     register, institutional assumptions to test, money scales,
                                      culture-sensitive topics, anti-patterns
references/verification.md            two-tier protocol: what scripts prove, what only a human
                                      reading the source can prove; release gate
scripts/verificar.py                  validator (stdlib only): fields, tags, grades, URL sweep,
                                      plain-language vocabulary and number-set diffing, counts
```

## Installing it

The skill is a directory with a `SKILL.md` carrying standard frontmatter (`name`, `description`,
`version`, `author`, `license`, `platforms`, `metadata.hermes`). That is enough for any agent that
loads skills from a directory:

```bash
# Hermes Agent
mkdir -p ~/.hermes/skills/research
cp -r skill/adapting-evidence-based-life-guides ~/.hermes/skills/research/

# Claude Code / Codex style setups that read a skills or instructions directory
cp -r skill/adapting-evidence-based-life-guides ~/.claude/skills/

# No skill loader? Point the agent at the file directly.
#   "Read skill/adapting-evidence-based-life-guides/SKILL.md and follow it."
```

The scripts are pure Python 3 stdlib — no install step, no dependencies.

## Using it

```
Read skill/adapting-evidence-based-life-guides/SKILL.md and adapt this guide to <country>.
Source corpus: <path>. Target: <country>, language <language>.
```

The skill will make the agent do the three things that decide whether the result is trustworthy:
classify items by evidence portability before writing, research the local institutional layer
against primary sources only, and mark — never invent — what it could not verify.

## Why the anti-invention rule is the whole point

A guide whose value is "each item states what it costs and what it buys" collapses the moment one
number is fabricated: the reader who checks one item has no reason to trust the other 499.
Everything in this skill exists to make the failure mode visible (a marker and a log entry) rather
than silent (a plausible value).

## License

Unlicense — public domain, same as the upstream guide. Use it, fork it, cut it up.
