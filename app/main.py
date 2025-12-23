from fastapi import FastAPI, Depends, HTTPException, Request
from slowapi.middleware import SlowAPIMiddleware
from app.auth import create_token, verify_token
from app.rate_limit import limiter
from app.session_store import track_session
from app.services.web_search import fetch_sector_news
from app.services.ai_analysis import analyze
from app.utils import markdown_report

app = FastAPI(title="Trade Opportunities API")

# Attach limiter
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.get("/token")
def get_token():
    return {"access_token": create_token()}

@app.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze_sector(
    request: Request,              # ✅ REQUIRED BY slowapi
    sector: str,
    token: str = Depends(verify_token)
):
    try:
        track_session(token)
        data = await fetch_sector_news(sector)
        analysis = await analyze(sector, data)
        return {"markdown_report": markdown_report(sector, analysis)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
