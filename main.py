from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from dotenv import load_dotenv
import os
load_dotenv()

# OpenAI LLM 초기화 (스트리밍 활성화)
llm = OpenAI(temperature=0.9, streaming=True, callbacks=[StreamingStdOutCallbackHandler()],)

# 대화 메모리 초기화
memory = ConversationBufferMemory()

# 스트리밍 핸들러 설정
stream_handler = StreamingStdOutCallbackHandler()

# ConversationChain 설정
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    callbacks=[stream_handler],

)

# 대화 시작
while True:
    try:
        user_input = input("User: ")
        print("Assistant: ", end="", flush=True)
        response = conversation.predict(input=user_input)
        print()  # 스트리밍 출력이 끝난 후 줄 바꿈
    except KeyboardInterrupt:
        print("\n대화를 종료합니다.")
        break

# 대화 기록 확인
print("대화 기록:")
print(memory.buffer)

# 이 대화기록을 가지고 그림을 그려야함.