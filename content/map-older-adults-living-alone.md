---
title: "How to Find Where Older Adults Live Alone in Your County"
description: "Map older adults living alone by census tract or ZIP code with ACS tables B09021, B09020, B11010 and S0102, plus margin-of-error checks and limits."
slug: map-older-adults-living-alone
type: guide
updated: 2026-11-03
faq:
  - q: "Which Census table shows how many older adults live alone?"
    a: "ACS table [B09021](https://api.census.gov/data/2024/acs/acs5/groups/B09021.html), line _023, gives people 65 and over who live alone. [B09020](https://api.census.gov/data/2024/acs/acs5/groups/B09020.html) splits the same group by sex. For 60+, Subject Table [S0102](https://api.census.gov/data/2024/acs/acs5/subject/groups/S0102.html) gives the percent of 60+ households whose householder lives alone."
  - q: "Can I get older adults living alone by census tract?"
    a: "Yes. ACS 5-year detailed tables are published down to [block groups and subject tables down to census tracts](https://www.census.gov/programs-surveys/acs/news/data-releases/2025/release-schedule.html). Both datasets are also offered by ZIP Code Tabulation Area ([detailed](https://api.census.gov/data/2024/acs/acs5/geography.json), [subject](https://api.census.gov/data/2024/acs/acs5/subject/geography.json)). Expect wide margins of error for small tracts."
  - q: "Does living alone mean an older adult is socially isolated?"
    a: "No. CDC defines social isolation as having [no relationships or contact with others and little to no social support](https://www.cdc.gov/social-connectedness/risk-factors/index.html). CDC lists adults living alone among groups that loneliness may affect more. Treat living alone as a marker of possible need."
  - q: "Do these counts include people in nursing homes?"
    a: "B09021 covers only [adults in households](https://api.census.gov/data/2024/acs/acs5/groups/B09021.json). Skilled nursing facilities are [group quarters](https://www2.census.gov/programs-surveys/acs/tech_docs/subject_definitions/2024_ACSSubjectDefinitions.pdf), so their residents are not in it. [B09020](https://api.census.gov/data/2024/acs/acs5/groups/B09020.json) counts all people 65 and over, with a separate group quarters line."
  - q: "Is there a free tool that maps Census data by ZIP code and tract?"
    a: "GeoChat Atlas is free with no credit card. It maps ACS 2020–2024 5-year estimates at county, ZIP code (ZCTA) and census tract level. Check whether it has a living-alone layer; nonprofits can request a new map if it does not. See [methods](/methods)."
sources:
  - title: "Census Data API: ACS 5-year 2024, group B09021 (Living Arrangements of Adults 18 Years and Over by Age)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B09021.html"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 5-year 2024, group B09021 variables with universe (JSON)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B09021.json"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 5-year 2024, group B09020 (Relationship by Household Type (Including Living Alone) for the Population 65 Years and Over)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B09020.html"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 5-year 2024, group B09020 variables with universe (JSON)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B09020.json"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 5-year 2024, group B11010 (Nonfamily Households by Sex of Householder by Living Alone by Age of Householder)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B11010.html"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 5-year 2024, group B11007 (Households by Presence of People 65 Years and Over, Household Size and Household Type)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B11007.html"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 5-year 2024, group B25011 (Tenure by Household Type (Including Living Alone) and Age of Householder)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B25011.html"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 5-year 2024, Subject Table S0102 (Population 60 Years and Over in the United States)"
    url: "https://api.census.gov/data/2024/acs/acs5/subject/groups/S0102.html"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 5-year 2024, Subject Table S0102 variables (JSON)"
    url: "https://api.census.gov/data/2024/acs/acs5/subject/groups/S0102.json"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 5-year 2024, group B01001 (Sex by Age)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B01001.html"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 5-year 2024, group B01001 variables with universe (JSON)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B01001.json"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 5-year 2024, group B18106 (Sex by Age by Self-Care Difficulty)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B18106.html"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 5-year 2024, group B18107 (Sex by Age by Independent Living Difficulty)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B18107.html"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 5-year 2024, available geographies (detailed tables, JSON)"
    url: "https://api.census.gov/data/2024/acs/acs5/geography.json"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 5-year 2024, available geographies (subject tables, JSON)"
    url: "https://api.census.gov/data/2024/acs/acs5/subject/geography.json"
    accessed: 2026-11-03
  - title: "2025 Data Release Schedule - American Community Survey"
    url: "https://www.census.gov/programs-surveys/acs/news/data-releases/2025/release-schedule.html"
    accessed: 2026-11-03
  - title: "When to Use 1-year or 5-year Estimates - American Community Survey"
    url: "https://www.census.gov/programs-surveys/acs/guidance/estimates.html"
    accessed: 2026-11-03
  - title: "American Community Survey and Puerto Rico Community Survey 2024 Subject Definitions - U.S. Census Bureau"
    url: "https://www2.census.gov/programs-surveys/acs/tech_docs/subject_definitions/2024_ACSSubjectDefinitions.pdf"
    accessed: 2026-11-03
  - title: "Understanding and Using ACS Data, Chapter 7: Understanding Error and Determining Statistical Significance - U.S. Census Bureau"
    url: "https://www.census.gov/content/dam/Census/library/publications/2018/acs/acs_general_handbook_2018_ch07.pdf"
    accessed: 2026-11-03
  - title: "Understanding and Using ACS Data, Chapter 8: Calculating Measures of Error for Derived Estimates - U.S. Census Bureau"
    url: "https://www.census.gov/content/dam/Census/library/publications/2018/acs/acs_general_handbook_2018_ch08.pdf"
    accessed: 2026-11-03
  - title: "Increased Margins of Error in the 5-Year Estimates Containing Data Collected in 2020 - U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/acs/technical-documentation/user-notes/2022-04.html"
    accessed: 2026-11-03
  - title: "Request a U.S. Census Data API Key"
    url: "https://api.census.gov/data/key_signup.html"
    accessed: 2026-11-03
  - title: "Cartographic Boundary Files - U.S. Census Bureau"
    url: "https://www.census.gov/geographies/mapping-files/time-series/geo/cartographic-boundary.html"
    accessed: 2026-11-03
  - title: "A smaller share of older U.S. adults live alone today than in 1990 - Pew Research Center (December 4, 2025)"
    url: "https://www.pewresearch.org/short-reads/2025/12/04/a-smaller-share-of-older-us-adults-live-alone-today-than-in-1990/"
    accessed: 2026-11-03
  - title: "Health Effects of Social Isolation and Loneliness - CDC"
    url: "https://www.cdc.gov/social-connectedness/risk-factors/index.html"
    accessed: 2026-11-03
  - title: "PLACES Measure Definitions: Health-Related Social Needs - CDC"
    url: "https://www.cdc.gov/places/measure-definitions/health-related-social-needs.html"
    accessed: 2026-11-03
  - title: "PLACES: Local Data for Better Health - CDC"
    url: "https://www.cdc.gov/places/index.html"
    accessed: 2026-11-03
  - title: "PLACES Current Release Notes - CDC"
    url: "https://www.cdc.gov/places/current-release-notes/index.html"
    accessed: 2026-11-03
---

To find where older adults live alone in your county, map Census table B09021, line _023, by census tract or ZIP code. This American Community Survey (ACS) line counts people 65+ living alone. Divide it by the 65+ population for a rate, and check margins of error before ranking areas.

## Which Census table to use

All of these come from the [2024 ACS 5-year release](https://api.census.gov/data/2024/acs/acs5/groups/B09021.html). A 5-year release covers [60 months of data](https://www.census.gov/programs-surveys/acs/guidance/estimates.html), here 2020–2024. Line numbers are from the Census Data API.

| Table | What it counts | Lines to use | Universe |
|---|---|---|---|
| [B09021](https://api.census.gov/data/2024/acs/acs5/groups/B09021.html) | Living arrangements of adults by age | _023: 65 and over, lives alone; _022: all 65 and over | [Population 18+ in households](https://api.census.gov/data/2024/acs/acs5/groups/B09021.json) |
| [B09020](https://api.census.gov/data/2024/acs/acs5/groups/B09020.html) | Relationship by household type for people 65+; living alone split by sex | _015: men living alone; _018: women living alone; _021: in group quarters | [Population 65+](https://api.census.gov/data/2024/acs/acs5/groups/B09020.json) |
| [B11010](https://api.census.gov/data/2024/acs/acs5/groups/B11010.html) | Nonfamily households by sex and age of householder | _005: male householder 65+ living alone; _012: female | Nonfamily households |
| [B11007](https://api.census.gov/data/2024/acs/acs5/groups/B11007.html) | Households with people 65+ | _003: 1-person households with someone 65+ | Households |
| [B25011](https://api.census.gov/data/2024/acs/acs5/groups/B25011.html) | Tenure by household type and age of householder | _021: owner, living alone, 65+; _045: renter, living alone, 65+ | Occupied housing units |
| [S0102](https://api.census.gov/data/2024/acs/acs5/subject/groups/S0102.html) | Population 60 years and over | _C02_021: households with a householder 60+; _C02_026: "Householder living alone," a percent | [Subject table](https://api.census.gov/data/2024/acs/acs5/subject/groups/S0102.json) |

Start with B09021_023. It is one published line, so its margin of error is ready to use.

Adding the two sex lines in B09020 gives the same group, but summed margins are only approximations. The Census Bureau says published, collapsed estimates have [more accurate margins of error](https://www.census.gov/content/dam/Census/library/publications/2018/acs/acs_general_handbook_2018_ch08.pdf) than ones users derive.

None of the B tables above splits living alone at 60. Area agencies on aging that plan for 60+ can use S0102 instead. Its living-alone line is a [percent, not a count](https://api.census.gov/data/2024/acs/acs5/subject/groups/S0102.json).

To estimate a 60+ count, multiply that percent by the 60+ household count (_C02_021). The result is a derived estimate, so its margin of error is an [approximation](https://www.census.gov/content/dam/Census/library/publications/2018/acs/acs_general_handbook_2018_ch08.pdf). Label each figure with its age group, so 60+ and 65+ results are never mixed.

## Pick a geography: tract, ZIP code or county

Use 5-year estimates. One-year estimates cover only areas with [65,000 or more people](https://www.census.gov/programs-surveys/acs/guidance/estimates.html); 5-year estimates cover all areas.

| Geography | Detailed tables (B) | Subject tables (S) | Best for |
|---|---|---|---|
| County | [Yes](https://api.census.gov/data/2024/acs/acs5/geography.json) | [Yes](https://api.census.gov/data/2024/acs/acs5/subject/geography.json) | Comparing your county with others |
| Census tract | [Yes](https://api.census.gov/data/2024/acs/acs5/geography.json) | [Yes](https://api.census.gov/data/2024/acs/acs5/subject/geography.json) | Finding neighborhoods within a county |
| ZIP Code Tabulation Area | [Yes](https://api.census.gov/data/2024/acs/acs5/geography.json) | [Yes](https://api.census.gov/data/2024/acs/acs5/subject/geography.json) | Matching outreach lists kept by ZIP code |
| Block group | Lowest level for [detailed tables](https://www.census.gov/programs-surveys/acs/news/data-releases/2025/release-schedule.html) | Not published; subject tables stop at [tracts](https://www.census.gov/programs-surveys/acs/news/data-releases/2025/release-schedule.html) | Very small areas; check that your table is published there |

The geography lists cover the whole dataset, not each table, so confirm your table downloads at the level you need. Tracts are a common choice for a county map. ZIP Code Tabulation Areas are Census approximations of ZIP code areas, not mail routes; see [ZCTA vs ZIP code](/glossary/zcta-vs-zip-code).

## Steps to build the map

1. **Download the table.** Pull B09021 for every tract in your county from data.census.gov or the Census Data API. In our test on November 3, 2026, API queries without a key returned a "Missing Key" page. [Request a key](https://api.census.gov/data/key_signup.html) first.
2. **Keep the estimate and the margin of error.** Each line has an E (estimate) and M (margin of error) column, such as B09021_023E and B09021_023M.
3. **Compute a rate.** Divide B09021_023 by a 65+ total. See the next section for which one.
4. **Compute a coefficient of variation (CV) for each count.** Divide the margin of error by 1.645 to get the [standard error](https://www.census.gov/content/dam/Census/library/publications/2018/acs/acs_general_handbook_2018_ch07.pdf). Then divide the standard error by the estimate.
5. **Flag unreliable areas.** Mark tracts with high CVs on the map, for example with hatching, instead of dropping them.
6. **Join to boundaries.** Use Census [cartographic boundary files](https://www.census.gov/geographies/mapping-files/time-series/geo/cartographic-boundary.html), which are simplified boundaries designed for [small-scale thematic mapping](https://www.census.gov/geographies/mapping-files/time-series/geo/cartographic-boundary.html). They come as shapefile, geodatabase, KML and, since 2024, geopackage.
7. **Map two layers.** Show the count and the rate side by side. Counts tell outreach staff where most people are; rates show where living alone is most common.

## Count or rate: choose the denominator

A count answers "where are most older adults who live alone?" A rate answers "where is living alone most common?" Tracts with many older residents can rank high on count and low on rate.

Two denominators are defensible:

- **B09021_022, people 65+ in households.** Numerator and denominator then share one [universe](https://api.census.gov/data/2024/acs/acs5/groups/B09021.json). Use this for "share of older adults at home who live alone."
- **B09020_001, all people 65+.** This includes people in [group quarters](https://api.census.gov/data/2024/acs/acs5/groups/B09020.json), such as nursing home residents. Rates come out lower where a large facility sits in the tract.

State which one you used in the map legend. National figures give a rough benchmark. Pew Research Center found that [26% of U.S. adults 65 and older lived alone in 2023](https://www.pewresearch.org/short-reads/2025/12/04/a-smaller-share-of-older-us-adults-live-alone-today-than-in-1990/), down from 29% in 1990.

## Check margins of error before ranking areas

ACS margins of error are published at the [90 percent confidence level](https://www.census.gov/content/dam/Census/library/publications/2018/acs/acs_general_handbook_2018_ch07.pdf). A tract with 120 ± 90 people living alone may not differ from a tract with 60 ± 50.

To test whether two areas differ, use the Census Bureau's [significance test](https://www.census.gov/content/dam/Census/library/publications/2018/acs/acs_general_handbook_2018_ch07.pdf). Its worked example compares the share of householders 65 and older who live alone in two states.

The 2020–2024 estimates include data collected in 2020. That year the ACS collected [only two-thirds of the responses it usually collects](https://www.census.gov/programs-surveys/acs/technical-documentation/user-notes/2022-04.html).

The Census Bureau expected similar effects on margins of error in later 5-year products that contain 2020 data. Its tract-level quality check uses a [CV benchmark of 0.30](https://www.census.gov/programs-surveys/acs/technical-documentation/user-notes/2022-04.html).

If many tracts are unreliable, combine neighboring tracts. Compute the combined margin of error as the [square root of the sum of the squared margins of error](https://www.census.gov/content/dam/Census/library/publications/2018/acs/acs_general_handbook_2018_ch08.pdf). This approximation gets [less accurate as more estimates are summed](https://www.census.gov/content/dam/Census/library/publications/2018/acs/acs_general_handbook_2018_ch08.pdf).

## Add layers that change who needs help

Living alone, by itself, does not tell you who needs services. Overlay it with other measures.

| Layer | Source | Why it matters |
|---|---|---|
| Women vs. men living alone | [B09020](https://api.census.gov/data/2024/acs/acs5/groups/B09020.html) _015 and _018 | Nationally, [31% of women and 19% of men](https://www.pewresearch.org/short-reads/2025/12/04/a-smaller-share-of-older-us-adults-live-alone-today-than-in-1990/) 65+ lived alone in 2023 |
| Renters vs. owners living alone | [B25011](https://api.census.gov/data/2024/acs/acs5/groups/B25011.html) _021 and _045 | Housing and home-modification programs differ by tenure |
| Oldest old | Age tables such as [B01001](https://api.census.gov/data/2024/acs/acs5/groups/B01001.html) | Nationally, [38% of people 85+](https://www.pewresearch.org/short-reads/2025/12/04/a-smaller-share-of-older-us-adults-live-alone-today-than-in-1990/) lived alone vs. 24% of those 65–84 |
| Self-care and independent living difficulty | ACS [B18106](https://api.census.gov/data/2024/acs/acs5/groups/B18106.html) and [B18107](https://api.census.gov/data/2024/acs/acs5/groups/B18107.html) | See [home care shortages](/map-home-care-provider-shortages) for line numbers |
| Loneliness | [CDC PLACES](https://www.cdc.gov/places/measure-definitions/health-related-social-needs.html), "Feelings of loneliness among adults" | Modeled for all adults, not only older adults |

[B09021](https://api.census.gov/data/2024/acs/acs5/groups/B09021.html) does not cross living alone with disability or income. An overlay shows areas where both are common. It does not count people who have both.

CDC PLACES publishes data by [county, place, census tract and ZCTA](https://www.cdc.gov/places/index.html). Its loneliness measure is [available only for states that administered](https://www.cdc.gov/places/measure-definitions/health-related-social-needs.html) the BRFSS Social Determinants and Health Equity module. The current release renamed ["Feelings of social isolation" to "Feelings of loneliness"](https://www.cdc.gov/places/current-release-notes/index.html).

## What the data cannot tell you

- **Living alone is not isolation.** CDC defines social isolation as [no relationships or contact with others and little to no social support](https://www.cdc.gov/social-connectedness/risk-factors/index.html). Loneliness is feeling alone or disconnected. CDC lists adults living alone among groups [loneliness may affect more](https://www.cdc.gov/social-connectedness/risk-factors/index.html).
- **Facility residents are outside B09021.** A household is everyone in a housing unit; [people not in households live in group quarters](https://www2.census.gov/programs-surveys/acs/tech_docs/subject_definitions/2024_ACSSubjectDefinitions.pdf). Group quarters include skilled nursing facilities and group homes.
- **Group quarters estimates are shaky below the state level.** The ACS controls its group quarters sample [at the state level only](https://www2.census.gov/programs-surveys/acs/tech_docs/subject_definitions/2024_ACSSubjectDefinitions.pdf). Treat B09020_021 for one tract with care.
- **A 5-year estimate is a period average.** It describes 2020–2024, not 2024 alone. As of November 2026, the 2021–2025 5-year release date is [listed as TBD](https://www.census.gov/programs-surveys/acs/news/data-releases/2025/release-schedule.html).
- **The ACS counts where people live.** It cannot show who has a caregiver nearby, a phone tree or a meal delivery.

For how these counts fit an area plan, see [AAA area plan needs assessment data](/aaa-area-plan-needs-assessment-data). For more on estimate periods, see [ACS 5-year estimates](/glossary/acs-5-year-estimates).

## Using GeoChat AI for this map

[GeoChat Atlas](https://atlas.geochat.ai) is free, with no credit card required. It maps ACS 2020–2024 5-year estimates at county, ZIP code (ZCTA) and census tract level. Its plain-language AI chat can drill into ZIP codes and compare regions.

The platform is new, so check whether it has the living-alone layer you need. If it does not, nonprofit organizations can request a new map. See [methods](/methods) for data versions.

The chat has no web search. It is instructed to report only figures from its own queries of the platform's datasets. That is an instruction to the model, not a guarantee, so check figures against the Census table.

## Common mistakes

1. **Mixing 60+ and 65+, or percents and counts.** S0102 uses 60 and over and gives living alone as a percent. B09021, B09020 and B11010 count people or households 65 and over.
2. **Ranking tracts on estimates with huge margins of error.** Flag high-CV tracts, or combine neighbors.
3. **Mapping counts only.** Large tracts dominate a count map. Show the rate too.
4. **Using a mismatched denominator.** B09021_023 over [B01001](https://api.census.gov/data/2024/acs/acs5/groups/B01001.json)'s 65+ total mixes a household universe with the total population.
5. **Calling the map an isolation map.** Title it "older adults living alone" and say what it leaves out.
6. **Comparing tract group quarters counts across years.** The Census Bureau says sub-state GQ estimates [should not be compared with earlier years](https://www2.census.gov/programs-surveys/acs/tech_docs/subject_definitions/2024_ACSSubjectDefinitions.pdf).
