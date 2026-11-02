---
title: "GeoChat AI Data Sources and Methods"
description: "How GeoChat AI builds its maps: ACS 2020-2024 estimates, NPPES provider records, HUD and Census crosswalks, data versions in use, and known limits."
slug: methods
type: page
show_cta: true
updated: 2026-11-02
sources:
  - title: "American Community Survey (ACS), U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/acs"
    accessed: 2026-11-02
  - title: "2020 Census, U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/decennial-census/decade/2020/2020-census-main.html"
    accessed: 2026-11-02
  - title: "NPPES NPI Registry, CMS"
    url: "https://npiregistry.cms.hhs.gov/"
    accessed: 2026-11-02
  - title: "NPPES Downloadable Files (NPI Files), CMS"
    url: "https://download.cms.gov/nppes/NPI_Files.html"
    accessed: 2026-11-02
  - title: "HUD USPS ZIP Code Crosswalk Files"
    url: "https://www.huduser.gov/portal/datasets/usps_crosswalk.html"
    accessed: 2026-11-02
  - title: "Relationship Files, U.S. Census Bureau"
    url: "https://www.census.gov/geographies/reference-files/time-series/geo/relationship-files.html"
    accessed: 2026-11-02
  - title: "ZIP Code Tabulation Areas (ZCTAs), U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html"
    accessed: 2026-11-02
  - title: "CMS Data"
    url: "https://data.cms.gov/"
    accessed: 2026-11-02
  - title: "HRSA Data Warehouse"
    url: "https://data.hrsa.gov/"
    accessed: 2026-11-02
  - title: "PLACES: Local Data for Better Health, CDC"
    url: "https://www.cdc.gov/places/"
    accessed: 2026-11-02
  - title: "42 CFR Part 5, Appendix A: Criteria for Primary Medical Care HPSAs (eCFR)"
    url: "https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-5/appendix-Appendix%20A%20to%20Part%205"
    accessed: 2026-11-02
---

GeoChat AI's maps combine U.S. Census Bureau population estimates with provider records from NPPES, the national registry of National Provider Identifiers (NPIs). This page describes [GeoChat Atlas](https://atlas.geochat.ai), the current version of the platform. It lists each source, the version in use, how records are prepared and what the data cannot tell you.

## Data versions in use

| Source | Version | Used for |
|---|---|---|
| [American Community Survey](https://www.census.gov/programs-surveys/acs) (ACS) | 2020–2024 5-year estimates | Population and its characteristics |
| [2020 Census](https://www.census.gov/programs-surveys/decennial-census/decade/2020/2020-census-main.html) | 2020 | Race and ethnicity |
| [NPPES](https://download.cms.gov/nppes/NPI_Files.html) | October 2026 monthly file | Clinician and organization counts |
| [HUD-USPS ZIP crosswalk](https://www.huduser.gov/portal/datasets/usps_crosswalk.html) | 2026, 2nd quarter | Linking ZIP codes and counties |
| [Census relationship files](https://www.census.gov/geographies/reference-files/time-series/geo/relationship-files.html) and ZCTA boundaries | 2020 | ZIP code areas and their counties |

Some organization map layers, such as home care agencies and adult day care, use NPPES extracts from 2025 to early 2026.

There is no automatic refresh. Each source is rebuilt by hand after its publisher releases a new version.

## Other data layers

GeoChat Atlas has more than 100 data layers. Beyond the core sources above, they include:

| Publisher | Examples | Data dates |
|---|---|---|
| [CMS](https://data.cms.gov/) | Hospitals, nursing homes, home health, hospice, Medicare and Medicare Advantage, Part D, PACE | Mostly 2024 to October 2026 releases; Medicare Advantage 2027 |
| [HRSA](https://data.hrsa.gov/) | Health Professional Shortage Areas and Medically Underserved Areas; health center sites; Uniform Data System (UDS) | Shortage areas downloaded October 28, 2026; UDS 2025 |
| [CDC](https://www.cdc.gov/places/) | PLACES local health estimates; Social Vulnerability Index (SVI); overdose and cancer data | PLACES 2025 release (2023 survey data); SVI 2022 |
| Other federal agencies | Census Bureau, USDA, HUD, SSA, BLS, VA, FCC, EPA and SAMHSA | Varies by layer |
| State of California | California-specific layers | Varies by layer |

Check the data year of any layer before you compare it with another. Survey years, release years and designation dates often differ.

## Population data: ACS and the 2020 Census

Population figures use ACS 2020–2024 5-year estimates, at county, ZIP code and census tract level. No 1-year estimates are used. Race and ethnicity are the exception: they come from the 2020 Census.

| Topic | ACS tables |
|---|---|
| Age and sex | B01001, S0101 |
| Poverty and household income | B17001, B19037 |
| Health insurance | B27010 |
| Employment | B23025; C18120 (by disability status); B23008 (children by parents' employment) |
| Disability | S1810, C18120 |
| Language spoken at home | C16001, S1601 |
| Living arrangements and vehicles | B09021, B08201 |
| Housing | B25018, B25034 |
| Computers and internet | B28005, S2801 |
| Fertility | S1301 |

What to keep in mind:

- ACS figures are survey estimates with margins of error. Error is largest for small areas and small subgroups. See [ACS 5-year estimates](/glossary/acs-5-year-estimates).
- A 5-year estimate describes the whole 2020–2024 period, not a single year.
- ACS describes where people live, not where they receive care.

## Provider data: NPPES

Provider counts come from the NPPES October 2026 monthly file. Records are prepared this way:

1. **Entity type.** Clinician counts use individual NPIs (entity type 1) only. Personal care and adult day care counts use organization NPIs (entity type 2) only.
2. **One count per NPI.** Each NPI is counted once per measure.
3. **Active NPIs only.** NPIs that were deactivated and not reactivated are excluded.
4. **Primary taxonomy.** A clinician counts only under their primary [taxonomy code](/glossary/npi-taxonomy-codes).
5. **Fixed code lists.** Each measure uses a fixed list of taxonomy codes. For example, family medicine physicians are counted by code 207Q00000X.
6. **Practice address.** Providers are placed by their practice-location address, not their mailing address. Only U.S. practice locations with a valid 5-digit ZIP code are kept.

What to keep in mind:

- An NPI shows that a provider registered, not that they see patients, accept new patients or work full time. Retirement does not deactivate an NPI. Counts are therefore an upper limit on practicing clinicians.
- Provider-to-population rates built this way run higher than full-time-equivalent ratios such as those HRSA uses for [shortage designations](/glossary/hpsa). HRSA's primary care count also includes OB/GYNs and excludes nurse practitioners ([eCFR](https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-5/appendix-Appendix%20A%20to%20Part%205)), so the ratios are not directly comparable. See [provider-to-population ratio](/glossary/provider-to-population-ratio).
- Providers at a PO-box-only ZIP code drop out of ZIP-level counts but are kept in county counts.

## Geography: counties, ZIP codes and tracts

Coverage is all 50 states, the District of Columbia and Puerto Rico: 3,222 counties, 33,791 ZIP code areas and about 85,000 census tracts. Connecticut appears as its 9 planning regions, which replaced its counties in Census geography. Block groups are not covered.

ZIP codes are mail routes, not areas. Values labeled "ZIP code" are ZIP Code Tabulation Areas (ZCTAs), the Census Bureau's 2020 approximations of ZIP code areas. See [ZCTA vs ZIP code](/glossary/zcta-vs-zip-code).

Areas are linked with these files:

- **HUD-USPS ZIP–County crosswalk, 2026 Q2.** Residential address ratios assign each ZIP code to one county. For measures published only by county, a ZIP code shows the rate of the county it is assigned to. Business address ratios place providers in counties. Total address ratios are the fallback.
- **2020 Census ZCTA–county relationship file,** for U.S. territories and Connecticut.
- **2020 ZCTA boundaries,** for ZIP code shapes on the map.
- **2010–2020 tract and ZCTA relationship files,** to line up older data with 2020 geography for trend maps.

Where a ZIP code spans two counties, read results near the border with care. A county-only measure looks the same in every ZIP code of that county; it does not show differences within the county.

## The AI chat

The chat has no web search. It is instructed to report only figures returned by its own queries of the platform's datasets. The model's general knowledge still shapes how it plans, interprets and words answers, so this is an instruction, not a guarantee. It also answers general questions, such as what the platform can do, without data.

Before a figure goes into a report, check it against the map and the original source, and record the source and data year.

## When you need expert review

For published or submitted assessments, GeoChat AI offers expert review of AI findings, primary research, community interviews and custom needs assessment reports. [Book a call](https://calendly.com/v-wong-geochat/30min) to discuss scope.

## Platform status

GeoChat AI is new. The current platform, [GeoChat Atlas](https://atlas.geochat.ai), is version 2 and replaces the earlier app at app.geochat.ai. A free account needs no payment details.

## Corrections

If you find an error on a map or on this site, [tell us](https://geochat.ai/about#contact). Corrections are made and dated on the page.
