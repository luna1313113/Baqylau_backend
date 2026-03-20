from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from api.api_router import api_router
import traceback

app = FastAPI(title="My API", debug=True)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    traceback.print_exc()
    return JSONResponse(status_code=500, content={"detail": str(exc)})

app.include_router(api_router)