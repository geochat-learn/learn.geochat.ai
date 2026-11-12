---
title: "How to Combine CDC PLACES and Census Data on One Map"
description: "Join CDC PLACES health estimates and ACS 5-year Census tables on one tract or ZCTA map: matching GEOIDs, boundary files, bivariate maps and pitfalls."
slug: combine-cdc-places-census-data-map
type: guide
updated: 2026-11-12
faq:
  - q: "What field do I use to join CDC PLACES to Census ACS data?"
    a: "Use the geographic identifier. In the PLACES GIS-friendly tract file it is the 11-digit tractfips column; in the ZCTA file it is zcta5. Census downloads from data.census.gov add nine characters in front of the GEOID. Strip them, or join on the GEOIDFQ field in 2023 or newer Census boundary files."
  - q: "Which PLACES release and ACS release should I use together in late 2026?"
    a: "As of November 2026, the current PLACES release is the 2025 release, published in December 2025. Most of its 40 measures use 2023 BRFSS data. The latest ACS 5-year estimates are 2020–2024, released January 29, 2026."
  - q: "Does CDC PLACES already include Census data?"
    a: "PLACES added 9 non-medical factor measures from ACS 5-year estimates in December 2023, but CDC says they are not updated in recent releases. For current social and economic measures, download the ACS tables yourself."
  - q: "Can I compare PLACES estimates for census tracts with different age profiles?"
    a: "Use care. Tract and ZCTA estimates are crude prevalence only; CDC provides age-adjusted estimates only for counties and places. A tract with more older adults can show higher prevalence for that reason alone."
  - q: "Can I map PLACES and Census data together without GIS software?"
    a: "Yes. As of November 2026, GeoChat Atlas, from GeoChat AI, has CDC PLACES (2025 release) and ACS 2020–2024 layers. Its free tier needs no credit card."
sources:
  - title: "CDC PLACES: Frequently Asked Questions"
    url: "https://www.cdc.gov/places/faqs/index.html"
    accessed: 2026-11-12
  - title: "CDC PLACES: Current Release Notes"
    url: "https://www.cdc.gov/places/current-release-notes/index.html"
    accessed: 2026-11-12
  - title: "CDC PLACES: Methodology"
    url: "https://www.cdc.gov/places/methodology/index.html"
    accessed: 2026-11-12
  - title: "CDC PLACES Data Portal"
    url: "https://www.cdc.gov/places/tools/data-portal.html"
    accessed: 2026-11-12
  - title: "PLACES: Census Tract Data (GIS Friendly Format), 2025 release (data.cdc.gov)"
    url: "https://data.cdc.gov/d/yjkw-uj5s"
    accessed: 2026-11-12
  - title: "PLACES: ZCTA Data (GIS Friendly Format), 2025 release (data.cdc.gov)"
    url: "https://data.cdc.gov/d/kee5-23sr"
    accessed: 2026-11-12
  - title: "PLACES: Local Data for Better Health, Census Tract Data, 2025 release (data.cdc.gov)"
    url: "https://data.cdc.gov/d/cwsq-ngmh"
    accessed: 2026-11-12
  - title: "ACS 2024 Data Release Schedule, U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release-schedule.html"
    accessed: 2026-11-12
  - title: "Census Data API: B08201 Household Size by Vehicles Available (2024 ACS 5-year)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B08201.html"
    accessed: 2026-11-12
  - title: "Census Data API: S1701 Poverty Status in the Past 12 Months (2024 ACS 5-year)"
    url: "https://api.census.gov/data/2024/acs/acs5/subject/groups/S1701.html"
    accessed: 2026-11-12
  - title: "American Community Survey 5-Year Data (Census Data API)"
    url: "https://www.census.gov/data/developers/data-sets/acs-5year.html"
    accessed: 2026-11-12
  - title: "Understanding Geographic Identifiers (GEOIDs), U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/geography/guidance/geo-identifiers.html"
    accessed: 2026-11-12
  - title: "How Can I Match the GEOID from data.census.gov with the GEOID from the TIGER/Line Shapefiles?"
    url: "https://www.census.gov/help/topics/faq.how-can-i-match-the-geoid-from-data-census-gov-with-tigerline-shapefiles.html"
    accessed: 2026-11-12
  - title: "Cartographic Boundary Files, U.S. Census Bureau"
    url: "https://www.census.gov/geographies/mapping-files/time-series/geo/cartographic-boundary.html"
    accessed: 2026-11-12
  - title: "ZIP Code Tabulation Areas (ZCTAs), U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html"
    accessed: 2026-11-12
  - title: "Change to County-Equivalents in the State of Connecticut for 2022 ACS"
    url: "https://www.census.gov/programs-surveys/acs/technical-documentation/user-notes/2023-01.html"
    accessed: 2026-11-12
  - title: "ACS Statistical Testing Tool, U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/acs/guidance/statistical-testing-tool.html"
    accessed: 2026-11-12
  - title: "When to Use 1-year or 5-year Estimates - American Community Survey"
    url: "https://www.census.gov/programs-surveys/acs/guidance/estimates.html"
    accessed: 2026-11-12
---

To combine CDC PLACES and Census data on one map, download both for the same geography and join them on the shared Census code. Use the 11-digit census tract GEOID or the 5-digit ZCTA. Then join both tables to a Census boundary file. Map one measure as color and the other as a second color scale or symbol.

The steps below use the [PLACES 2025 release](https://www.cdc.gov/places/current-release-notes/index.html) and the [ACS 2020–2024 5-year estimates](https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release-schedule.html). Both were current as of November 2026.

## What each source gives you

PLACES and the ACS answer different questions. PLACES estimates health conditions and behaviors among adults. The ACS measures who lives in an area and how they live.

| | CDC PLACES (2025 release) | ACS 5-year (2020–2024) |
|---|---|---|
| What it measures | [40 measures](https://www.cdc.gov/places/methodology/index.html): health outcomes, prevention, risk behaviors, disabilities, health status and health-related social needs | Population and household traits, such as [poverty](https://api.census.gov/data/2024/acs/acs5/subject/groups/S1701.html) and [vehicles available](https://api.census.gov/data/2024/acs/acs5/groups/B08201.html) |
| How it is made | [Model-based estimates](https://www.cdc.gov/places/methodology/index.html) from BRFSS survey data, Census population counts and ACS data | Survey estimates with [margins of error](https://www.census.gov/programs-surveys/acs/guidance/statistical-testing-tool.html) |
| Who it covers | [Adults 18 and over only](https://www.cdc.gov/places/faqs/index.html) | The universe set by each table, such as [households](https://api.census.gov/data/2024/acs/acs5/groups/B08201.html) |
| Smallest areas | [County, place, census tract and ZCTA](https://www.cdc.gov/places/faqs/index.html) | [Block groups](https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release-schedule.html) for detailed tables; census tracts for subject tables |
| Uncertainty | [95% confidence intervals](https://www.cdc.gov/places/faqs/index.html) | Margins of error for each estimate |
| Data years | [35 measures from 2023 BRFSS, 5 from 2022](https://www.cdc.gov/places/current-release-notes/index.html) | Survey responses collected 2020–2024 |

PLACES gives [one estimate per measure](https://www.cdc.gov/places/faqs/index.html) for each area. It has no breakdowns by age, sex, race, ethnicity or poverty. The ACS is where you get those population details.

## Step 1: Pick one geography

Choose census tracts or ZCTAs for local detail, or counties for a regional view. Both sources must use the same level.

- **Census tracts** give the most detail PLACES offers. They nest inside counties, so the [tract GEOID](https://www.census.gov/programs-surveys/geography/guidance/geo-identifiers.html) is state (2 digits) plus county (3) plus tract (6).
- **ZCTAs** approximate postal ZIP Code areas. CDC notes that [postal ZIP Codes change over time, while ZCTAs stay the same for 10 years](https://www.cdc.gov/places/faqs/index.html). See [ZCTA vs. ZIP code](/glossary/zcta-vs-zip-code).
- **Counties** are the only level besides places where PLACES offers [age-adjusted estimates](https://www.cdc.gov/places/faqs/index.html).

Age adjustment matters when you compare areas. Tract and ZCTA files give crude prevalence only, so an older tract can show more arthritis simply because its residents are older.

## Step 2: Download PLACES in GIS-friendly format

Each PLACES release has [8 datasets](https://www.cdc.gov/places/tools/data-portal.html): 4 geographic levels in 2 formats, "opendata" and "GIS friendly." Use the GIS-friendly file for mapping. It has one row per area and one column per measure.

- Tract file: [PLACES: Census Tract Data (GIS Friendly Format), 2025 release](https://data.cdc.gov/d/yjkw-uj5s). The join field is `tractfips`.
- ZCTA file: [PLACES: ZCTA Data (GIS Friendly Format), 2025 release](https://data.cdc.gov/d/kee5-23sr). The join field is `zcta5`.

Each measure has two columns: a crude prevalence, such as `diabetes_crudeprev`, and its confidence interval, such as `diabetes_crude95ci`. The files also carry [TotalPopulation and TotalPop18plus](https://www.cdc.gov/places/faqs/index.html), the total and adult population of each area.

CDC does not report an estimate for an area with an [adult population under 50](https://www.cdc.gov/places/faqs/index.html). Expect some blank tracts. The 2025 release also has gaps by state:

- Kentucky and Pennsylvania have no estimates for the [35 measures based on 2023 BRFSS](https://www.cdc.gov/places/current-release-notes/index.html).
- The 7 health-related social needs measures cover only [39 states and the District of Columbia](https://www.cdc.gov/places/methodology/index.html).
- Cervical cancer screening is [not in this release](https://www.cdc.gov/places/current-release-notes/index.html).

## Step 3: Download the ACS tables

Pick ACS tables that answer your question. Two common pairings for access-gap maps:

| ACS table | Lines | Pairs with PLACES measure |
|---|---|---|
| [B08201](https://api.census.gov/data/2024/acs/acs5/groups/B08201.html) Household Size by Vehicles Available | _002E (no vehicle available) ÷ _001E (total households) | Routine checkup (`checkup`), lack of reliable transportation (`lacktrpt`) |
| [S1701](https://api.census.gov/data/2024/acs/acs5/subject/groups/S1701.html) Poverty Status in the Past 12 Months | _C03_001E (percent below poverty level) | Diagnosed diabetes (`diabetes`), lack of health insurance (`access2`) |

The PLACES lack-of-insurance measure covers [adults aged 18 to 64](https://data.cdc.gov/d/cwsq-ngmh). The lack-of-transportation measure is one of the health-related social needs measures, so it is missing in some states.

Use 5-year estimates for tracts and ZCTAs. Standard 1-year estimates exist only for areas of [65,000 or more people](https://www.census.gov/programs-surveys/acs/guidance/estimates.html). See [ACS 5-year estimates](/glossary/acs-5-year-estimates).

You can download tables from data.census.gov or pull them from the Census Data API. The API now [requires a key for all data queries](https://www.census.gov/data/developers/data-sets/acs-5year.html).

### Fix the GEOID before joining

A data.census.gov download has a GEO_ID with [nine extra characters at the start](https://www.census.gov/help/topics/faq.how-can-i-match-the-geoid-from-data-census-gov-with-tigerline-shapefiles.html). They encode the summary level, geographic variant and component, and "US." For example, Harris County, Texas, is [0500000US48201](https://www.census.gov/programs-surveys/geography/guidance/geo-identifiers.html), while its plain GEOID is 48201.

Remove the first nine characters to get the plain GEOID that PLACES uses. Store the result as text, not a number. Codes for some states start with a zero, such as tract [01001020100](https://data.cdc.gov/d/yjkw-uj5s) in Alabama, and a number column drops it.

## Step 4: Get a boundary file

Download tract or ZCTA polygons from the Census Bureau's [cartographic boundary files](https://www.census.gov/geographies/mapping-files/time-series/geo/cartographic-boundary.html). They are simplified for thematic mapping and come as shapefile, geodatabase, KML and, since 2024, geopackage.

Match the boundary vintage to your data:

- CDC says the PLACES tract file joins with the [Census tract 2023 boundary file](https://data.cdc.gov/d/yjkw-uj5s).
- The PLACES ZCTA file joins with the [Census 2020 ZCTA boundary file](https://data.cdc.gov/d/kee5-23sr). ZCTAs are [built from 2020 Census tabulation blocks](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html).

Boundary files from 2023 onward include a [GEOIDFQ field](https://www.census.gov/geographies/mapping-files/time-series/geo/cartographic-boundary.html) built for joining to data.census.gov downloads. In TIGER/Line files, GEOIDFQ is an [exact match](https://www.census.gov/help/topics/faq.how-can-i-match-the-geoid-from-data-census-gov-with-tigerline-shapefiles.html) for the data.census.gov GEO_ID. You can join ACS on GEOIDFQ and PLACES on the plain GEOID in the same file.

### Watch Connecticut

Starting with 2022 ACS data, Connecticut's [nine planning regions replaced its eight counties](https://www.census.gov/programs-surveys/acs/technical-documentation/user-notes/2023-01.html) as county-equivalents. PLACES switched in its [2024 release](https://www.cdc.gov/places/current-release-notes/index.html). Connecticut county-level files from before each switch will not line up with current ones.

## Step 5: Join and check the match

In QGIS, ArcGIS Pro or another GIS, join the PLACES table and the ACS table to the boundary layer on the GEOID. Then check the result before you map anything.

1. Count the boundary features with no PLACES match. Some will be blank because of the 50-adult rule or the state gaps above.
2. Count the features with no ACS match. A large number usually means a GEOID formatting problem, such as a dropped leading zero.
3. Spot-check three areas against the source tables by hand.
4. Note any area where an ACS margin of error is large next to its estimate.

## Step 6: Design the two-variable map

Keep both measures as rates or percentages. Never map a raw ACS count next to a PLACES percentage: large tracts will look worse only because more people live there.

Three designs work well:

- **Bivariate choropleth:** split each measure into three classes and cross them into a 3 × 3 color grid. The top corner shows areas high on both, such as high diabetes and high poverty.
- **Color plus symbols:** shade the PLACES measure and place graduated dots for the ACS measure.
- **Side-by-side maps:** two maps with the same extent are often easier for a board or community audience.

To estimate how many adults a percentage represents, CDC's formula is [population × prevalence ÷ 100](https://www.cdc.gov/places/faqs/index.html). Use the population the measure covers: TotalPop18plus for most measures, but ages 18–64 for lack of insurance. Treat the result as approximate. PLACES tract estimates use [2020 Census block-level population counts](https://www.cdc.gov/places/methodology/index.html), not ACS 2020–2024 figures.

## Common mistakes

- **Reading a PLACES-poverty overlap as proof.** The PLACES model already uses [county-level poverty from the 5-year ACS](https://www.cdc.gov/places/methodology/index.html). Its prediction step also uses [tract-level poverty](https://www.cdc.gov/places/faqs/index.html). The county measure is the [share of adults below 150% of the federal poverty level](https://www.cdc.gov/places/methodology/index.html). Some overlap between a PLACES measure and ACS poverty comes from the model itself.
- **Using PLACES to evaluate a program.** CDC cautions that the small-area model [cannot detect effects due to local interventions](https://data.cdc.gov/d/cwsq-ngmh). Do not use it to show a local program worked.
- **Relying on PLACES' own ACS measures.** PLACES added [9 non-medical factor measures from the ACS](https://www.cdc.gov/places/faqs/index.html) in December 2023. CDC says they are not updated in recent releases. Pull current ACS tables instead.
- **Ignoring uncertainty.** Check PLACES confidence intervals and ACS margins of error before calling two areas different. The Census Bureau's [Statistical Testing Tool](https://www.census.gov/programs-surveys/acs/guidance/statistical-testing-tool.html) tests ACS differences in a spreadsheet.
- **Averaging percentages across tracts.** To get a service-area rate, add up the counts and divide by the summed population. A plain average gives small tracts as much weight as large ones.
- **Mixing years without saying so.** Most PLACES 2025 measures use 2023 survey data; the ACS pools 2020–2024. State both in the map's source note.

## Doing it without GIS software

[GeoChat AI](https://atlas.geochat.ai) is a free, AI-powered mapping platform for community health assessments, community needs assessments and healthcare supply-demand studies. As of November 2026, GeoChat Atlas has [CDC PLACES (2025 release) and ACS 2020–2024 layers](/methods). The platform covers all 50 states, DC and Puerto Rico at county, ZIP code (ZCTA) and census tract level. CDC PLACES itself covers only the [50 states and the District of Columbia](https://data.cdc.gov/d/yjkw-uj5s). Its free tier needs no credit card.

As of November 2026, its AI chat answers follow-up questions in plain language, such as drilling into ZIP codes or comparing regions. The chat has no web search. It is instructed to report only figures from its own queries of the platform's datasets. That is an instruction to the model, not a guarantee. The platform is new; the current version is GeoChat Atlas (version 2). There is no automatic refresh; sources are rebuilt by hand after each new release. GeoChat AI is not affiliated with GeoChat, the MBZUAI remote-sensing model, or GeoChat, the InSTEDD messaging tool.

## Next steps

1. Write down the question the map must answer, such as "Where do high diabetes and no-vehicle households overlap?"
2. Pick the geography and download the PLACES GIS-friendly file and one or two ACS tables.
3. Join, check unmatched areas, and record the release and years of each source.
4. Add supply layers, such as providers or shortage areas, to turn the need map into an access-gap map. See [How to map healthcare access gaps for a CHNA](/chna-access-gap-mapping-guide) and [HPSA](/glossary/hpsa).
