def markdown_report(sector: str, analysis: str) -> str:
    return f"""
# Trade Opportunities Report – {sector.title()} (India)

## Market Analysis
{analysis}

## Notes
Generated using live market data and AI analysis.
"""
