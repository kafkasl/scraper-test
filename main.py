from fastapi import FastAPI
from pydantic import BaseModel
from trafilatura import fetch_url, extract

app = FastAPI()

class ScrapeRequest(BaseModel):
    url: str

@app.post("/scrape")
async def scrape(request: ScrapeRequest):
    downloaded = fetch_url(request.url)
    if downloaded:
        return {"content": extract(downloaded, output_format='markdown')}
    return {"error": "Failed to fetch the URL."}
