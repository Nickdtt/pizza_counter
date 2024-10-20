from fastapi import WebSocketDisconnect, WebSocket
from websockets_models import ConnectionManager
from sqlalchemy.ext.asyncio import AsyncSession
from models.database_model import Competicao
from sqlalchemy.future import select



manager = ConnectionManager()

async def websocket_endpoint(websocket: WebSocket, db: AsyncSession):
    await manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            name, action = data.split(":")
            competidor_stmt = await db.execute(select(Competicao).where(Competicao.nome_competidor == name))
            competidor = competidor_stmt.scalar_one_or_none()
            
            if action == "add":
                competidor.pizza_slices += 1
                await db.commit()
            else:
                continue
            await manager.broadcast(f"{name}:{competidor.pizza_slices}")
                
    except WebSocketDisconnect:
        manager.disconnect(websocket)