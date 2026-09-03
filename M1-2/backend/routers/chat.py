from fastapi import APIRouter
from pydantic import BaseModel
from services.openai_service import chat_with_ai
from services.conversation_service import get_all_conversations

router = APIRouter(
    prefix="/api",
    tags=["Chat"],
)

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat_endpoint(req: ChatRequest):
    return chat_with_ai(req.message)


@router.get("/conversations")
def read_conversations():
    return get_all_conversations()