from fastapi import APIRouter
from pydantic import BaseModel, Field
from llm import model

router = APIRouter(
  tags=['chat']
)

class ChattingInput(BaseModel):
  user_input: str = Field(
    alias='chatting',
    default='',
    description="User's input for the chatting."
  )

@router.post('/chat')
async def chatting(body: ChattingInput) -> model.LLMResult:
  response = model.llm_chain.invoke({
    "user_input": body.user_input
  })
  return response