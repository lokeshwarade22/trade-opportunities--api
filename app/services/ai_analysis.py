import httpx, os

async def analyze(sector: str, data: str) -> str:
    prompt = f"""
Analyze Indian {sector} sector.

Include:
- Market Overview
- Trade Opportunities
- Risks
- Recommendations

Data:
{data}
"""

    async with httpx.AsyncClient() as client:
        res = await client.post(
            "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent",
            params={"key": os.getenv("GEMINI_API_KEY")},
            json={"contents": [{"parts": [{"text": prompt}]}]}
        )

    return res.json()["candidates"][0]["content"]["parts"][0]["text"]
