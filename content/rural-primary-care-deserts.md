---
title: "How to Find Primary Care Deserts in Rural Counties"
description: "Flag rural tracts with USDA RUCA codes, count primary care NPIs and health center sites, divide by ACS population, then overlay HRSA primary care HPSAs."
slug: rural-primary-care-deserts
type: guide
updated: 2026-11-20
faq:
  - q: "How do I find primary care deserts in rural areas?"
    a: "Mark rural census tracts with USDA ERS RUCA codes, then count primary care providers and health center sites near each tract. Divide by ACS 2020–2024 population to get a provider-to-population ratio, and overlay HRSA's primary care HPSA file to see which gaps are already designated."
  - q: "Which rural definition should I use for a primary care access study?"
    a: "Use 2020 RUCA codes for census tracts when you want to find rural pockets inside metro counties. Use the 2023 Rural-Urban Continuum Codes when your report is organized by county. If you need grant eligibility, check HRSA's Rural Health Grants Eligibility Analyzer instead of your own rule."
  - q: "Is a primary care HPSA the same as a primary care desert?"
    a: "Not exactly. A HPSA is a formal HRSA designation with its own criteria and review. A desert analysis is your own measure of supply, population and distance, and it can find gaps that have no designation yet."
  - q: "Can I count primary care doctors with the NPPES file?"
    a: "Yes, but the result is a count of NPI registrations, not full-time clinicians. CMS says an NPI does not validate that a provider is licensed or credentialed, so label the result 'NPI-registered providers'."
  - q: "Does GeoChat Atlas map HPSAs and provider counts for rural counties?"
    a: "As of November 2026, GeoChat Atlas, from GeoChat AI, has HRSA layers for HPSAs, MUAs and health center sites. It also has NPPES provider counts by county and ZIP code. The counts are registrations, not full-time clinicians. It has a free plan, and no credit card is required."
sources:
  - title: "Rural-Urban Commuting Area Codes, USDA Economic Research Service"
    url: "https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes"
    accessed: 2026-11-20
  - title: "Rural-Urban Commuting Area Codes: Documentation, USDA Economic Research Service"
    url: "https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/documentation"
    accessed: 2026-11-20
  - title: "Rural-Urban Commuting Area Codes: Users' Guide, USDA Economic Research Service"
    url: "https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/users-guide"
    accessed: 2026-11-20
  - title: "Rural-Urban Continuum Codes, USDA Economic Research Service"
    url: "https://www.ers.usda.gov/data-products/rural-urban-continuum-codes"
    accessed: 2026-11-20
  - title: "Rural-Urban Continuum Codes: Documentation, USDA Economic Research Service"
    url: "https://www.ers.usda.gov/data-products/rural-urban-continuum-codes/documentation"
    accessed: 2026-11-20
  - title: "Urban and Rural, U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/geography/guidance/geo-areas/urban-rural.html"
    accessed: 2026-11-20
  - title: "Rural Health Grants Eligibility Analyzer, HRSA Data Warehouse"
    url: "https://data.hrsa.gov/tools/rural-health"
    accessed: 2026-11-20
  - title: "Health Workforce Shortage Areas, HRSA Data Warehouse"
    url: "https://data.hrsa.gov/topics/health-workforce/shortage-areas"
    accessed: 2026-11-20
  - title: "Data Downloads: Shortage Areas, HRSA Data Warehouse"
    url: "https://data.hrsa.gov/data/download?titleFilter=Shortage+Areas"
    accessed: 2026-11-20
  - title: "HPSA – Primary Care, all HPSAs (CSV), HRSA Data Warehouse"
    url: "https://data.hrsa.gov/DataDownload/DD_Files/BCD_HPSA_FCT_DET_PC.csv"
    accessed: 2026-11-20
  - title: "HPSA data download metadata (XLSX), HRSA Data Warehouse"
    url: "https://data.hrsa.gov/DataDownload/DD_Files/HPSA_DATAMART_METADATA.XLSX"
    accessed: 2026-11-20
  - title: "Data Downloads (Health Center Program Service Delivery and Look-Alike Sites), HRSA Data Warehouse"
    url: "https://data.hrsa.gov/data/download"
    accessed: 2026-11-20
  - title: "Health Center Service Delivery and Look-Alike Sites (CSV), HRSA Data Warehouse"
    url: "https://data.hrsa.gov/DataDownload/DD_Files/Health_Center_Service_Delivery_and_LookAlike_Sites.csv"
    accessed: 2026-11-20
  - title: "Rural Health Clinics, Centers for Medicare & Medicaid Services"
    url: "https://www.cms.gov/medicare/health-safety-standards/certification-compliance/rural-health-clinics"
    accessed: 2026-11-20
  - title: "NPI Files (NPPES Downloadable File), CMS"
    url: "https://download.cms.gov/nppes/NPI_Files.html"
    accessed: 2026-11-20
  - title: "Data Dissemination (NPPES), CMS"
    url: "https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination"
    accessed: 2026-11-20
  - title: "NPPES Data Dissemination – Readme, CMS"
    url: "https://www.cms.gov/regulations-and-guidance/administrative-simplification/nationalprovidentstand/downloads/data_dissemination_file-readme.pdf"
    accessed: 2026-11-20
  - title: "NPI Registry API: Family Medicine, Montana, individual NPIs"
    url: "https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Family%20Medicine&state=MT&enumeration_type=NPI-1&limit=5"
    accessed: 2026-11-20
  - title: "NPI Registry API: Internal Medicine, Montana, individual NPIs"
    url: "https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Internal%20Medicine&state=MT&enumeration_type=NPI-1&limit=5"
    accessed: 2026-11-20
  - title: "NPI Registry API: General Practice, Montana, individual NPIs"
    url: "https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=General%20Practice&state=MT&enumeration_type=NPI-1&limit=5"
    accessed: 2026-11-20
  - title: "NPI Registry API: Pediatrics, Vermont, individual NPIs"
    url: "https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Pediatrics&state=VT&enumeration_type=NPI-1&limit=20"
    accessed: 2026-11-20
  - title: "NPI Registry API: Nurse Practitioner, Wyoming, individual NPIs"
    url: "https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Nurse%20Practitioner&state=WY&enumeration_type=NPI-1&limit=20"
    accessed: 2026-11-20
  - title: "NPI Registry API: Physician Assistant, Montana, individual NPIs"
    url: "https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Physician%20Assistant&state=MT&enumeration_type=NPI-1&limit=5"
    accessed: 2026-11-20
  - title: "Census Data API: B01001 Sex by Age (2024 ACS 5-year)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B01001.html"
    accessed: 2026-11-20
  - title: "Census Data API: S0101 Age and Sex (2024 ACS 5-year)"
    url: "https://api.census.gov/data/2024/acs/acs5/subject/groups/S0101.html"
    accessed: 2026-11-20
  - title: "Census Data API: S1701 Poverty Status in the Past 12 Months (2024 ACS 5-year)"
    url: "https://api.census.gov/data/2024/acs/acs5/subject/groups/S1701.html"
    accessed: 2026-11-20
  - title: "Census Data API: S2701 Selected Characteristics of Health Insurance Coverage (2024 ACS 5-year)"
    url: "https://api.census.gov/data/2024/acs/acs5/subject/groups/S2701.html"
    accessed: 2026-11-20
  - title: "Census Data API: B25044 Tenure by Vehicles Available (2024 ACS 5-year)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B25044.html"
    accessed: 2026-11-20
  - title: "ACS 2024 Data Release Schedule, U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release-schedule.html"
    accessed: 2026-11-20
  - title: "When to Use 1-year or 5-year Estimates, American Community Survey"
    url: "https://www.census.gov/programs-surveys/acs/guidance/estimates.html"
    accessed: 2026-11-20
---

To find primary care deserts in rural counties, mark rural census tracts with USDA RUCA codes and count primary care supply near each one. Divide by ACS population, add distance to the nearest site, then overlay HRSA's primary care HPSAs.

"Primary care desert" is a working term in this guide, not a federal designation. It means a rural area with few or no primary care providers for its population, or a long trip to reach one. HRSA's formal shortage designation is the [Health Professional Shortage Area (HPSA)](/glossary/hpsa).

## Step 1: Choose a rural definition

Your rural definition decides which places you study. Pick one, write it down, and use it for every map in the report.

| Definition | Unit | Latest version | Best for |
|---|---|---|---|
| [Rural-Urban Commuting Area (RUCA) codes](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes) | Census tract and ZIP code | 2020 tract codes; ZIP codes built from [June 2024 data](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/documentation) | Finding rural pockets inside metro counties |
| [Rural-Urban Continuum Codes (RUCC)](https://www.ers.usda.gov/data-products/rural-urban-continuum-codes) | County | 2023 | County-level reports |
| [Census urban and rural](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/urban-rural.html) | Census blocks | 2020 Census | Land-use view of settlement |

### RUCA codes for tracts

USDA's Economic Research Service (ERS) built RUCA codes because counties are ["often too large to accurately delineate boundaries between rural and urban areas"](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes). Its documentation adds that ["most counties include people living in both rural and urban territory."](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/documentation)

There are [10 primary codes](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/documentation). Code 1 is a metropolitan core, an urban area of 50,000 or more people. Codes 4 and 7 are micropolitan and small town cores. Code 10 is a rural area whose "primary flow is to a tract outside an UA."

ERS gives example groupings in its [Users' Guide](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/users-guide). It describes the HHS Federal Office of Rural Health Policy scheme as "Urban/Metropolitan: RUCA 1–3" and "Rural/Nonmetropolitan: RUCA 4–10." If you need a program's official rural status, check HRSA's [Rural Health Grants Eligibility Analyzer](https://data.hrsa.gov/tools/rural-health) by address or county.

The [tract file](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes) includes population, land area and population density. The ZIP code file "only includes geographic identifiers and RUCA codes."

### RUCC codes for counties

The [2023 Rural-Urban Continuum Codes](https://www.ers.usda.gov/data-products/rural-urban-continuum-codes/documentation) give each county one of nine codes. Codes 1–3 are metro counties, grouped by metro area population. Codes 4–9 are nonmetro counties, grouped by urban population and whether they are adjacent to a metro area.

Codes 8 and 9 mark nonmetro counties with an [urban population under 5,000](https://www.ers.usda.gov/data-products/rural-urban-continuum-codes/documentation). Code 9 counties are also not adjacent to a metro area. These are often the first places to look.

## Step 2: Count primary care supply

Use more than one supply source. Each one misses something.

### NPPES clinician registrations

CMS publishes the full [NPPES downloadable file](https://download.cms.gov/nppes/NPI_Files.html) each month; the current file is dated November 9, 2026. The data file inside the zip [exceeds 4 GB](https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination), so load it into a database.

Filter individual (Type 1) NPIs by the primary taxonomy code. The [readme](https://www.cms.gov/regulations-and-guidance/administrative-simplification/nationalprovidentstand/downloads/data_dissemination_file-readme.pdf) says the file marks "the Primary Taxonomy with the Primary Taxonomy Flag." Common primary care codes, as shown in the NPI Registry:

| Code | Taxonomy |
|---|---|
| 207Q00000X | [Family Medicine](https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Family%20Medicine&state=MT&enumeration_type=NPI-1&limit=5) |
| 207R00000X | [Internal Medicine](https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Internal%20Medicine&state=MT&enumeration_type=NPI-1&limit=5) |
| 208D00000X | [General Practice](https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=General%20Practice&state=MT&enumeration_type=NPI-1&limit=5) |
| 208000000X | [Pediatrics](https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Pediatrics&state=VT&enumeration_type=NPI-1&limit=20) |
| 363LF0000X | [Nurse Practitioner, Family](https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Nurse%20Practitioner&state=WY&enumeration_type=NPI-1&limit=20) |
| 363A00000X | [Physician Assistant](https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Physician%20Assistant&state=MT&enumeration_type=NPI-1&limit=5) |

This table is not a complete primary care list. Other codes include [363LP0200X, Nurse Practitioner, Pediatrics](https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Pediatrics&state=VT&enumeration_type=NPI-1&limit=20) and [363LP2300X, Nurse Practitioner, Primary Care](https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Nurse%20Practitioner&state=WY&enumeration_type=NPI-1&limit=20).

Decide whether to include nurse practitioners and physician assistants, and report both versions if you can. In rural counties they can change the picture. See [NPI taxonomy codes](/glossary/npi-taxonomy-codes) for more on code selection.

Geocode the business practice location, not the mailing address. The [readme](https://www.cms.gov/regulations-and-guidance/administrative-simplification/nationalprovidentstand/downloads/data_dissemination_file-readme.pdf) lists separate "Business Mailing Address" and "Business Practice Location Address" fields. Each zipped file also has a [Practice Location Reference File](https://download.cms.gov/nppes/NPI_Files.html) for non-primary locations.

### HRSA health center sites

HRSA's [Health Center Service Delivery and Look-Alike Sites](https://data.hrsa.gov/data/download) file lists HRSA-supported health center sites and refreshes daily. Most sites have an address and coordinates; geocode the few that lack them. For domestic violence shelters, the listing says ["the building number, street name, and ZIP Code are suppressed."](https://data.hrsa.gov/data/download)

Read the site fields before counting. The [file](https://data.hrsa.gov/DataDownload/DD_Files/Health_Center_Service_Delivery_and_LookAlike_Sites.csv) records "Operating Hours per Week" and a location type of Permanent, Seasonal or Mobile. Its setting field also flags sites "Co-located with School." A school-based or 8-hour-a-week site does not serve a whole county.

### Rural Health Clinics

CMS defines a Rural Health Clinic (RHC) as a clinic ["located in a rural area designated as a shortage area"](https://www.cms.gov/medicare/health-safety-standards/certification-compliance/rural-health-clinics). RHCs are part of rural supply. Their clinicians may also appear in NPPES, so avoid counting a clinic and its staff twice.

## Step 3: Measure population and need

Use the [ACS 2020–2024 5-year estimates](https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release-schedule.html). The Census Bureau's schedule lists their planned release as January 29, 2026. The Census Bureau says 5-year data cover ["all areas"](https://www.census.gov/programs-surveys/acs/guidance/estimates.html) and suit "Examining tracts and other smaller geographies."

| Need | 2024 ACS 5-year table | Lines |
|---|---|---|
| Total population | [S0101](https://api.census.gov/data/2024/acs/acs5/subject/groups/S0101.html) | `S0101_C01_001E` |
| Age 65 and over | [S0101](https://api.census.gov/data/2024/acs/acs5/subject/groups/S0101.html) or [B01001](https://api.census.gov/data/2024/acs/acs5/groups/B01001.html) | `S0101_C01_030E` "65 years and over"; or B01001 age lines from "65 and 66 years" to "85 years and over" for each sex |
| Poverty | [S1701](https://api.census.gov/data/2024/acs/acs5/subject/groups/S1701.html) | `S1701_C02_001E` "Below poverty level" |
| Uninsured | [S2701](https://api.census.gov/data/2024/acs/acs5/subject/groups/S2701.html) | `S2701_C04_001E` "Uninsured" |
| No vehicle | [B25044](https://api.census.gov/data/2024/acs/acs5/groups/B25044.html) | `_003E` and `_010E` "No vehicle available" (owner and renter households) |

Vehicle access matters most in rural areas, where the nearest clinic may be far away. B25044 counts households, not people. For uninsured counts by area, see [How to estimate the uninsured population by ZIP code](/uninsured-population-by-zip-code).

## Step 4: Compute ratios and distance

1. **Join supply to tracts.** Assign each geocoded provider and site to a census tract.
2. **Build a ratio.** Divide tract population by the number of primary care registrations. For rural tracts, also build it for a wider area, such as the county or a group of neighboring tracts.
3. **Measure travel.** Compute drive time or distance from each tract's population center to the nearest primary care site. See [drive-time access](/glossary/drive-time-access).
4. **Set thresholds before you look.** HRSA's primary care [HPSA scoring rubric](https://data.hrsa.gov/DataDownload/DD_Files/HPSA_DATAMART_METADATA.XLSX) is a useful reference point, not a rule for your study. It gives the most travel points at "Time GE 60 minutes or Distance GE 50 miles." It gives zero points under 20 minutes or 10 miles.
5. **Flag deserts.** Mark rural tracts that fail your ratio test, your travel test, or both. Keep the two tests separate on the map.

A ratio alone can mislead in rural areas. A tract with no clinician may sit next to a town with several. Travel time shows whether residents can actually reach care.

For benchmarks on population-to-provider ratios, see [provider-to-population ratio](/glossary/provider-to-population-ratio).

## Step 5: Overlay HRSA primary care HPSAs

Download the [HPSA – Primary Care](https://data.hrsa.gov/data/download?titleFilter=Shortage+Areas) files from HRSA's Data Warehouse. They come as a CSV of all HPSAs plus shapefiles of area designation and component boundaries. The listing says the data refresh daily.

Use these fields from the [primary care CSV](https://data.hrsa.gov/DataDownload/DD_Files/BCD_HPSA_FCT_DET_PC.csv):

- **HPSA Status:** the file includes "Designated," "Withdrawn" and "Proposed For Withdrawal" records. Filter to the status you need.
- **Designation Type:** "Geographic HPSA," "High Needs Geographic HPSA," "HPSA Population" and facility types such as "Rural Health Clinic."
- **HPSA Component Type Description:** whether the piece is a "Census Tract," "County Subdivision" or "Single County."
- **Rural Status:** "Rural," "Partially Rural" or "Non-Rural." Many rows are blank or "Unknown," so filtering to "Rural" drops them.
- **HPSA Score:** the [metadata](https://data.hrsa.gov/DataDownload/DD_Files/HPSA_DATAMART_METADATA.XLSX) says scores range "from 0 to 26 where the higher the score, the greater the priority."

The [metadata](https://data.hrsa.gov/DataDownload/DD_Files/HPSA_DATAMART_METADATA.XLSX) lists four primary care scoring factors. They are population per FTE primary care physician, poverty, infant health, and travel to the "nearest source of accessible care outside the HPSA." Each factor scores up to 5 points. The ratio points "are doubled in calculating the final score," so the primary care maximum is 25.

For a quick check of single places, use [HPSA Find or Find Shortage Area by Address](https://data.hrsa.gov/topics/health-workforce/shortage-areas). The batch tool takes up to 100 addresses.

Compare your flagged tracts with the HPSA layer. Tracts flagged by both are well supported. Tracts flagged only by you may be new gaps worth a closer look. HPSAs you did not flag may be population HPSAs, such as low-income groups, or facility HPSAs, such as Rural Health Clinics. Neither always means a lack of clinicians overall.

## Mapping rural primary care gaps in GeoChat Atlas

[GeoChat AI](https://app.geochat.ai) is an AI-powered mapping platform for community health assessments, community needs assessments and healthcare supply-demand studies. Rural health is one of its use cases. It has a free plan, with no credit card required.

As of November 2026, GeoChat Atlas has HRSA layers for HPSAs, MUAs and health center sites. It also has [NPPES provider counts](/methods) by county and ZIP code. Those counts are registrations, not full-time clinicians. Coverage is county, ZIP code (ZCTA) and census tract level for all 50 states, DC and Puerto Rico.

Its AI chat answers follow-up questions in plain language, such as drilling into ZIP codes or comparing regions. The chat is instructed to report only figures from its own queries of the platform's datasets. That is an instruction to the model, not a guarantee. The platform is new, and data are rebuilt by hand after each source release; see [methods](/methods) for versions.

GeoChat AI is not affiliated with HRSA. It is also not affiliated with GeoChat, the MBZUAI remote-sensing model, or GeoChat, the InSTEDD messaging tool. For a list of free tools, see [free tools for mapping healthcare access gaps](/free-tools-healthcare-access-mapping).

## Common mistakes

- **Using county averages only.** A county ratio can hide an empty tract far from the county seat. ERS notes [most counties mix rural and urban territory](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/documentation).
- **Treating rural tracts as small areas.** ERS says rural tracts can be ["so large that they are coextensive with counties."](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/documentation) Distance to care can vary widely inside one tract.
- **Counting NPIs as clinicians.** An NPI [does not confirm a license or credential](https://download.cms.gov/nppes/NPI_Files.html). Check large counts against state licensing data where you can.
- **Geocoding mailing addresses.** A billing office in a city can make a rural clinician look urban. Use the practice location fields.
- **Trusting small numbers.** In a tract of a few hundred people, one clinician moving changes the ratio sharply. Pool neighboring tracts or show counts beside ratios.
- **Ignoring margins of error.** ACS estimates for small rural tracts can be imprecise. Publish the margin of error, and see [ACS 5-year estimates](/glossary/acs-5-year-estimates).
- **Mixing RUCA vintages.** ERS says RUCA versions ["are not directly comparable"](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes) because tract boundaries and methods change each decade. Use 2020 codes with 2020-based tracts.
- **Joining ZIP RUCA codes to ZCTAs without checking.** The ZIP file includes ["point" ZIP codes](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/documentation) for post offices and large mail customers. See [ZCTA vs. ZIP code](/glossary/zcta-vs-zip-code).
- **Keeping withdrawn HPSAs.** The HRSA primary care file keeps withdrawn records. Filter on HPSA Status before mapping.
