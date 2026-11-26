---
title: "RUCA Codes: Rural-Urban Commuting Areas Explained"
description: "RUCA codes classify census tracts and ZIP codes from 1 (metro core) to 10 (rural) by urbanization and commuting. How they work and how to use them."
slug: glossary/ruca-codes
type: glossary
updated: 2026-11-23
faq:
  - q: "What are RUCA codes?"
    a: "Rural-Urban Commuting Area codes are a USDA Economic Research Service classification of census tracts and ZIP codes. [They rate each area](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes) by urbanization and the strength of commuting ties to urban cores."
  - q: "Which RUCA codes count as rural?"
    a: "It depends on the definition you use. ERS's users' guide gives the Federal Office of Rural Health Policy scheme as an example: [codes 1–3 are urban and 4–10 are rural](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/users-guide). Always state which codes you treated as rural."
  - q: "Are there RUCA codes for ZIP codes?"
    a: "Yes. ERS publishes a separate [2020 ZIP code file](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes) built from the tract codes. Each ZIP code area takes the code that covers [the largest share of its population](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/documentation)."
  - q: "Can I compare 2010 and 2020 RUCA codes?"
    a: "Not directly. ERS says the versions [are not directly comparable](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes) because tract boundaries and methods changed. The 2020 urban core rule is also [stricter](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/users-guide)."
sources:
  - title: "USDA ERS: Rural-Urban Commuting Area Codes"
    url: "https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes"
    accessed: 2026-11-23
  - title: "USDA ERS: Rural-Urban Commuting Area Codes, Documentation"
    url: "https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/documentation"
    accessed: 2026-11-23
  - title: "USDA ERS: Rural-Urban Commuting Area Codes, Users' Guide"
    url: "https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/users-guide"
    accessed: 2026-11-23
  - title: "USDA ERS: 2020 RUCA codes, census tract file (Excel)"
    url: "https://www.ers.usda.gov/media/5441/2020-rural-urban-commuting-area-codes-census-tracts.xlsx"
    accessed: 2026-11-23
  - title: "U.S. Census Bureau: Urban and Rural"
    url: "https://www.census.gov/programs-surveys/geography/guidance/geo-areas/urban-rural.html"
    accessed: 2026-11-23
---

RUCA (Rural-Urban Commuting Area) codes classify every census tract by how urban it is and where its workers commute ([USDA ERS](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes)). Health planners use them to find rural areas inside counties that are metropolitan on paper.

## Why tracts instead of counties

Most counties hold both rural and urban residents, especially large western counties ([ERS documentation](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/documentation)). A county-level label can hide remote towns in a metro county. RUCA codes work at the census tract level, and ERS adapts them to ZIP codes.

## How the codes work

The 2020 codes use the 2020 Census, Census urban areas and 2017–21 ACS tract-to-tract commuting flows ([ERS documentation](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/documentation)). A tract joins an urban core if at least half its residents live in a single urban area.

| Primary code | Meaning |
|---|---|
| 1, 4, 7 | Core of a metropolitan (50,000+), micropolitan (10,000–49,999) or small town (9,999 or fewer) urban area |
| 2, 5, 8 | High commuting: the largest flow, 30% or more of commuters, goes to that size of core |
| 3, 6, 9 | Low commuting: the largest flow, 10% to 30% of commuters, goes to that size of core |
| 10 | Rural: the largest flow is to a tract outside an urban area |
| 99 | Water only, with no population or land area |

Source: [ERS documentation](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/documentation).

There are [10 primary codes and 21 secondary codes](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/users-guide). [Secondary codes](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/documentation) such as 10.1 mark a second commuting flow of 30% to 50% to a larger core.

## Common definitions

ERS says few, if any, uses need the full set of codes ([Users' Guide](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/users-guide)). Its guide gives two examples:

- **Federal Office of Rural Health Policy scheme:** urban is RUCA 1–3; rural is RUCA 4–10.
- **Closest match to metro and micro areas:** a five-level scheme using secondary codes, with "rural/noncore" as 3.0, 6.0, 7.0, 8.0, 9.0, 10.0 and 10.3.

Grant programs may apply their own rules on top of RUCA codes. Check the program's own eligibility rules before you label an area rural.

## Using RUCA codes in a health assessment

1. Download the [2020 census tract file](https://www.ers.usda.gov/media/5441/2020-rural-urban-commuting-area-codes-census-tracts.xlsx). It gives 11-digit tract IDs for both 2020 and 2023, because Connecticut moved to planning regions. Use the 2023 IDs when your other data use Connecticut's planning regions.
2. Join it to [ACS 5-year](/glossary/acs-5-year-estimates) tract data on the tract ID, kept as text with leading zeros.
3. Group tracts with the definition you chose, and state it in your methods.
4. Compare provider supply or [HPSA](/glossary/hpsa) status between rural and urban tracts.

For ZIP-coded data, use the ZIP code file, and read [why ZIP codes and ZCTAs differ](/glossary/zcta-vs-zip-code).

## Limits to state

- **Big rural tracts:** sparse tracts can be as large as a county. One commuting town in a corner can affect the whole tract's code ([ERS documentation](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/documentation)).
- **Fewer small town cores in 2020:** a 2020 urban area needs [at least 5,000 people or 2,000 housing units](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/urban-rural.html). The 2010 minimum was [2,500 residents](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/documentation).
- **Commuting data:** the 2017–21 flows [overlap the COVID-19 pandemic](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/documentation). Nearly 25% of workers had unclear workplaces and were omitted.

[GeoChat AI](https://app.geochat.ai), a healthcare access mapping platform, lists rural health as a use case (as of November 2026). It maps county, ZIP code and tract data.
