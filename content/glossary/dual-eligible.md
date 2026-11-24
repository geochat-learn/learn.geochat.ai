---
title: "Dual Eligible: Definition and County Counts"
description: "Dual eligible people have both Medicare and Medicaid. Full vs partial duals, the QMB, SLMB, QI and QDWI groups, and where CMS publishes county counts."
slug: glossary/dual-eligible
type: glossary
updated: 2026-11-24
faq:
  - q: "What does the yearly dual-eligible figure in Medicare Monthly Enrollment mean?"
    a: "It is a person-year count: each person's months of enrollment, summed and divided by 12. A person whose status changes mid-year can count partly in more than one category ([methodology](https://data.cms.gov/sites/default/files/2024-06/b7a86e30-1e72-49aa-bf0f-68d6f1206467/MME_RY24_Methodology_20240627_508.pdf))."
  - q: "Why do some county dual-eligible counts show an asterisk?"
    a: "CMS suppresses enrollee counts of 1 to 10 and counter-suppresses other counts so the small ones cannot be recalculated. Both are shown as an asterisk ([methodology](https://data.cms.gov/sites/default/files/2024-06/b7a86e30-1e72-49aa-bf0f-68d6f1206467/MME_RY24_Methodology_20240627_508.pdf))."
  - q: "Can I get dual-eligible counts by age for a county from this file?"
    a: "No. The Medicare Monthly Enrollment file reports dual status and age groups as separate columns, with no column that crosses them ([data dictionary](https://data.cms.gov/sites/default/files/2025-12/Medicare%20Monthly%20Enrollment%20Data%20Dictionary.pdf))."
  - q: "How far back do county Medicare enrollment counts go?"
    a: "The Medicare Monthly Enrollment file gives monthly and yearly counts by state and county beginning with calendar year 2013 ([methodology](https://data.cms.gov/sites/default/files/2024-06/b7a86e30-1e72-49aa-bf0f-68d6f1206467/MME_RY24_Methodology_20240627_508.pdf))."
  - q: "Can providers bill QMB patients for Medicare cost sharing?"
    a: "No. Medicare providers can't bill QMB patients for Medicare deductibles, coinsurance or copayments. In some cases, a patient may owe a small Medicaid copayment ([MLN fact sheet](https://www.cms.gov/files/document/beneficiaries-dually-eligible-medicare-medicaid.pdf))."
sources:
  - title: "CMS: About the Medicare-Medicaid Coordination Office"
    url: "https://www.cms.gov/medicare/medicaid-coordination/about"
    accessed: 2026-11-24
  - title: "CMS MMCO Fact Sheet: People Dually Eligible for Medicare and Medicaid (March 2023)"
    url: "https://www.cms.gov/medicare-medicaid-coordination/medicare-and-medicaid-coordination/medicare-medicaid-coordination-office/downloads/mmco_factsheet.pdf"
    accessed: 2026-11-24
  - title: "CMS MLN Fact Sheet MLN006977: Beneficiaries Dually Eligible for Medicare & Medicaid (June 2024)"
    url: "https://www.cms.gov/files/document/beneficiaries-dually-eligible-medicare-medicaid.pdf"
    accessed: 2026-11-24
  - title: "CMS: Data & Statistical Resources for Dually Eligible Beneficiaries"
    url: "https://www.cms.gov/data-research/research/statistical-resources-dually-eligible-beneficiaries"
    accessed: 2026-11-24
  - title: "data.cms.gov: Medicare Monthly Enrollment"
    url: "https://data.cms.gov/summary-statistics-on-beneficiary-enrollment/medicare-and-medicaid-reports/medicare-monthly-enrollment"
    accessed: 2026-11-24
  - title: "data.cms.gov API: Medicare Monthly Enrollment dataset resources (Aug 2026 file, dictionary, methodology)"
    url: "https://data.cms.gov/data-api/v1/dataset-resources/d7fabe1e-d19b-4333-9eff-e80e0643f2fd"
    accessed: 2026-11-24
  - title: "data.cms.gov API: Medicare Monthly Enrollment, national row, August 2026"
    url: "https://data.cms.gov/data-api/v1/dataset/d7fabe1e-d19b-4333-9eff-e80e0643f2fd/data?filter%5BYEAR%5D=2026&filter%5BMONTH%5D=August&filter%5BBENE_GEO_LVL%5D=National"
    accessed: 2026-11-24
  - title: "data.cms.gov: Medicare Monthly Enrollment Data Dictionary (12/9/2025)"
    url: "https://data.cms.gov/sites/default/files/2025-12/Medicare%20Monthly%20Enrollment%20Data%20Dictionary.pdf"
    accessed: 2026-11-24
  - title: "data.cms.gov: Medicare Monthly Enrollment Methodology (June 2024)"
    url: "https://data.cms.gov/sites/default/files/2024-06/b7a86e30-1e72-49aa-bf0f-68d6f1206467/MME_RY24_Methodology_20240627_508.pdf"
    accessed: 2026-11-24
---

A dual eligible person is enrolled in both Medicare and Medicaid ([CMS](https://www.cms.gov/medicare/medicaid-coordination/about)). County counts come from the CMS [Medicare Monthly Enrollment](https://data.cms.gov/summary-statistics-on-beneficiary-enrollment/medicare-and-medicaid-reports/medicare-monthly-enrollment) dataset on data.cms.gov.

CMS also calls this group "Medicare-Medicaid enrollees" ([CMS](https://www.cms.gov/medicare/medicaid-coordination/about)). Medicare covers most primary and acute care and drugs. Medicaid covers long-term services and supports, certain behavioral health services, and Medicare premiums and cost sharing ([MMCO fact sheet](https://www.cms.gov/medicare-medicaid-coordination/medicare-and-medicaid-coordination/medicare-medicaid-coordination-office/downloads/mmco_factsheet.pdf)).

## Full-benefit vs partial-benefit duals

Full-benefit duals "qualify for the full package of Medicaid benefits." Partial-benefit duals "are enrolled only in Medicare and an MSP" ([MMCO fact sheet](https://www.cms.gov/medicare-medicaid-coordination/medicare-and-medicaid-coordination/medicare-medicaid-coordination-office/downloads/mmco_factsheet.pdf)). MSP means Medicare Savings Program.

CMS describes four MSP groups ([MLN fact sheet](https://www.cms.gov/files/document/beneficiaries-dually-eligible-medicare-medicaid.pdf)):

| Group | What Medicaid pays | Income limit (FPL = federal poverty level) |
|---|---|---|
| QMB (Qualified Medicare Beneficiary) | Part A (if any) and Part B premiums, deductibles, coinsurance and copayments | Up to 100% of FPL |
| SLMB (Specified Low-Income Medicare Beneficiary) | Part B premiums only | 100%–120% of FPL |
| QI (Qualifying Individual) | Part B premiums only; no other Medicaid eligibility | 120%–135% of FPL |
| QDWI (Qualified Disabled Working Individual) | Part A premiums only, for certain working people under 65 with disabilities | Up to 200% of FPL ([data dictionary](https://data.cms.gov/sites/default/files/2025-12/Medicare%20Monthly%20Enrollment%20Data%20Dictionary.pdf)) |

A QMB or SLMB who also has full Medicaid is counted as "QMB Plus" or "SLMB Plus" ([MLN fact sheet](https://www.cms.gov/files/document/beneficiaries-dually-eligible-medicare-medicaid.pdf)). States can raise income and resource limits above the federal floor, except for QDWIs ([MLN fact sheet](https://www.cms.gov/files/document/beneficiaries-dually-eligible-medicare-medicaid.pdf)).

## Where county counts come from

The [Medicare Monthly Enrollment](https://data.cms.gov/data-api/v1/dataset-resources/d7fabe1e-d19b-4333-9eff-e80e0643f2fd) file has national, state and county rows. The latest file listed on 2026-11-24 covers [August 2026](https://data.cms.gov/data-api/v1/dataset-resources/d7fabe1e-d19b-4333-9eff-e80e0643f2fd).

Dual-status columns, as named in the dataset's [API output](https://data.cms.gov/data-api/v1/dataset/d7fabe1e-d19b-4333-9eff-e80e0643f2fd/data?filter%5BYEAR%5D=2026&filter%5BMONTH%5D=August&filter%5BBENE_GEO_LVL%5D=National), with meanings from the [data dictionary](https://data.cms.gov/sites/default/files/2025-12/Medicare%20Monthly%20Enrollment%20Data%20Dictionary.pdf):

- `DUAL_TOT_BENES`: all Medicare-Medicaid enrollees.
- `FULL_DUAL_TOT_BENES` and `PART_DUAL_TOT_BENES`: full and partial duals.
- `QMB_ONLY_BENES`, `QMB_PLUS_BENES`, `SLMB_ONLY_BENES`, `SLMB_PLUS_BENES`: the QMB and SLMB groups.
- `QDWI_QI_BENES`: QDWI and QI combined.
- `OTHR_FULL_DUAL_MDCD_BENES`: full Medicaid without QMB or SLMB.

In the [August 2026 national row](https://data.cms.gov/data-api/v1/dataset/d7fabe1e-d19b-4333-9eff-e80e0643f2fd/data?filter%5BYEAR%5D=2026&filter%5BMONTH%5D=August&filter%5BBENE_GEO_LVL%5D=National), `DUAL_TOT_BENES` is 12,129,039. Full duals are 8,644,481 and partial duals 3,484,558.

For state-level reports and profiles, see CMS's [dual-eligible data resources](https://www.cms.gov/data-research/research/statistical-resources-dually-eligible-beneficiaries).

## How to use county counts

- **Pick a month for point-in-time counts.** Monthly counts represent beneficiaries enrolled in that month ([methodology](https://data.cms.gov/sites/default/files/2024-06/b7a86e30-1e72-49aa-bf0f-68d6f1206467/MME_RY24_Methodology_20240627_508.pdf)).
- **Use full duals for long-term care planning.** Medicaid may cover nursing home care, personal care and home- and community-based services ([MLN fact sheet](https://www.cms.gov/files/document/beneficiaries-dually-eligible-medicare-medicaid.pdf)). Pair counts with [home care supply](/map-home-care-provider-shortages) or a [PACE expansion map](/pace-expansion-mapping).
- **Add age data separately.** For [AAA area plans](/aaa-area-plan-needs-assessment-data), combine county dual counts with [ACS 5-year](/glossary/acs-5-year-estimates) age data.

[GeoChat Atlas](https://app.geochat.ai) is GeoChat AI's healthcare access mapping platform. As of November 2026, it has CMS Medicare, Medicare Advantage and PACE layers.
