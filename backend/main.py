from fastapi import FastAPI
from database import engine, Base
from routes import router
from fastapi.middleware.cors import CORSMiddleware

def create_app():
    
    #FastAPIアプリケーションのインスタンスを作成する関数
   
    # テーブル作成（初回のみ自動で作るパターン）
    Base.metadata.create_all(bind=engine)

    app = FastAPI()

    # CORS設定（開発時は全許可でもOK）
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # ルーターを登録
    app.include_router(router)
    
    
    return app

app = create_app()