from fastapi import FastAPI, Depends
from database import engine, Base
import uvicorn
from database import SessionLocal



app = FastAPI(title="Pizza Competition")



async def get_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()


















if __name__ == '__main__':
    uvicorn.run(app, port=8000)