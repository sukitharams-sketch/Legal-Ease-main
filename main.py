from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="LegalEase AI",
    description="AI-Powered Legal Document Generator",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "LegalEase AI is running successfully!"
    }


app.include_router(router)
