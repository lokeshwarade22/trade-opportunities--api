import httpx
from bs4 import BeautifulSoup

async def fetch_sector_news(sector: str) -> str:
    url = f"https://duckduckgo.com/html/?q={sector}+India+market+news"
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    snippets = [s.text for s in soup.select(".result__snippet")[:5]]
    return "\n".join(snippets)
