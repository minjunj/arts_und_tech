from langchain_openai import OpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

# OpenAI LLM 초기화
llm = OpenAI(
  temperature=0.9
)

class LLMResult(BaseModel):
  result: str = Field(description="유저의 입력에 대한 대답")
  mood: str = Field(description="유저의 입력을 들을 사람이 느낄 기분")

output_parser = JsonOutputParser(pydantic_object=LLMResult)

format_instructions = output_parser.get_format_instructions()

template = """
## About Me
나는 사용자가 한 말을 들을 사람이 어떤 기분을 느낄지 예측하고, 그에 맞는 대답을 해 준다.
{format_instructions}
유저의 입력: {user_input}
"""
prompt = PromptTemplate(
  template=template,
  partial_variables={"format_instructions": format_instructions},
  input_variables=["user_input"]
)

llm_chain = prompt | llm | output_parser