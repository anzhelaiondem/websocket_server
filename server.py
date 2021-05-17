import websockets
import asyncio
import ephem

from pyngrok import ngrok

PORT = 5000


async def send_msg(websocket, path):
    while True:
        await websocket.send(calculating_ra_dec_of_moon())
        await asyncio.sleep(1)


def calculating_ra_dec_of_moon():
    m = ephem.Moon()
    m.compute()
    return f"RA: {m.ra}, DEC: {m.dec}"


def main():
    url = ngrok.connect(PORT).public_url
    print("Ngrok tunnel address is: \"{}\" -> \"http://127.0.0.1:{}\"".format(url, PORT))
    start_server = websockets.serve(send_msg, "localhost", PORT)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
