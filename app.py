import asyncio
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crawl4ai import AsyncWebCrawler

app = FastAPI(
    title="Crawl4AI Web Content Extraction API",
    version="1.0.0"
)


class URLRequest(BaseModel):
    url: str


@app.get("/")
def home():
    return {
        "message": "Crawl4AI API is running successfully!"
    }


@app.post("/extract")
async def extract(request: URLRequest):
    try:
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(request.url)

        return {
            "url": request.url,
            "markdown": result.markdown
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))