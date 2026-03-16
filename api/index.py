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

# Test basic imports first
try:
    from fastapi import FastAPI
    print("FastAPI import: OK")
except ImportError as e:
    print(f"FastAPI import failed: {e}")

# Create a simple test app first
test_app = FastAPI()

@test_app.get("/api/test")
async def test_endpoint():
    return {"message": "Test endpoint working", "env": "vercel"}

@test_app.get("/api/env-test")
async def env_test():
    return {
        "database_url_exists": bool(os.environ.get("DATABASE_URL")),
        "python_path": sys.path[:3],
        "project_root": project_root
    }

# Try to import the main app
try:
    from app.main import app
    print("Main app import: OK")
    handler = app
except ImportError as e:
    print(f"Main app import failed: {e}")
    print("Using test app instead")
    handler = test_app

# This is the Vercel entry point
# Vercel's Edge/Serverless functions look for 'app' by default

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(handler, host="0.0.0.0", port=8001)
