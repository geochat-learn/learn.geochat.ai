---
title: "How to Map Home Care and Personal Care Shortages"
description: "Map home care shortages: ACS self-care need, CMS and NPPES agencies, BLS OEWS aide counts, ratios by county or ZIP, and service-area checks."
slug: map-home-care-provider-shortages
type: guide
updated: 2026-11-03
faq:
  - q: "What is the NPI taxonomy code for a home health agency?"
    a: "[251E00000X](https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Home%20Health&limit=20), shown in NPPES as \"Home Health.\" For non-medical personal care agencies, start with [253Z00000X](https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=In%20Home%20Supportive%20Care&limit=20), \"In Home Supportive Care.\" The NUCC maintains the code set; [version 26.1](https://nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40/csv-mainmenu-57) took effect July 1, 2026."
  - q: "Is there free data on home care workers by county?"
    a: "Not from BLS. Its OEWS survey publishes free estimates for home health and personal care aides ([SOC 31-1120](https://www.bls.gov/ooh/healthcare/home-health-aides-and-personal-care-aides.htm)) for [states, metropolitan areas and nonmetropolitan areas](https://www.bls.gov/oes/oes_ques.htm), not counties. NPPES lists aides who registered for an NPI, but registrations are not a workforce count."
  - q: "What is the difference between home health and personal care?"
    a: "Medicare home health is [part-time or intermittent skilled care](https://www.medicare.gov/coverage/home-health-services) for homebound patients, ordered by a provider and delivered by a Medicare-certified agency. Personal care is help with daily living activities, which Medicare does not cover when it is the only care needed. States can cover personal care through Medicaid under [several authorities](https://www.medicaid.gov/tmsis/dataguide/v4/technical-instructions/cms-technical-instructions-reporting-personal-care-and-home-health-services-in-t-msis/)."
  - q: "Does CMS publish which ZIP codes a home health agency serves?"
    a: "Yes. The [Home Health Care - Zip Codes](https://data.cms.gov/provider-data/dataset/m5eg-upu5) dataset has one record for each ZIP code where an agency served at least one patient, based on the agency's [OASIS assessments](https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/home_health/HHS_Data_Dictionary.pdf)."
  - q: "Can GeoChat AI map home care agencies by county or ZIP code?"
    a: "Yes. GeoChat Atlas has a personal care and home health use case and counts providers by county and ZIP code from NPPES. Counts are registrations, not staff, and its home care agency layers use [NPPES extracts from 2025 to early 2026](/methods)."
sources:
  - title: "Home Health Services Coverage - Medicare.gov"
    url: "https://www.medicare.gov/coverage/home-health-services"
    accessed: 2026-11-03
  - title: "CMS Technical Instructions: Reporting personal care and home health services in T-MSIS - Medicaid.gov"
    url: "https://www.medicaid.gov/tmsis/dataguide/v4/technical-instructions/cms-technical-instructions-reporting-personal-care-and-home-health-services-in-t-msis/"
    accessed: 2026-11-03
  - title: "Self-Directed Services - Medicaid.gov"
    url: "https://www.medicaid.gov/medicaid/long-term-services-supports/self-directed-services"
    accessed: 2026-11-03
  - title: "Home Health Care Agencies - CMS Provider Data Catalog"
    url: "https://data.cms.gov/provider-data/dataset/6jpm-sxkc"
    accessed: 2026-11-03
  - title: "Home Health Care - Zip Codes - CMS Provider Data Catalog"
    url: "https://data.cms.gov/provider-data/dataset/m5eg-upu5"
    accessed: 2026-11-03
  - title: "HHQRP and HHVBP Data Dictionary, updated April 2026 - CMS"
    url: "https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/home_health/HHS_Data_Dictionary.pdf"
    accessed: 2026-11-03
  - title: "Data Dissemination (NPPES) - CMS"
    url: "https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination"
    accessed: 2026-11-03
  - title: "NPPES Downloadable Files (NPI Files) - CMS"
    url: "https://download.cms.gov/nppes/NPI_Files.html"
    accessed: 2026-11-03
  - title: "Health Care Provider Taxonomy CSV versions - NUCC"
    url: "https://nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40/csv-mainmenu-57"
    accessed: 2026-11-03
  - title: "NPPES NPI Registry API: taxonomy search, Home Health"
    url: "https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Home%20Health&limit=20"
    accessed: 2026-11-03
  - title: "NPPES NPI Registry API: taxonomy search, In Home Supportive Care"
    url: "https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=In%20Home%20Supportive%20Care&limit=20"
    accessed: 2026-11-03
  - title: "NPPES NPI Registry API: taxonomy search, Nursing Care"
    url: "https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Nursing%20Care&limit=20"
    accessed: 2026-11-03
  - title: "NPPES NPI Registry API: taxonomy search, Adult Day Care"
    url: "https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Adult%20Day%20Care&limit=20"
    accessed: 2026-11-03
  - title: "NPPES NPI Registry API: taxonomy search, Home Health Aide"
    url: "https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Home%20Health%20Aide&limit=20"
    accessed: 2026-11-03
  - title: "NPPES NPI Registry API: taxonomy search, Personal Care Attendant"
    url: "https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Personal%20Care%20Attendant&limit=20"
    accessed: 2026-11-03
  - title: "NPPES NPI Registry API: taxonomy search, Attendant Care Provider"
    url: "https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Attendant%20Care%20Provider&limit=20"
    accessed: 2026-11-03
  - title: "Home Health and Personal Care Aides - Occupational Outlook Handbook, BLS"
    url: "https://www.bls.gov/ooh/healthcare/home-health-aides-and-personal-care-aides.htm"
    accessed: 2026-11-03
  - title: "Occupational Employment and Wages - May 2025 (news release) - BLS"
    url: "https://www.bls.gov/news.release/ocwage.htm"
    accessed: 2026-11-03
  - title: "OEWS Frequently Asked Questions - BLS"
    url: "https://www.bls.gov/oes/oes_ques.htm"
    accessed: 2026-11-03
  - title: "Occupational Employment and Wage Statistics home - BLS"
    url: "https://www.bls.gov/oes/"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 5-year 2024, group B18106 (Sex by Age by Self-Care Difficulty)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B18106.html"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 5-year 2024, group B18107 (Sex by Age by Independent Living Difficulty)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B18107.html"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 5-year 2024, group B01001 (Sex by Age)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B01001.html"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 5-year 2024, group B09021 (Living Arrangements of Adults 18 Years and Over by Age)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B09021.html"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 5-year 2024, group B27010 (Types of Health Insurance Coverage by Age)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B27010.html"
    accessed: 2026-11-03
  - title: "How Disability Data are Collected from the American Community Survey - U.S. Census Bureau"
    url: "https://www.census.gov/topics/health/disability/guidance/data-collection-acs.html"
    accessed: 2026-11-03
  - title: "When to Use 1-year or 5-year Estimates - American Community Survey"
    url: "https://www.census.gov/programs-surveys/acs/guidance/estimates.html"
    accessed: 2026-11-03
  - title: "ZIP Code Tabulation Areas (ZCTAs) - U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html"
    accessed: 2026-11-03
  - title: "HUD USPS ZIP Code Crosswalk Files"
    url: "https://www.huduser.gov/portal/datasets/usps_crosswalk.html"
    accessed: 2026-11-03
---

To map home care and personal care shortages, compare people needing help at home with the agencies and aides that serve each area. Use ACS tables for need, CMS and NPPES files for agencies, and BLS OEWS estimates for aides. Map Medicare home health and personal care as separate layers, then check the results against where agencies actually serve.

## Home health and personal care are different services

Medicare covers home health only for people who are homebound and need [part-time or intermittent skilled services](https://www.medicare.gov/coverage/home-health-services). A provider must see the patient in person and order the care, and a [Medicare-certified home health agency](https://www.medicare.gov/coverage/home-health-services) must deliver it.

Medicare does not pay for [24-hour care at home or homemaker services unrelated to the care plan](https://www.medicare.gov/coverage/home-health-services). It also excludes custodial or personal care when that is the only care needed. "Part-time or intermittent" usually means [up to 8 hours a day and 28 hours a week](https://www.medicare.gov/coverage/home-health-services) of skilled nursing and aide services combined.

Medicaid personal care services provide [assistance that enables people to accomplish tasks they would normally do themselves](https://www.medicaid.gov/tmsis/dataguide/v4/technical-instructions/cms-technical-instructions-reporting-personal-care-and-home-health-services-in-t-msis/). States can offer them under [several authorities](https://www.medicaid.gov/tmsis/dataguide/v4/technical-instructions/cms-technical-instructions-reporting-personal-care-and-home-health-services-in-t-msis/): the state plan under 1905(a)(24), 1915(c) waivers, 1915(i), 1915(j), 1915(k) and 1115 demonstrations.

Through self-direction, Medicaid participants can [recruit, hire, train and supervise the individuals who furnish their services](https://www.medicaid.gov/medicaid/long-term-services-supports/self-directed-services). Those workers may not belong to any agency, so agency counts miss them.

Aides differ too. Home health aides [may be allowed to give a client medication](https://www.bls.gov/ooh/healthcare/home-health-aides-and-personal-care-aides.htm) under a nurse's direction. Personal care aides are generally limited to nonmedical services.

| | Medicare home health | Personal care |
|---|---|---|
| Service | Part-time or intermittent skilled care for homebound patients | Help with daily living activities |
| Public payer | Medicare | Medicaid, under several state options |
| National agency list | [CMS Home Health Care Agencies](https://data.cms.gov/provider-data/dataset/6jpm-sxkc) | NPPES organization NPIs |
| Where agencies serve | [CMS Home Health Care - Zip Codes](https://data.cms.gov/provider-data/dataset/m5eg-upu5) | Ask agencies and state directories |

## Demand data: ACS 5-year tables

Use ACS 5-year estimates, which cover [all areas](https://www.census.gov/programs-surveys/acs/guidance/estimates.html). One-year estimates exist only for areas of [65,000 or more people](https://www.census.gov/programs-surveys/acs/guidance/estimates.html). The line numbers below are from the [2024 ACS 5-year tables](https://api.census.gov/data/2024/acs/acs5/groups/B18106.html), which cover 2020–2024.

| Table | Title | Lines to use |
|---|---|---|
| [B18106](https://api.census.gov/data/2024/acs/acs5/groups/B18106.html) | Sex by Age by Self-Care Difficulty | Ages 65–74 and 75+ with a self-care difficulty: _013, _016, _029, _032 |
| [B18107](https://api.census.gov/data/2024/acs/acs5/groups/B18107.html) | Sex by Age by Independent Living Difficulty | Ages 65–74 and 75+ with the difficulty: _010, _013, _023, _026 |
| [B01001](https://api.census.gov/data/2024/acs/acs5/groups/B01001.html) | Sex by Age | Ages 65+: _020 to _025 and _044 to _049; ages 85+: _025 and _049 |
| [B09021](https://api.census.gov/data/2024/acs/acs5/groups/B09021.html) | Living Arrangements of Adults 18 Years and Over by Age | _023: ages 65+, lives alone |
| [B27010](https://api.census.gov/data/2024/acs/acs5/groups/B27010.html) | Types of Health Insurance Coverage by Age | _062: ages 65+ with Medicare and Medicaid/means-tested coverage |

A self-care difficulty means [difficulty bathing or dressing](https://www.census.gov/topics/health/disability/guidance/data-collection-acs.html). An independent living difficulty is trouble doing errands alone, such as visiting a doctor's office or shopping. It must stem from a physical, mental or emotional problem.

Both disability tables cover the [civilian noninstitutionalized population](https://api.census.gov/data/2024/acs/acs5/groups/B18106.html), so people living in institutions are excluded. Their top age band is 75 and over, so take people 85 and over from B01001.

For ages 65 and over, [B27010](https://api.census.gov/data/2024/acs/acs5/groups/B27010.html) has no Medicaid-only line. Line _062 (Medicare plus Medicaid) is the closest proxy. The "other public only combinations" and "other coverage combinations" lines may also include Medicaid.

## Supply data: agencies and aides

| Source | What it lists | Geography | Latest version |
|---|---|---|---|
| [CMS Home Health Care Agencies](https://data.cms.gov/provider-data/dataset/6jpm-sxkc) | Medicare-registered agencies, with address and services offered | Agency address | October 2026 |
| [CMS Home Health Care - Zip Codes](https://data.cms.gov/provider-data/dataset/m5eg-upu5) | Each ZIP code where an agency served at least one patient | USPS ZIP code | October 2026 |
| [NPPES monthly file](https://download.cms.gov/nppes/NPI_Files.html) | Organization and individual NPIs with taxonomy codes | Practice location address | November 2, 2026 |
| [BLS OEWS](https://www.bls.gov/news.release/ocwage.htm) | Aide employment and wages, SOC 31-1120 | State, metro and nonmetro areas | May 2025, released May 15, 2026 |

### Medicare home health agencies

The agency file is ["a list of all Home Health Agencies that have been registered with Medicare"](https://data.cms.gov/provider-data/dataset/6jpm-sxkc). Medicare.gov shows data for [over 12,000 agencies](https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/home_health/HHS_Data_Dictionary.pdf). A yes/no column records whether each agency [offers home health aide services](https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/home_health/HHS_Data_Dictionary.pdf).

The ZIP file is built from [OASIS assessments submitted by each agency](https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/home_health/HHS_Data_Dictionary.pdf). It has one record for each ZIP code where the agency served at least one patient during the data collection period. CMS typically refreshes these data [each quarter, in January, April, July and October](https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/home_health/HHS_Data_Dictionary.pdf).

### Personal care agencies in NPPES

CMS publishes a free [full replacement monthly NPI file, weekly incremental files and a deactivation file](https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination). Records are [as reported to NPPES](https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination) by providers or people acting for them.

Filter by Health Care Provider Taxonomy code. As of November 2026, the NUCC lists [version 26.1, effective July 1, 2026](https://nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40/csv-mainmenu-57), as current. Descriptions below are as the NPPES registry shows them.

| Code | NPPES description | How to use it |
|---|---|---|
| [251E00000X](https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Home%20Health&limit=20) | Home Health | Agencies; cross-check against the CMS list |
| [253Z00000X](https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=In%20Home%20Supportive%20Care&limit=20) | In Home Supportive Care | Start here for personal care agencies |
| [251J00000X](https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Nursing%20Care&limit=20) | Nursing Care | Optional nursing agency layer |
| [261QA0600X](https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Adult%20Day%20Care&limit=20) | Clinic/Center, Adult Day Care | Related layer, not home care |
| [374U00000X](https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Home%20Health%20Aide&limit=20) | Home Health Aide | Individual aides; not a workforce count |
| [3747P1801X](https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Personal%20Care%20Attendant&limit=20) | Technician, Personal Care Attendant | Individual aides; not a workforce count |
| [3747A0650X](https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=Attendant%20Care%20Provider&limit=20) | Technician, Attendant Care Provider | Individual aides; not a workforce count |

Count agencies with organization NPIs (entity type 2) only, as our [methods page](/methods) does for personal care. Agency records can carry several of these codes, as [NPPES results show](https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=In%20Home%20Supportive%20Care&limit=20), so count each NPI once. See [NPI taxonomy codes](/glossary/npi-taxonomy-codes).

### Aides in BLS OEWS

BLS reports home health aides and personal care aides together as [SOC 31-1120](https://www.bls.gov/ooh/healthcare/home-health-aides-and-personal-care-aides.htm), Home Health and Personal Care Aides. It was the [largest occupation in May 2025, with employment of 4.3 million](https://www.bls.gov/news.release/ocwage.htm).

OEWS publishes estimates for [the nation, states, metropolitan statistical areas and nonmetropolitan areas](https://www.bls.gov/oes/oes_ques.htm). Counties are not on that list. The May 2025 data cover [about 530 metropolitan and nonmetropolitan areas](https://www.bls.gov/news.release/ocwage.htm).

OEWS measures [wage and salary workers in nonfarm establishments](https://www.bls.gov/news.release/ocwage.htm). It excludes the self-employed and [private households (NAICS 814)](https://www.bls.gov/news.release/ocwage.htm), so aides employed directly by households are missing. Look up area figures with the [OEWS Profiles and data search tools](https://www.bls.gov/oes/).

## Step-by-step: mapping home care shortages

### Step 1: Choose the geography

| Geography | Use it for | Caveats |
|---|---|---|
| County | First pass; workforce comparisons | Hides gaps inside large counties |
| ZIP code (ZCTA) | Agency coverage within priority counties | Larger ACS margins of error; ZIP and ZCTA mismatches |

ZCTAs are [generalized areal representations](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html) of ZIP codes built from 2020 census blocks, and [not all valid ZIP codes have one](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html). The CMS ZIP file lists [the ZIP code where service was provided](https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/home_health/HHS_Data_Dictionary.pdf), so crosswalk it before joining census data. See [ZCTA vs ZIP code](/glossary/zcta-vs-zip-code).

The [HUD-USPS crosswalk](https://www.huduser.gov/portal/datasets/usps_crosswalk.html) links ZIP codes to counties and tracts each quarter. It requires a login and omits ZIP codes that only serve PO boxes.

### Step 2: Build demand counts

1. Download B18106, B18107, B01001, B09021 and B27010 for every county or ZCTA in your study area.
2. Add the male and female lines for each age band, and carry the margins of error.
3. Build three need counts: ages 65+ with a self-care difficulty, ages 65+ with an independent living difficulty, and ages 85+.
4. Do not add the two disability counts together. One person can report both difficulties.
5. Add adults 18–64 with a self-care difficulty if your programs serve younger people with disabilities.
6. Convert counts to rates per 1,000 residents for the need maps.

See [ACS 5-year estimates](/glossary/acs-5-year-estimates) for handling margins of error.

### Step 3: Build supply counts

1. **Medicare home health.** Load the agency file and keep the CMS Certification Number as text, because Excel [removes leading zeros](https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/home_health/HHS_Data_Dictionary.pdf). Assign each agency to a county.
2. **Service coverage.** From the ZIP file, count the distinct agencies serving each ZIP code.
3. **Personal care agencies.** From the NPPES monthly file, keep type 2 NPIs with code [253Z00000X](https://npiregistry.cms.hhs.gov/api/?version=2.1&taxonomy_description=In%20Home%20Supportive%20Care&limit=20). Drop NPIs in the [deactivation file](https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination) and place each agency by practice location.
4. **Aides.** Take [31-1120](https://www.bls.gov/ooh/healthcare/home-health-aides-and-personal-care-aides.htm) employment for each OEWS area that covers your counties.
5. **State lists.** If your state health or aging department publishes a licensed home care agency list, add agencies missing from NPPES. Formats differ by state.

[GeoChat AI](https://atlas.geochat.ai) offers a personal care and home health use case. GeoChat Atlas counts providers by county and ZIP code from NPPES, and its layers include CMS home health data. It has a free tier with no credit card required.

Its counts are NPPES registrations, not staff. Its home care agency and adult day care layers use [NPPES extracts from 2025 to early 2026](/methods). The platform is new; the current version is GeoChat Atlas (version 2). Nonprofit organizations can request a new map, and requests shape what gets added.

### Step 4: Compute ratios

| Ratio | Numerator | Denominator | Geography |
|---|---|---|---|
| Personal care agencies | Type 2 NPIs with 253Z00000X | Per 1,000 people 65+ with a self-care difficulty | County or ZCTA |
| Home health coverage | Medicare agencies serving the ZIP code | Per 1,000 people 85+ | ZCTA |
| Aide supply | OEWS 31-1120 employment | Per 1,000 people 65+ with a self-care difficulty | OEWS area |

For the aide ratio, sum ACS counts for every county in each OEWS area before dividing. BLS links [shapefiles for OEWS metropolitan and nonmetropolitan areas](https://www.bls.gov/oes/oes_ques.htm) from its FAQ.

This guide sets no shortage threshold. Compare each area with your state or regional median, and test more than one cutoff. Combine or suppress areas whose denominators have large margins of error.

### Step 5: Map and flag gaps

1. Map need rates and supply ratios on the same geography.
2. Flag areas in the top third for need and the bottom third for supply.
3. Flag ZIP codes served by zero or one Medicare agency in the CMS file.
4. Shade OEWS ratios across whole areas, so readers do not assume they vary by county.
5. Label every layer with its source and date, such as "NPPES November 2026, type 2 NPIs, 253Z00000X."

### Step 6: Check against service areas

An agency's address is not its service area. By our count of the [October 2026 ZIP file](https://data.cms.gov/provider-data/dataset/m5eg-upu5), the median Medicare agency served patients in 33 ZIP codes.

1. Compare address-based and service-based counts for each county. A county with no agency office may still be served.
2. For personal care agencies, add secondary sites from the NPPES [Practice Location Reference File](https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination).
3. Ask agencies, your Area Agency on Aging and your state Medicaid agency which areas each agency covers and whether it takes new clients.
4. Record each change and its reason in your methods note.

## Limits to state in your report

- **Agencies serve areas larger than their address.** Address counts can show gaps where agencies based elsewhere already serve.
- **NPPES registrations are not staff.** An agency NPI says nothing about how many aides it employs or whether it takes new clients.
- **OEWS covers metro and nonmetro areas, not counties.** It also excludes the self-employed and private households, and BLS [does not encourage using OEWS data for time-series analysis](https://www.bls.gov/oes/oes_ques.htm).
- **Medicare home health is a different service from personal care.** Medicare does not cover [personal care when it is the only care needed](https://www.medicare.gov/coverage/home-health-services). Medicare agency counts therefore do not measure personal care supply.
- **The CMS ZIP file shows past service.** It reflects patients served in the data collection period, not current capacity.

## Common mistakes

- **Adding self-care and independent living counts.** The same person can appear in both tables.
- **Treating aide NPIs as the workforce.** Individual aide codes capture only aides who registered for an NPI.
- **Dividing a metro-area aide count by one county's population.** Match the ACS denominator to the OEWS area.
- **Joining CMS ZIP codes straight to ZCTA shapes.** Some ZIP codes have no ZCTA, so check what drops out.

For a county-level example built from ACS and NPPES, see [healthcare access in 10 California counties](/california-county-healthcare-access-2026). For other free mapping options, see [free tools for healthcare access mapping](/free-tools-healthcare-access-mapping).
