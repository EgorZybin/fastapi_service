from fastapi import FastAPI
import uvicorn
from routes.route_browse import router as browse_router

app = FastAPI()

app.include_router(browse_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
