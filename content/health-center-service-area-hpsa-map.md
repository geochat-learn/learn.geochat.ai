---
title: "How to Map a Health Center Service Area Against HPSAs"
description: "List your Form 5B ZIP codes, convert them to ZCTAs, download HRSA HPSA boundaries by discipline, then overlay and report the HPSAs that touch your area."
slug: health-center-service-area-hpsa-map
type: guide
updated: 2026-11-05
faq:
  - q: "How do I find out which HPSAs overlap our health center's service area?"
    a: "Convert your Form 5B ZIP codes to ZCTAs, then overlay them on HRSA's primary care, dental and mental health HPSA layers. The GeoCare Navigator shows [HPSA layers by discipline](https://data.hrsa.gov/DataDownload/GeoCareNavigator/AboutTheData.pdf), and HRSA's [Data Downloads](https://data.hrsa.gov/data/download) page offers the same designations as CSV files and shapefiles."
  - q: "Which ZIP codes make up a health center's service area?"
    a: "The ZIP codes on Form 5B: Service Sites. HRSA's Compliance Manual says they should be consistent with UDS patient origin. Its example includes [the ZIP codes where at least 75 percent of current patients reside](https://bphc.hrsa.gov/compliance/compliance-manual/chapter3)."
  - q: "Is our FQHC already an HPSA?"
    a: "Yes. HRSA lists FQHCs and FQHC Look-Alikes as [automatic facility HPSAs](https://bhw.hrsa.gov/workforce-shortage-areas/shortage-designation). A facility HPSA describes your sites, so map geographic and population HPSAs separately to describe your service area."
  - q: "Do HPSAs marked 'proposed for withdrawal' still count?"
    a: "Yes, for now. HRSA says these communities [continue to be recognized as HPSAs](https://www.hrsa.gov/about/news/press-releases/extended-timeline-health-professional-shortage-area-designations) until final withdrawal decisions are made through a future Federal Register notice. The next annual notice is scheduled on or before July 1, 2027. Report them separately."
  - q: "Do I need GIS software to do this?"
    a: "Not for a map. The GeoCare Navigator [does not require a login](https://data.hrsa.gov/DataDownload/GeoCareNavigator/HCP-GeoCareNavigator-User-Guide.pdf) and accepts a pasted or uploaded ZIP code list. A population count inside HPSAs needs the HRSA files and Census relationship files, usually in a GIS or spreadsheet."
sources:
  - title: "HRSA Health Center Program Compliance Manual, Chapter 3: Needs Assessment"
    url: "https://bphc.hrsa.gov/compliance/compliance-manual/chapter3"
    accessed: 2026-11-05
  - title: "HRSA Site Visit Protocol: Needs Assessment"
    url: "https://bphc.hrsa.gov/compliance/site-visits/site-visit-protocol/needs-assessment"
    accessed: 2026-11-05
  - title: "HRSA: Service Area Competition Frequently Asked Questions"
    url: "https://bphc.hrsa.gov/funding/funding-opportunities/service-area-competition/faq"
    accessed: 2026-11-05
  - title: "HRSA UDS: Patients by ZIP Code (updated June 2025)"
    url: "https://bphc.hrsa.gov/sites/default/files/bphc/data-reporting/zip-code-fact-sheet-2025.pdf"
    accessed: 2026-11-05
  - title: "HRSA: Health Center Program GeoCare Navigator User Guide (V1.0)"
    url: "https://data.hrsa.gov/DataDownload/GeoCareNavigator/HCP-GeoCareNavigator-User-Guide.pdf"
    accessed: 2026-11-05
  - title: "HRSA: GeoCare Navigator About the Data (Version 3.0, 2026)"
    url: "https://data.hrsa.gov/DataDownload/GeoCareNavigator/AboutTheData.pdf"
    accessed: 2026-11-05
  - title: "HRSA: Health Center Program GeoCare Navigator Resources"
    url: "https://data.hrsa.gov/GeoCareNavigator/Resources"
    accessed: 2026-11-05
  - title: "HRSA: 2025 ZIP Code to ZCTA Crosswalk (XLSX)"
    url: "https://data.hrsa.gov/DataDownload/GeoCareNavigator/ZIPCodetoZCTACrosswalk2025UDS.xlsx"
    accessed: 2026-11-05
  - title: "HRSA Data Warehouse: Data Downloads"
    url: "https://data.hrsa.gov/data/download"
    accessed: 2026-11-05
  - title: "HRSA Data Warehouse: HPSA data mart metadata (XLSX)"
    url: "https://data.hrsa.gov/DataDownload/DD_Files/HPSA_DATAMART_METADATA.XLSX"
    accessed: 2026-11-05
  - title: "HRSA Data Warehouse: HPSA Find"
    url: "https://data.hrsa.gov/topics/health-workforce/shortage-areas/hpsa-find"
    accessed: 2026-11-05
  - title: "HRSA Data Warehouse: Find Shortage Areas by Address"
    url: "https://data.hrsa.gov/topics/health-workforce/shortage-areas/by-address"
    accessed: 2026-11-05
  - title: "HRSA Bureau of Health Workforce: What Is Shortage Designation?"
    url: "https://bhw.hrsa.gov/workforce-shortage-areas/shortage-designation"
    accessed: 2026-11-05
  - title: "HRSA Bureau of Health Workforce: Scoring Shortage Designations"
    url: "https://bhw.hrsa.gov/workforce-shortage-areas/shortage-designation/scoring"
    accessed: 2026-11-05
  - title: "HRSA: HRSA Extends Timeline for Review of Certain HPSA Designations (July 1, 2026)"
    url: "https://www.hrsa.gov/about/news/press-releases/extended-timeline-health-professional-shortage-area-designations"
    accessed: 2026-11-05
  - title: "NHSC: Understanding Loan Repayment Funding Priorities"
    url: "https://nhsc.hrsa.gov/loan-repayment/funding-priorities"
    accessed: 2026-11-05
  - title: "Cornell LII: 42 CFR Appendix A to Part 5"
    url: "https://www.law.cornell.edu/cfr/text/42/appendix-A_to_part_5"
    accessed: 2026-11-05
  - title: "U.S. Census Bureau: 2020 Relationship Files"
    url: "https://www.census.gov/geographies/reference-files/time-series/geo/relationship-files.2020.html"
    accessed: 2026-11-05
  - title: "U.S. Census Bureau: 2020 ZCTA Relationship File Record Layouts"
    url: "https://www.census.gov/programs-surveys/geography/technical-documentation/records-layout/2020-zcta-record-layout.html"
    accessed: 2026-11-05
---

To map your service area against HPSAs, convert your Form 5B ZIP codes to ZCTAs and overlay them on HRSA's HPSA boundaries by discipline. Then list every HPSA that touches the area, with its ID, type, score and status.

The quickest route is HRSA's Health Center Program GeoCare Navigator, the tool that replaced UDS Mapper. It has [primary care, mental health and dental HPSA layers](https://data.hrsa.gov/DataDownload/GeoCareNavigator/AboutTheData.pdf) and needs no GIS staff. For a written count of residents inside HPSAs, add HRSA's downloadable HPSA files and Census relationship files.

## What counts as your service area

HRSA defines the service area by ZIP code. The [Compliance Manual](https://bphc.hrsa.gov/compliance/compliance-manual/chapter3) says a health center "identifies and annually reviews its service area." It bases that area on where patients reside, "as documented by the ZIP codes reported" on Form 5B: Service Sites.

Those ZIP codes should match UDS patient origin. In the manual's example, Form 5B "would include the ZIP codes in which at least 75 percent of current health center patients reside." The source is the most recent UDS report ([Compliance Manual](https://bphc.hrsa.gov/compliance/compliance-manual/chapter3)).

New and competing supplement applicants in the Service Area Competition face a firmer rule. They "must propose to serve at least 75% of the current health center's patients within the service area" ([SAC FAQ](https://bphc.hrsa.gov/funding/funding-opportunities/service-area-competition/faq)). They show this with the ZIP code patient percentages in HRSA's Service Area Announcement Table (SAAT). Competing continuation applicants must compare their Form 5B ZIP codes "with patient origin data reported by ZIP code in UDS."

UDS reports patients by "the ZIP code on file as of the last visit" ([UDS ZIP code table](https://bphc.hrsa.gov/sites/default/files/bphc/data-reporting/zip-code-fact-sheet-2025.pdf)). ZIP codes with ten or fewer patients are grouped as "Other," so small ZIP codes will not appear in your patient origin list.

## Why the geographies do not line up

Service areas are ZIP code lists, but HPSAs are not built from ZIP codes. [42 CFR Part 5, Appendix A](https://www.law.cornell.edu/cfr/text/42/appendix-A_to_part_5) requires a "rational area for the delivery of primary medical care services." That area can be "a county, or a group of contiguous counties." It can also be part of a county or a metropolitan neighborhood.

HRSA's HPSA records reflect this. Component types in HRSA's [HPSA files](https://data.hrsa.gov/data/download) include Single County, County Subdivision and Census Tract. All components of one HPSA share the same [HPSA source ID](https://data.hrsa.gov/DataDownload/DD_Files/HPSA_DATAMART_METADATA.XLSX).

ZIP codes are also not areas. The Navigator guide explains that ["ZCTAs represent geographic areas while ZIP Codes are point-based"](https://data.hrsa.gov/DataDownload/GeoCareNavigator/HCP-GeoCareNavigator-User-Guide.pdf). So you need two conversions: ZIP code to [ZCTA](/glossary/zcta-vs-zip-code), then ZCTA to the HPSA's counties, county subdivisions or tracts.

## HPSA types to keep apart

| Type | What it covers | How to use it in a service area map |
|---|---|---|
| Geographic | ["A shortage of providers for an entire group of people within a defined geographic area"](https://bhw.hrsa.gov/workforce-shortage-areas/shortage-designation) | Count residents inside it |
| Population | A shortage for ["a specific group of people"](https://bhw.hrsa.gov/workforce-shortage-areas/shortage-designation) in an area, such as low-income or migrant farmworker groups | Name the group; do not describe the whole area as short |
| Facility | A site, including auto-HPSAs such as FQHCs and Look-Alikes ([HRSA](https://bhw.hrsa.gov/workforce-shortage-areas/shortage-designation)) | Describes your sites, not the surrounding area |

HRSA's Navigator data guide confirms that ["all federally qualified health centers facilities receive automatic facility HPSA designation"](https://data.hrsa.gov/DataDownload/GeoCareNavigator/AboutTheData.pdf). Your FQHC's facility HPSA is therefore not evidence of an area shortage.

Scores run [0–25 for primary care and mental health, and 0–26 for dental](https://bhw.hrsa.gov/workforce-shortage-areas/shortage-designation/scoring). The National Health Service Corps reviews loan repayment applications ["by descending HPSA score"](https://nhsc.hrsa.gov/loan-repayment/funding-priorities). See the [HPSA glossary entry](/glossary/hpsa) for scoring components.

## Step by step

### 1. List your service area ZIP codes

1. Export the ZIP codes from your Form 5B site entries.
2. Compare them with your latest UDS patient origin table. HRSA's site visit protocol asks whether you use ["patient origin data from its most recent UDS report"](https://bphc.hrsa.gov/compliance/site-visits/site-visit-protocol/needs-assessment) when updating Form 5B.
3. Note any ZIP code you serve that UDS lumps into "Other."

### 2. Convert ZIP codes to ZCTAs

1. Download HRSA's [2025 ZIP Code to ZCTA Crosswalk](https://data.hrsa.gov/DataDownload/GeoCareNavigator/ZIPCodetoZCTACrosswalk2025UDS.xlsx) from the [Navigator Resources page](https://data.hrsa.gov/GeoCareNavigator/Resources).
2. Check the `ZIP_JOIN_TYPE` column. Values include "Zip matches ZCTA" and "Spatial join to ZCTA."
3. Replace each spatially joined ZIP code with its matching ZCTA. The Navigator will not add a ZIP code with ["Spatial Join to ZCTA"](https://data.hrsa.gov/DataDownload/GeoCareNavigator/HCP-GeoCareNavigator-User-Guide.pdf) as its join type.
4. Remove duplicates, since several ZIP codes can share one ZCTA.

By our count, 7,243 of the [crosswalk's](https://data.hrsa.gov/DataDownload/GeoCareNavigator/ZIPCodetoZCTACrosswalk2025UDS.xlsx) 41,041 distinct ZIP codes join by spatial join. Most of them are labeled "Post Office or large volume customer."

### 3. Get HPSA data by discipline

1. On HRSA's [Data Downloads](https://data.hrsa.gov/data/download) page, open "Shortage Areas." It has separate primary care, dental and mental health sections.
2. Download "All HPSAs" (CSV or XLSX) for the HPSA ID, type, score and status.
3. Download "Area HPSA Designation Boundaries" or "Area HPSA Component Boundaries" shapefiles for mapping. Facility HPSAs come in a separate "All Facility HPSAs" shapefile.
4. Keep the status field. Valid values include Designated, Proposed For Withdrawal and Withdrawn ([HPSA metadata](https://data.hrsa.gov/DataDownload/DD_Files/HPSA_DATAMART_METADATA.XLSX)). Drop withdrawn records.

HRSA lists the shortage area data with a [daily refresh cycle](https://data.hrsa.gov/data/download). Record your download date.

For a quick check of one address or a few HPSAs, use [HPSA Find](https://data.hrsa.gov/topics/health-workforce/shortage-areas/hpsa-find) or [Shortage Areas by Address](https://data.hrsa.gov/topics/health-workforce/shortage-areas/by-address). The address tool covers ["HPSA Geographic, HPSA Geographic High Needs, Population Group HPSA, and MUA/P designated areas."](https://data.hrsa.gov/topics/health-workforce/shortage-areas/by-address)

### 4. Overlay the two

**Without GIS staff:** use the GeoCare Navigator.

1. Choose any application type. The guide says this also works for exploration ["for research or other purposes"](https://data.hrsa.gov/DataDownload/GeoCareNavigator/HCP-GeoCareNavigator-User-Guide.pdf).
2. Paste or upload your ZCTA list. The guide recommends these options ["if there are many ZIP Codes or ZCTAs"](https://data.hrsa.gov/DataDownload/GeoCareNavigator/HCP-GeoCareNavigator-User-Guide.pdf). If you paste, click "Validate ZCTAs" before adding them.
3. Turn on one HPSA layer at a time in the Map Layers widget. The layers draw from the HRSA Data Warehouse and update to the [previous day](https://data.hrsa.gov/DataDownload/GeoCareNavigator/AboutTheData.pdf).
4. Click each HPSA shape to read its information card.
5. Export the map as a PDF report, or the data table as [CSV](https://data.hrsa.gov/DataDownload/GeoCareNavigator/HCP-GeoCareNavigator-User-Guide.pdf). The tool cannot save your work, so export before closing the tab.

**With a GIS or spreadsheet:** join by geography codes.

1. Download the Census [2020 ZCTA relationship files](https://www.census.gov/geographies/reference-files/time-series/geo/relationship-files.2020.html) to counties, county subdivisions and tracts.
2. Match each HPSA component's code to those files.
3. Flag each ZCTA as fully, partly or not inside each HPSA.

The relationship files report the [overlapping land area](https://www.census.gov/programs-surveys/geography/technical-documentation/records-layout/2020-zcta-record-layout.html) (`AREALAND_PART`), not population. For population shares, join 2020 Census block populations to the ZCTA-to-block file, or label partial overlaps as partial.

HRSA's 2025 shortage update applied ["2020 Census geographies"](https://www.hrsa.gov/about/news/press-releases/extended-timeline-health-professional-shortage-area-designations). Use 2020 boundary files throughout.

### 5. Summarize by discipline

For each discipline, report:

- Each HPSA's ID, name, type (geographic, population or facility), score and status.
- Which service area ZCTAs fall fully or partly inside it.
- The residents in fully covered ZCTAs, with partial ZCTAs listed separately. Name the ACS year if you use [ACS 5-year estimates](/glossary/acs-5-year-estimates).
- Proposed-for-withdrawal HPSAs in their own line. They [remain HPSAs](https://www.hrsa.gov/about/news/press-releases/extended-timeline-health-professional-shortage-area-designations) until HRSA's final withdrawal decisions in a future Federal Register notice.

### 6. Add MUA/Ps and other context

Add [MUA/Ps](/glossary/mua-mup) to the same map. SAC service area maps must show [MUAs and MUPs](https://bphc.hrsa.gov/funding/funding-opportunities/service-area-competition/faq). The Navigator guide says all applications [require the MUA/P layer](https://data.hrsa.gov/DataDownload/GeoCareNavigator/HCP-GeoCareNavigator-User-Guide.pdf). MUA/Ps are on the same [Data Downloads](https://data.hrsa.gov/data/download) page.

The Compliance Manual's needs assessment must cover ["factors associated with access to care and health care utilization"](https://bphc.hrsa.gov/compliance/compliance-manual/chapter3). Your HPSA map supports that section. Add [provider-to-population ratios](/glossary/provider-to-population-ratio) and [drive times](/glossary/drive-time-access) for local detail.

## Where GeoChat AI fits

GeoChat AI is a free healthcare access mapping platform for community health assessments and supply-demand studies. The platform is new; its current version is [GeoChat Atlas](https://atlas.geochat.ai) (version 2). It is not affiliated with HRSA or the GeoCare Navigator. It is also not affiliated with GeoChat, the MBZUAI remote-sensing model, or GeoChat, the InSTEDD messaging tool.

As of November 2026, GeoChat Atlas has HRSA HPSA, MUA and health center site layers, plus [NPPES provider counts](/methods) by county and ZIP code. Provider counts are registrations, not full-time clinicians. A plain-language AI chat lets you drill into ZIP codes and compare regions. It has no web search. It is instructed to report only figures from its own dataset queries; that is an instruction to the model, not a guarantee.

GeoChat AI uses public data, not your patient records. **The GeoCare Navigator is the better choice** for HRSA application maps and service areas built from UDS patient origin. GeoChat AI suits the follow-up questions, such as provider supply in your ZIP codes. See [GeoChat AI vs UDS Mapper](/geochat-ai-vs-uds-mapper) for the full comparison.

## Common mistakes

- **Counting your own facility HPSA as an area shortage.** FQHCs are auto-HPSAs; map geographic and population HPSAs for the service area.
- **Joining ZIP codes straight to maps.** Convert to ZCTAs first and count unmatched codes.
- **Mixing disciplines.** Report primary care, dental and mental health HPSAs separately, since dental scores run to 26.
- **Keeping withdrawn records.** The HPSA files include withdrawn designations; filter on status.
- **Describing a population HPSA as area-wide.** Name the population group it covers.
- **Undated maps.** HPSA data changes daily, so print the download date and data year on every map.

For other options, see [free tools for mapping healthcare access gaps](/free-tools-healthcare-access-mapping).
