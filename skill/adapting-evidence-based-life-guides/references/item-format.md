# Item format specification

Every recommendation is one block. Fixed heading pattern, fixed field order, one machine-readable
tag. The validator (`scripts/verificar.py`) enforces all of it.

## Skeleton

```markdown
### 7. Take your blood pressure; if it is high, treat it to target
<!-- costos: plata=0 tiempo=poco aguante=algo beneficio=alto medida=muerte -->
- Costo: $0; 1 minute per reading. A home monitor costs $25.000–$60.000 CLP (2026).
- En simple: For every 10 mmHg your pressure comes down, the chance of a heart attack or stroke
  drops by about a fifth and the chance of dying by about 13%. In Chile, 1 in 4 adults has high
  blood pressure and most don't know it.
- Beneficio: meta-analysis (123 trials, >610,000 people): each 10 mmHg drop in systolic pressure
  gives major cardiovascular events RR 0.80 (95% CI 0.77–0.83), stroke RR 0.73, heart failure
  RR 0.72, all-cause mortality RR 0.87 (95% CI 0.84–0.91).
- Evidencia: A
- Fuentes: Ettehad D et al. (2016). Blood pressure lowering for prevention of cardiovascular
  disease and death. Lancet. <https://doi.org/10.1016/S0140-6736(15)01225-8> ; Ministry of Health.
  National Health Survey 2016–2017. <https://www.minsal.cl/>
- Notas: The 130 vs 140 target is still debated; knowing you have it and bringing it down is not.
  Most hypertensive adults locally are untreated or not at target.
```

## Rules

### Heading

`### N. Verb-first imperative`. Numbering restarts per chapter and must be contiguous from 1 —
the validator fails on gaps or repeats. The title names the action, not the topic: "Buckle up",
not "Seat belts".

### Cost tag (mandatory, immediately after the heading)

```
<!-- costos: plata=0|poco|mucho tiempo=poco|medio|mucho aguante=no|algo|si beneficio=alto|medio|bajo medida=muerte|plata|tiempo|libertad -->
```

Invisible on GitHub, parsed by the search page. An out-of-vocabulary value breaks filtering
silently, so the validator rejects it. Localize the tag *keys* with the rest of the guide, but keep
them positional and keep exactly five: the parser depends on order and count.

| Key | Values | Meaning (adapt the money figure per country) |
|---|---|---|
| money | `0` / `low` / `high` | `0` free or saves money; `low` tens of local currency units, or up to ~a day's wage per month; `high` hundreds of thousands or a significant recurring cost |
| time | `low` / `mid` / `high` | `low` minutes or incidental; `mid` hours once, or hours weekly; `high` daily |
| willpower | `no` / `some` / `yes` | `no` once and done; `some` change a habit or tolerate discomfort; `yes` fight an ingrained habit daily |
| benefit | `high` / `mid` / `low` | assigned mechanically, see below |
| dimension | `death` / `money` / `time` / `freedom` | what the item mainly buys back. Not comparable across values. |

### Fields

| Field | Content | Rules |
|---|---|---|
| `Costo` | What it takes from your pocket and your day | Concrete local amounts **with the year**; time as minutes/days |
| `En simple` | 1–2 sentences translating `Beneficio` into ordinary speech | No `RR`/`HR`/`OR`/`CI`/cohort/meta-analysis, no number absent from `Beneficio`/`Costo`, no hedging loss, no marketing words |
| `Beneficio` | The numbers, raw, with intervals | Verbatim from the source. This field is never "simplified". |
| `Evidencia` | `A`, `B`, `C`, or `X (en disputa)` | See evidence grading |
| `Fuentes` | Primary sources with URLs | At least one URL; article numbers and DOI where applicable |
| `Notas` | Limits, who it applies to, what it omits, `pending:` markers | Optional field, expected in practice |

Body ≤ 10 lines beyond the tag; longer explanations go to a separate long-read document.

## Plain-language line: the load-bearing detail

This is the line most readers use to decide. Two failure modes, both fatal to the guide's purpose:

1. **Statistics vocabulary.** The reader who needs this line does not know what an interval is.
   Translate: "about half as likely", "about a fifth lower", "1 death in 10".
2. **New numbers.** Inventing a percentage here that isn't in the benefit field means the guide
   now contains a number with no source. The validator diffs the number sets.

Write it for someone deciding in 5 seconds, then keep the raw numbers right below for the person
who will check.

## Mechanical benefit grading

Assign from the item's own `Beneficio` by threshold — never by intuition. This keeps ranking
comparable across hundreds of items written by different people.

| Dimension | `high` | `mid` | `low` |
|---|---|---|---|
| `death` | relative reduction ≥ 20% | 10–20% | < 10%, or surrogate endpoint only |
| `money` | millions | hundreds of thousands | tens of thousands |
| `freedom` | avoids a criminal conviction | avoids detention or a fine | avoids civil litigation |
| `time` | hours daily | hours weekly | once |

When the numbers genuinely cannot decide it, judge and **write the justification in `Notas`**.
"Not enough data" is not an acceptable grade reason on its own.

## Ordering and ratio tiers

Within a chapter, order by value for money, highest first. Never publish a ratio tier by hand —
synthesize it from benefit level plus the three cost dimensions (that is how the search page does
it), so the ranking stays consistent when an item is edited.
