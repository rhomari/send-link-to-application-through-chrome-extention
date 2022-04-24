
import asyncio
import websockets
async def handler(websocket, path):
    datareceived = await websocket.recv()
    print(datareceived)
    await websocket.send("link received, thank you !")

websocketserver=websockets.serve(handler,"localhost",23048)
try:
    asyncio.get_event_loop().run_until_complete(websocketserver)
    asyncio.get_event_loop().run_forever()
except (Exception,KeyboardInterrupt):
    exit()

    