'''
Name: tcp_client.py
Desc: A TCP client to interact with listener server
Auth: Keiran O'Sullivan
Date: 02/05/2022
'''

import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 11000

CLIENT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

CLIENT_SOCKET.connect((SERVER_HOST, SERVER_PORT))

# Open the text file we will be uploading
with open("upload.txt", "r") as f:
    USER_MESSAGE = f.read() # Read the text file

# Create an array that we can chunk the data into
output = []
output.append("") # Create a buffer
currentChunk = 0 # Use this to keep a note of what chunk we're on
for word in USER_MESSAGE.split(" "): # Split the input by spaces
    if len(output[currentChunk] + word + " ") < 512: # If the length is under 512 bytes
        output[currentChunk] += word + " " # Then add the spaces back in but no need to move the buffer and chunk num.
    else:
        currentChunk += 1 # Add 1 to the chunk
        output.append("") # Move the buffer
        output[currentChunk] += word + " " # Put the spaces back in!

total = 0
for i in output: # Loop to upload and  recieve.
    CLIENT_SOCKET.sendall(i.encode()) # upload all chunks
    RECEIVED_MESSAGE, SERVER_ADDRESS = CLIENT_SOCKET.recvfrom(4096) # receiving the word count
    total = total + int(RECEIVED_MESSAGE.decode('utf-8')) # add up the total words.

CLIENT_SOCKET.close() # Close the client connection.

print("The amount of words uploaded was: " + str(total)) # Output the result!




