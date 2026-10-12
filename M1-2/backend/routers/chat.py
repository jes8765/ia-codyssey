from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import HTTPException
from services.conversation_service import delete_conversation
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


@router.delete("/conversations/{conversation_id}")
def remove_conversation(conversation_id: str):
    deleted = delete_conversation(conversation_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="대화 기록을 찾을 수 없습니다."
        )

    return {"message": "대화 기록이 삭제되었습니다."}