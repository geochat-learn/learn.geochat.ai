---
title: "How to Map Healthcare Access Gaps for a CHNA"
description: "Map access gaps for a 501(r) CHNA: define the community, layer ACS need over NPPES and HRSA supply, measure ratios and drive time, and document sources."
slug: chna-access-gap-mapping-guide
type: guide
updated: 2026-11-02
faq:
  - q: "How often does a nonprofit hospital have to do a CHNA?"
    a: "Every three years. A hospital facility meets the rule if it conducted a CHNA in the current taxable year or either of the two preceding taxable years, and adopted an implementation strategy on time."
  - q: "Does the IRS require maps in a CHNA report?"
    a: "Maps are not among the report contents listed in Treas. Reg. §1.501(r)-3(b)(6). The report must define the community and explain how it was determined, and maps are a clear way to show that."
  - q: "Can a hospital CHNA use data collected by others, such as Census or health department data?"
    a: "Yes. The report must describe the data and methods used, but for data collected by others it may cite the source material instead of describing how the data were collected."
  - q: "Which geography should a hospital use to map its CHNA community?"
    a: "Patient-origin ZIP codes, converted to ZCTAs, match how hospitals track discharges and how the Census Bureau publishes ACS data. Census tracts show more detail inside a ZIP code, and counties match county-level sources such as County Health Rankings and AHRF. HPSA designations can be whole counties, parts of counties or neighborhoods, so overlay their boundaries."
  - q: "Can GeoChat AI count providers in my hospital's service area?"
    a: "Not on the free tier, which does not answer questions about specific providers, such as provider counts in a given area. Its maps show supply-demand gaps and provider deserts built from public data such as ACS and NPPES."
sources:
  - title: "IRS: Consequences of non-compliance with Section 501(r)"
    url: "https://www.irs.gov/charities-non-profits/consequence-of-non-compliance-with-section-501r"
    accessed: 2026-11-02
  - title: "Community Health Needs Assessment for Charitable Hospital Organizations - Section 501(r)(3)"
    url: "https://www.irs.gov/charities-non-profits/community-health-needs-assessment-for-charitable-hospital-organizations-section-501r3"
    accessed: 2026-11-02
  - title: "26 CFR § 1.501(r)-3 - Community health needs assessments (Cornell LII)"
    url: "https://www.law.cornell.edu/cfr/text/26/1.501(r)-3"
    accessed: 2026-11-02
  - title: "Requirements for 501(c)(3) Hospitals Under the Affordable Care Act - Section 501(r)"
    url: "https://www.irs.gov/charities-non-profits/charitable-organizations/requirements-for-501c3-hospitals-under-the-affordable-care-act-section-501r"
    accessed: 2026-11-02
  - title: "Glossary - Geography Program, U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/geography/about/glossary.html"
    accessed: 2026-11-02
  - title: "HUD USPS ZIP Code Crosswalk Files"
    url: "https://www.huduser.gov/portal/datasets/usps_crosswalk.html"
    accessed: 2026-11-02
  - title: "When to Use 1-year or 5-year Estimates - American Community Survey"
    url: "https://www.census.gov/programs-surveys/acs/guidance/estimates.html"
    accessed: 2026-11-02
  - title: "CDC/ATSDR Social Vulnerability Index"
    url: "https://www.atsdr.cdc.gov/place-health/php/svi/index.html"
    accessed: 2026-11-02
  - title: "Explore Census Data (data.census.gov)"
    url: "https://data.census.gov/"
    accessed: 2026-11-02
  - title: "About PLACES - CDC"
    url: "https://www.cdc.gov/places/about/index.html"
    accessed: 2026-11-02
  - title: "PLACES Current Release Notes - CDC"
    url: "https://www.cdc.gov/places/help/data-notes/"
    accessed: 2026-11-02
  - title: "PLACES Frequently Asked Questions - CDC"
    url: "https://www.cdc.gov/places/faqs/index.html"
    accessed: 2026-11-02
  - title: "Data Dissemination (NPPES) - CMS"
    url: "https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination"
    accessed: 2026-11-02
  - title: "Health Care Provider Taxonomy - NUCC"
    url: "https://www.nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40"
    accessed: 2026-11-02
  - title: "Shortage Areas - HRSA Data Warehouse"
    url: "https://data.hrsa.gov/topics/health-workforce/shortage-areas"
    accessed: 2026-11-02
  - title: "Scoring Shortage Designations - HRSA Bureau of Health Workforce"
    url: "https://bhw.hrsa.gov/workforce-shortage-areas/shortage-designation/scoring"
    accessed: 2026-11-02
  - title: "42 CFR Appendix A to Part 5 - Criteria for Designation of Areas Having Shortages of Primary Medical Care Professional(s) (Cornell LII)"
    url: "https://www.law.cornell.edu/cfr/text/42/appendix-A_to_part_5"
    accessed: 2026-11-02
  - title: "Data Downloads - HRSA Data Warehouse"
    url: "https://data.hrsa.gov/data/download"
    accessed: 2026-11-02
  - title: "Primary Care Physicians - County Health Rankings & Roadmaps"
    url: "https://www.countyhealthrankings.org/health-data/health-factors/clinical-care/access-to-care/primary-care-physicians"
    accessed: 2026-11-02
  - title: "QGIS"
    url: "https://qgis.org/"
    accessed: 2026-11-02
  - title: "openrouteservice Plans"
    url: "https://openrouteservice.org/plans/"
    accessed: 2026-11-02
  - title: "Service area analysis layer - ArcGIS Pro documentation"
    url: "https://doc.esri.com/en/arcgis-pro/latest/help/analysis/networks/service-area-analysis-layer.html"
    accessed: 2026-11-02
  - title: "Measures of Spatial Accessibility to Health Care in a GIS Environment (Luo and Wang, 2003) - TRID record"
    url: "https://trid.trb.org/View/688048"
    accessed: 2026-11-02
---

To map access gaps for a CHNA, define your community, layer need over provider supply, measure access, and document every source. The IRS rules below decide what your maps must show and what your report must explain.

## What the IRS requires of a CHNA

Section 501(r)(3) requires each hospital facility to conduct a [community health needs assessment every three years](https://www.irs.gov/charities-non-profits/community-health-needs-assessment-for-charitable-hospital-organizations-section-501r3). A facility complies only if it conducted one in the current or either of the two preceding taxable years and adopted an implementation strategy for it. CHNA failures trigger a [$50,000 excise tax per noncompliant facility](https://www.irs.gov/charities-non-profits/consequence-of-non-compliance-with-section-501r), and failing Section 501(r) [may result in revocation of tax-exempt status](https://www.irs.gov/charities-non-profits/consequence-of-non-compliance-with-section-501r).

An authorized body must adopt the implementation strategy by the [15th day of the fifth month after the CHNA's taxable year ends](https://www.law.cornell.edu/cfr/text/26/1.501%28r%29-3). Failing the Section 501(r) requirements [may result in revocation of tax-exempt status](https://www.irs.gov/charities-non-profits/charitable-organizations/requirements-for-501c3-hospitals-under-the-affordable-care-act-section-501r). For background, see the [CHNA glossary entry](/glossary/chna).

The detailed rules sit in [Treas. Reg. §1.501(r)-3](https://www.law.cornell.edu/cfr/text/26/1.501%28r%29-3). This table maps each rule to mapping work.

| Rule in §1.501(r)-3 | What it requires | What it means for your maps |
|---|---|---|
| (b)(3) Community served | You may define the community by geographic area, target populations, and principal functions. You may not exclude medically underserved, low-income, or minority residents of the areas you draw patients from. The exception is groups outside your target population or principal functions. | Draw the boundary from patient origin, then check that no low-income or minority neighborhoods were cut out. |
| (b)(4) Assessing needs | Identify, prioritize, and find resources for significant health needs. Needs include "the need to address financial and other barriers to accessing care." | Access gaps count as health needs in their own right. |
| (b)(5) Community input | Get input from at least one governmental public health department or a State Office of Rural Health. Also include members or representatives of medically underserved, low-income, and minority populations, plus written comments on the last CHNA and implementation strategy. | Review draft maps with these groups before you finalize priorities. |
| (b)(6) Written report | Define the community and how it was determined. Describe methods and input. List prioritized needs, criteria, and available resources. Evaluate actions taken since the last CHNA. | Every map needs a source note and a methods note. |
| (b)(7) Widely available | Post the report on a website at least until two later CHNA reports are posted, and make a paper copy available for public inspection, without charge, at the facility. | Save a static copy of each map with the report, because live dashboards change. |
| (c) Implementation strategy | For each significant need, describe how the facility will address it or explain why it will not. | Use the gap maps to show where new actions will go. |

The regulation defines medically underserved populations to include people at risk of inadequate care "due to geographic, language, financial, or other barriers" ([§1.501(r)-3(b)(5)](https://www.law.cornell.edu/cfr/text/26/1.501%28r%29-3)). Travel time, language, and insurance maps speak directly to that definition.

## Step-by-step: mapping access gaps for your CHNA

### Step 1: Define the service area

1. Export inpatient discharges by patient ZIP code for the most recent full year. Add emergency and outpatient visits if your system can link them.
2. Rank ZIP codes by share of discharges and pick a cumulative cutoff. Record the cutoff, because the report must say [how the community was determined](https://www.law.cornell.edu/cfr/text/26/1.501%28r%29-3).
3. Convert ZIP codes to ZCTAs before joining census data. ZCTAs are "approximate area representations" of USPS ZIP Code service routes, built from whole census blocks ([Census Bureau](https://www.census.gov/programs-surveys/geography/about/glossary.html)). See [ZCTA vs. ZIP code](/glossary/zcta-vs-zip-code).
4. Use the [HUD-USPS ZIP Code Crosswalk Files](https://www.huduser.gov/portal/datasets/usps_crosswalk.html) to split ZIP codes across census tracts or counties. HUD updates them quarterly, offers residential and total address ratios, and requires a HUD account login to download.
5. Overlay low-income and minority populations on the draft boundary. Expand it if the cutoff drops neighborhoods the rule says you may not exclude.

ZIP codes that serve only PO Boxes do not appear in the [HUD crosswalk](https://www.huduser.gov/portal/datasets/usps_crosswalk.html), so assign them by hand. Hospitals that collaborate on one CHNA may share substantively identical report sections [where the facts support it](https://www.law.cornell.edu/cfr/text/26/1.501%28r%29-3).

### Step 2: Pull population and social-need data

Use American Community Survey (ACS) 5-year estimates for ZCTAs and tracts. ACS 1-year estimates cover only [areas with 65,000 or more people](https://www.census.gov/programs-surveys/acs/guidance/estimates.html), while 5-year estimates cover all areas. See [ACS 5-year estimates](/glossary/acs-5-year-estimates).

Download tables from [data.census.gov](https://data.census.gov/) for age, poverty, health insurance, limited English, disability, and vehicle access. These match the financial, language, and geographic barriers named in the regulation.

Two free indexes save time:

- The [CDC/ATSDR Social Vulnerability Index](https://www.atsdr.cdc.gov/place-health/php/svi/index.html) ranks census tracts using 16 ACS 5-year variables grouped into four themes.
- [CDC PLACES](https://www.cdc.gov/places/about/index.html) gives model-based estimates for 40 health measures by county, place, census tract, and ZCTA.

The [December 2025 PLACES release](https://www.cdc.gov/places/help/data-notes/) bases 35 measures on 2023 BRFSS data. Its 2023-based estimates were not available for Kentucky or Pennsylvania.

### Step 3: Map provider supply

CMS publishes the National Plan and Provider Enumeration System (NPPES) as a [free Full Replacement Monthly NPI File, plus weekly incremental files and a monthly deactivation file](https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination). The data are as reported to NPPES by providers or people acting for them.

1. Filter NPPES records by Health Care Provider Taxonomy code, a code set [maintained by the National Uniform Claim Committee](https://www.nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40). See [NPI taxonomy codes](/glossary/npi-taxonomy-codes).
2. Drop NPIs listed in the deactivation file.
3. Geocode practice location addresses, not mailing addresses.
4. Download HRSA's [Shortage Areas file](https://data.hrsa.gov/topics/health-workforce/shortage-areas) in XLSX, CSV, or SHP format. It covers primary care, dental, and mental health HPSAs, plus Medically Underserved Areas and Populations.
5. Add HRSA's [Health Center Program Service Delivery and Look-Alike Sites](https://data.hrsa.gov/data/download) to list resources available to address needs, a required report element.

HRSA's [batch tool checks up to 200 addresses](https://data.hrsa.gov/topics/health-workforce/shortage-areas) for shortage-area status at once. See [HPSA](/glossary/hpsa) and [MUA/MUP](/glossary/mua-mup).

Label NPPES counts as headcounts, because HPSA criteria use [full-time-equivalent ratios](https://www.law.cornell.edu/cfr/text/42/appendix-A_to_part_5). The two are not directly comparable. NPPES depends on providers updating their records, so spot-check counts against local directories.

[GeoChat AI](https://atlas.geochat.ai) is one option for a first pass, with a free tier and no credit card required. It maps supply-demand gaps and provider deserts from public data such as ACS and NPPES. Its AI chat lets you drill into ZIP codes.

The free tier does not answer questions about specific providers, such as provider counts in an area, and the platform is new: the current version is GeoChat Atlas (version 2).

### Step 4: Measure access

| Measure | What it shows | How to compute it free | Watch for |
|---|---|---|---|
| Provider-to-population ratio | Supply per resident in each area | NPPES providers by area divided by ACS population | Residents cross area borders for care |
| Travel time to nearest provider | Geographic barriers by neighborhood | QGIS or openrouteservice isochrones from geocoded sites | Car-based times understate barriers for households without vehicles |
| Two-step floating catchment area (2SFCA) | Supply and demand that cross boundaries | Custom GIS workflow | Results shift with the travel-time threshold you choose |
| Shortage designation overlay | Federally designated shortage areas | HRSA Shortage Areas file | Designation boundaries may not match your service area |

For ratio benchmarks, a geographic primary care HPSA needs a population to FTE primary care physician ratio of [at least 3,500:1](https://www.law.cornell.edu/cfr/text/42/appendix-A_to_part_5). Areas between 3,000:1 and 3,500:1 also qualify with unusually high needs or insufficient provider capacity. See [provider-to-population ratio](/glossary/provider-to-population-ratio).

[County Health Rankings](https://www.countyhealthrankings.org/health-data/health-factors/clinical-care/access-to-care/primary-care-physicians) publishes a county primary care physician ratio from AHRF and AMA data. It excludes nurse practitioners and physician assistants, so add those taxonomies from NPPES if they deliver primary care locally.

HPSA rules let contiguous counties form one rational service area if their population centers are [within 30 minutes travel time](https://www.law.cornell.edu/cfr/text/42/appendix-A_to_part_5) of each other. See [drive-time access](/glossary/drive-time-access).

Tool options for travel time:

- [QGIS](https://qgis.org/) is free, open source under GNU GPLv2+, and runs on Windows, Mac, and Linux.
- [openrouteservice](https://openrouteservice.org/plans/) has a free Standard plan with 500 isochrone requests per day and 20 per minute, as of November 2026.
- [ArcGIS Pro service area analysis](https://doc.esri.com/en/arcgis-pro/latest/help/analysis/networks/service-area-analysis-layer.html) builds polygons reachable within a time or distance cutoff. Solving with ArcGIS Online as the network source consumes credits, so it suits teams that already hold licenses.

[Luo and Wang (2003)](https://trid.trb.org/View/688048) describe the floating catchment approach, which defines physician service areas by a threshold travel time. Test more than one threshold and report the one you use.

### Step 5: Find priority populations

1. Join SVI, travel time, ratio, and HPSA layers to the same geography.
2. Flag tracts or ZCTAs that rank high on social vulnerability and long travel time, or that sit in a HPSA.
3. Check those areas for uninsured, limited-English, and no-vehicle households.
4. Rank needs with stated criteria.

The regulation lets you prioritize using [burden, scope, severity, or urgency](https://www.law.cornell.edu/cfr/text/26/1.501%28r%29-3). It also allows feasibility and effectiveness of interventions, related health disparities, and the importance the community places on the need.

### Step 6: Combine maps with community input

Bring draft maps to the [required input groups](https://www.law.cornell.edu/cfr/text/26/1.501%28r%29-3). These are a governmental public health department or State Office of Rural Health, and representatives of medically underserved, low-income, and minority populations. Ask them to mark closed clinics, missing bus routes, and places people actually go for care.

Record each change and its reason. The report must describe [how you solicited and took input into account](https://www.law.cornell.edu/cfr/text/26/1.501%28r%29-3).

Your local health department may already map the same indicators for its own assessment. See [community health assessment mapping for health departments](/community-health-assessment-mapping-guide) to align geographies.

If you lack staff for this step, GeoChat AI offers paid expert services, including community interviews and expert review of AI findings. You can [book a call](https://calendly.com/v-wong-geochat/30min) to discuss scope.

### Step 7: Document data sources and limitations

The report must describe the data used and how they were collected and analyzed. For data collected by others, it [may cite the source material](https://www.law.cornell.edu/cfr/text/26/1.501%28r%29-3) rather than describe collection methods.

Add a methods note under each map with:

1. Dataset and vintage, such as "ACS 2020-2024 5-year estimates."
2. Geography and boundary vintage, such as 2020 ZCTAs.
3. Crosswalk file, quarter, and ratio type.
4. NPPES file date and taxonomy codes included.
5. Travel mode, time cutoff, and routing tool.
6. Known limits: self-reported NPPES data, model-based PLACES estimates, and ACS margins of error.

Keep the same geographies next cycle. The next report must [evaluate the impact of actions](https://www.law.cornell.edu/cfr/text/26/1.501%28r%29-3) taken since this CHNA, which is easier with matching boundaries. Our [methods page](/methods) shows how we document sources.

## Common mistakes

- **Mapping raw counts.** Large ZIP codes look worse on counts alone. Map rates, ratios, or travel times.
- **Joining ZIP data to ZCTA data directly.** Use a crosswalk and note which one.
- **Using ACS 1-year data for small areas.** It exists only for [areas of 65,000 or more](https://www.census.gov/programs-surveys/acs/guidance/estimates.html).
- **Treating NPPES records as full-time providers.** Label provider counts as headcounts.
- **Using PLACES to judge past actions.** CDC says its estimates [should not be used to evaluate local programs](https://www.cdc.gov/places/faqs/index.html) or track local change.
- **Trimming low-income areas from the boundary.** The rule bars excluding them if they live in areas you draw patients from.
- **Bringing in the public health department last.** Its input is one of the required options, and early review catches errors in your maps.

For a wider list of free mapping options, see [free tools for healthcare access mapping](/free-tools-healthcare-access-mapping).
