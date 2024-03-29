# websocket_server
## Summary
This program creates a publicly available websocket server that sends to connected clients, particularly to "WebSocket Test Client" extension, the right ascension (RA) and declination (DEC) of the Moon every 10 seconds.

### Required packages in addition to virtual environment (venv)
websockets (pip install websockets)\
ephem (pip install pyephem)\
ngrok from pyngrok (pip install pyngrok)

### Steps to follow
1. Before running server.py module, run requirements.txt by writing "pip install -r requirements.txt" to install websockets, pyngrok and pyephem packages.
2. When running server.py, it returns _"Ngrok tunnel address: ws://ngrok.address"_ as an output.
3. Copy the websocket address and past it into the "WebSocket Test Client" extension:\
  . If you have already added the WebSocket Test Client extension into Chrom, then use this link:\
  chrome-extension://fgponpodhbmadfljofbimhhlengambbn/index.html \
  . If you have not added it into chrome, open this link to add:\
  https://chrome.google.com/webstore/detail/websocket-test-client/fgponpodhbmadfljofbimhhlengambbn/related?hl=en \
  then use the link mentioned above to use it.\
The picture should look like this:
<img width="600" alt="image" src="https://user-images.githubusercontent.com/82014669/119537994-b047ad00-bd9b-11eb-8307-47b98a7a7172.png">
 
4. After pressing "Open", the program will start providing the RA and DEC of the Moon every 10 seconds.\
The final picture should look like this:
<img width="600" alt="image" src="https://user-images.githubusercontent.com/82014669/119551541-cd37ac80-bdaa-11eb-9f86-f1d0124ea43f.png">

 
### Information about the program
_First run:_ When running the program first time, it will automatically install pyngrok.

_Client.log file:_ After running, the program creates client.log file where first 17 rows show the ngrok tunnel creation process, starting from the row 18 we get flow of the connected and/or disconnected clients.

_Information displayed in terminal:_ The flow of the connected and/or disconnected clients is being printed in terminal too. 

_Message from a client:_ For any message sent from a client the response is "You are connected. Close the program to disconnect."

_Stop the server:_ After running the websocket server, it can be stopped by closing the program. 


### Additional information
_Declination:_ The pyephem package expresses DEC as degrees, but put colons between the components of an angle, because the traditional style (21°46′15.66′′) is not possible with the symbols on a standard computer keyboard.





  
