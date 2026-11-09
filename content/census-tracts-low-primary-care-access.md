---
title: "How to Find Census Tracts With Low Primary Care Access"
description: "Find low-access tracts by combining HRSA shortage areas, NPPES provider supply, ACS population and barriers, travel time and CDC PLACES checkup rates."
slug: census-tracts-low-primary-care-access
type: guide
updated: 2026-11-09
faq:
  - q: "Is there one federal score for primary care access by census tract?"
    a: "No. HRSA designates shortage areas, some built from census tracts, but there is no single tract-level access score. Analysts combine shortage designations, provider supply, travel time and need indicators."
  - q: "Can I download HPSA designations by census tract?"
    a: "Yes. HRSA's primary care HPSA file lists the components of each area designation, and census tract is one component type. Each tract component carries an 11-digit tract code you can join to Census data. Filter the HPSA Status column, because the file also lists withdrawn designations."
  - q: "Can I use CDC PLACES to rank census tracts?"
    a: "CDC says PLACES estimates are modeled, not direct, and should not be used to rank the overall health of any tract. Use measures such as routine checkups as one flag next to supply and barrier data."
  - q: "How do I count primary care providers in a census tract?"
    a: "Download the free NPPES file from CMS, keep primary care taxonomies, and geocode practice addresses with the Census Geocoder, which returns tract codes. Label the result as NPI registrations, not full-time clinicians."
  - q: "Does GeoChat Atlas show provider counts by census tract?"
    a: "No. As of November 2026, GeoChat Atlas counts NPPES providers by county and ZIP code. GeoChat Atlas maps data at county, ZIP code (ZCTA) and census tract level. Its layers include HRSA shortage areas, CDC PLACES (2025 release) and ACS 2020–2024 estimates."
sources:
  - title: "Glossary - Geography Program, U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/geography/about/glossary.html"
    accessed: 2026-11-09
  - title: "TIGER/Line Shapefiles - U.S. Census Bureau"
    url: "https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html"
    accessed: 2026-11-09
  - title: "Shortage Areas - HRSA Data Warehouse"
    url: "https://data.hrsa.gov/topics/health-workforce/shortage-areas"
    accessed: 2026-11-09
  - title: "HPSA Find - HRSA Data Warehouse"
    url: "https://data.hrsa.gov/topics/health-workforce/shortage-areas/hpsa-find"
    accessed: 2026-11-09
  - title: "Data Downloads - HRSA Data Warehouse"
    url: "https://data.hrsa.gov/data/download"
    accessed: 2026-11-09
  - title: "HRSA HPSA Primary Care detail file (CSV)"
    url: "https://data.hrsa.gov/DataDownload/DD_Files/BCD_HPSA_FCT_DET_PC.csv"
    accessed: 2026-11-09
  - title: "HRSA MUA/P detail file (CSV)"
    url: "https://data.hrsa.gov/DataDownload/DD_Files/MUA_DET.csv"
    accessed: 2026-11-09
  - title: "Unmet Need Score Map Tool - HRSA Data Warehouse"
    url: "https://data.hrsa.gov/topics/health-centers/sanam"
    accessed: 2026-11-09
  - title: "Data Dissemination (NPPES) - CMS"
    url: "https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination"
    accessed: 2026-11-09
  - title: "NPI Files - CMS NPPES"
    url: "https://download.cms.gov/nppes/NPI_Files.html"
    accessed: 2026-11-09
  - title: "Census Geocoder Documentation - U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/geography/technical-documentation/complete-technical-documentation/census-geocoder.html"
    accessed: 2026-11-09
  - title: "Census Geocoder User Guide (PDF) - U.S. Census Bureau"
    url: "https://www2.census.gov/geo/pdfs/maps-data/data/Census_Geocoder_User_Guide.pdf"
    accessed: 2026-11-09
  - title: "ACS 2024 5-year, table B01003 (Total Population) - Census Data API"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B01003.html"
    accessed: 2026-11-09
  - title: "ACS 2024 5-year, table B27010 (Types of Health Insurance Coverage by Age) - Census Data API"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B27010.html"
    accessed: 2026-11-09
  - title: "ACS 2024 5-year, subject table S2701 (Selected Characteristics of Health Insurance Coverage) - Census Data API"
    url: "https://api.census.gov/data/2024/acs/acs5/subject/groups/S2701.html"
    accessed: 2026-11-09
  - title: "ACS 2024 5-year, table B25044 (Tenure by Vehicles Available) - Census Data API"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B25044.html"
    accessed: 2026-11-09
  - title: "ACS 2024 5-year, table B17001 (Poverty Status in the Past 12 Months by Sex by Age) - Census Data API"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B17001.html"
    accessed: 2026-11-09
  - title: "Using 1-Year or 5-Year American Community Survey Data - U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/acs/guidance/estimates.html"
    accessed: 2026-11-09
  - title: "Statistical Testing Tool - American Community Survey"
    url: "https://www.census.gov/programs-surveys/acs/guidance/statistical-testing-tool.html"
    accessed: 2026-11-09
  - title: "About PLACES - CDC"
    url: "https://www.cdc.gov/places/about/index.html"
    accessed: 2026-11-09
  - title: "PLACES Current Release Notes - CDC"
    url: "https://www.cdc.gov/places/help/data-notes/"
    accessed: 2026-11-09
  - title: "PLACES Measure Definitions: Prevention - CDC"
    url: "https://www.cdc.gov/places/measure-definitions/prevention.html"
    accessed: 2026-11-09
  - title: "PLACES Frequently Asked Questions - CDC"
    url: "https://www.cdc.gov/places/faqs/index.html"
    accessed: 2026-11-09
  - title: "2020 Relationship Files - U.S. Census Bureau"
    url: "https://www.census.gov/geographies/reference-files/time-series/geo/relationship-files.2020.html"
    accessed: 2026-11-09
  - title: "Rural-Urban Commuting Area Codes - USDA ERS"
    url: "https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes"
    accessed: 2026-11-09
---

To find census tracts with low primary care access, combine four tract-level signals: shortage designations, provider supply, travel barriers and use of care. No single federal score does this for you, so the work is joining public files on one 11-digit tract code. HRSA's [Unmet Need Score tool](https://data.hrsa.gov/topics/health-centers/sanam), for example, works with ZIP codes, not tracts.

## Why census tracts

Census tracts are "small, relatively permanent statistical subdivisions of a county," with [1,200 to 8,000 people and an optimum of 4,000](https://www.census.gov/programs-surveys/geography/about/glossary.html). A tract [cannot cross a county line](https://www.census.gov/programs-surveys/geography/about/glossary.html), so tract results add up cleanly to county totals.

Tracts show pockets that county or ZIP code averages hide. They also match how HRSA builds many shortage designations, as the next section shows.

Use 2020 tract boundaries as your base, and expect some files to carry other vintages (see Common mistakes). The Census Bureau's [TIGER/Line shapefiles](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html) hold the boundaries and geographic codes but no demographic data, so you join data to them by code.

## The signals and where to get them

| Signal | Source | Geography | What it tells you |
|---|---|---|---|
| Shortage designation | [HRSA HPSA and MUA/P files](https://data.hrsa.gov/data/download) | Tract, county subdivision or county components | Whether HRSA has formally designated the area |
| Provider supply | [CMS NPPES files](https://download.cms.gov/nppes/NPI_Files.html), geocoded | Point locations you assign to tracts | Where primary care clinicians register a practice address |
| Population and barriers | [ACS 5-year tables](https://www.census.gov/programs-surveys/acs/guidance/estimates.html) | Tract | Who lives there: uninsured, in poverty, without a vehicle |
| Use of care | [CDC PLACES](https://www.cdc.gov/places/about/index.html) | Tract | Modeled share of adults with a routine checkup |
| Rural context | [USDA ERS RUCA codes](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes) | Tract | How urban or rural a tract is, from commuting ties |

Rural context is not an access signal on its own. It tells you which travel-time standard and comparison group fit each tract.

## Step-by-step

### Step 1: Pull HRSA shortage designations

HRSA's [Shortage Areas page](https://data.hrsa.gov/topics/health-workforce/shortage-areas) offers downloads in XLSX, CSV and SHP. It covers geographic HPSAs, population HPSAs and Medically Underserved Areas and Populations (MUA/P).

1. Download the primary care HPSA file from [HRSA Data Downloads](https://data.hrsa.gov/data/download). Shapefiles are offered for both "Area HPSA Component Boundaries" and "Area HPSA Designation Boundaries."
2. In the [primary care HPSA CSV](https://data.hrsa.gov/DataDownload/DD_Files/BCD_HPSA_FCT_DET_PC.csv), use the "HPSA Component Type Description" column. Its values include Census Tract, County Subdivision and Single County.
3. For tract components, the "HPSA Geography Identification Number" holds the 11-digit tract code. Join on it, then check unmatched codes: some older designations use 2010 tract codes.
4. Filter the "HPSA Status" column. The [file](https://data.hrsa.gov/DataDownload/DD_Files/BCD_HPSA_FCT_DET_PC.csv) lists Designated, Proposed For Withdrawal and Withdrawn records.
5. Keep the "HPSA Population Type" column. Tract components include geographic designations and population designations such as Low Income and Medicaid Eligible.
6. Repeat with the [MUA/P file](https://data.hrsa.gov/DataDownload/DD_Files/MUA_DET.csv). Its components are also typed as Census Tract, County Subdivision or Single County.

The MUA/P file includes the Index of Medical Underservice (IMU) score and its parts. These are [scores for providers per 1,000 population, poverty, population aged 65 and over, and infant mortality](https://data.hrsa.gov/DataDownload/DD_Files/MUA_DET.csv).

A population HPSA covers a group inside the tract, not every resident. Label it that way on your map. See [HPSA](/glossary/hpsa) and [MUA/MUP](/glossary/mua-mup).

For a quick look rather than a download, [HPSA Find](https://data.hrsa.gov/topics/health-workforce/shortage-areas/hpsa-find) searches by state and county. It filters by discipline, HPSA type, score, status and rural status. HRSA's batch tool checks [up to 100 addresses](https://data.hrsa.gov/topics/health-workforce/shortage-areas) at once.

### Step 2: Build tract-level provider supply

CMS publishes NPPES as a [free full replacement monthly NPI file, weekly incremental files and a deactivation file](https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination). The November 9, 2026 monthly file is a [1,079 MB ZIP](https://download.cms.gov/nppes/NPI_Files.html), so plan for a database or a scripting tool, not a spreadsheet.

1. Keep individual (Type 1) records whose primary taxonomy is primary care. Common choices are family medicine, internal medicine, pediatrics and general practice. Add nurse practitioners and physician assistants if they deliver primary care locally. See [NPI taxonomy codes](/glossary/npi-taxonomy-codes).
2. Drop deactivated NPIs.
3. Use the practice location address, not the mailing address. Each zipped file also includes a [Practice Location Reference File](https://download.cms.gov/nppes/NPI_Files.html) for non-primary practice locations.
4. Geocode addresses with the [Census Geocoder](https://www.census.gov/programs-surveys/geography/technical-documentation/complete-technical-documentation/census-geocoder.html), which takes batches of up to 10,000 addresses.
5. Choose the "Find Geographies" batch option. Its output adds [state, county, tract and block codes](https://www2.census.gov/geo/pdfs/maps-data/data/Census_Geocoder_User_Guide.pdf) to each match.

The Census Geocoder interpolates coordinates from [address ranges, which "include all possible structure numbers even though actual structures may not exist"](https://www.census.gov/programs-surveys/geography/technical-documentation/complete-technical-documentation/census-geocoder.html). Spot-check unmatched and suburban addresses by hand.

CMS notes that issuing an NPI [does not ensure or validate that a provider is licensed or credentialed](https://download.cms.gov/nppes/NPI_Files.html). Treat counts as registrations, not full-time clinicians.

### Step 3: Add population and barrier data

Use ACS 5-year estimates. They are the only ACS estimates published for [all areas](https://www.census.gov/programs-surveys/acs/guidance/estimates.html), while 1-year estimates cover areas of 65,000 or more. As of November 2026, the [2020–2024 5-year release](https://api.census.gov/data/2024/acs/acs5/groups/B01003.html) is the latest one to use. See [ACS 5-year estimates](/glossary/acs-5-year-estimates).

| Need | ACS table | Universe | Key fields |
|---|---|---|---|
| Denominator | [B01003](https://api.census.gov/data/2024/acs/acs5/groups/B01003.html) Total Population | Total population | B01003_001E |
| Uninsured by age | [B27010](https://api.census.gov/data/2024/acs/acs5/groups/B27010.html) Types of Health Insurance Coverage by Age | Civilian noninstitutionalized population | "No health insurance coverage" rows for each age group |
| Uninsured rate | [S2701](https://api.census.gov/data/2024/acs/acs5/subject/groups/S2701.html) Selected Characteristics of Health Insurance Coverage | Civilian noninstitutionalized population | S2701_C05_001E, Percent Uninsured |
| No vehicle | [B25044](https://api.census.gov/data/2024/acs/acs5/groups/B25044.html) Tenure by Vehicles Available | Occupied housing units | B25044_003E and B25044_010E, "No vehicle available" |
| Poverty | [B17001](https://api.census.gov/data/2024/acs/acs5/groups/B17001.html) Poverty Status by Sex by Age | Population for whom poverty status is determined | B17001_002E, below poverty level |

Note the universes. The no-vehicle count is households, not people, so divide by occupied housing units.

Every ACS estimate comes with a margin of error. Before calling one tract worse than another, test the difference. The Census Bureau's [Statistical Testing Tool](https://www.census.gov/programs-surveys/acs/guidance/statistical-testing-tool.html) does this using each estimate's margin of error.

### Step 4: Measure access

Start with a provider-to-population ratio for each tract: primary care NPIs divided by B01003 population. See [provider-to-population ratio](/glossary/provider-to-population-ratio).

Tract ratios break down fast. Many tracts have zero providers, yet residents drive a few minutes to a clinic next door. Two better options:

- **Nearest-provider travel time.** Compute road travel time from each tract's population center to the closest primary care site.
- **Two-step floating catchment area (2SFCA).** Count supply and demand within a travel-time catchment that crosses tract lines. See [drive-time access](/glossary/drive-time-access) for how it works and which thresholds policy uses.

Both need a desktop GIS such as QGIS or ArcGIS Pro, or a routing service. If you need travel-time models, a GIS is the better tool for this step than any ready-made map.

Include providers outside your county or state border. Leaving them out makes edge tracts look worse than they are.

### Step 5: Add use of care from CDC PLACES

[CDC PLACES](https://www.cdc.gov/places/about/index.html) gives model-based estimates for counties, places, census tracts and ZIP Code Tabulation Areas. It covers [83,522 of 84,112 census tracts](https://www.cdc.gov/places/about/index.html) in the 50 states and DC, those with 50 or more adult residents.

Two measures fit primary care access ([CDC measure definitions](https://www.cdc.gov/places/measure-definitions/prevention.html)):

- "Routine checkup within the past year among adults"
- "Lack of health insurance among adults aged 18–64 years"

The [December 2025 release](https://www.cdc.gov/places/help/data-notes/) bases 35 of its 40 measures on 2023 BRFSS data. Estimates from 2023 BRFSS were not available for Kentucky or Pennsylvania, so tracts there lack both measures above.

CDC says the estimates are modeled, not direct, and [should not be used for ranking the overall health](https://www.cdc.gov/places/faqs/index.html) of any tract. Use a low checkup rate as a flag that confirms other signals, not as a rank.

### Step 6: Add rural context

USDA ERS publishes [2020 Rural-Urban Commuting Area (RUCA) codes for census tracts](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes), with the tract file last updated July 31, 2025. RUCA codes were designed to address ["a major limitation associated with county-based classifications"](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes).

Compare rural tracts with rural tracts. A 25-minute drive means something different in a metro core than in a remote area.

### Step 7: Flag and review priority tracts

1. Join all layers on the 11-digit tract code.
2. Flag tracts that meet two or more of these conditions:
   - inside a designated primary care HPSA or MUA/P
   - low supply or long travel time
   - a high uninsured or no-vehicle share
   - a low checkup estimate
3. Check each flag against its margin of error or model caveat.
4. Take the shortlist to local partners. Ask about closed clinics, new sites, bus routes and where people actually go for care.
5. Write a methods note: file dates, taxonomy codes, travel mode, thresholds and tract vintage.

If you are a hospital, the same tract flags feed your [CHNA access-gap maps](/chna-access-gap-mapping-guide). Health departments can align with the [community health assessment mapping guide](/community-health-assessment-mapping-guide).

## Which tool fits which step

HRSA's own files and HPSA Find are the better choice for official designation status. More than [34 federal programs depend on HPSA/MUA/MUP designations](https://data.hrsa.gov/data/download) for eligibility or funding preference, so quote HRSA directly for anything that affects funding.

CDC's PLACES site is the better choice when you need the full set of 40 measures or the raw download. A desktop GIS is the better choice for travel time, 2SFCA and custom provider geocoding.

[GeoChat Atlas](https://atlas.geochat.ai), GeoChat AI's free mapping platform, offers interactive maps of supply-demand gaps and provider deserts, with no GIS software needed to view them. GeoChat AI is not affiliated with HRSA. GeoChat AI is not affiliated with GeoChat, the MBZUAI remote-sensing model, or GeoChat, the InSTEDD messaging tool.

As of November 2026, GeoChat Atlas maps data by census tract, ZIP code (ZCTA) and county. It covers all 50 states, DC and Puerto Rico. Its layers include HRSA HPSAs and MUAs, CDC PLACES (2025 release), CDC SVI 2022 and ACS 2020–2024 5-year estimates.

Its NPPES provider counts are by county and ZIP code, not tract, and are registrations, not full-time clinicians. For tract-level supply, run Step 2 yourself.

Its AI chat answers plain-language follow-up questions. It is instructed to report only figures from the platform's own datasets, which is an instruction to the model, not a guarantee. The platform is new; the current version is GeoChat Atlas (version 2). It has a free tier with no credit card required. See our [methods page](/methods) for data versions.

## Common mistakes

- **Mixing ZIP codes and tracts.** ZIP codes are mail routes and cross tract lines. Use a crosswalk, and see [ZCTA vs. ZIP code](/glossary/zcta-vs-zip-code).
- **Counting NPIs as full-time clinicians.** NPPES records are registrations. A part-time clinician counts the same as a full-time one.
- **Using mailing addresses.** Geocode practice locations, or your supply map shows billing offices.
- **Keeping withdrawn HPSAs.** The HRSA file includes withdrawn records. Filter the status column first.
- **Ignoring margins of error.** Small tracts swing widely. Test differences before ranking.
- **Ranking tracts on PLACES.** CDC advises against it. Use PLACES as a supporting flag.
- **Stopping at the county or state line.** Residents cross borders for care, so include nearby providers outside your area.
- **Mixing tract vintages.** HRSA files include some 2010 tract codes, and PLACES uses [Connecticut planning regions as county equivalents](https://www.cdc.gov/places/about/index.html), which changes Connecticut tract codes. Check unmatched codes after every join, using the Census [2020 relationship files](https://www.census.gov/geographies/reference-files/time-series/geo/relationship-files.2020.html) for 2010–2020 changes.

For a wider list of free options, see [free tools for healthcare access mapping](/free-tools-healthcare-access-mapping).
