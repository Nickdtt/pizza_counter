from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


DATABASE_URL = "postgresql+asyncpg://postgres.gltsfchwljizdgmiiwzh:.Gk7Zfk95R6i-_f@aws-0-sa-east-1.pooler.supabase.com:5432/postgres"

Base = declarative_base()

engine = create_async_engine(DATABASE_URL)

SessionLocal = async_sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False )