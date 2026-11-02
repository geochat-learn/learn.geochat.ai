---
title: "Drive-Time Access: Isochrones, Distance and 2SFCA"
description: "Drive-time access measures travel time to care: nearest-provider distance, isochrones and 2SFCA, plus HRSA and CMS time and distance thresholds."
slug: glossary/drive-time-access
type: glossary
updated: 2026-11-02
faq:
  - q: "What drive time is used to define access to primary care?"
    a: "HRSA's primary care HPSA criteria build service areas around [30 minutes of travel time](https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-5/appendix-Appendix%20A%20to%20Part%205). CMS sets Medicare Advantage primary care limits from [10 minutes in large metro counties to 70 minutes in the most sparsely populated counties](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-422/subpart-C/section-422.116)."
  - q: "What is the two-step floating catchment area (2SFCA) method?"
    a: "It computes a supply-to-demand ratio within a travel-time catchment around each provider, then sums those ratios for each population location. [McGrail (2012)](https://ij-healthgeographics.biomedcentral.com/articles/10.1186/1476-072X-11-50) credits Luo and Wang (2003) with pioneering it."
  - q: "Should rural and urban areas use the same drive-time threshold?"
    a: "No. CMS standards differ by county type. [McGrail (2012)](https://ij-healthgeographics.biomedcentral.com/articles/10.1186/1476-072X-11-50) found that access measures across urban and rural regions need both variable catchment sizes and distance decay."
  - q: "Is straight-line distance good enough?"
    a: "It is a rough proxy, because road-network travel time reflects terrain and road type. HRSA's guidelines equate 30 minutes with [25 miles on flat terrain or interstates, but only 15 miles on mountainous or secondary roads](https://www.law.cornell.edu/cfr/text/42/appendix-A_to_part_5)."
sources:
  - title: "Luo W, Wang F. Measures of spatial accessibility to health care in a GIS environment: synthesis and a case study in the Chicago region. Environment and Planning B 30(6):865-884, 2003 (RePEc record and abstract)"
    url: "https://econpapers.repec.org/RePEc:sae:envirb:v:30:y:2003:i:6:p:865-884"
    accessed: 2026-11-02
  - title: "McGrail MR. Spatial accessibility of primary health care utilising the two step floating catchment area method. Int J Health Geographics 11:50, 2012"
    url: "https://ij-healthgeographics.biomedcentral.com/articles/10.1186/1476-072X-11-50"
    accessed: 2026-11-02
  - title: "eCFR: 42 CFR Part 5, Appendix A (Primary Medical Care Shortage Criteria)"
    url: "https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-5/appendix-Appendix%20A%20to%20Part%205"
    accessed: 2026-11-02
  - title: "Cornell LII: 42 CFR Appendix A to Part 5"
    url: "https://www.law.cornell.edu/cfr/text/42/appendix-A_to_part_5"
    accessed: 2026-11-02
  - title: "eCFR: 42 CFR Part 5, Appendix B (Dental Shortage Criteria)"
    url: "https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-5/appendix-Appendix%20B%20to%20Part%205"
    accessed: 2026-11-02
  - title: "eCFR: 42 CFR Part 5, Appendix C (Mental Health Shortage Criteria)"
    url: "https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-5/appendix-Appendix%20C%20to%20Part%205"
    accessed: 2026-11-02
  - title: "eCFR: 42 CFR 422.116, Network adequacy (Medicare Advantage)"
    url: "https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-422/subpart-C/section-422.116"
    accessed: 2026-11-02
---

Drive-time access measures how long residents need to reach health care by road. It is reported as minutes or miles to the nearest provider, or as the share of residents within a travel-time threshold.

## Common measures

| Measure | What it reports | Main limitation |
|---|---|---|
| Nearest-provider time or distance | Minutes or miles from each population point to the closest provider | Ignores provider capacity and competing demand |
| Drive-time isochrone | The area reachable within a set time from a site | Treats everyone inside the boundary as equally served |
| [Provider-to-population ratio](/glossary/provider-to-population-ratio) | Residents per provider inside a fixed boundary | Misses travel across boundaries ([McGrail 2012](https://ij-healthgeographics.biomedcentral.com/articles/10.1186/1476-072X-11-50)) |
| Two-step floating catchment area (2SFCA) | Supply relative to demand within a travel-time catchment | Assumes no distance decay inside the catchment ([McGrail 2012](https://ij-healthgeographics.biomedcentral.com/articles/10.1186/1476-072X-11-50)) |

## Two-step floating catchment area (2SFCA)

Luo and Wang (2003) combined the floating catchment area and gravity methods into one framework ([Environment and Planning B 30(6)](https://econpapers.repec.org/RePEc:sae:envirb:v:30:y:2003:i:6:p:865-884)). The floating catchment defines a physician's service area by a threshold travel time.

The method runs in two steps ([McGrail 2012](https://ij-healthgeographics.biomedcentral.com/articles/10.1186/1476-072X-11-50)):

1. For each provider location, find the population within the threshold and compute a provider-to-population ratio.
2. For each population location, sum the ratios of all providers within the threshold. The sum is that location's access score.

Luo and Wang suggested the method could help HHS and state health departments improve HPSA designation. Later variants add distance decay and variable catchment sizes. McGrail (2012) concluded that measuring access across all regions needs both.

## Thresholds used in policy

HRSA's primary care [HPSA](/glossary/hpsa) criteria build service areas around 30 minutes of travel time ([42 CFR Part 5, App. A](https://www.law.cornell.edu/cfr/text/42/appendix-A_to_part_5)). The rule equates 30 minutes with 20 miles on primary roads and 15 miles in mountainous terrain or on secondary roads. It allows 25 miles on flat terrain or interstates, and uses public transit in inner metropolitan areas.

Dental and mental health HPSA criteria use 40 minutes ([App. B](https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-5/appendix-Appendix%20B%20to%20Part%205); [App. C](https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-5/appendix-Appendix%20C%20to%20Part%205)).

CMS sets Medicare Advantage maximum time and distance standards by county type ([42 CFR 422.116](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-422/subpart-C/section-422.116)):

| County type | Primary care, max minutes / miles |
|---|---|
| Large metro | 10 / 5 |
| Metro | 15 / 10 |
| Micro | 30 / 20 |
| Rural | 40 / 30 |
| CEAC (density under 10 people per sq. mi.) | 70 / 60 |

Plans must meet the standards for at least 90% of beneficiaries in large metro and metro counties. The figure is 85% in micro, rural and CEAC counties ([42 CFR 422.116](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-422/subpart-C/section-422.116)).

## Common pitfalls

- **One threshold everywhere.** Policy thresholds differ by county type. McGrail notes that fixed catchment sizes do not suit both rural and metropolitan settings.
- **Edge effects.** Include providers beyond your study boundary. McGrail added neighboring-state data up to one catchment wide ([McGrail 2012](https://ij-healthgeographics.biomedcentral.com/articles/10.1186/1476-072X-11-50)).
- **Coarse population points.** County centroids hide variation inside a county. Use tract or block group points from [ACS 5-year data](/glossary/acs-5-year-estimates).
- **Wrong provider addresses.** Geocode NPPES practice locations, not mailing addresses ([NPI and taxonomy codes](/glossary/npi-taxonomy-codes)).
- **Assuming everyone drives.** HRSA's criteria use public transportation for inner metropolitan areas.

## How to run a drive-time analysis

1. Choose population points (tract or block group) and provider points (practice locations).
2. Compute road-network travel times from each population point to nearby providers.
3. Report nearest-provider time and the share of residents beyond a stated policy threshold.
4. Run 2SFCA with a catchment suited to the setting, then test a second catchment size.
5. Compare results with [HPSA](/glossary/hpsa) and [MUA/P](/glossary/mua-mup) boundaries.
