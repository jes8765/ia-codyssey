from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.data import router as data_router



app = FastAPI(
    title="StockMate API",
    description="NVDA 주가 데이터를 기반으로 분석하고 대화하는 AI 서비스",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(data_router)


@app.get("/")
def root():
    return {
        "message": "StockMate API is running!"
    }

from routers.chat import router as chat_router
# 기존 코드 아래에 추가
app.include_router(chat_router)