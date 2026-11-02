---
title: "NPI and Provider Taxonomy Codes: NPPES Explained"
description: "What NPIs, entity types and NUCC taxonomy codes in NPPES mean, how to filter them, and why raw NPI counts overstate active clinicians."
slug: glossary/npi-taxonomy-codes
type: glossary
updated: 2026-11-02
faq:
  - q: "What is the difference between a Type 1 and a Type 2 NPI?"
    a: "Type 1 NPIs belong to individual providers, such as physicians and sole proprietors. Type 2 NPIs belong to organizations, such as hospitals and group practices ([CMS](https://www.hhs.gov/guidance/sites/default/files/hhs-guidance-documents/MLN909434_NPI_508.pdf))."
  - q: "What is a provider taxonomy code?"
    a: "A [10-character code from the NUCC](https://www.nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40) that records provider type and specialty in three levels: grouping, classification and area of specialization. For example, 207Q00000X is Family Medicine."
  - q: "Can I count clinicians in an area by counting NPIs?"
    a: "Only as an upper bound. NPPES specialty is self-reported and unverified, and out-of-date records do not deactivate an NPI ([Bindman 2013](https://www.cms.gov/mmrr/Downloads/MMRR2013_003_03_b03.pdf))."
  - q: "Where can I download NPPES data?"
    a: "CMS offers a free, query-only NPI Registry plus monthly full, weekly incremental and deactivation files ([CMS](https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination))."
sources:
  - title: "CMS MLN909434: NPI: What You Need to Know (March 2022)"
    url: "https://www.hhs.gov/guidance/sites/default/files/hhs-guidance-documents/MLN909434_NPI_508.pdf"
    accessed: 2026-11-02
  - title: "CMS: Data Dissemination (NPPES)"
    url: "https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination"
    accessed: 2026-11-02
  - title: "CMS: NPPES Data Dissemination Readme, July 2018 (copy hosted by NBER)"
    url: "https://mobile.nber.org/npi/2019/NPPES_Data_Dissemination_Readme.pdf"
    accessed: 2026-11-02
  - title: "NUCC: Health Care Provider Taxonomy"
    url: "https://www.nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40"
    accessed: 2026-11-02
  - title: "NUCC: Taxonomy CSV versions"
    url: "https://www.nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40/csv-mainmenu-57"
    accessed: 2026-11-02
  - title: "NUCC: Taxonomy code set version 26.1 (CSV)"
    url: "https://www.nucc.org/images/stories/CSV/nucc_taxonomy_261.csv"
    accessed: 2026-11-02
  - title: "eCFR: 45 CFR 162.410, Implementation specifications: Health care providers"
    url: "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-162/subpart-D/section-162.410"
    accessed: 2026-11-02
  - title: "Bindman AB. Using the National Provider Identifier for Health Care Workforce Evaluation. Medicare & Medicaid Research Review 3(3), 2013"
    url: "https://www.cms.gov/mmrr/Downloads/MMRR2013_003_03_b03.pdf"
    accessed: 2026-11-02
---

A National Provider Identifier (NPI) is a 10-digit number that identifies a health care provider in HIPAA transactions. It carries no information about the provider's state, provider type or specialty ([CMS](https://www.hhs.gov/guidance/sites/default/files/hhs-guidance-documents/MLN909434_NPI_508.pdf)). Type and specialty are recorded separately with NUCC taxonomy codes in the National Plan and Provider Enumeration System (NPPES).

## Where the data comes from

CMS releases FOIA-disclosable NPPES data in two ways ([CMS](https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination)):

- **NPI Registry:** a free, query-only database updated daily.
- **Download files:** a full monthly replacement file, weekly incremental files and an NPI deactivation file. A separate file lists non-primary practice locations for Type 1 and Type 2 NPIs.

## Entity types

| Entity type | Who | Examples |
|---|---|---|
| Type 1 | Individual providers, including sole proprietors | Physicians |
| Type 2 | Organization providers | Hospitals, group practices |

A sole proprietor may get only one NPI, like any other individual. An NPI does not change when the provider's name, address or taxonomy changes ([CMS](https://www.hhs.gov/guidance/sites/default/files/hhs-guidance-documents/MLN909434_NPI_508.pdf)).

## Taxonomy codes

The National Uniform Claim Committee (NUCC) maintains the Health Care Provider Taxonomy code set ([NUCC](https://www.nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40)). Each code is 10 alphanumeric characters with three levels: grouping, classification and area of specialization.

Examples from [version 26.1](https://www.nucc.org/images/stories/CSV/nucc_taxonomy_261.csv), all in the "Allopathic & Osteopathic Physicians" grouping:

| Code | Classification |
|---|---|
| 207Q00000X | Family Medicine |
| 207R00000X | Internal Medicine |
| 208000000X | Pediatrics |
| 208D00000X | General Practice |

As of November 2026, NUCC lists version 26.1, effective July 1, 2026, as current. Past versions took effect on January 1 or July 1 ([NUCC](https://www.nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40/csv-mainmenu-57)).

Each NPPES record holds up to 15 taxonomy codes, with a switch marking the primary one ([NPPES readme](https://mobile.nber.org/npi/2019/NPPES_Data_Dissemination_Readme.pdf)).

## Practice location vs mailing address

Each record has separate business mailing address and business practice location address fields ([NPPES readme](https://mobile.nber.org/npi/2019/NPPES_Data_Dissemination_Readme.pdf)). For access maps, geocode the practice location. Add sites from the non-primary practice location file, without counting one clinician twice.

## Why NPI counts overstate active clinicians

- **Stale records stay active.** Covered providers must report changes within 30 days ([45 CFR 162.410](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-162/subpart-D/section-162.410)). Yet out-of-date information does not deactivate an NPI, and no explicit penalty applies ([Bindman 2013](https://www.cms.gov/mmrr/Downloads/MMRR2013_003_03_b03.pdf)).
- **Specialty is self-reported.** CMS does not verify the specialty a provider reports.
- **Organizations mixed in.** Counting Type 2 records adds facilities and groups to clinician totals.
- **Multiple taxonomies.** Counting every taxonomy slot counts one person several times.
- **Deactivated NPIs.** The files disclose only the deactivated NPI and its date ([CMS](https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination)). Remove them before counting.
- **Headcount, not FTE.** A part-time clinician counts the same as a full-time one.

## Using NPI data in access-gap work

1. Keep Type 1 records for clinician counts and Type 2 records for facility counts.
2. Select clinicians by primary taxonomy code.
3. Drop deactivated NPIs.
4. Geocode practice locations, then build [provider-to-population ratios](/glossary/provider-to-population-ratio) or [drive-time measures](/glossary/drive-time-access).
5. Label results "NPI-registered providers," not "active clinicians."

[GeoChat AI](https://atlas.geochat.ai) uses the NPPES registry as a data source. Its free tier does not answer questions about specific providers, such as provider counts in an area.
