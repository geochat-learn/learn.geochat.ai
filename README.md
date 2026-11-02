# GeoChat AI Learn

Source for [learn.geochat.ai](https://learn.geochat.ai): guides, tool comparisons, data briefs and definitions for mapping healthcare access gaps, published by GeoChat AI.

Every page is plain HTML, so readers, search engines and AI assistants get the full text without running JavaScript.

| Path | What it is |
| --- | --- |
| `content/` | One Markdown file per page, with front matter (title, description, FAQ, sources) |
| `static/` | Files served as-is, such as data downloads |
| `build.py` | Builds the site into `dist/`, with sitemap.xml, robots.txt, llms.txt and structured data |

Build locally: `pip install markdown pyyaml && python3 build.py`, then open `dist/index.html`.

Data on these pages comes from public sources (U.S. Census Bureau, CMS, HRSA and others); each page lists its sources. To report an error, use the contact link on [geochat.ai](https://geochat.ai).
