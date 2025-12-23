from time import time

sessions = {}

def track_session(token: str):
    if token not in sessions:
        sessions[token] = {"count": 0, "last_used": time()}
    sessions[token]["count"] += 1
    sessions[token]["last_used"] = time()
