# Install Craw4lAi
# pip install crawl4ai
# crawl4ai-setup
# crawl4ai doctor
import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://geeksforgeeks.com")
        print(result.markdown[:1000])  # Print first 1000 chars

if __name__ == "__main__":
    asyncio.run(main())

