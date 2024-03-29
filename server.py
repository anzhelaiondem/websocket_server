import websockets
import asyncio
import ephem
import logging

from pyngrok import ngrok

HOST = "localhost"
PORT = 5050
USERS = set()

logging.basicConfig(filename='client.log', filemode='w', level=logging.INFO, datefmt='%m-%d %H:%M:%S',
                    format=' %(levelname)-8s %(asctime)s - %(message)s')


async def client_handler(websocket, path):
    try:
        while True:
            if await websocket.recv():
                await websocket.send("You are connected. Close the program to disconnect.")
    except (websockets.ConnectionClosedError, websockets.ConnectionClosedOK):
        pass


async def producer_handler(websocket, path):
    USERS.add(websocket.remote_address[:2])
    print(f"Client {websocket.remote_address[:2]} is connected. Active clients number: {len(USERS)}")
    logging.info(f"Client {websocket.remote_address[:2]} is connected. Active clients number: {len(USERS)}")
    try:
        while True:
            msg = await calculating_ra_dec_of_moon()
            await websocket.send(msg)
            await asyncio.sleep(10)
    except (websockets.ConnectionClosedError, websockets.ConnectionClosedOK):
        print(f"Client {websocket.remote_address[:2]} is disconnected. Active clients number: {len(USERS) - 1}")
        logging.info(f"Client {websocket.remote_address[:2]} is disconnected. Active clients number: {len(USERS) - 1}")
        USERS.remove(websocket.remote_address[:2])


async def handler(websocket, path):
    try:
        request_task = asyncio.ensure_future(client_handler(websocket, path))
        sender_task = asyncio.ensure_future(producer_handler(websocket, path))
        done, pending = await asyncio.wait([request_task, sender_task], return_when=asyncio.ALL_COMPLETED, )
        for task in pending:
            task.cancel()
    except (websockets.ConnectionClosedError, websockets.ConnectionClosedOK):
        pass


async def calculating_ra_dec_of_moon():
    m = ephem.Moon()
    m.compute()
    return f"RA: {m.ra}, DEC: {m.dec}"


def main():
    ng_url = ngrok.connect(PORT).public_url
    print("Ngrok tunnel address: ws{}".format(ng_url[4:], PORT))
    start_server = websockets.serve(handler, "localhost", PORT)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
