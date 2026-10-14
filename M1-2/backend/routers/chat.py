
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.conversation_service import (
    delete_conversation,
    get_all_conversations,
)
from services.openai_service import chat_with_ai

router = APIRouter(
    prefix="/api",
    tags=["Chat"],
)


class ChatRequest(BaseModel):
    message: str
    conversation_id: str | None = None


@router.post("/chat")
def chat_endpoint(req: ChatRequest):
    return chat_with_ai(
        user_message=req.message,
        conversation_id=req.conversation_id,
    )


@router.get("/conversations")
def read_conversations():
    return get_all_conversations()


@router.delete("/conversations/{conversation_id}")
def remove_conversation(conversation_id: str):
    deleted = delete_conversation(conversation_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="대화 기록을 찾을 수 없습니다.",
        )

    return {"message": "대화 기록이 삭제되었습니다."}
