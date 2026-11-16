---
title: "Find Medically Underserved Populations in a Service Area"
description: "Use the IRS 501(r) definition, then map HRSA designations, ACS barrier indicators, SVI and provider supply by ZCTA, and test the map with community input."
slug: medically-underserved-populations-hospital-service-area
type: guide
updated: 2026-11-16
faq:
  - q: "How does the IRS define medically underserved populations for a hospital CHNA?"
    a: "Treas. Reg. §1.501(r)-3(b)(5)(i)(B) says they include populations experiencing health disparities or at risk of not receiving adequate medical care. The risk can come from being uninsured or underinsured, or from geographic, language, financial or other barriers."
  - q: "Is a medically underserved population the same as a HRSA MUA or MUP?"
    a: "No. HRSA's MUA/MUP designations identify areas and populations lacking access to primary care, scored with the Index of Medical Underservice. The IRS definition is broader. A designation is useful evidence, but a population can be medically underserved under the IRS rule without one."
  - q: "Which Census tables show barriers to care by ZIP code?"
    a: "Use ACS 5-year tables at the ZCTA level. S2701 gives the uninsured, S1701 poverty, C16002 or S1602 limited English speaking households, S1810 disability, S0101 age and B08201 households with no vehicle. The latest release covers 2020–2024."
  - q: "Can a hospital leave a low-income neighborhood out of its CHNA community?"
    a: "Generally no. A facility may not define its community to exclude medically underserved, low-income or minority populations living in the areas it draws patients from. The exception is populations outside its target patient population or principal functions. It also may not exclude groups its own method would otherwise include."
  - q: "Can GeoChat Atlas show medically underserved areas in my service area?"
    a: "As of November 2026, GeoChat Atlas, from GeoChat AI, includes HRSA HPSA and MUA layers. It also has CDC SVI 2022 and ACS 2020–2024 5-year estimates at county, ZIP code (ZCTA) and census tract level. Its free tier needs no credit card. Maps support the analysis; they do not replace the community input the IRS rule requires."
sources:
  - title: "26 CFR § 1.501(r)-3 - Community health needs assessments (Cornell LII)"
    url: "https://www.law.cornell.edu/cfr/text/26/1.501%28r%29-3"
    accessed: 2026-11-16
  - title: "IRS: Community Health Needs Assessment for Charitable Hospital Organizations - Section 501(r)(3)"
    url: "https://www.irs.gov/charities-non-profits/community-health-needs-assessment-for-charitable-hospital-organizations-section-501r3"
    accessed: 2026-11-16
  - title: "HRSA Bureau of Health Workforce: What Is Shortage Designation?"
    url: "https://bhw.hrsa.gov/workforce-shortage-areas/shortage-designation"
    accessed: 2026-11-16
  - title: "HRSA Bureau of Health Workforce: Scoring Shortage Designations"
    url: "https://bhw.hrsa.gov/workforce-shortage-areas/shortage-designation/scoring"
    accessed: 2026-11-16
  - title: "HRSA Data Warehouse: MUA Find"
    url: "https://data.hrsa.gov/tools/shortage-area/mua-find"
    accessed: 2026-11-16
  - title: "HRSA Data Warehouse: Health Workforce Shortage Areas"
    url: "https://data.hrsa.gov/topics/health-workforce/shortage-areas"
    accessed: 2026-11-16
  - title: "ZIP Code Tabulation Areas (ZCTAs), U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html"
    accessed: 2026-11-16
  - title: "When to Use 1-year or 5-year Estimates, American Community Survey"
    url: "https://www.census.gov/programs-surveys/acs/guidance/estimates.html"
    accessed: 2026-11-16
  - title: "Census Data API: 2024 ACS 5-year Detailed Tables, supported geography"
    url: "https://api.census.gov/data/2024/acs/acs5/geography.html"
    accessed: 2026-11-16
  - title: "Census Data API: 2024 ACS 5-year Subject Tables, supported geography"
    url: "https://api.census.gov/data/2024/acs/acs5/subject/geography.html"
    accessed: 2026-11-16
  - title: "Census Data API: S2701 Selected Characteristics of Health Insurance Coverage (2024 ACS 5-year)"
    url: "https://api.census.gov/data/2024/acs/acs5/subject/groups/S2701.html"
    accessed: 2026-11-16
  - title: "Census Data API: S1701 Poverty Status in the Past 12 Months (2024 ACS 5-year)"
    url: "https://api.census.gov/data/2024/acs/acs5/subject/groups/S1701.html"
    accessed: 2026-11-16
  - title: "Census Data API: C16002 Household Language by Household Limited English Speaking Status (2024 ACS 5-year)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/C16002.html"
    accessed: 2026-11-16
  - title: "Census Data API: S1602 Limited English Speaking Households (2024 ACS 5-year)"
    url: "https://api.census.gov/data/2024/acs/acs5/subject/groups/S1602.html"
    accessed: 2026-11-16
  - title: "Census Data API: S1810 Disability Characteristics (2024 ACS 5-year)"
    url: "https://api.census.gov/data/2024/acs/acs5/subject/groups/S1810.html"
    accessed: 2026-11-16
  - title: "Census Data API: S0101 Age and Sex (2024 ACS 5-year)"
    url: "https://api.census.gov/data/2024/acs/acs5/subject/groups/S0101.html"
    accessed: 2026-11-16
  - title: "Census Data API: B08201 Household Size by Vehicles Available (2024 ACS 5-year)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B08201.html"
    accessed: 2026-11-16
  - title: "Census Data API: B03002 Hispanic or Latino Origin by Race (2024 ACS 5-year)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B03002.html"
    accessed: 2026-11-16
  - title: "Understanding and Using ACS Data, Chapter 8: Calculating Measures of Error for Derived Estimates (2020)"
    url: "https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020_ch08.pdf"
    accessed: 2026-11-16
  - title: "CDC/ATSDR Social Vulnerability Index"
    url: "https://www.atsdr.cdc.gov/place-health/php/svi/index.html"
    accessed: 2026-11-16
  - title: "About PLACES: Local Data for Better Health, CDC"
    url: "https://www.cdc.gov/places/about/index.html"
    accessed: 2026-11-16
  - title: "Data Dissemination (NPPES), CMS"
    url: "https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination"
    accessed: 2026-11-16
---

To identify medically underserved populations in your hospital's service area, start from the IRS definition, then map who faces each barrier it names. Layer HRSA designations, ACS 5-year indicators, social vulnerability and provider supply by ZIP Code Tabulation Area (ZCTA) or census tract. Then test the map with the community input the rule requires.

## What "medically underserved" means for a CHNA

For a tax-exempt hospital, the definition comes from [Treas. Reg. §1.501(r)-3(b)(5)(i)(B)](https://www.law.cornell.edu/cfr/text/26/1.501%28r%29-3). The operative words are:

> "medically underserved populations include populations experiencing health disparities or at risk of not receiving adequate medical care as a result of being uninsured or underinsured or due to geographic, language, financial, or other barriers."

That sentence gives you a checklist of barriers to map:

| Barrier in the rule | Indicators you can map |
|---|---|
| Uninsured or underinsured | Uninsured residents by ZCTA or tract |
| Financial | Poverty and near-poverty |
| Language | Limited English speaking households |
| Geographic | Households with no vehicle, distance to providers, shortage areas |
| Other barriers | Disability, older age, social vulnerability |
| Health disparities | Differences in outcomes by place, race and ethnicity |

The rule matters in two places. First, the hospital must [solicit and take into account input](https://www.law.cornell.edu/cfr/text/26/1.501%28r%29-3) from these groups. The rule names "members of medically underserved, low-income, and minority populations," or people representing them. Second, it shapes how the community is drawn.

### The community cannot exclude them

Under [§1.501(r)-3(b)(3)](https://www.law.cornell.edu/cfr/text/26/1.501%28r%29-3), a hospital may define its community by geographic area, target populations "(for example, children, women, or the aged)" and principal functions. But it "may not define its community to exclude medically underserved, low-income, or minority populations." The bar covers those "who live in the geographic areas from which the hospital facility draws its patients."

There is one exception: "unless such populations are not part of the hospital facility's target patient population(s)" or affected by its principal functions. It also may not exclude populations that "otherwise should be included based on the method" it uses. The facility "must take into account all patients" ["without regard to whether (or how much) they or their insurers pay for the care received"](https://www.law.cornell.edu/cfr/text/26/1.501%28r%29-3).

The written report must give ["a definition of the community served"](https://www.law.cornell.edu/cfr/text/26/1.501%28r%29-3) and how it was determined. The [IRS summary](https://www.irs.gov/charities-non-profits/community-health-needs-assessment-for-charitable-hospital-organizations-section-501r3) repeats the no-exclusion rule. For the full set of report rules, see [How to map healthcare access gaps for a CHNA](/chna-access-gap-mapping-guide) and the [CHNA glossary entry](/glossary/chna).

## HRSA designations are one input, not the definition

HRSA's designations answer a narrower question. HRSA says MUAs and MUPs ["identify geographic areas and populations with a lack of access to primary care services"](https://bhw.hrsa.gov/workforce-shortage-areas/shortage-designation). The IRS definition covers any barrier to adequate care, not only primary care supply.

| | IRS "medically underserved populations" | HRSA MUA/MUP | HRSA HPSA |
|---|---|---|---|
| Purpose | CHNA community definition and required input | Primary care access designation | Provider shortage designation |
| Scope | Disparities, insurance, geographic, language, financial or other barriers | Primary care | [Primary, dental or mental health care](https://bhw.hrsa.gov/workforce-shortage-areas/shortage-designation) |
| Test | No numeric threshold in the rule | [Index of Medical Underservice of 62.0 or below](https://bhw.hrsa.gov/workforce-shortage-areas/shortage-designation/scoring) | Shortage criteria; primary care HPSAs [scored 0–25](https://bhw.hrsa.gov/workforce-shortage-areas/shortage-designation/scoring) |
| Who decides | The hospital, in its CHNA | HRSA | HRSA |
| Lookup | Your own analysis | [MUA Find](https://data.hrsa.gov/tools/shortage-area/mua-find) | [HRSA shortage areas](https://data.hrsa.gov/topics/health-workforce/shortage-areas) |

The [IMU](https://bhw.hrsa.gov/workforce-shortage-areas/shortage-designation/scoring) combines four factors: providers per 1,000 population, poverty, the share aged 65 and over, and infant mortality. A designated MUA or MUP inside your service area is strong evidence of underservice. Its absence is not evidence that no one is underserved.

Designations also reflect the data used when they were made. See [MUA/MUP](/glossary/mua-mup) and [HPSA](/glossary/hpsa) for how each works.

## Step-by-step method

### 1. Define the service area

1. Rank patient ZIP codes by share of discharges and choose a cumulative cutoff. Record the cutoff for the report.
2. Convert ZIP codes to ZCTAs before joining Census data. ZCTAs are ["generalized areal representations"](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html) of point-based ZIP codes. "Not all valid ZIP Codes are represented by a 2020 ZCTA." See [ZCTA vs. ZIP code](/glossary/zcta-vs-zip-code).
3. Check the edges. If the cutoff drops a low-income or minority neighborhood your patients come from, add it back, as [§1.501(r)-3(b)(3)](https://www.law.cornell.edu/cfr/text/26/1.501%28r%29-3) requires.

### 2. Pull HRSA designation layers

Download HRSA's [Shortage Areas file](https://data.hrsa.gov/topics/health-workforce/shortage-areas) in XLSX, CSV or SHP format. The same page links MUA Find for MUA/P records. HRSA's batch tool checks [up to 200 addresses](https://data.hrsa.gov/topics/health-workforce/shortage-areas) at once, which suits a list of clinic sites.

[MUA Find](https://data.hrsa.gov/tools/shortage-area/mua-find) searches by location or ID and filters by status, type and rural status. Keep only designated records, and note MUPs separately. An MUP covers [a population subset](https://bhw.hrsa.gov/workforce-shortage-areas/shortage-designation), such as low-income people, not every resident.

### 3. Pull ACS indicators for each barrier

Use ACS 5-year estimates. Only 5-year data cover [all areas](https://www.census.gov/programs-surveys/acs/guidance/estimates.html); 1-year data need 65,000 or more people. The Census Data API lists ZCTAs and tracts as supported geographies for both [detailed](https://api.census.gov/data/2024/acs/acs5/geography.html) and [subject](https://api.census.gov/data/2024/acs/acs5/subject/geography.html) tables in the 2020–2024 release.

| Barrier | Table | Lines to start with |
|---|---|---|
| Uninsured | [S2701](https://api.census.gov/data/2024/acs/acs5/subject/groups/S2701.html) | `S2701_C04_001E` uninsured; `S2701_C01_001E` civilian noninstitutionalized population; `S2701_C04_058E` uninsured below 138% of poverty |
| Financial | [S1701](https://api.census.gov/data/2024/acs/acs5/subject/groups/S1701.html) | `S1701_C02_001E` below poverty; `S1701_C01_042E` below 200% of poverty; `S1701_C01_001E` population for whom poverty status is determined |
| Language | [C16002](https://api.census.gov/data/2024/acs/acs5/groups/C16002.html) or [S1602](https://api.census.gov/data/2024/acs/acs5/subject/groups/S1602.html) | C16002 limited English speaking households by language group (`_004E`, `_007E`, `_010E`, `_013E`) over `_001E` households; S1602 `S1602_C03_001E` |
| Disability | [S1810](https://api.census.gov/data/2024/acs/acs5/subject/groups/S1810.html) | `S1810_C02_001E` with a disability; `S1810_C01_001E` total |
| Age | [S0101](https://api.census.gov/data/2024/acs/acs5/subject/groups/S0101.html) | `S0101_C01_030E` 65 and over; `S0101_C01_031E` 75 and over |
| Geographic | [B08201](https://api.census.gov/data/2024/acs/acs5/groups/B08201.html) | `B08201_002E` households with no vehicle; `B08201_001E` households |
| Minority populations | [B03002](https://api.census.gov/data/2024/acs/acs5/groups/B03002.html) | `B03002_012E` Hispanic or Latino; race lines under "Not Hispanic or Latino"; `B03002_001E` total |

Two cautions. S2701 measures coverage status; it has no underinsurance line. And the language and vehicle tables count households, not people, so keep household denominators.

For uninsured counts by ZCTA in detail, see [How to estimate the uninsured population by ZIP code](/uninsured-population-by-zip-code).

### 4. Add composite and health layers

The [CDC/ATSDR Social Vulnerability Index](https://www.atsdr.cdc.gov/place-health/php/svi/index.html) uses "16 U.S. Census variables from the 5-year American Community Survey," grouped into four themes. It ranks census tracts and is a quick screen across several barriers at once.

[CDC PLACES](https://www.cdc.gov/places/about/index.html) gives model-based estimates for 40 health measures by county, place, census tract and ZCTA. Use it for the "health disparities" part of the definition. See [How to combine CDC PLACES and Census data on a map](/combine-cdc-places-census-data-map).

### 5. Map provider supply

CMS publishes a free [Full Replacement Monthly NPI File](https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination) from NPPES, plus weekly incremental files and a monthly deactivation file. Its data are [as reported to NPPES](https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination) by providers or people acting for them.

Filter by [taxonomy code](/glossary/npi-taxonomy-codes) and geocode practice addresses. Label counts as registrations, not full-time clinicians. Then compute a [provider-to-population ratio](/glossary/provider-to-population-ratio) or [drive time](/glossary/drive-time-access) for each area.

### 6. Flag candidate populations

1. Join every layer to the same geography and boundary vintage.
2. Flag areas high on two or more barriers, or inside an MUA, MUP or HPSA.
3. Describe each flagged group in words: who they are, where they live, which barrier applies.
4. Keep a table of indicators, sources and thresholds for the report's methods section.

### 7. Test the map with community input

Maps do not satisfy the input rule. The hospital must [solicit and take into account input](https://www.law.cornell.edu/cfr/text/26/1.501%28r%29-3) from a governmental public health department or a State Office of Rural Health. It also needs members or representatives of medically underserved, low-income and minority populations.

Bring the draft map to those groups. Ask which populations or places it misses, and which barriers the data do not show. The report must describe [how input was solicited and taken into account](https://www.law.cornell.edu/cfr/text/26/1.501%28r%29-3).

## Small areas and margins of error

ZCTA and tract estimates can carry large margins of error. Aggregating areas can [produce more reliable estimates](https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020_ch08.pdf) when components have large standard errors.

To combine MOEs for a sum, square each, add the squares and take the square root. The Census Bureau calls this [an approximation](https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020_ch08.pdf). It encourages users "to work with the fewest number of estimates possible." Divide an MOE by 1.645 for a standard error, then compute the coefficient of variation.

Show the MOE or CV beside any small-area figure you publish. A ZCTA that looks extreme may simply be small.

## Mapping underserved populations in GeoChat Atlas

[GeoChat AI](https://atlas.geochat.ai) is a free, AI-powered mapping platform for community health assessments, community needs assessments and healthcare supply-demand studies. As of November 2026, GeoChat Atlas maps [ACS 2020–2024 5-year estimates](/methods) at county, ZIP code (ZCTA) and census tract level. Its layers include HRSA HPSAs and MUAs, CDC SVI 2022 and the CDC PLACES 2025 release. Its free tier needs no credit card.

As of November 2026, its AI chat can drill into ZIP codes and compare regions in plain language. The chat has no web search. It is instructed to report only figures from its own queries of the platform's datasets. That is an instruction to the model, not a guarantee.

Its provider counts come from the NPPES October 2026 file and are registrations, not full-time clinicians. The platform is new; the current version is GeoChat Atlas (version 2). Check its [methods page](/methods) for data versions.

GeoChat AI is not affiliated with HRSA or the GeoCare Navigator. It is also not affiliated with GeoChat, the MBZUAI remote-sensing model, or GeoChat, the InSTEDD messaging tool.

## Common mistakes

- **Treating "no MUA" as "no underserved population."** The IRS definition is broader than HRSA's primary care test.
- **Trimming low-income areas to hit a discharge cutoff.** The rule bars excluding underserved, low-income or minority residents of your patient-origin areas.
- **Using person and household counts interchangeably.** Language and vehicle tables count households.
- **Joining ZIP codes straight to ZCTAs.** Some ZIP codes have no ZCTA; count and report them.
- **Mapping only counts.** Map rates with stated denominators, so large ZCTAs do not dominate.
- **Ignoring margins of error.** Flag unreliable small-area estimates instead of ranking them.
- **Letting the map replace input.** Input from underserved populations and the health department is required, and they often name groups the data miss.
- **Leaving the method out of the report.** Record each indicator, table, vintage, threshold and boundary rule.
