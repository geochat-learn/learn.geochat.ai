---
title: "How to Map Community Health Worker (CHW) Coverage"
description: "Map where your CHWs work, score need by ZIP code or tract with ACS and CDC PLACES, overlay HRSA shortage areas, then list high-need areas no CHW covers."
slug: community-health-worker-coverage-map
type: guide
updated: 2026-11-26
faq:
  - q: "How do I map community health worker coverage?"
    a: "Start with your own program records: where each CHW works and where clients live, summed by ZIP code or census tract. Then build a need score from ACS and CDC PLACES measures for the same areas. The gaps are high-need areas with few or no clients or CHW hours."
  - q: "Is there a public dataset of where community health workers work?"
    a: "No single public file lists every CHW and where they work. NPPES has a Community Health Worker taxonomy code (172V00000X), but it only shows CHWs who registered an NPI. Medicare's 2024 claims data show community health integration billing by state, not CHW locations."
  - q: "Which census tables help find areas that need CHWs?"
    a: "Common choices come from the ACS 2020–2024 5-year estimates. They are C17002 (income to poverty ratio), B27010 (health insurance), C16002 (limited English speaking households) and B25044 (households with no vehicle). Pick the measures that match the program's goals."
  - q: "Should I map CHW coverage by ZIP code or census tract?"
    a: "Use ZIP codes (ZCTAs) if your client records and partners think in ZIP codes. Use census tracts if CHWs serve a few neighborhoods in one county, since tracts are smaller. CDC PLACES and the ACS publish both levels."
  - q: "Can GeoChat AI map need for a CHW program?"
    a: "As of November 2026, community health worker programs are one of GeoChat AI's listed use cases. It has ACS, CDC PLACES and HRSA shortage-area layers at county, ZIP code and tract level. Its layers come from public federal sources, so your CHW roster and client counts still come from your program's own records."
sources:
  - title: "Resources for Community Health Workers, CDC"
    url: "https://www.cdc.gov/chronic-disease/php/community-health-worker-resources/index.html"
    accessed: 2026-11-26
  - title: "Calendar Year (CY) 2024 Medicare Physician Fee Schedule Final Rule (fact sheet), CMS"
    url: "https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2024-medicare-physician-fee-schedule-final-rule"
    accessed: 2026-11-26
  - title: "Medicare Physician & Other Practitioners – by Geography and Service, CMS"
    url: "https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-geography-and-service"
    accessed: 2026-11-26
  - title: "Medicare Physician & Other Practitioners – by Geography and Service, 2024, HCPCS G0019 (API query), CMS"
    url: "https://data.cms.gov/data-api/v1/dataset/0c75b0b3-b40f-4007-a5ac-f9f2fed95862/data?filter%5BHCPCS_Cd%5D=G0019&size=200"
    accessed: 2026-11-26
  - title: "Medicare Physician & Other Practitioners – by Geography and Service, 2024, HCPCS G0022 (API query), CMS"
    url: "https://data.cms.gov/data-api/v1/dataset/0c75b0b3-b40f-4007-a5ac-f9f2fed95862/data?filter%5BHCPCS_Cd%5D=G0022&size=200"
    accessed: 2026-11-26
  - title: "Medicare Physician & Other Practitioners – by Geography and Service Data Dictionary (PDF), CMS"
    url: "https://data.cms.gov/sites/default/files/2021-10/7008e69d-eaec-4460-8a15-8a733dd32477/MUP_PHY_RY21_20211021_DD_Geo.pdf"
    accessed: 2026-11-26
  - title: "Medicare Physician & Other Practitioners Methodology (PDF), CMS"
    url: "https://data.cms.gov/sites/default/files/2025-04/MUP_PHY_RY25_202350312_Methodology_508.pdf"
    accessed: 2026-11-26
  - title: "NPI Files (NPPES Downloadable File), CMS"
    url: "https://download.cms.gov/nppes/NPI_Files.html"
    accessed: 2026-11-26
  - title: "NPI Registry API: Community Health Worker, Vermont"
    url: "https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Community%20Health%20Worker&state=VT&limit=200"
    accessed: 2026-11-26
  - title: "PLACES: Local Data for Better Health, CDC"
    url: "https://www.cdc.gov/places/index.html"
    accessed: 2026-11-26
  - title: "PLACES Current Release Notes, CDC"
    url: "https://www.cdc.gov/places/current-release-notes/index.html"
    accessed: 2026-11-26
  - title: "PLACES Measure Definitions: Health-Related Social Needs, CDC"
    url: "https://www.cdc.gov/places/measure-definitions/health-related-social-needs.html"
    accessed: 2026-11-26
  - title: "PLACES Frequently Asked Questions, CDC"
    url: "https://www.cdc.gov/places/faqs/index.html"
    accessed: 2026-11-26
  - title: "ACS 2024 5-year, table C17002: Ratio of Income to Poverty Level, U.S. Census Bureau"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/C17002.html"
    accessed: 2026-11-26
  - title: "ACS 2024 5-year, table B27010: Types of Health Insurance Coverage by Age, U.S. Census Bureau"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B27010.html"
    accessed: 2026-11-26
  - title: "ACS 2024 5-year, table C16002: Household Language by Household Limited English Speaking Status, U.S. Census Bureau"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/C16002.html"
    accessed: 2026-11-26
  - title: "ACS 2024 5-year, table B25044: Tenure by Vehicles Available, U.S. Census Bureau"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B25044.html"
    accessed: 2026-11-26
  - title: "Census Geocoder Documentation, U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/geography/technical-documentation/complete-technical-documentation/census-geocoder.html"
    accessed: 2026-11-26
  - title: "Health Workforce Shortage Areas, HRSA Data Warehouse"
    url: "https://data.hrsa.gov/topics/health-workforce/shortage-areas"
    accessed: 2026-11-26
  - title: "MUA Find, HRSA Data Warehouse"
    url: "https://data.hrsa.gov/tools/shortage-area/mua-find"
    accessed: 2026-11-26
---

To map community health worker (CHW) coverage, map where your CHWs work and where their clients live. Then compare that with a need score for the same ZIP codes or census tracts. The gaps are high-need areas with few clients or no assigned CHW.

No public file shows where every CHW works. Your own program records do most of the work. Public data supply the need side and a few partial checks on supply.

## What "coverage" means for a CHW program

CDC [describes a CHW](https://www.cdc.gov/chronic-disease/php/community-health-worker-resources/index.html) as "a frontline public health worker who lives in or is trusted by the community." CDC notes CHWs go by [other names](https://www.cdc.gov/chronic-disease/php/community-health-worker-resources/index.html), such as promotores de salud, lay health advisors, community health representatives and peer navigators.

That range matters for mapping. A roster pulled only by the job title "community health worker" will miss staff with other titles. Agree on who counts before you count.

Decide which of three coverage measures you need:

| Measure | What it shows | Data you need |
|---|---|---|
| Assignment | Which areas each CHW is responsible for | Roster with assigned ZIP codes or tracts |
| Reach | Where clients actually live | Client home addresses, geocoded |
| Capacity | CHW time per resident in need | CHW hours or full-time equivalents by area |

Reach is usually the most honest measure. Assigned areas can look covered on paper while few clients there are served.

## Step 1: Build the supply layer from your own records

1. **List every CHW and their service area.** Record assigned ZIP codes or tracts, hours per week and languages spoken.
2. **Geocode client addresses.** The [Census Geocoder](https://www.census.gov/programs-surveys/geography/technical-documentation/complete-technical-documentation/census-geocoder.html) accepts a single address or a batch of up to 10,000 addresses. It can return census geographies such as the tract.
3. **Sum clients by area.** Count unique clients per ZIP code or tract for one period, such as the last 12 months.
4. **Protect privacy.** Never publish client points. Publish counts by area and suppress small cells. CMS, for example, [excludes records derived from 10 or fewer beneficiaries](https://data.cms.gov/sites/default/files/2025-04/MUP_PHY_RY25_202350312_Methodology_508.pdf) from its public Medicare files.

If partners run their own CHW programs, ask for counts by ZIP code in the same format. A shared template makes the counts easier to combine.

## Step 2: Check public data on CHW supply

Public sources show only slices of the CHW workforce. Use them as checks, not as the supply layer.

### NPPES: CHWs with an NPI

NPPES has a "Community Health Worker" taxonomy, [code 172V00000X](https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Community%20Health%20Worker&state=VT&limit=200). You can search it with the [NPI Registry API](https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Community%20Health%20Worker&state=VT&limit=200) or the full [NPPES downloadable file](https://download.cms.gov/nppes/NPI_Files.html).

Two cautions apply:

- **It is a registration, not a workforce count.** CMS states that [issuing an NPI does not ensure or validate](https://download.cms.gov/nppes/NPI_Files.html) that the provider is licensed or credentialed. Only CHWs who registered an NPI appear.
- **Check every taxonomy slot.** In the [Vermont API results](https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Community%20Health%20Worker&state=VT&limit=200), some records list 172V00000X as a secondary taxonomy, not the primary one. Filtering on the primary taxonomy alone drops them.

For more on taxonomy codes, see [NPI taxonomy codes](/glossary/npi-taxonomy-codes).

### Medicare community health integration claims

From 2024, Medicare pays separately for [Community Health Integration (CHI) services](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2024-medicare-physician-fee-schedule-final-rule). The new codes cover CHI, SDOH risk assessment and principal illness navigation. CMS calls them the first "specifically designed to describe services involving community health workers, care navigators, and peer support specialists."

CMS also [clarified](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2024-medicare-physician-fee-schedule-final-rule) that these workers may be employed by community-based organizations, with the required supervision by the billing practitioner.

CMS publishes yearly use of each billing code in [Medicare Physician & Other Practitioners – by Geography and Service](https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-geography-and-service). The base CHI code is [G0019, for 60 minutes per calendar month](https://data.cms.gov/data-api/v1/dataset/0c75b0b3-b40f-4007-a5ac-f9f2fed95862/data?filter%5BHCPCS_Cd%5D=G0019&size=200). Add-on code [G0022 covers each additional 30 minutes](https://data.cms.gov/data-api/v1/dataset/0c75b0b3-b40f-4007-a5ac-f9f2fed95862/data?filter%5BHCPCS_Cd%5D=G0022&size=200).

CMS labels each row by place of service. [Non-facility is generally an office setting](https://data.cms.gov/sites/default/files/2021-10/7008e69d-eaec-4460-8a15-8a733dd32477/MUP_PHY_RY21_20211021_DD_Geo.pdf), but other entities are included. By our count from the [2024 file](https://data.cms.gov/data-api/v1/dataset/0c75b0b3-b40f-4007-a5ac-f9f2fed95862/data?filter%5BHCPCS_Cd%5D=G0019&size=200):

- In the non-facility (mostly office) setting, 179 rendering providers billed G0019 for 2,517 beneficiaries and 5,365 services nationally.
- Only 15 states had a non-facility row for G0019. Other states had too few beneficiaries to publish, or none.

Read these numbers with the file's limits in mind. The data cover only [Medicare Part B fee-for-service](https://data.cms.gov/sites/default/files/2025-04/MUP_PHY_RY25_202350312_Methodology_508.pdf) patients, not Medicare Advantage enrollees. The state table is [organized by provider state](https://data.cms.gov/sites/default/files/2025-04/MUP_PHY_RY25_202350312_Methodology_508.pdf), not where patients live. CHW work paid for by Medicaid, grants or other payers does not appear in this file. Rural health clinics and FQHCs [bill CHI under G0511](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2024-medicare-physician-fee-schedule-final-rule), so their CHI work is not in the G0019 counts.

## Step 3: Build a need score for the same areas

Pick measures that match what your CHWs do. Use the same geography as the supply layer.

### ACS measures

These tables come from the ACS 2020–2024 5-year estimates. Each is published for ZCTAs and census tracts.

| Need | Table | Lines to use |
|---|---|---|
| Low income | [C17002](https://api.census.gov/data/2024/acs/acs5/groups/C17002.html) | Ratio of income to poverty level; for example, under 2.00 (lines 002–007) |
| No health insurance | [B27010](https://api.census.gov/data/2024/acs/acs5/groups/B27010.html) | "No health insurance coverage" lines 017, 033, 050 and 066 |
| Language barriers | [C16002](https://api.census.gov/data/2024/acs/acs5/groups/C16002.html) | "Limited English speaking household" lines 004, 007, 010 and 013 |
| No car | [B25044](https://api.census.gov/data/2024/acs/acs5/groups/B25044.html) | "No vehicle available" lines 003 and 010 |

Watch the universes. C17002 counts the [population for whom poverty status is determined](https://api.census.gov/data/2024/acs/acs5/groups/C17002.html). C16002 and B25044 count [households](https://api.census.gov/data/2024/acs/acs5/groups/C16002.html) and [occupied housing units](https://api.census.gov/data/2024/acs/acs5/groups/B25044.html), not people. For uninsured counts by ZIP code, see [How to estimate the uninsured population by ZIP code](/uninsured-population-by-zip-code).

Small ZCTAs and tracts can have large margins of error. See [ACS 5-year estimates](/glossary/acs-5-year-estimates) before you rank small areas.

### CDC PLACES measures

[CDC PLACES](https://www.cdc.gov/places/index.html) publishes model-based estimates by county, place, census tract and ZCTA. The [December 2025 release](https://www.cdc.gov/places/current-release-notes/index.html) has 40 measures, mostly from 2023 BRFSS data.

Chronic disease measures, such as diabetes or high blood pressure, fit CHW programs that support chronic care. PLACES also has [seven health-related social needs measures](https://www.cdc.gov/places/measure-definitions/health-related-social-needs.html). They include food insecurity, housing insecurity, lack of reliable transportation and loneliness.

Three limits matter here:

- The social needs measures use an optional BRFSS module. CDC says each is [only available for states that chose to administer the module](https://www.cdc.gov/places/measure-definitions/health-related-social-needs.html).
- The December 2025 release has [no Kentucky or Pennsylvania estimates](https://www.cdc.gov/places/current-release-notes/index.html) for measures based on 2023 BRFSS data.
- PLACES gives [one estimate per measure](https://www.cdc.gov/places/faqs/index.html) for each area. It has no splits by age, sex, race or ethnicity.

To join PLACES and ACS on one map, see [How to combine CDC PLACES and Census data on one map](/combine-cdc-places-census-data-map).

### Combine the measures

1. Convert each measure to a percentile across the areas in your region.
2. Average the percentiles, with weights if program leaders agree on them.
3. Keep the parts visible. A single score hides why an area ranks high.

Keep the score simple enough to explain to a funder in two sentences.

## Step 4: Overlay shortage areas

HRSA's [shortage area tools](https://data.hrsa.gov/topics/health-workforce/shortage-areas) show primary care, dental and mental health HPSAs. [MUA Find](https://data.hrsa.gov/tools/shortage-area/mua-find) lets you search Medically Underserved Areas and Populations (MUAs and MUPs) by location or MUA ID.

These layers help CHW programs that link people to clinical care. A high-need area inside a primary care HPSA may need both a CHW and a clinic. See [HPSA](/glossary/hpsa) and [MUA/MUP](/glossary/mua-mup) for what each designation means.

## Step 5: Find the gaps

Put the supply and need layers side by side for each area:

| | Low CHW reach | High CHW reach |
|---|---|---|
| **High need** | Priority gap | Covered; check capacity |
| **Low need** | Lower priority | Check whether effort could move |

Then compute capacity. Divide CHW hours, or clients served, by the number of residents in need. For example, use clients per 1,000 people below twice the poverty level. See [provider-to-population ratio](/glossary/provider-to-population-ratio) for how to build and read a ratio.

Check travel too. CHWs who visit homes cover distance, not just area. See [drive-time access](/glossary/drive-time-access) for travel-time methods.

## Using GeoChat AI for the need side

[GeoChat AI](https://app.geochat.ai) is an AI-powered mapping platform for community health assessments, community needs assessments and healthcare supply-demand studies. Community health worker programs are one of its listed use cases, as of November 2026.

As of November 2026, it has layers from the ACS 2020–2024 5-year estimates, CDC PLACES (2025 release) and HRSA HPSAs and MUAs. They cover county, ZIP code (ZCTA) and census tract level. Its NPPES provider counts are registrations, not full-time clinicians. Check the [methods page](/methods) for data versions.

Its AI chat can drill into ZIP codes and compare regions in plain language. The chat has no web search. It is instructed to report only figures from its own queries of the platform's datasets. That is an instruction to the model, not a guarantee.

GeoChat AI's layers come from public federal sources. The supply layer, your CHW roster and client counts, still comes from your program's own records. The platform is new. It has a free plan, and no credit card is required. GeoChat AI is not affiliated with GeoChat, the MBZUAI remote-sensing model, or GeoChat, the InSTEDD messaging tool.

## Common mistakes

- **Counting only one job title.** CHWs work under [many names](https://www.cdc.gov/chronic-disease/php/community-health-worker-resources/index.html). Use roles, not titles.
- **Treating NPI counts as the CHW workforce.** An NPI is a registration. Only CHWs who registered one appear.
- **Reading Medicare CHI claims as CHW locations.** The state table follows the [provider's state](https://data.cms.gov/sites/default/files/2025-04/MUP_PHY_RY25_202350312_Methodology_508.pdf) and covers only fee-for-service patients.
- **Mixing people and households.** Language and vehicle tables count households. Keep units straight before you combine them.
- **Assuming PLACES social needs data exist everywhere.** They depend on whether the [state ran the BRFSS module](https://www.cdc.gov/places/measure-definitions/health-related-social-needs.html).
- **Publishing client points.** Share counts by area and suppress small numbers.
- **Mapping assignment and calling it reach.** An assigned ZIP code with few clients is a gap, not coverage.
