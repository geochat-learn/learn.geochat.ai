---
title: "Healthcare Access in 10 California Counties (2026 Data)"
description: "Older adults, uninsured rates, primary care supply and shortage-area coverage for 10 California counties, from ACS, NPPES and HRSA data."
slug: california-county-healthcare-access-2026
type: data
updated: 2026-11-02
dataset:
  name: "Healthcare access measures for 10 California counties, 2026"
  csv: /data/california-10-counties-healthcare-access-2026.csv
  spatial: "California, United States"
  temporal: "2020/2026"
  variables:
    - "Adults aged 65 and older"
    - "Share of population aged 65 and older"
    - "Share uninsured, all ages"
    - "Share uninsured, aged 65 and older"
    - "Primary care physicians per 10,000 residents"
    - "Primary care nurse practitioners per 10,000 residents"
    - "Primary care HPSA coverage and highest score"
    - "Mental health HPSA coverage"
  based_on:
    - "https://www.census.gov/programs-surveys/acs"
    - "https://download.cms.gov/nppes/NPI_Files.html"
    - "https://data.hrsa.gov/topics/health-workforce/shortage-areas"
faq:
  - q: "Which of these California counties has the fewest primary care physicians?"
    a: "Imperial County, with 4.1 primary care physicians per 10,000 residents (NPPES, October 2026; ACS 2020–2024 population). Counting primary care nurse practitioners too, Imperial is still lowest, at about 11.4 per 10,000."
  - q: "Are any of these counties entirely inside primary care shortage areas?"
    a: "Yes. Every land census tract in Tulare, Imperial and Humboldt lies inside a primary care HPSA, based on HRSA data from October and November 2026. None has a single countywide designation; the coverage comes from several local designations."
  - q: "Why can a county with many registered physicians still be a shortage area?"
    a: "HRSA designations count full-time-equivalent clinicians, not registrations. Many designations also cover a population group, such as low-income residents, rather than everyone."
  - q: "Where do these numbers come from?"
    a: "Population and insurance figures come from ACS 2020–2024 5-year estimates (tables B01001 and B27010). Provider counts come from the NPPES October 2026 monthly file. Shortage areas come from HRSA data downloaded October 28, 2026 and rechecked November 2, 2026. See [data sources and methods](/methods/)."
sources:
  - title: "American Community Survey (ACS), U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/acs"
    accessed: 2026-11-02
  - title: "NPPES Downloadable Files (NPI Files), CMS"
    url: "https://download.cms.gov/nppes/NPI_Files.html"
    accessed: 2026-11-02
  - title: "Health Workforce Shortage Areas, HRSA Data Warehouse"
    url: "https://data.hrsa.gov/topics/health-workforce/shortage-areas"
    accessed: 2026-11-02
  - title: "Scoring Shortage Designations, HRSA"
    url: "https://bhw.hrsa.gov/workforce-shortage-areas/shortage-designation/scoring"
    accessed: 2026-11-02
  - title: "Extended Timeline for HPSA Designations, HRSA"
    url: "https://www.hrsa.gov/about/news/press-releases/extended-timeline-health-professional-shortage-area-designations"
    accessed: 2026-11-02
  - title: "42 CFR Part 5, Appendix A: Criteria for Primary Medical Care HPSAs (eCFR)"
    url: "https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-5/appendix-Appendix%20A%20to%20Part%205"
    accessed: 2026-11-02
  - title: "HUD USPS ZIP Code Crosswalk Files"
    url: "https://www.huduser.gov/portal/datasets/usps_crosswalk.html"
    accessed: 2026-11-02
---

Primary care physician supply differs more than threefold across these 10 California counties: Alameda has 13.7 per 10,000 residents and Imperial has 4.1. The four lowest, Imperial, Kern, Tulare and Riverside, are all in inland Southern California or the southern San Joaquin Valley.

The counties cover large metro areas, the Central Valley, inland Southern California, the Mexico border and the rural North Coast. GeoChat AI computed all figures from public data. The sources are [ACS](https://www.census.gov/programs-surveys/acs) 2020–2024 5-year estimates, the [NPPES](https://download.cms.gov/nppes/NPI_Files.html) October 2026 provider file and [HRSA](https://data.hrsa.gov/topics/health-workforce/shortage-areas) shortage area data.

## Key findings

- **Physician supply is lowest in four inland counties.** Imperial (4.1), Kern (7.0), Tulare (7.2) and Riverside (7.4) have the fewest primary care physicians per 10,000 residents. Alameda (13.7), San Diego (12.5) and Sacramento (12.0) have the most.
- **Nurse practitioners narrow some gaps.** Imperial is the only county with more primary care nurse practitioners (7.3 per 10,000) than primary care physicians (4.1). Counting both, Imperial (about 11.4) and Riverside (about 12.0) are the two lowest.
- **Riverside has the lowest nurse practitioner rate.** Its 4.6 per 10,000 is the lowest of the 10, and Humboldt's 8.3 is the highest.
- **Three counties are fully covered by primary care shortage areas.** Every land census tract in Tulare, Imperial and Humboldt lies inside a primary care [HPSA](/glossary/hpsa). In each, the coverage comes from several local designations, not one countywide designation. Alameda's primary care designations are for specific facilities only.
- **Countywide mental health shortage areas target population groups.** Tulare and Imperial have countywide mental health HPSAs for low-income residents. Humboldt's covers low-income, homeless and migrant farmworker residents. Tulare and Imperial also have countywide geographic mental health HPSAs that HRSA has proposed for withdrawal. Kern is fully covered by several local mental health designations.
- **Shortage scores do not track physician rates.** Imperial has the fewest physicians but the lowest primary care HPSA score of the nine scored counties (15). Fresno has the highest (19). Kern's 19 rests on a designation proposed for withdrawal. Scores also weigh poverty, travel time and other factors ([HRSA](https://bhw.hrsa.gov/workforce-shortage-areas/shortage-designation/scoring)).
- **Humboldt has the oldest population.** 19.8% of residents are 65 or older, against 11.9% in Kern and Tulare.
- **Los Angeles and Tulare have the highest uninsured rates.** About 8.2% and 8.1% of residents lack health insurance, about twice Alameda's 4.0%. Among adults 65 and older, the uninsured rate is 1.6% or lower in every county.

## The data

| County | Adults 65+ | Share 65+ | Uninsured, all ages | Uninsured, 65+ | Primary care physicians per 10,000 | Primary care NPs per 10,000 | Primary care HPSA coverage (highest score) | Mental health HPSA coverage |
|---|---|---|---|---|---|---|---|---|
| Los Angeles | 1,487,700 | 15.2% | 8.2% | 1.6% | 11.2 | 6.4 | Part of county (18) | Part of county |
| San Diego | 507,734 | 15.4% | 6.4% | 0.9% | 12.5 | 6.7 | Part of county (17) | Part of county |
| Riverside | 382,888 | 15.4% | 7.7% | 1.1% | 7.4 | 4.6 | Part of county (16) | Part of county |
| Sacramento | 243,370 | 15.3% | 4.9% | 0.7% | 12.0 | 5.6 | Part of county (16)\* | Part of county |
| Alameda | 254,161 | 15.4% | 4.0% | 1.0% | 13.7 | 5.0 | Facilities only | Part of county\* |
| Fresno | 131,488 | 12.9% | 6.7% | 1.2% | 10.0 | 6.6 | Part of county (19) | Part of county |
| Kern | 108,560 | 11.9% | 7.8% | 1.1% | 7.0 | 6.0 | Part of county (19)\* | Entire county |
| Tulare | 57,101 | 11.9% | 8.1% | 1.3% | 7.2 | 5.7 | Entire county (17) | Entire county |
| Imperial | 24,701 | 13.7% | 6.0% | 0.9% | 4.1 | 7.3 | Entire county (15) | Entire county |
| Humboldt | 26,660 | 19.8% | 4.9% | 0.1%† | 10.6 | 8.3 | Entire county (16) | Entire county |

\* Rests on a designation HRSA has proposed for withdrawal. In Sacramento, it is the only geographic or population primary care HPSA. In Kern, it sets the score; the highest fully designated score is 18. In Alameda, it is the only mental health HPSA.

† Unreliable: an estimate of 28 people with a margin of error of ±28.

[Download the data (CSV)](/data/california-10-counties-healthcare-access-2026.csv). You may reuse it with a link to this page.

## How to read these numbers

- **Provider rates count registrations, not full-time clinicians.** An NPI stays active after a clinician retires or cuts back hours, so these rates are an upper limit. They run higher than the full-time-equivalent ratios HRSA uses. HRSA's primary care count also includes OB/GYNs and excludes nurse practitioners ([eCFR](https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-5/appendix-Appendix%20A%20to%20Part%205)), so the ratios are not directly comparable. See [provider-to-population ratio](/glossary/provider-to-population-ratio).
- **Numerator and denominator come from different years.** Rates divide an October 2026 provider count by the 2020–2024 average population.
- **"Entire county" does not mean one designation covers everyone.** It can be several local designations, or one designation for a population group, such as low-income residents. Both are reasons a county with a mid-range physician rate, such as Humboldt, can still be fully covered.
- **Proposed withdrawals are still HPSAs.** Designations proposed for withdrawal remain recognized until HRSA's final decisions, expected by July 1, 2027 ([HRSA](https://www.hrsa.gov/about/news/press-releases/extended-timeline-health-professional-shortage-area-designations)). The table counts them and marks where a result depends on one.
- **County figures hide local gaps.** "Part of county" means some census tracts are outside every designation. Map tracts or ZIP codes to see where the designated areas are.
- **Small counties have wider margins of error.** ACS estimates for Imperial and Humboldt rest on smaller samples than those for Los Angeles. See [ACS 5-year estimates](/glossary/acs-5-year-estimates).

## Definitions

- **Adults 65+ and share 65+:** ACS 2020–2024 5-year estimates, table B01001.
- **Uninsured:** share of the civilian noninstitutionalized population with no health insurance, ACS table B27010.
- **Primary care physicians:** individual NPIs whose primary taxonomy is family medicine, general internal medicine or pediatrics.
- **Primary care NPs:** individual NPIs whose primary taxonomy is a primary care nurse practitioner code.
- **Provider placement:** providers are placed by practice-location ZIP code and assigned to counties with the [HUD-USPS ZIP–County crosswalk](https://www.huduser.gov/portal/datasets/usps_crosswalk.html) business address ratios.
- **HPSA coverage:** "Entire county" means every land census tract lies inside at least one HPSA of that discipline. "Part of county" means some tracts do not. "Facilities only" means the only designations are for specific facilities, such as health centers. Designated HPSAs and those proposed for withdrawal both count.
- **Highest score:** the highest score among the county's geographic and population primary care HPSAs, including those proposed for withdrawal. Facility HPSAs are excluded. Primary care scores run from 0 to 25 ([HRSA](https://bhw.hrsa.gov/workforce-shortage-areas/shortage-designation/scoring)); higher scores mean greater need (see [HPSA](/glossary/hpsa)).
- **HPSA data dates:** HRSA files downloaded October 28, 2026 and rechecked against HRSA's November 2, 2026 files with the same results.

Full processing steps are on the [data sources and methods](/methods/) page.

## Using this data in a needs assessment

1. **Cite the source and year for each figure.** Hospital CHNAs must describe the data used; see the [CHNA access-gap mapping guide](/chna-access-gap-mapping-guide/).
2. **Confirm HPSA status before you publish.** Designations change; check the HPSA ID, type, score and status in HRSA's [HPSA Find](https://data.hrsa.gov/tools/shortage-area/hpsa-find).
3. **Look below the county level.** Where a county shows "Part of county," map ZIP codes or tracts to find where the gaps are. In GeoChat AI you can drill into ZIP codes and compare regions.
4. **Ask for another county.** If you want a county added to this table, [tell us](https://geochat.ai/about#contact).
