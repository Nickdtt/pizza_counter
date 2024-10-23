from sqlalchemy.ext.asyncio import AsyncSession

async def registrar_competidor(nome_competidor: str, db: AsyncSession):
    ...