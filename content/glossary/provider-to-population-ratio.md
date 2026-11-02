---
title: "Provider-to-Population Ratio: Calculation and Benchmarks"
description: "How to calculate a provider-to-population ratio, the HRSA shortage thresholds in 42 CFR Part 5, and the counting errors that distort access-gap maps."
slug: glossary/provider-to-population-ratio
type: glossary
updated: 2026-11-02
faq:
  - q: "What population-to-physician ratio counts as a primary care shortage?"
    a: "Under HRSA's criteria, a geographic area qualifies at [3,500:1 or more](https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-5/appendix-Appendix%20A%20to%20Part%205) residents per FTE primary care physician. Areas above 3,000:1 also qualify if they have unusually high needs or insufficient capacity."
  - q: "Should I count providers by headcount or FTE?"
    a: "Use FTE when you can. HRSA's criteria treat a [40-hour week as one FTE](https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-5/appendix-Appendix%20A%20to%20Part%205) and count interns and residents as 0.1 FTE."
  - q: "Why do provider-to-population ratios mislead in rural areas?"
    a: "A fixed boundary ignores residents who cross it for care ([McGrail 2012](https://ij-healthgeographics.biomedcentral.com/articles/10.1186/1476-072X-11-50)). Small populations also make the ratio swing sharply when one provider arrives or leaves."
  - q: "Which specialties count as primary care in HPSA ratios?"
    a: "HRSA counts non-federal MDs and DOs in direct patient care in [general or family practice, general internal medicine, pediatrics, and obstetrics and gynecology](https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-5/appendix-Appendix%20A%20to%20Part%205)."
sources:
  - title: "HRSA: Designated HPSA quarterly summary report"
    url: "https://data.hrsa.gov/Default/GenerateHPSAQuarterlyReport"
    accessed: 2026-11-02
  - title: "eCFR: 42 CFR Part 5, Appendix A (Primary Medical Care Shortage Criteria)"
    url: "https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-5/appendix-Appendix%20A%20to%20Part%205"
    accessed: 2026-11-02
  - title: "Cornell LII: 42 CFR Appendix A to Part 5"
    url: "https://www.law.cornell.edu/cfr/text/42/appendix-A_to_part_5"
    accessed: 2026-11-02
  - title: "eCFR: 42 CFR Part 5, Appendix B (Dental Shortage Criteria)"
    url: "https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-5/appendix-Appendix%20B%20to%20Part%205"
    accessed: 2026-11-02
  - title: "Cornell LII: 42 CFR Appendix B to Part 5"
    url: "https://www.law.cornell.edu/cfr/text/42/appendix-B_to_part_5"
    accessed: 2026-11-02
  - title: "eCFR: 42 CFR Part 5, Appendix C (Mental Health Shortage Criteria)"
    url: "https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-5/appendix-Appendix%20C%20to%20Part%205"
    accessed: 2026-11-02
  - title: "HRSA Bureau of Health Workforce: Scoring Shortage Designations"
    url: "https://bhw.hrsa.gov/workforce-shortage-areas/shortage-designation/scoring"
    accessed: 2026-11-02
  - title: "HRSA Data Warehouse: HPSA Find"
    url: "https://data.hrsa.gov/tools/shortage-area/hpsa-find"
    accessed: 2026-11-02
  - title: "Bindman AB. Using the National Provider Identifier for Health Care Workforce Evaluation. Medicare & Medicaid Research Review 3(3), 2013"
    url: "https://www.cms.gov/mmrr/Downloads/MMRR2013_003_03_b03.pdf"
    accessed: 2026-11-02
  - title: "McGrail MR. Spatial accessibility of primary health care utilising the two step floating catchment area method. Int J Health Geographics 11:50, 2012"
    url: "https://ij-healthgeographics.biomedcentral.com/articles/10.1186/1476-072X-11-50"
    accessed: 2026-11-02
---

A provider-to-population ratio compares the residents of an area with the providers serving them, usually written as residents per full-time-equivalent (FTE) provider. HRSA's shortage criteria state it as population to FTE provider, for example 3,500:1 ([eCFR](https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-5/appendix-Appendix%20A%20to%20Part%205)).

## How it is calculated

1. Count the population of the service area.
2. Count providers and convert them to FTEs.
3. Divide population by FTE providers to get residents per provider.

The inverse, providers per 1,000 residents, is the form used in HRSA's [Index of Medical Underservice](/glossary/mua-mup) ([HRSA](https://bhw.hrsa.gov/workforce-shortage-areas/shortage-designation/scoring)).

HRSA's primary care criteria set the counting rules ([42 CFR Part 5, App. A](https://www.law.cornell.edu/cfr/text/42/appendix-A_to_part_5)):

- **Population:** the permanent resident civilian population, excluding institutional inmates. Seasonal residents may be added, weighted by time present, and tourists at a 0.25 weight.
- **Who counts:** non-federal MDs and DOs in direct patient care in family or general practice, general internal medicine, pediatrics, and obstetrics and gynecology.
- **Who does not:** physicians working solely in administration, research or teaching, hospital physicians working only in inpatient care, and emergency room physicians.
- **FTE:** a 40-hour week is one FTE, and each four hours of patient care is 0.1 FTE. Interns and residents count as 0.1 FTE.

## Benchmarks HRSA uses

| Discipline and provider | Geographic area qualifies at | With unusually high need |
|---|---|---|
| Primary care, FTE physicians | 3,500:1 or more | Over 3,000:1 and under 3,500:1 |
| Dental, FTE dentists | 5,000:1 or more | Over 4,000:1 and under 5,000:1 |
| Mental health, psychiatrists only | 30,000:1 or more | 20,000:1 or more |
| Mental health, core professionals only | 9,000:1 or more | 6,000:1 or more |
| Mental health, both together | 6,000:1 core and 20,000:1 psychiatrists | 4,500:1 core and 15,000:1 psychiatrists |

Sources: [Appendix A](https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-5/appendix-Appendix%20A%20to%20Part%205), [Appendix B](https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-5/appendix-Appendix%20B%20to%20Part%205) and [Appendix C](https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-5/appendix-Appendix%20C%20to%20Part%205) to 42 CFR Part 5. Population groups qualify at 3,000:1 for primary care and 4,000:1 for dental.

Note: the codified text of Appendix B, Part I.A.2(a) reads "less than 5,000:1" ([Cornell LII](https://www.law.cornell.edu/cfr/text/42/appendix-B_to_part_5)), an apparent drafting error. HRSA requires ["at least 5,000 to 1"](https://data.hrsa.gov/Default/GenerateHPSAQuarterlyReport) for dental geographic designations, consistent with Part I.C.

## Data sources

- **Population:** [ACS 5-year estimates](/glossary/acs-5-year-estimates) for tracts, block groups and ZCTAs.
- **Providers:** the NPPES registry filtered by [taxonomy code](/glossary/npi-taxonomy-codes), or state licensing data. NPPES gives headcounts, not FTEs.

## Common pitfalls

- **Headcount instead of FTE.** An NPI count treats a half-day clinician like a full-time one.
- **Counting providers who do not see patients.** NPPES specialty is self-reported, and CMS does not verify it ([Bindman 2013](https://www.cms.gov/mmrr/Downloads/MMRR2013_003_03_b03.pdf)). Out-of-date information does not deactivate an NPI.
- **Ignoring cross-border use.** Boundary-based ratios miss patients who travel between areas ([McGrail 2012](https://ij-healthgeographics.biomedcentral.com/articles/10.1186/1476-072X-11-50)). HRSA treats contiguous-area providers as available unless they are over 30 minutes away, overutilized or inaccessible ([eCFR](https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-5/appendix-Appendix%20A%20to%20Part%205)).
- **Small denominators.** In a small population, one provider moves the ratio sharply. Check ACS margins of error.
- **Mixed conventions.** 3,500:1 and 0.29 providers per 1,000 describe the same supply, so label units.

## Using ratios in access-gap work

1. Build service areas the way HRSA does: a county, or contiguous counties whose population centers are within 30 minutes of each other ([eCFR](https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-5/appendix-Appendix%20A%20to%20Part%205)).
2. Convert provider counts to FTE where you have hours data.
3. Compare results with the thresholds above, then confirm designations in [HPSA Find](https://data.hrsa.gov/tools/shortage-area/hpsa-find).
4. Pair ratios with [drive-time measures](/glossary/drive-time-access), which account for travel across boundaries.
