---
title: "ZCTA vs ZIP Code: Why They Differ and How to Map"
description: "ZIP Codes are USPS delivery routes; ZCTAs are Census areas built from blocks. Why they differ, which crosswalks to use, and common ZIP mapping errors."
slug: glossary/zcta-vs-zip-code
type: glossary
updated: 2026-11-02
faq:
  - q: "Is a ZCTA the same as a ZIP Code?"
    a: "No. A ZIP Code is tied to USPS delivery points and routes, while a ZCTA is a Census Bureau area built from census blocks. [Not every valid ZIP Code has a 2020 ZCTA](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html)."
  - q: "Which ACS data is available by ZCTA?"
    a: "ZCTA data is published only in [ACS 5-year estimates](https://www.census.gov/programs-surveys/acs/geography-acs/areas-published.html), not in 1-year estimates."
  - q: "How do I convert ZIP Codes to counties or census tracts?"
    a: "Use the [HUD-USPS ZIP Code Crosswalk Files](https://www.huduser.gov/portal/datasets/usps_crosswalk.html). They allocate each ZIP Code to tracts, counties or CBSAs by its share of residential, business, other and total addresses."
  - q: "Why are some ZIP Codes missing from my map?"
    a: "PO Box-only ZIP Codes do not appear in the HUD crosswalk, and not every ZIP Code has a ZCTA. Records with those ZIP Codes need separate handling."
sources:
  - title: "U.S. Census Bureau: ZIP Code Tabulation Areas (ZCTAs)"
    url: "https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html"
    accessed: 2026-11-02
  - title: "U.S. Census Bureau: 2020 Relationship Files"
    url: "https://www.census.gov/geographies/reference-files/time-series/geo/relationship-files.2020.html"
    accessed: 2026-11-02
  - title: "U.S. Census Bureau: Geography and ACS, Areas Published"
    url: "https://www.census.gov/programs-surveys/acs/geography-acs/areas-published.html"
    accessed: 2026-11-02
  - title: "HUD USER: HUD-USPS ZIP Code Crosswalk Files"
    url: "https://www.huduser.gov/portal/datasets/usps_crosswalk.html"
    accessed: 2026-11-02
  - title: "UDS Mapper: ZIP Code to ZCTA Crosswalk"
    url: "https://udsmapper.org/zip-code-to-zcta-crosswalk/"
    accessed: 2026-11-02
---

A ZIP Code is a USPS designation tied to mail delivery points and routes. A ZIP Code Tabulation Area (ZCTA) is a Census Bureau area built from census blocks to represent a ZIP Code's extent ([Census Bureau](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html)). Census data is tabulated for ZCTAs, not ZIP Codes.

## How ZCTAs are built

Each 2020 ZCTA is made of whole 2020 census tabulation blocks, and each block belongs to one ZCTA ([Census Bureau](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html)). A block with housing units takes the ZIP Code used by most of its addresses.

All 2020 ZCTA codes were valid USPS ZIP Codes as of January 1, 2020. All inhabited areas are covered, and a ZCTA can be noncontiguous.

## Why they differ

| | ZIP Code | ZCTA |
|---|---|---|
| Maintained by | USPS | Census Bureau |
| Geometry | Points: delivery points and routes | Polygons made of census blocks |
| Coverage | Every valid ZIP Code | Not every valid ZIP Code has a 2020 ZCTA |
| Census data | Not tabulated | Tabulated, including [ACS 5-year estimates](/glossary/acs-5-year-estimates) |

Sources: [Census Bureau](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html); ACS publishes ZCTAs in 5-year data only ([Census Bureau](https://www.census.gov/programs-surveys/acs/geography-acs/areas-published.html)).

## Crosswalks

- **HUD-USPS ZIP Code Crosswalk Files** link ZIP Codes to tracts, counties and CBSAs, and back ([HUD](https://www.huduser.gov/portal/datasets/usps_crosswalk.html)). Ratios split each ZIP Code by residential, business, other and total addresses. HUD updates them quarterly from USPS data, and downloads require a login.
- **Census 2020 ZCTA relationship files** link ZCTAs to counties, county subdivisions, places, tracts and 2010 ZCTAs ([Census Bureau](https://www.census.gov/geographies/reference-files/time-series/geo/relationship-files.2020.html)).
- **UDS Mapper ZIP Code to ZCTA crosswalk**, developed by John Snow, Inc., is updated annually for Uniform Data System patient data ([UDS Mapper](https://udsmapper.org/zip-code-to-zcta-crosswalk/)). It states that it is not an official USPS or Census product.

## Common pitfalls

- **Joining ZIP Codes straight to ZCTA polygons.** Some ZIP Codes have no ZCTA, so records drop silently. Run a crosswalk first and count unmatched records.
- **Treating PO Box ZIP Codes as residences.** UDS Mapper warns that PO Box and large-volume customer ZIP Codes may not match where people live. HUD's crosswalk omits ZIP Codes that serve only PO Boxes. It also excludes under 1% of active ZIP Codes that HUD could not geocode ([HUD](https://www.huduser.gov/portal/datasets/usps_crosswalk.html)).
- **Using the total ratio for population data.** Allocate residents with HUD's residential ratio, not the total ratio.
- **Mixing vintages.** HUD files from 2012 Q1 through 2022 Q4 use 2010 Census geographies, and later files use 2020 geographies.
- **Over-reading small ZCTAs.** ZCTA estimates come from ACS 5-year samples, so check margins of error.

## How to map ZIP-coded data

1. Clean ZIP Codes to five digits and flag PO Box and large-volume customer ZIP Codes.
2. Assign each ZIP Code to a ZCTA, tract or county with a documented crosswalk.
3. Use residential ratios to split records that span several areas.
4. Join ACS 5-year ZCTA data from the same census vintage.
5. Report how many records could not be matched.
