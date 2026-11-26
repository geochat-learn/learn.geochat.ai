---
title: "How to Analyze Unmet Need for a New FQHC Site"
description: "Score the proposed service area with HRSA's Unmet Need Score, check health center penetration by ZCTA, then map nearby sites, HPSAs and MUA/Ps."
slug: new-fqhc-site-unmet-need-analysis
type: guide
updated: 2026-11-19
faq:
  - q: "What is HRSA's Unmet Need Score (UNS)?"
    a: "The UNS is HRSA's 0–100 score of unmet need for primary and preventive care, calculated for each ZIP Code Tabulation Area (ZCTA). It is a weighted sum of percentile ranks on 25 measures for the 50 states and DC, and larger values mean higher need."
  - q: "Which measures carry the most weight in the Unmet Need Score?"
    a: "Health center penetration carries 25%, and the share of people below 200% of the federal poverty level and the share uninsured carry 10% each. Together these three core measures make up 45% of the score."
  - q: "How do I get a UNS for a service area with several ZIP codes?"
    a: "Select the ZIP codes in HRSA's Unmet Need Score Map Tool, which converts them to ZCTAs and shows the service area score. HRSA computes it as the population-weighted average of each ZCTA's UNS."
  - q: "Does the GeoCare Navigator show the Unmet Need Score?"
    a: "No. The GeoCare Navigator user guide says the tool does not currently include the UNS and points to the separate Unmet Need Score Map Tool. Use the Navigator for penetration, low-income residents not served and nearby sites."
  - q: "Can GeoChat AI help with a new site analysis?"
    a: "As of November 2026, GeoChat AI maps supply-demand gaps by county, ZIP code and census tract. Its HRSA layers include HPSAs, MUAs, health center sites and UDS 2025. For any Unmet Need Score you report to HRSA, use HRSA's own Unmet Need Score Map Tool."
sources:
  - title: "Unmet Need Score Map Tool, HRSA Data Warehouse"
    url: "https://data.hrsa.gov/topics/health-centers/sanam"
    accessed: 2026-11-19
  - title: "Unmet Need Score (UNS) User Guide, HRSA (March 2026)"
    url: "https://data.hrsa.gov/Content/Documents/topics/UNS_User_Guide.pdf"
    accessed: 2026-11-19
  - title: "Data Sources Used in the Unmet Need Score (UNS), HRSA (March 2026)"
    url: "https://data.hrsa.gov/Content/Documents/topics/UNS_Data_Sources.pdf"
    accessed: 2026-11-19
  - title: "UNS Map Tool Quick Start Guide, HRSA"
    url: "https://data.hrsa.gov/Content/Documents/topics/UNS_Map_Tool_Quick_Start_Guide.pdf"
    accessed: 2026-11-19
  - title: "Full Unmet Need Score File (XLSX), HRSA"
    url: "https://data.hrsa.gov/Content/Documents/topics/Full_Unmet_Need_Score_File.xlsx"
    accessed: 2026-11-19
  - title: "Health Center Program GeoCare Navigator: Resources, HRSA"
    url: "https://data.hrsa.gov/GeoCareNavigator/Resources"
    accessed: 2026-11-19
  - title: "Health Center Program GeoCare Navigator User Guide, HRSA"
    url: "https://data.hrsa.gov/DataDownload/GeoCareNavigator/HCP-GeoCareNavigator-User-Guide.pdf"
    accessed: 2026-11-19
  - title: "Health Center Program GeoCare Navigator: About the Data, Version 3.0 (2026), HRSA"
    url: "https://data.hrsa.gov/DataDownload/GeoCareNavigator/AboutTheData.pdf"
    accessed: 2026-11-19
  - title: "Health Center Program Compliance Manual, Chapter 3: Needs Assessment, HRSA"
    url: "https://bphc.hrsa.gov/compliance/compliance-manual/chapter3"
    accessed: 2026-11-19
  - title: "Service Area Competition (SAC) Frequently Asked Questions, HRSA"
    url: "https://bphc.hrsa.gov/funding/funding-opportunities/service-area-competition/faq"
    accessed: 2026-11-19
  - title: "Census Data API: S1701 Poverty Status in the Past 12 Months (2024 ACS 5-year)"
    url: "https://api.census.gov/data/2024/acs/acs5/subject/groups/S1701.html"
    accessed: 2026-11-19
  - title: "Census Data API: S2701 Selected Characteristics of Health Insurance Coverage in the United States (2024 ACS 5-year)"
    url: "https://api.census.gov/data/2024/acs/acs5/subject/groups/S2701.html"
    accessed: 2026-11-19
  - title: "HPSA Find, HRSA Data Warehouse"
    url: "https://data.hrsa.gov/topics/health-workforce/shortage-areas/hpsa-find"
    accessed: 2026-11-19
  - title: "MUA Find, HRSA Data Warehouse"
    url: "https://data.hrsa.gov/tools/shortage-area/mua-find"
    accessed: 2026-11-19
---

To analyze unmet need for a new FQHC site, score the proposed service area with HRSA's [Unmet Need Score Map Tool](https://data.hrsa.gov/topics/health-centers/sanam). Then check health center penetration in each ZIP code and map the sites and shortage designations around it. HRSA [says the tool](https://data.hrsa.gov/topics/health-centers/sanam) "can help determine if an area needs a new health center site."

## The three HRSA sources to use

| Source | What it gives you | Geography |
|---|---|---|
| [Unmet Need Score Map Tool](https://data.hrsa.gov/topics/health-centers/sanam) | A 0–100 need score for each ZCTA and for a proposed service area | ZIP Code Tabulation Area (ZCTA) |
| [Health Center Program GeoCare Navigator](https://data.hrsa.gov/GeoCareNavigator/Resources) | Health center penetration, low-income residents not served, existing sites, hospitals and rural health clinics | ZCTA |
| [HPSA Find](https://data.hrsa.gov/topics/health-workforce/shortage-areas/hpsa-find) and [MUA Find](https://data.hrsa.gov/tools/shortage-area/mua-find) | Shortage and medically underserved designations | Varies by designation |

The GeoCare Navigator replaced UDS Mapper. Its [user guide](https://data.hrsa.gov/DataDownload/GeoCareNavigator/HCP-GeoCareNavigator-User-Guide.pdf) says UDS Mapper would sunset on March 26, 2024. The same guide says the Navigator does not currently include the Unmet Need Score, so you need both tools. See [GeoChat AI vs UDS Mapper](/geochat-ai-vs-uds-mapper) for more on the change.

## What the Unmet Need Score measures

HRSA's [UNS User Guide](https://data.hrsa.gov/Content/Documents/topics/UNS_User_Guide.pdf) (March 2026) calls the score a "weighted sum of standardized measure values." It measures unmet need for primary and preventive care. The measures fall into four classes:

| Class | Weight | Measures |
|---|---|---|
| Core | 45% | Health center penetration (25%), below 200% of the federal poverty level (10%), uninsured (10%) |
| Access | 24% | Broadband, cervical cancer screening, dental visit, limited access to healthy foods, linguistic isolation, no vehicle, preterm births, preventable hospital stays (3% each) |
| Socioeconomic status | 15% | Associate degree or higher, housing stress, no high school diploma, single-parent household, unemployment (3% each) |
| Health status | 16% | All-cause mortality, drug poisoning mortality, chlamydia, obesity, smoking (2% each); asthma, diabetes, poor mental health, poor physical health (1.5% each) |

Health center penetration is the [ratio of people served by a health center](https://data.hrsa.gov/Content/Documents/topics/UNS_User_Guide.pdf) to people below 200% of the poverty level. It is capped at 1, and a smaller value means higher need.

### How the score is calculated

The [user guide's Appendix A](https://data.hrsa.gov/Content/Documents/topics/UNS_User_Guide.pdf) sets out the steps:

1. Each measure value is turned into a percentile rank against all other ZCTAs, so larger always means higher need.
2. Each percentile rank is multiplied by the measure's weight, and the results are summed.
3. The sums are rescaled to 0–100, using the 0.5th and 99.5th percentiles of all ZCTA sums as the ends.
4. A service area score is the population-weighted sum of its ZCTA scores.

A ZCTA with many residents moves the service area score more than a small one. That means adding a large, low-need ZIP code can pull a high-need area's score down.

### How current the data are

HRSA's [data sources supplement](https://data.hrsa.gov/Content/Documents/topics/UNS_Data_Sources.pdf) says the states' scores use data current as of September 13, 2025. Its GeoCare Navigator data date from November 6, 2025. Most ACS measures come from 2019–2023 5-year estimates. Health center patient counts come from 2024 UDS data. Several measures, such as chlamydia, drug poisoning mortality and preterm births, come from county data, not ZCTA data.

So the UNS lags the newest releases. The GeoCare Navigator's [About the Data](https://data.hrsa.gov/DataDownload/GeoCareNavigator/AboutTheData.pdf) (Version 3.0, 2026) already uses ACS 2020–2024 and UDS 2025. Expect the two tools to differ slightly for the same ZCTA.

## Step-by-step: unmet need analysis for a new site

1. **Define the proposed service area as ZIP codes.** HRSA's [Compliance Manual, Chapter 3](https://bphc.hrsa.gov/compliance/compliance-manual/chapter3) ties a service area to the ZIP codes where current or proposed patients live. List the ZIP codes your new site would draw from.
2. **Score the area in the UNS Map Tool.** Add ZIP codes one at a time, or pick a state and county to load a list. The [quick start guide](https://data.hrsa.gov/Content/Documents/topics/UNS_Map_Tool_Quick_Start_Guide.pdf) warns that a county list can include ZIP codes outside the county, so review it.
3. **Export the Service Area Details table.** The [quick start guide](https://data.hrsa.gov/Content/Documents/topics/UNS_Map_Tool_Quick_Start_Guide.pdf) says the table can be exported as XLSX. A browser refresh resets the map, so export before you leave.
4. **Find the measures that drive the score.** The table shows each measure as a value and a percentile, and a higher percentile means higher need. Multiply each percentile by its weight to see which measures push the score up.
5. **Compare with nearby areas.** HRSA's [full UNS file](https://data.hrsa.gov/Content/Documents/topics/Full_Unmet_Need_Score_File.xlsx) lists every ZCTA's score, population and measures. Rank alternative locations or neighboring ZIP codes against your proposed area.
6. **Check penetration and people not served in the GeoCare Navigator.** "HCP: Low Income Not Served by Health Centers" [subtracts health center patients](https://data.hrsa.gov/DataDownload/GeoCareNavigator/AboutTheData.pdf) in a ZCTA from its low-income residents. HRSA says this is "only an estimate," because UDS does not report income by ZIP code.
7. **Map existing capacity.** For New Access Point applications, the Navigator's [default map layers](https://data.hrsa.gov/DataDownload/GeoCareNavigator/HCP-GeoCareNavigator-User-Guide.pdf) include health center and look-alike sites, hospitals, rural health clinics and MUA/Ps. Its data table shows each ZCTA's dominant health center.
8. **Add shortage designations.** Use [HPSA Find](https://data.hrsa.gov/topics/health-workforce/shortage-areas/hpsa-find) and [MUA Find](https://data.hrsa.gov/tools/shortage-area/mua-find) to list designations that overlap the area. See the [HPSA](/glossary/hpsa) and [MUA/MUP](/glossary/mua-mup) glossary entries for how each is defined.
9. **Rebuild the core counts from the ACS if you need margins of error.** Table S1701 line [S1701_C01_042E](https://api.census.gov/data/2024/acs/acs5/subject/groups/S1701.html) counts people below 200% of poverty. Table S2701 line [S2701_C04_001E](https://api.census.gov/data/2024/acs/acs5/subject/groups/S2701.html) counts the uninsured. See [how to estimate the uninsured population by ZIP code](/uninsured-population-by-zip-code) for adding ZCTAs and their margins of error.
10. **Write up need, not only the score.** HRSA's [Chapter 3](https://bphc.hrsa.gov/compliance/compliance-manual/chapter3) expects a needs assessment to address access factors such as geography, transportation, income and education. It also covers leading causes of illness and death, and health disparities.

## Market analysis: questions the maps should answer

A market analysis for a new community health center adds competition and reach to need. Use the steps above to answer these questions:

- **Who already serves the area?** Penetration and the dominant health center by ZCTA show whether patients already use another health center.
- **How many low-income residents are not served?** This is the Navigator's not-served count, read with HRSA's caution that it is an estimate.
- **Where are the gaps within the area?** Map each ZCTA's score, not only the total, to place the site near the highest-need ZIP codes.
- **What other safety-net capacity exists?** Hospitals and rural health clinics on the Navigator map are part of the landscape a reviewer will see.

If you apply in a Service Area Competition as a new or competing supplement applicant, a 75% rule applies. The [SAC FAQ](https://bphc.hrsa.gov/funding/funding-opportunities/service-area-competition/faq) says "you must propose to serve at least 75% of the current health center's patients within the service area." It also says Form 5B uses ZIP codes, not ZCTAs.

## Where GeoChat AI fits

GeoChat AI is an AI-powered mapping platform for community health assessments, community needs assessments and healthcare supply-demand studies. It is not affiliated with HRSA or the GeoCare Navigator. It is also not affiliated with GeoChat, the MBZUAI remote-sensing model, or GeoChat, the InSTEDD messaging tool.

As of November 2026, [GeoChat AI](https://app.geochat.ai) has more than 100 layers. They include HRSA HPSAs, MUAs, health center sites and UDS 2025, plus CDC PLACES, CDC SVI and CMS facility layers. It maps supply-demand gaps at county, ZIP code (ZCTA) and census tract level. Its plain-language AI chat can drill into ZIP codes and compare regions.

Limits to keep in mind:

- For any Unmet Need Score you report to HRSA, use HRSA's own [Unmet Need Score Map Tool](https://data.hrsa.gov/topics/health-centers/sanam).
- The AI chat has no web search. It is instructed to report only figures from its own queries of the platform's datasets. That is an instruction to the model, not a guarantee.
- Provider counts come from NPPES and are registrations, not full-time clinicians.
- The platform is new, and its sources are rebuilt by hand after each release. Check the [methods page](/methods) for data versions.

As of November 2026, GeoChat AI has a free plan with no credit card required.

## Common mistakes

- **Treating ZIP codes and ZCTAs as the same.** The UNS tool [converts ZIP codes to ZCTAs](https://data.hrsa.gov/Content/Documents/topics/UNS_Map_Tool_Quick_Start_Guide.pdf), but Form 5B [uses ZIP codes](https://bphc.hrsa.gov/funding/funding-opportunities/service-area-competition/faq). See [ZCTA vs ZIP code](/glossary/zcta-vs-zip-code).
- **Padding the service area.** Because the score is [population-weighted](https://data.hrsa.gov/Content/Documents/topics/UNS_User_Guide.pdf), adding large, lower-need ZIP codes lowers it. Include the ZIP codes your patients would really come from.
- **Reading penetration as exact.** HRSA [calls penetration an estimate](https://data.hrsa.gov/DataDownload/GeoCareNavigator/AboutTheData.pdf), since it divides all patients by low-income residents.
- **Mixing data years without saying so.** The UNS uses [mostly 2019–2023 ACS and 2024 UDS](https://data.hrsa.gov/Content/Documents/topics/UNS_Data_Sources.pdf); the Navigator uses [2020–2024 ACS and 2025 UDS](https://data.hrsa.gov/DataDownload/GeoCareNavigator/AboutTheData.pdf). Label each figure with its source and years.
- **Ignoring county-level measures.** Some UNS measures [come from county data](https://data.hrsa.gov/Content/Documents/topics/UNS_Data_Sources.pdf), so they vary little or not at all between ZIP codes in one county.
