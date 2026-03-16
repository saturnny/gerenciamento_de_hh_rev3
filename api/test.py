"""
Minimal Vercel API handler for testing
"""
import os
import sys

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Basic FastAPI app for testing
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from Vercel!"}

@app.get("/api/health")
async def health():
    return {"status": "ok", "environment": "vercel"}

# Test database connection
@app.get("/api/test-db")
async def test_db():
    try:
        database_url = os.environ.get("DATABASE_URL")
        return {
            "database_url_exists": bool(database_url),
            "database_url_length": len(database_url) if database_url else 0,
            "message": "Environment check complete"
        }
    except Exception as e:
        return {"error": str(e)}

# This is the Vercel handler
handler = app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
