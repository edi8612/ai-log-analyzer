from fastapi import FastAPI

app = FastAPI(title="AI Log Analyzer")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the AI Log Analyzer API!"}
