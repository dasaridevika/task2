# Crawl4AI Web Content Extraction

A simple Python project that demonstrates web content extraction using **Crawl4AI**. The application crawls a webpage and converts the extracted content into Markdown format.

## What this project does

- Installs and configures Crawl4AI.
- Downloads the required Playwright browser binaries.
- Verifies the installation using `crawl4ai-doctor`.
- Crawls a webpage using `AsyncWebCrawler`.
- Extracts the webpage content.
- Prints the generated Markdown output.

## Tech Stack

- Python
- Crawl4AI
- Playwright
- AsyncIO

## Installation

```bash
pip install crawl4ai

crawl4ai-setup

crawl4ai-doctor
```

## Run

```bash
python task2.py
```

## Sample Code

```python
import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://geeksforgeeks.com")
        print(result.markdown[:1000])

if __name__ == "__main__":
    asyncio.run(main())
```

## Output

The application crawls the specified webpage and prints the first 1000 characters of the extracted content in Markdown format.
