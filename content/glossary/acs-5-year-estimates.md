---
title: "ACS 5-Year vs 1-Year Estimates: Which to Use"
description: "ACS 5-year estimates pool 60 months of data for every area, including tracts and ZCTAs. How they differ from 1-year data, MOEs and release dates."
slug: glossary/acs-5-year-estimates
type: glossary
updated: 2026-11-02
faq:
  - q: "When should I use ACS 5-year instead of 1-year estimates?"
    a: "Use 5-year estimates for census tracts, block groups, ZCTAs and other small areas, where [1-year estimates are not published](https://www.census.gov/programs-surveys/acs/geography-acs/areas-published.html). Use 1-year estimates for large areas when currency matters more than precision."
  - q: "What confidence level do ACS margins of error use?"
    a: "ACS margins of error are published at the [90 percent confidence level](https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020_ch07.pdf). Add and subtract the MOE from the estimate to get the 90 percent confidence interval."
  - q: "Can I compare 2019-2023 and 2020-2024 ACS 5-year data?"
    a: "The Census Bureau says [not to compare overlapping periods](https://www.census.gov/programs-surveys/acs/guidance/comparing-acs-data.html). Compare non-overlapping 5-year periods instead."
  - q: "Is a 2020-2024 ACS 5-year estimate the same as a 2022 estimate?"
    a: "No. It describes the whole 60-month period, and the Census Bureau advises [against labeling it with the midpoint year](https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020_ch03.pdf)."
sources:
  - title: "U.S. Census Bureau: When to Use 1-year or 5-year Estimates"
    url: "https://www.census.gov/programs-surveys/acs/guidance/estimates.html"
    accessed: 2026-11-02
  - title: "U.S. Census Bureau: Geography and ACS, Areas Published"
    url: "https://www.census.gov/programs-surveys/acs/geography-acs/areas-published.html"
    accessed: 2026-11-02
  - title: "U.S. Census Bureau: Understanding and Using ACS Data, Ch. 3, Single-Year and Multiyear Estimates"
    url: "https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020_ch03.pdf"
    accessed: 2026-11-02
  - title: "U.S. Census Bureau: Understanding and Using ACS Data, Ch. 7, Understanding Error and Determining Statistical Significance"
    url: "https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020_ch07.pdf"
    accessed: 2026-11-02
  - title: "U.S. Census Bureau: Comparing ACS Data"
    url: "https://www.census.gov/programs-surveys/acs/guidance/comparing-acs-data.html"
    accessed: 2026-11-02
  - title: "U.S. Census Bureau: ACS 2024 Data Release Schedule"
    url: "https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release-schedule.html"
    accessed: 2026-11-02
  - title: "U.S. Census Bureau: ACS 2025 Data Release Schedule"
    url: "https://www.census.gov/programs-surveys/acs/news/data-releases/2025/release-schedule.html"
    accessed: 2026-11-02
---

American Community Survey (ACS) 5-year estimates pool 60 months of responses and are published for all areas. ACS 1-year estimates use 12 months and cover only areas with 65,000 or more people ([Census Bureau](https://www.census.gov/programs-surveys/acs/guidance/estimates.html)).

## 5-year vs 1-year estimates

| | 1-year | 5-year |
|---|---|---|
| Data collected | 12 months | 60 months |
| Areas published | Population 65,000+ | All areas |
| Sample size | Smallest | Largest |
| Reliability | Less reliable than 5-year | Most reliable |
| Currency | Most current | Least current |
| Best when | Currency matters more than precision; large populations | Precision matters more than currency; very small populations and tracts |

Source: [Census Bureau](https://www.census.gov/programs-surveys/acs/guidance/estimates.html). Supplemental 1-year estimates extend to areas of 20,000 or more people.

Census tracts, block groups and ZIP Code Tabulation Areas appear only in 5-year data ([Census Bureau](https://www.census.gov/programs-surveys/acs/geography-acs/areas-published.html)). See [ZCTA vs ZIP Code](/glossary/zcta-vs-zip-code).

## What a 5-year estimate represents

A 5-year estimate is a period estimate built from data collected over 60 months ([Census handbook, ch. 3](https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020_ch03.pdf)). It does not describe any specific day, month or year. The Census Bureau advises against labeling 2014–2018 data as "2016."

## Margins of error

ACS margins of error (MOEs) are published at the 90 percent confidence level ([Census handbook, ch. 7](https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020_ch07.pdf)). Add and subtract the MOE from the estimate to get the 90 percent confidence interval. Divide the MOE by 1.645 to get the standard error.

The coefficient of variation (CV) is the standard error divided by the estimate, usually shown as a percent. The Census Bureau sets no hard-and-fast rule for acceptable error.

## Release timing (as of November 2026)

- 2020–2024 5-year estimates: released January 29, 2026 ([2024 schedule](https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release-schedule.html)).
- 2025 1-year estimates: released October 29, 2026 ([Census Bureau](https://www.census.gov/programs-surveys/acs/news/data-releases/2025/release.html)).
- 2021–2025 5-year estimates: listed as "TBD" on the schedule last revised October 13, 2026.

## Common pitfalls

- **Comparing overlapping periods.** Do not compare 2019–2023 with 2020–2024; compare non-overlapping periods ([Census Bureau](https://www.census.gov/programs-surveys/acs/guidance/comparing-acs-data.html)).
- **Mixing products.** Compare 1-year estimates only with 1-year, and 5-year only with 5-year.
- **Ignoring MOEs in small areas.** Run significance tests before calling a difference real ([Census handbook, ch. 7](https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020_ch07.pdf)).
- **Adding MOEs directly.** Aggregated estimates need extra MOE calculations. The Variance Replicate Tables give exact MOEs for selected 5-year Detailed Tables.
- **Using ACS for headcounts beside the census.** When comparing with the decennial census, use census counts for totals and ACS for percentages, medians and rates ([Census Bureau](https://www.census.gov/programs-surveys/acs/guidance/comparing-acs-data.html)).

## Using ACS in access-gap and needs-assessment work

1. Use 5-year data for tracts, block groups and ZCTAs.
2. Download the MOE with every estimate and compute a CV.
3. Combine adjacent small areas when CVs are high, and recompute the MOE.
4. Use one 5-year vintage for every indicator on the same map.
5. Cite the full period, for example "2020–2024 ACS 5-year estimates."

[GeoChat AI](https://atlas.geochat.ai)'s maps draw on ACS population figures, so read its ZIP-level views with the same period and margin-of-error cautions.
