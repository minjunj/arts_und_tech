import dotenv
from fastapi import FastAPI

import routers

# .env 파일에서 환경 변수 로드
dotenv.load_dotenv()

app = FastAPI()

app.include_router(routers.home.router)
app.include_router(routers.chat.router)