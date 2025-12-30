###
# Interface server for running the Redwolf browser interface along with the back end asynchronously,
#   implementing a queue of instructions and updates for transferring module requests and inputs from
#   the UI side, and processing output messages for the various panels from the back end side
###

#Basics
import math,time,random

#JS stuff
import asyncio,websockets
import webbrowser

#File stuff
import glob

#Serving on localhost port 8080
HOST = "127.0.0.1"
PORT = 8080

async def handle_client(websocket):
    #The actual server code can either be handling a call from the UI or the
    #   Redwolf software, both process the messages into queues for the other

    #Global evnt queues to share between client calls
    global to_UI,to_AI

    try: #main try for the server
        async for message in websocket: #For each message

            #Default response 
            resp = "DEFAULT"

            if message[0] == "&": #From the AI

                if message[1] == "R": #If a reset
                    print(message) #print the message
                    to_AI = [] #Reset both queues
                    to_UI = []

                #If a panel, feed, output, warning, input, or setup message
                elif message[1] in ["P","F","O","W","I","S"]:
                    #Panel/Feed/Output/Warn/Input/Setup update printed
                    print(message)
                    to_UI = to_UI + [message[1:]] #Send message to the queue
                    resp = "&Done" #Respond that it was done

                elif message[1] == "U": #Update request
                    if len(to_AI) > 0: #If some messages for the AI side
                        print("to_AI",to_AI) #Print it
                        resp = to_AI[0] #respond with the message for the AI
                        to_AI = to_AI[1:] #Clear that one from the queue
                    else: #otherwise, nothing to send, say so
                        resp = "&None"

            elif message[0] == "@": #From the UI

                #If a module, input, cancel, setup, or reset message
                if message[1] in ["M","I","C","S","R"]:
                    #Module/Input/Cancel/Setup/Reset update printed
                    print(message)
                    to_AI = to_AI + [message[1:]] #Put in the queue
                    resp = "@Done" #Reply it's done

                elif message[1] == "U": #Update request
                    if len(to_UI) > 0: #If anything in the queue
                        print("to_UI",to_UI) #Print it
                        resp = to_UI[0] #grab the first one
                        to_UI = to_UI[1:] #remove it from the queue
                    else: #Otherwise report nothing
                        resp = "@None"

            #Send the response
            await websocket.send(resp)

    #If the connection closed, print and pass
    except websockets.exceptions.ConnectionClosed:
        print("CONNECTION CLOSED")
        pass

#Main loop
async def main():

    #Globals for each queue
    global to_UI,to_AI
    to_UI = []
    to_AI = []

    #Make the server object, and attach the client call handler
    server = await websockets.serve(handle_client, HOST, PORT)

    #Open the actual browser window
    webbrowser.open("REDWOLF2_face.html")

    #Spin until it closes
    await server.wait_closed()

#Actual run call
if __name__ == "__main__":
    #Async call the main function
    asyncio.run(main())

