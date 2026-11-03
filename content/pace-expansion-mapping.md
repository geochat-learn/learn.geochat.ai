---
title: "How to Map a PACE Expansion: Data and Steps"
description: "Plan a PACE service area expansion with maps: eligibility rules, CMS enrollment data, ACS self-care proxies, drive-time tests and state approval."
slug: pace-expansion-mapping
type: guide
updated: 2026-11-03
faq:
  - q: "Who is eligible for PACE?"
    a: "People 55 or older who need a nursing-home level of care as certified by their state, live in a PACE organization's service area, and can live safely in the community with PACE's help. Medicare or Medicaid coverage is not required to enroll (42 CFR §460.150)."
  - q: "How does a PACE organization expand its service area?"
    a: "It files a service area expansion application with CMS in HPMS, with a signed State assurance that the state will amend its PACE program agreement. CMS and the State administering agency must both approve the change, and only after the organization has passed its first trial period audit."
  - q: "Where can I find PACE enrollment data?"
    a: "CMS's monthly Contract/Plan/State/County (CPSC) enrollment file includes 'National PACE' contracts, with enrollment by county. Counts of 10 or fewer are left blank. Some states, such as California, also publish PACE service-area ZIP code lists."
  - q: "How do you estimate the number of people eligible for PACE in an area?"
    a: "No public dataset counts people who meet a state's nursing-home level of care. Analysts build a proxy from ACS self-care difficulty (table B18106) and age (table B01001), then label it as a proxy, not a count of eligible people."
  - q: "Does GeoChat AI have PACE data?"
    a: "Yes. GeoChat Atlas includes PACE sites, PACE coverage by county and PACE service ZIP codes, plus estimates of people who may be eligible for PACE built from ACS self-care difficulty for ages 55 and over. These estimates are proxies: they do not check nursing-home level of care or PACE service areas."
sources:
  - title: "PACE | Medicare.gov"
    url: "https://www.medicare.gov/health-drug-plans/health-plans/your-coverage-options/other-medicare-health-plans/pace"
    accessed: 2026-11-03
  - title: "eCFR: 42 CFR Part 460, Subpart I (Participant Enrollment and Disenrollment), incl. §460.150"
    url: "https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-E/part-460/subpart-I"
    accessed: 2026-11-03
  - title: "42 CFR §460.150 - Eligibility to enroll in a PACE program (Cornell LII)"
    url: "https://www.law.cornell.edu/cfr/text/42/460.150"
    accessed: 2026-11-03
  - title: "eCFR: 42 CFR Part 460, Subpart B (PACE Organization Application and Waiver Process), incl. §§460.10, 460.12, 460.20"
    url: "https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-E/part-460/subpart-B"
    accessed: 2026-11-03
  - title: "42 CFR §460.12 - Application requirements (Cornell LII)"
    url: "https://www.law.cornell.edu/cfr/text/42/460.12"
    accessed: 2026-11-03
  - title: "eCFR: 42 CFR §460.32 - Content and terms of PACE program agreement"
    url: "https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-E/part-460/subpart-C/section-460.32"
    accessed: 2026-11-03
  - title: "eCFR: 42 CFR Part 460, Subpart F (PACE Services), incl. §460.98"
    url: "https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-E/part-460/subpart-F"
    accessed: 2026-11-03
  - title: "Program of All-Inclusive Care for the Elderly (PACE) - CMS (applications, HPMS)"
    url: "https://www.cms.gov/medicare/medicaid-coordination/pace"
    accessed: 2026-11-03
  - title: "Program of All-Inclusive Care for the Elderly (PACE) - CMS Medicare-Medicaid Coordination"
    url: "https://www.cms.gov/medicare/medicaid-coordination/about/pace"
    accessed: 2026-11-03
  - title: "Programs of All-Inclusive Care for the Elderly for States - Medicaid.gov"
    url: "https://www.medicaid.gov/medicaid/long-term-services-supports/pace/programs-of-all-inclusive-care-for-elderly-for-states/index.html"
    accessed: 2026-11-03
  - title: "CMS memo: Policies Related to Expanding Access to PACE in Rural Areas, July 22, 2026 (copy posted by LeadingAge)"
    url: "https://leadingage.org/wp-content/uploads/2026/07/2026-PACE-Rural-Memo_072226.pdf"
    accessed: 2026-11-03
  - title: "Medicare Advantage/Part D Contract and Enrollment Data - CMS"
    url: "https://cms.gov/data-research/statistics-trends-and-reports/medicare-advantagepart-d-contract-and-enrollment-data"
    accessed: 2026-11-03
  - title: "Monthly Enrollment by Contract/Plan/State/County - CMS"
    url: "https://cms.gov/data-research/statistics-trends-and-reports/medicare-advantagepart-d-contract-and-enrollment-data/monthly-enrollment-contract/plan/state/county"
    accessed: 2026-11-03
  - title: "Monthly Enrollment by CPSC 2026-07 - CMS (release page; file readme lists 'National PACE' and the 10-or-fewer suppression rule)"
    url: "https://www.cms.gov/data-research/statistics-trends-and-reports/medicare-advantagepart-d-contract-and-enrollment-data/monthly-enrollment-contract/plan/state/county/monthly-enrollment-cpsc-2026-07"
    accessed: 2026-11-03
  - title: "MMCO Statistical & Analytic Reports - CMS (Medicare-Medicaid dual enrollment snapshots)"
    url: "https://www.cms.gov/data-research/research/statistical-resources-dually-eligible-beneficiaries/mmco-statistical-analytic-reports"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 2024 5-year, group B18106 (Sex by Age by Self-Care Difficulty)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B18106.html"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 2024 5-year, group B01001 (Sex by Age)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B01001.html"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 2024 5-year, group B27010 (Types of Health Insurance Coverage by Age)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B27010.html"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 2024 5-year group list with table universes"
    url: "https://api.census.gov/data/2024/acs/acs5/groups.json"
    accessed: 2026-11-03
  - title: "ACS 2024 5-year table-based Summary File, table B18106 (geographies published)"
    url: "https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b18106.dat"
    accessed: 2026-11-03
  - title: "ACS 2024 5-year table-based Summary File, table B01001 (geographies published)"
    url: "https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b01001.dat"
    accessed: 2026-11-03
  - title: "ACS 2024 5-year table-based Summary File, table B27010 (geographies published)"
    url: "https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b27010.dat"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 2024 5-year PUMS variable AGEP (Age)"
    url: "https://api.census.gov/data/2024/acs/acs5/pums/variables/AGEP.html"
    accessed: 2026-11-03
  - title: "Census Data API: ACS 2024 5-year PUMS variable DDRS (Self-care difficulty)"
    url: "https://api.census.gov/data/2024/acs/acs5/pums/variables/DDRS.html"
    accessed: 2026-11-03
  - title: "Understanding and Using ACS PUMS, Chapter 2 - U.S. Census Bureau (2021)"
    url: "https://www.census.gov/content/dam/Census/library/publications/2021/acs/acs_pums_handbook_2021_ch02.pdf"
    accessed: 2026-11-03
  - title: "How Disability Data are Collected from the American Community Survey - U.S. Census Bureau"
    url: "https://www.census.gov/topics/health/disability/guidance/data-collection-acs.html"
    accessed: 2026-11-03
  - title: "ZIP Code Tabulation Areas (ZCTAs) - U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html"
    accessed: 2026-11-03
  - title: "HUD USPS ZIP Code Crosswalk Files"
    url: "https://www.huduser.gov/portal/datasets/usps_crosswalk.html"
    accessed: 2026-11-03
  - title: "California PACE Plans - DHCS"
    url: "https://www.dhcs.ca.gov/individuals/Pages/PACEPlans.aspx"
    accessed: 2026-11-03
  - title: "California PACE Plans County Zip Codes, July 2026 - DHCS"
    url: "https://www.dhcs.ca.gov/ko/file/website-zip-code-tracker/"
    accessed: 2026-11-03
  - title: "DHCS PACE Policy Letter 23-01: Application Process (April 14, 2023)"
    url: "https://www.dhcs.ca.gov/services/ltc/Documents/PL-23-01-Application-Process-DHCS.pdf"
    accessed: 2026-11-03
  - title: "DHCS PACE Policy Letter 25-02: Application Pause (November 17, 2025)"
    url: "https://www.dhcs.ca.gov/services/ltc/Documents/PL-25-02-Application-Pause.pdf"
    accessed: 2026-11-03
  - title: "Policy - ALTSA PACE Service Area, Washington DSHS (February 13, 2025)"
    url: "https://dshs.wa.gov/sites/default/files/ALTSA/stakeholders/documents/PACE/ALTSA%20PACE%20Service%20Area%20Policy.pdf"
    accessed: 2026-11-03
  - title: "Find a PACE Program Near You - National PACE Association (context)"
    url: "https://www.npaonline.org/find-a-pace-program"
    accessed: 2026-11-03
  - title: "PACE Application Process - National PACE Association (context)"
    url: "https://npaonline.org/starting-expanding-a-pace-program/application-process"
    accessed: 2026-11-03
---

To map a PACE expansion, plot centers and service ZIP codes, estimate the eligible pool outside them, and test drive times from candidate sites. Then check competing organizations and state rules, because [CMS and the State administering agency must approve any change in the designated service area](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-E/part-460/subpart-C/section-460.32).

## The PACE rules that shape your map

Federal eligibility rules sit in [42 CFR §460.150](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-E/part-460/subpart-I). [Medicare.gov](https://www.medicare.gov/health-drug-plans/health-plans/your-coverage-options/other-medicare-health-plans/pace) lists the same tests in plain language. Each one points to a different map layer.

| Rule in §460.150 | What it requires | What it means for your map |
|---|---|---|
| (b)(1) Age | 55 or older | Count residents 55 and over. |
| (b)(2) Level of care | The State administering agency finds the person needs nursing facility level of care under the state Medicaid plan | No public dataset measures this. You can only map proxies. |
| (b)(3) Residence | Lives in the PACE organization's service area | Map approved service areas before you count anyone. |
| (c) Community safety | Can live in a community setting without jeopardizing health or safety, using state criteria in the program agreement | Your pool is people living in the community. |
| (d) Coverage | Medicare or Medicaid entitlement is not required | Do not limit the pool to dual-eligible people. |

Most enrollees are still dual eligible. CMS says ["most of the participants who are in PACE are dually eligible"](https://www.cms.gov/medicare/medicaid-coordination/about/pace) for Medicare and Medicaid.

PACE is not offered everywhere. Medicare.gov says it is [only available in some states that offer PACE under Medicaid](https://www.medicare.gov/health-drug-plans/health-plans/your-coverage-options/other-medicare-health-plans/pace). For context, the National PACE Association's directory, viewed November 2026, reports [206 programs serving more than 98,800 participants in 33 states and DC](https://www.npaonline.org/find-a-pace-program). These are NPA's figures, not CMS's.

## How PACE service areas are defined and expanded

Each PACE program agreement designates a service area. It may be identified by [county, ZIP code, street boundaries, census tract, block or tribal jurisdictional area](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-E/part-460/subpart-C/section-460.32). [California](https://www.dhcs.ca.gov/services/ltc/Documents/PL-23-01-Application-Process-DHCS.pdf) and [Washington](https://dshs.wa.gov/sites/default/files/ALTSA/stakeholders/documents/PACE/ALTSA%20PACE%20Service%20Area%20Policy.pdf) both define service areas by ZIP code, so plan at the ZIP level.

A PACE organization must run [at least one PACE center in, or contiguous to, its service area](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-E/part-460/subpart-F), with room for routine attendance. Under §460.98(e)(2), it must [add centers, staff or services](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-E/part-460/subpart-F) if needed to keep services accessible and adequate.

### The federal expansion process

1. **Get state approval first.** The organization must get approval from both the [State Medicaid agency and the State administering agency](https://www.medicaid.gov/medicaid/long-term-services-supports/pace/programs-of-all-inclusive-care-for-elderly-for-states/index.html). Without a signed State assurance, CMS treats the application as [incomplete and will not evaluate it](https://www.law.cornell.edu/cfr/text/42/460.12).
2. **Apply in HPMS.** CMS says applicants complete [both initial and service area expansion applications in HPMS](https://www.cms.gov/medicare/medicaid-coordination/pace). The application must [describe the proposed service area](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-E/part-460/subpart-B).
3. **Meet the timing rules.** CMS and the state approve expansions [only after the first trial period audit](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-E/part-460/subpart-B) and any required corrective action plan. CMS has [45 days to act on a service area expansion or a new center, and 90 days for both together](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-E/part-460/subpart-B). Acting means approving, denying or asking for more information.
4. **Pass a readiness review for new sites.** For a new center, [the SAA conducts a readiness review of the new site](https://www.medicaid.gov/medicaid/long-term-services-supports/pace/programs-of-all-inclusive-care-for-elderly-for-states/index.html) while the review clock is stopped.
5. **Amend Appendix C.** If CMS approves, [Appendix C of the program agreement is amended](https://www.medicaid.gov/medicaid/long-term-services-supports/pace/programs-of-all-inclusive-care-for-elderly-for-states/index.html) to show the new area or site.

CMS, in consultation with the state, [may exclude an area already covered by another PACE program agreement](https://www.law.cornell.edu/cfr/text/42/460.12). CMS accepts applications on quarterly deadlines. Its [July 22, 2026 rural PACE memo](https://leadingage.org/wp-content/uploads/2026/07/2026-PACE-Rural-Memo_072226.pdf) points to a January 15, 2026 HPMS memo for the 2026 dates. The National PACE Association's [application process page](https://npaonline.org/starting-expanding-a-pace-program/application-process) summarizes these steps (NPA guidance, not regulation).

## Public data for PACE expansion planning

| Data | Publisher | Geography | Use it for | Watch for |
|---|---|---|---|---|
| [Monthly Enrollment by Contract/Plan/State/County (CPSC)](https://cms.gov/data-research/statistics-trends-and-reports/medicare-advantagepart-d-contract-and-enrollment-data/monthly-enrollment-contract/plan/state/county) | CMS | County | Enrollment of each "National PACE" contract | Counts of 10 or fewer are blank |
| [PACE service-area ZIP list](https://www.dhcs.ca.gov/ko/file/website-zip-code-tracker/) (California example) | State Medicaid agency | ZIP code | Current approved service areas | Check the list date; California's is July 2026 |
| [Find a PACE Program](https://www.npaonline.org/find-a-pace-program) | NPA (context) | City | Program names and locations | Shows no service areas |
| [B18106](https://api.census.gov/data/2024/acs/acs5/groups/B18106.html), Sex by Age by Self-Care Difficulty | Census Bureau, ACS 5-year | County, tract, ZCTA | Proxy for needing help with daily care | No 55–64 age group |
| [B01001](https://api.census.gov/data/2024/acs/acs5/groups/B01001.html), Sex by Age | Census Bureau, ACS 5-year | County, tract, ZCTA | People 55 and over | Total population, including people in institutions |
| [B27010](https://api.census.gov/data/2024/acs/acs5/groups/B27010.html), Types of Health Insurance Coverage by Age | Census Bureau, ACS 5-year | County, tract, ZCTA | Self-reported Medicare plus Medicaid coverage | Survey-based proxy, not a CMS count |
| [Dual enrollment snapshot](https://www.cms.gov/data-research/research/statistical-resources-dually-eligible-beneficiaries/mmco-statistical-analytic-reports) | CMS Medicare-Medicaid Coordination Office | State, county | Dual enrollees by dual status | No age breakdown |
| [ZIP crosswalk](https://www.huduser.gov/portal/datasets/usps_crosswalk.html) | HUD | ZIP to county, tract | Splitting ZIP lists across counties or tracts | Login required |

## Step-by-step: mapping a PACE expansion

### Step 1: Map current PACE centers and service ZIP codes

1. Download your state's PACE ZIP list. California's DHCS says enrollees [must reside in one of the service areas and ZIP codes listed](https://www.dhcs.ca.gov/individuals/Pages/PACEPlans.aspx).
2. Join ZIP codes to ZCTA boundaries. ZCTAs are ["generalized areal representations"](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html) of ZIP codes, and not every ZIP code has one. See [ZCTA vs. ZIP code](/glossary/zcta-vs-zip-code).
3. Geocode each PACE center address. NPA's [directory](https://www.npaonline.org/find-a-pace-program) lists program names and cities, not service areas.
4. Add CMS enrollment. The [CPSC file](https://www.cms.gov/data-research/statistics-trends-and-reports/medicare-advantagepart-d-contract-and-enrollment-data/monthly-enrollment-contract/plan/state/county/monthly-enrollment-cpsc-2026-07) readme lists "National PACE" among its organization types. It reports enrollees by legal county of residence and blanks counts of 10 or fewer.

[GeoChat AI](https://atlas.geochat.ai) is one free option for this step, with no credit card required. GeoChat Atlas includes PACE layers: PACE sites, PACE coverage by county and PACE service ZIP codes. The platform is new; the current version is GeoChat Atlas (version 2).

### Step 2: Estimate the eligible pool by ZIP code or county

No public file counts people who meet a state's nursing facility level of care. Build a proxy and label it as one.

1. Pull table [B18106](https://api.census.gov/data/2024/acs/acs5/groups/B18106.html) from the ACS 2020–2024 5-year release for ZCTAs or tracts. Self-care difficulty means [difficulty bathing or dressing](https://www.census.gov/topics/health/disability/guidance/data-collection-acs.html).
2. Note its age groups: [5–17, 18–34, 35–64, 65–74, and 75 and over](https://api.census.gov/data/2024/acs/acs5/groups/B18106.html). There is no 55–64 group.
3. Pick one rule for ages 55–64 and write it down:
   - **65 and over only.** Add the 65–74 and 75-and-over groups. This leaves out people 55 to 64.
   - **Apportion 35–64.** Apply the 35–64 self-care rate to the 55–64 population from [B01001](https://api.census.gov/data/2024/acs/acs5/groups/B01001.html), which has 55–59, 60–61 and 62–64 groups. This assumes ages 55 to 64 share the rate of the whole 35–64 group.
   - **Use microdata.** ACS PUMS has [age in single years](https://api.census.gov/data/2024/acs/acs5/pums/variables/AGEP.html) and [self-care difficulty](https://api.census.gov/data/2024/acs/acs5/pums/variables/DDRS.html). Its smallest geography is the PUMA, with [100,000 or more people](https://www.census.gov/content/dam/Census/library/publications/2021/acs/acs_pums_handbook_2021_ch02.pdf). Use it to check regional totals, not to map ZIP codes.
4. Keep the margins of error with each estimate. See [ACS 5-year estimates](/glossary/acs-5-year-estimates).
5. Add CMS dual counts as context, not as the denominator. The [MMCO snapshot](https://www.cms.gov/data-research/research/statistical-resources-dually-eligible-beneficiaries/mmco-statistical-analytic-reports) gives county counts by dual status through September 2025.

GeoChat Atlas also includes estimates of people who may be eligible for PACE, built from ACS self-care difficulty for ages 55 and over. These estimates are proxies: they do not check nursing-home level of care or PACE service areas. Its AI chat lets you drill into ZIP codes and compare regions.

### Step 3: Find gaps outside current service areas

1. Flag ZCTAs with a sizable proxy count but no PACE coverage.
2. Rank them by proxy count and by proxy rate per 1,000 residents 55 and over.
3. Overlay county CPSC enrollment to see where programs already reach. The [CPSC file](https://www.cms.gov/data-research/statistics-trends-and-reports/medicare-advantagepart-d-contract-and-enrollment-data/monthly-enrollment-contract/plan/state/county/monthly-enrollment-cpsc-2026-07) has no field marking which counties are inside a contract's approved service area.
4. Group adjacent gap ZIP codes into candidate areas. A center must sit [in or contiguous to](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-E/part-460/subpart-F) the area it serves.

### Step 4: Test drive times from a candidate center

CMS states it ["does not have a specific travel time requirement"](https://leadingage.org/wp-content/uploads/2026/07/2026-PACE-Rural-Memo_072226.pdf), but states may set their own. California requires a [60-minute one-way drive time](https://www.dhcs.ca.gov/services/ltc/Documents/PL-23-01-Application-Process-DHCS.pdf) from participants' homes to the adult day health center. Applicants must use [commute hours of 6:00 to 8:00 a.m. and 2:00 to 4:00 p.m.](https://www.dhcs.ca.gov/services/ltc/Documents/PL-23-01-Application-Process-DHCS.pdf)

1. Geocode two or three candidate sites.
2. Build drive-time areas at your state's threshold, using traffic for the stated hours. See [drive-time access](/glossary/drive-time-access).
3. Test every ZIP code in the candidate area. Record the point you measured from.
4. Drop ZIP codes that fail. DHCS runs its own review and [requires removal of ZIP codes that miss the drive-time rule](https://www.dhcs.ca.gov/services/ltc/Documents/PL-23-01-Application-Process-DHCS.pdf).
5. Recount the eligible-pool proxy inside the ZIP codes that pass.

### Step 5: Check competing PACE organizations and state approval rules

1. List every existing or pending PACE organization in your candidate ZIP codes. Washington requires new applicants to [identify overlap with an existing or pending PACE organization](https://dshs.wa.gov/sites/default/files/ALTSA/stakeholders/documents/PACE/ALTSA%20PACE%20Service%20Area%20Policy.pdf).
2. Read your state's overlap rule. Washington allows [only a single PACE organization per service area ZIP code](https://dshs.wa.gov/sites/default/files/ALTSA/stakeholders/documents/PACE/ALTSA%20PACE%20Service%20Area%20Policy.pdf). King County is the exception: two are allowed, based on an assumed 10% penetration rate.
3. Expect a response from incumbents. California decides [overlap at the ZIP code level](https://www.dhcs.ca.gov/services/ltc/Documents/PL-23-01-Application-Process-DHCS.pdf), and existing or pending organizations may file a counter-feasibility study within 30 days of notice.
4. Confirm the state is taking applications. California paused [new PACE organization and service area expansion applications](https://www.dhcs.ca.gov/services/ltc/Documents/PL-25-02-Application-Pause.pdf) from November 20, 2025, for at least two years, through November 19, 2027.
5. Build the feasibility study the state asks for. [California](https://www.dhcs.ca.gov/services/ltc/Documents/PL-23-01-Application-Process-DHCS.pdf) and [Washington](https://dshs.wa.gov/sites/default/files/ALTSA/stakeholders/documents/PACE/ALTSA%20PACE%20Service%20Area%20Policy.pdf) both require an estimate of PACE-eligible individuals, the method behind it, competitive factors and projected capture rates.

### Step 6: Document the map for the application

California's application needs a [service area map with the PACE center clearly marked](https://www.dhcs.ca.gov/services/ltc/Documents/PL-23-01-Application-Process-DHCS.pdf), plus boundaries and traffic arteries. Put a methods note under each map:

1. ACS release and table IDs, such as B18106 and B01001 from the 2020–2024 5-year estimates.
2. Your rule for ages 55–64.
3. ZIP list date, ZCTA vintage and any crosswalk quarter.
4. CPSC month and its suppression rule.
5. Drive-time tool, threshold and departure times.

## Limits to state in your analysis

- **ACS cannot identify nursing-home level of care.** The [State administering agency makes that finding](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-E/part-460/subpart-I). Self-care difficulty is a survey answer, not a clinical assessment.
- **ACS dual proxies are not CMS counts.** B27010's category is ["With Medicare and Medicaid/means-tested public coverage"](https://api.census.gov/data/2024/acs/acs5/groups/B27010.html), which is self-reported and broader than Medicaid. Use the [MMCO snapshot](https://www.cms.gov/data-research/research/statistical-resources-dually-eligible-beneficiaries/mmco-statistical-analytic-reports) for administrative county counts.
- **Disability tables leave out institutions.** B18106 covers the [civilian noninstitutionalized population 5 years and over](https://api.census.gov/data/2024/acs/acs5/groups.json), so nursing home residents are not in it.
- **ZIP codes are not ZCTAs.** Service areas use USPS ZIP codes, while ACS uses ZCTAs. PO Box-only ZIP codes are [not in the HUD crosswalk](https://www.huduser.gov/portal/datasets/usps_crosswalk.html), so place them by hand.
- **CMS enrollment is county-level and partly blank.** Blank cells hide counts of 10 or fewer, so summed county totals understate enrollment.
- **State approval decides the final map.** States can set travel rules, overlap limits and application pauses on top of federal rules.

## Common mistakes

- **Calling the proxy "eligible people."** Label it as an estimate of potential need, and name the tables.
- **Hiding the 55–64 step.** B18106 has no 55–64 group, so state how you handled it.
- **Measuring midday drive times.** Use the hours your state specifies.
- **Treating CPSC counties as service areas.** Use the state ZIP list for boundaries.
- **Checking only current competitors.** Washington and California also ask about pending organizations.
- **Assuming a federal drive-time standard.** CMS has none; check your state.

For related methods, see the [CHNA access-gap mapping guide](/chna-access-gap-mapping-guide) and our [California county healthcare access data](/california-county-healthcare-access-2026).
