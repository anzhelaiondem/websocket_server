import websockets
import asyncio
import ephem


async def send_msg(websocket, path):
    while True:
        await websocket.send(calculating_ra_dec_of_moon())
        await asyncio.sleep(10)


def calculating_ra_dec_of_moon():
    m = ephem.Moon()
    m.compute()
    return f"RA: {m.ra}, DEC: {m.dec}"


if __name__ == "__main__":
    start_server = websockets.serve(send_msg, "localhost", 80)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
