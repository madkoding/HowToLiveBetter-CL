# Verification protocol

The value of a cost/benefit guide is entirely in whether its numbers hold. Two tiers: what a script
can prove, and what only a human reading the source can prove.

## Tier 1 — automated (`scripts/verificar.py`)

| Check | Failure means |
|---|---|
| Cost tag present, exactly five fields, values in vocabulary | The search page's filters break silently |
| All mandatory fields present and non-empty, in order | The item does not render as an item |
| Evidence grade ∈ {A, B, C} | An ungradeable claim is in the corpus |
| Disputed grade accompanied by counter-evidence in `Notas` | One-sided presentation |
| Grade A items cite an official/primary source | Grade A means "verified against the text" |
| At least one URL per item; no placeholder sources | An unsourced claim |
| Plain-language line free of `RR`/`HR`/`OR`/`CI`/cohort/meta-analysis | The line loses its reader |
| Plain-language numbers ⊆ numbers in benefit/cost | A number with no source exists in the corpus |
| Item numbering contiguous per chapter | Broken anchors and references |
| Every `pending` marker has a matching entry in the verification log | Silent holes |
| README total equals actual item count | The guide misstates its own size |
| URL sweep | Dead links (403/429/503 = warning: sites block bots) |

Run it with `--urls` before every release; run it with `--json` in CI.

## Tier 2 — human, cannot be skipped

The script proves structure. It cannot prove that a cited statute says what the item claims.
Sample per chapter, and always include the top three ranked items (they are the most read):

1. **Open the cited source.** Not the URL's title — the text. Find the number.
2. **Check the number's meaning**: relative vs. absolute risk, per-year vs. lifetime, adjusted vs.
   crude, per-100,000 vs. percent. Misframing a real number is as wrong as inventing one.
3. **Check the local figure's version.** Benefit amounts, fee schedules, phone numbers and forms
   change on a legislative calendar. If the item has no date, it is already suspect.
4. **Check the legal article is in force.** Especially where a reform is phased in: an article may
   be published, not yet effective, or since replaced. Confirm the current text, not the amendment
   that created it.
5. **Read the item as a local reader would.** Does a phone number, agency, currency or procedure
   from the source country survive anywhere? Grep the corpus for the source country's name,
   currency, and agencies — leftovers hide in `Notas`.
6. **Check the item does not promise a benefit without its conditions** — means tests, waiting
   periods, contribution minimums, deadlines. This is where an item becomes actively harmful.

## The unverified marker

Where a datum cannot be confirmed, the item carries an explicit marker in `Notas` and a line in the
verification log naming the datum, the suspected value and the source that could not be read.

A visible marker is the correct outcome. A plausible invented value is the only unacceptable one:
it is undetectable in review, and one of them invalidates the entire corpus for a reader who
happens to check it.

## Release gate

- [ ] `verificar.py` exits 0 (warnings acceptable, errors not)
- [ ] `verificar.py --urls` has no 4xx/5xx errors
- [ ] Item counts reconciled with the README, badges, and the search page's metadata
- [ ] Search page rebuilt from the current markdown and opens without a fallback error
- [ ] Sampled items re-read against their sources (top-ranked item per chapter, minimum)
- [ ] Source country's currency, agencies and phone numbers grep to zero hits outside the
      adaptation document itself
- [ ] `pending` marker count equals the verification-log entry count
- [ ] License, adaptation contract and verification log present in the repository
