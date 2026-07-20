# Web Content Extraction using Crawl4AI

A simple Python application that uses **Crawl4AI** to crawl a webpage and extract its content in **Markdown** format.

## Features

- Crawl any publicly accessible webpage.
- Extract webpage content.
- Generate structured Markdown output.
- Asynchronous implementation using `AsyncWebCrawler`.

## Tech Stack

- Python
- Crawl4AI
- AsyncIO

## Project Structure

```text
.
├── task2.py
├── requirements.txt
└── README.md
```

## Installation

1. Install the required package:

```bash
pip install crawl4ai
```

2. Download the required browser binaries:

```bash
crawl4ai-setup
```

3. Verify the installation:

```bash
crawl4ai-doctor
```

## Run the Project

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

## Sample Output

The application crawls the specified webpage and prints the first 1000 characters of the extracted content in Markdown format.
