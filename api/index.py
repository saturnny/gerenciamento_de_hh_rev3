"""
Vercel-compatible API handler
"""
import sys
import os

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Load environment variables
from dotenv import load_dotenv
load_dotenv(os.path.join(project_root, '.env'))

# Import the FastAPI app
from app.main import app

# Vercel handler
from fastapi import Request
from fastapi.responses import JSONResponse

# This is the Vercel entry point
# Vercel's Edge/Serverless functions look for 'app' by default
handler = app

# Optional: Add a health check endpoint
@app.get("/api/health")
async def health_check():
    return {"status": "ok", "message": "API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
