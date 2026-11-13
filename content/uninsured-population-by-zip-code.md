---
title: "How to Estimate the Uninsured Population by ZIP Code"
description: "Use ACS 5-year table S2701 for each ZCTA in your service area, add the counts, and combine margins of error. Steps, formulas and a SAHIE cross-check."
slug: uninsured-population-by-zip-code
type: guide
updated: 2026-11-13
faq:
  - q: "Which Census table gives the number of uninsured people by ZIP code?"
    a: "Use ACS 5-year subject table S2701 at the ZIP Code Tabulation Area (ZCTA) level. Line S2701_C04_001E is the uninsured count and S2701_C01_001E is the civilian noninstitutionalized population. Detailed tables B27010 and B27001 give the same measure split by age or by sex and age."
  - q: "Can I get uninsured estimates for ZIP codes from SAHIE?"
    a: "No. The Census Bureau's Small Area Health Insurance Estimates (SAHIE) program publishes state and county estimates only. Use SAHIE as a county-level cross-check and the ACS 5-year estimates for ZCTAs."
  - q: "How do I combine margins of error when I add up several ZCTAs?"
    a: "Square each ZCTA's margin of error, add the squares, and take the square root. The Census Bureau calls this an approximation that ignores correlation between areas, so use as few pieces as you can."
  - q: "Why is there no ACS 1-year estimate for my ZIP code?"
    a: "The ACS does not produce 1-year estimates for ZCTAs at any population size. ZCTA data come only from the 5-year estimates; the latest are 2020–2024."
  - q: "Does GeoChat Atlas map ACS data by ZIP code?"
    a: "As of November 2026, GeoChat Atlas, from GeoChat AI, maps ACS 2020–2024 5-year estimates at county, ZIP code (ZCTA) and census tract level. Its AI chat can drill into ZIP codes, and its free tier needs no credit card. Check its methods page for which ACS tables it includes."
sources:
  - title: "Census Data API: S2701 Selected Characteristics of Health Insurance Coverage in the United States (2024 ACS 5-year)"
    url: "https://api.census.gov/data/2024/acs/acs5/subject/groups/S2701.html"
    accessed: 2026-11-13
  - title: "Census Data API: B27010 Types of Health Insurance Coverage by Age (2024 ACS 5-year)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B27010.html"
    accessed: 2026-11-13
  - title: "Census Data API: B27001 Health Insurance Coverage Status by Sex by Age (2024 ACS 5-year)"
    url: "https://api.census.gov/data/2024/acs/acs5/groups/B27001.html"
    accessed: 2026-11-13
  - title: "Census Data API: 2024 ACS 5-year Subject Tables, supported geography"
    url: "https://api.census.gov/data/2024/acs/acs5/subject/geography.html"
    accessed: 2026-11-13
  - title: "American Community Survey 5-Year Data (Census Data API)"
    url: "https://www.census.gov/data/developers/data-sets/acs-5year.html"
    accessed: 2026-11-13
  - title: "ACS 2024 Data Release Schedule, U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release-schedule.html"
    accessed: 2026-11-13
  - title: "ACS 2025 Data Release Schedule, U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/acs/news/data-releases/2025/release-schedule.html"
    accessed: 2026-11-13
  - title: "ACS Areas Published, U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/acs/geography-acs/areas-published.html"
    accessed: 2026-11-13
  - title: "ZIP Code Tabulation Areas (ZCTAs), U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html"
    accessed: 2026-11-13
  - title: "2020 Census Relationship Files, U.S. Census Bureau"
    url: "https://www.census.gov/geographies/reference-files/time-series/geo/relationship-files.2020.html"
    accessed: 2026-11-13
  - title: "Understanding and Using ACS Data, Chapter 8: Calculating Measures of Error for Derived Estimates (2020)"
    url: "https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020_ch08.pdf"
    accessed: 2026-11-13
  - title: "Small Area Health Insurance Estimates (SAHIE) Program, U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/sahie.html"
    accessed: 2026-11-13
  - title: "About SAHIE, U.S. Census Bureau"
    url: "https://www.census.gov/programs-surveys/sahie/about.html"
    accessed: 2026-11-13
  - title: "Guidance for Health Insurance Data Users, U.S. Census Bureau"
    url: "https://www.census.gov/topics/health/health-insurance/guidance.html"
    accessed: 2026-11-13
  - title: "Health Insurance Glossary, U.S. Census Bureau"
    url: "https://www.census.gov/topics/health/health-insurance/about/glossary.html"
    accessed: 2026-11-13
---

To estimate the uninsured population by ZIP code, download ACS 5-year table S2701 for each ZIP Code Tabulation Area (ZCTA) in your service area. Add the uninsured counts and the population counts across ZCTAs, then divide. Combine the margins of error with the Census Bureau's square-root formula.

The latest ZCTA data are the [ACS 2020–2024 5-year estimates](https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release-schedule.html), released January 29, 2026. As of its [October 29, 2026 update](https://www.census.gov/programs-surveys/acs/news/data-releases/2025/release-schedule.html), the Census Bureau lists the 2021–2025 5-year release date as "TBD."

## Which table to use

Three ACS 5-year tables cover most needs at the ZCTA level. All three use the same universe: the [civilian noninstitutionalized population](https://api.census.gov/data/2024/acs/acs5/groups/B27010.html).

| Table | What it gives you | Lines to use |
|---|---|---|
| [S2701](https://api.census.gov/data/2024/acs/acs5/subject/groups/S2701.html) Selected Characteristics of Health Insurance Coverage | Total uninsured, percent uninsured, and splits by age, income-to-poverty ratio and other traits | `S2701_C04_001E` "Uninsured" count; `S2701_C01_001E` "Total" population |
| [B27010](https://api.census.gov/data/2024/acs/acs5/groups/B27010.html) Types of Health Insurance Coverage by Age | Coverage type by four age groups | "No health insurance coverage" lines `_017E`, `_033E`, `_050E` and `_066E`; total `_001E` |
| [B27001](https://api.census.gov/data/2024/acs/acs5/groups/B27001.html) Health Insurance Coverage Status by Sex by Age | Insured and uninsured by sex and detailed age | Each "No health insurance coverage" line, such as `_005E` for males under 6 |

S2701 is the simplest choice. One line gives the total uninsured count, and its margin of error is the matching `M` variable, `S2701_C04_001M`.

S2701 also splits the uninsured by [income-to-poverty ratio](https://api.census.gov/data/2024/acs/acs5/subject/groups/S2701.html). Line `S2701_C04_058E` counts uninsured people "below 138 percent of the poverty threshold." That is close to the [Medicaid expansion limit](https://www.census.gov/programs-surveys/sahie/about.html) of 138 percent of the poverty line in participating states. It measures income, not eligibility.

In Census health insurance data, a person who reports [only Indian Health Service coverage is counted as uninsured](https://www.census.gov/topics/health/health-insurance/about/glossary.html). Keep this in mind in service areas with large American Indian and Alaska Native populations.

## ZIP codes are not ZCTAs

Census tables report ZCTAs, not ZIP codes. The USPS assigns [ZIP Codes to delivery routes](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html) and addresses, not to mapped areas. A ZCTA is a Census area [built from 2020 Census tabulation blocks](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html) to approximate a ZIP Code's extent.

Three rules from the Census Bureau's [ZCTA page](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html) matter here:

- "Not all valid ZIP Codes are represented by a 2020 ZCTA." Some patient ZIP codes will have no match.
- Each block with housing units takes "the ZIP Code associated with the most addresses in that block." A ZCTA's edge only approximates the delivery area.
- A ZCTA "may represent a single institutional or corporate delivery point address." Expect some ZCTAs with very few residents.

The ACS does not produce [1-year estimates for ZCTAs](https://www.census.gov/programs-surveys/acs/geography-acs/areas-published.html) "regardless of population size." ZCTA data come only from the [5-year estimates](https://www.census.gov/data/developers/data-sets/acs-5year.html). For crosswalk options, see [ZCTA vs. ZIP code](/glossary/zcta-vs-zip-code).

## Step-by-step method

1. **List your service-area ZIP codes.** Use the ZIP codes your organization already uses to define its area, such as patient ZIP codes from your records. Clean them to five digits and store them as text, so leading zeros survive.
2. **Match each ZIP code to a ZCTA.** Every 2020 ZCTA code was a [valid USPS ZIP code](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html) as of January 1, 2020. Where a ZCTA shares your ZIP code, use it. For the rest, use a documented crosswalk and record which ZIP codes did not match. The [ZCTA glossary entry](/glossary/zcta-vs-zip-code) compares the HUD-USPS and Census options.
3. **Download S2701 for those ZCTAs.** Use data.census.gov or the Census Data API. The API lists ["zip code tabulation area"](https://api.census.gov/data/2024/acs/acs5/subject/geography.html) as a supported geography for 2024 subject tables. All API data queries now [require a key](https://www.census.gov/data/developers/data-sets/acs-5year.html).
4. **Keep the estimate and margin of error for each ZCTA.** You need `S2701_C04_001E` and `_001M` for the uninsured, and `S2701_C01_001E` and `_001M` for the population.
5. **Add the counts.** Sum the uninsured counts across ZCTAs. Sum the population counts the same way.
6. **Compute the service-area rate from the sums.** Divide total uninsured by total population. Do not average the ZCTA percentages; that gives a ZCTA of 500 people the same weight as one of 50,000.
7. **Compute the margin of error for each sum.** Use the formula in the next section.
8. **Check reliability.** Compute the coefficient of variation (CV) for the total and for each ZCTA you plan to show on a map.
9. **Cross-check against SAHIE.** SAHIE covers [people under 65 only](https://www.census.gov/programs-surveys/sahie/about.html), so build an under-65 rate first. In [S2701](https://api.census.gov/data/2024/acs/acs5/subject/groups/S2701.html), add uninsured `S2701_C04_011E` (under 19) and `S2701_C04_012E` (19 to 64). Add totals `S2701_C01_011E` and `S2701_C01_012E` the same way. Compare that rate with SAHIE's 0–64 rate for your county or counties. These are sums, so combine their MOEs with the method below. A large gap is a prompt to check your ZCTA list and joins.

## Combining margins of error

The Census Bureau's ACS handbook gives a [four-step method](https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020_ch08.pdf) for the margin of error (MOE) of a sum across areas:

1. Obtain the MOE of each component estimate.
2. Square each MOE.
3. Sum the squared MOEs.
4. Take the square root of the sum.

Written out: MOE of the sum = √(MOE₁² + MOE₂² + … + MOEₙ²).

The handbook's own example adds three Virginia areas. Their MOEs of ±3,860, ±2,642 and ±1,957 give an [MOE of ±5,070](https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020_ch08.pdf) for the combined count.

### MOE of the service-area percentage

The uninsured count is a subset of the population, so treat the rate as a proportion. The [handbook formula](https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020_ch08.pdf) is:

MOE(P) = (1 ÷ Y) × √( MOE(X)² − P² × MOE(Y)² )

Here X is total uninsured, Y is total population and P is X ÷ Y. Multiply by 100 for a percentage. If the value under the square root is negative, the handbook says to "substitute a 'plus' for the 'minus' sign."

### Reliability

Convert an MOE to a standard error (SE) by dividing by [1.645](https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020_ch08.pdf). The CV is SE ÷ estimate × 100. A lower CV means a more reliable estimate.

Adding areas together usually helps. The handbook notes that aggregating can ["produce more reliable estimates"](https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020_ch08.pdf) when component estimates have large standard errors. A service-area total is often far steadier than any single small ZCTA.

### Limits of the formula

The handbook calls this method "an approximation." It "does not consider the correlation or covariance between the component estimates." The result may be too high or too low.

The gap also grows with the number of pieces. The Census Bureau says ["Users are encouraged to work with the fewest number of estimates possible."](https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020_ch08.pdf) That favors summing one S2701 line per ZCTA over summing four age lines from B27010.

Advanced users can use the ACS [Variance Replicate Tables](https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020_ch08.pdf), which include the covariance this formula leaves out. They cover a subset of 5-year detailed tables and selected geographic levels.

## ZCTAs that straddle your boundary

Some ZCTAs will sit partly inside your service area. Decide on one rule and write it down:

- **Include or exclude whole ZCTAs.** Simplest, and the usual choice when the service area is defined by ZIP code anyway.
- **Use census tracts at the edge.** The Census Bureau publishes a [2020 ZCTA to Census Tract Relationship File](https://www.census.gov/geographies/reference-files/time-series/geo/relationship-files.2020.html). It shows which tracts overlap each ZCTA. Subject tables such as S2701 are published [down to census tracts](https://www.census.gov/programs-surveys/acs/news/data-releases/2024/release-schedule.html).

For a county-based report, the [2020 ZCTA to County Relationship File](https://www.census.gov/geographies/reference-files/time-series/geo/relationship-files.2020.html) shows which counties each ZCTA overlaps.

## Why SAHIE is a cross-check, not the answer

The Census Bureau's [Small Area Health Insurance Estimates (SAHIE)](https://www.census.gov/programs-surveys/sahie/about.html) program publishes "STATE and COUNTY estimates" only. It has no ZIP code or ZCTA estimates. It also covers [people under 65 only](https://www.census.gov/programs-surveys/sahie/about.html); its widest age group is 0–64.

SAHIE is still worth checking. It is model-based and is the [only source of single-year health insurance estimates for all U.S. counties](https://www.census.gov/programs-surveys/sahie.html). Its estimates run from [2008 to 2024](https://www.census.gov/programs-surveys/sahie/about.html). It covers age groups such as 18–64 and income groups such as [0–138% and 138–400% of poverty](https://www.census.gov/programs-surveys/sahie/about.html).

The Census Bureau's [guidance for health insurance data users](https://www.census.gov/topics/health/health-insurance/guidance.html) recommends "SAHIE for counties, else ACS 5-year period estimates" for areas under 20,000 people. It says SAHIE "is the preferred source if it produces estimates for all of your characteristics of interest." For ZIP-level work, ACS 5-year is the source; SAHIE checks the county total.

Expect some difference. SAHIE describes one year, while the 2020–2024 ACS pools five years of responses.

## Mapping ZCTA data in GeoChat Atlas

[GeoChat AI](https://atlas.geochat.ai) is a free, AI-powered mapping platform for community health assessments, community needs assessments and healthcare supply-demand studies. As of November 2026, GeoChat Atlas maps [ACS 2020–2024 5-year estimates](/methods) at county, ZIP code (ZCTA) and census tract level. Its free tier needs no credit card.

As of November 2026, its AI chat can drill into ZIP codes and compare regions in plain language. The chat has no web search. It is instructed to report only figures from its own queries of the platform's datasets. That is an instruction to the model, not a guarantee. The platform is new; the current version is GeoChat Atlas (version 2). Check its [methods page](/methods) for which ACS tables and data versions are behind its layers.

Health centers may also know UDS Mapper, which HRSA replaced with the Health Center Program GeoCare Navigator. See [GeoChat AI vs UDS Mapper](/geochat-ai-vs-uds-mapper). GeoChat AI is not affiliated with HRSA or the GeoCare Navigator. It is also not affiliated with GeoChat, the MBZUAI remote-sensing model, or GeoChat, the InSTEDD messaging tool.

## Common mistakes

- **Joining patient ZIP codes straight to ZCTAs.** ZIP codes without a ZCTA drop out silently. Count unmatched ZIP codes and report them.
- **Averaging ZCTA percentages.** Add the counts first, then divide.
- **Using the wrong denominator.** The uninsured line's universe is the civilian noninstitutionalized population, not the total population. Use `S2701_C01_001E`.
- **Ignoring margins of error.** Small ZCTAs can have MOEs close to their estimates. Show the CV or MOE beside any ZCTA-level figure you publish.
- **Treating a 5-year estimate as one year.** The 2020–2024 figure describes the whole period. See [ACS 5-year estimates](/glossary/acs-5-year-estimates).
- **Comparing overlapping periods.** For trends, the Census Bureau [recommends non-overlapping periods](https://www.census.gov/topics/health/health-insurance/guidance.html). Its comparison profiles set [2020–2024 against 2015–2019](https://www.census.gov/data/developers/data-sets/acs-5year.html).
- **Counting residents as patients.** ACS counts uninsured residents of an area, not people who use your clinic. Pair it with your own patient data. For a full access-gap workflow, see [How to map healthcare access gaps for a CHNA](/chna-access-gap-mapping-guide).
