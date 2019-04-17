import requests
import websockets
import asyncio
import json


# Format the response from thr serve
def display_response(key, value):
    print(f'"{key}": "{value}"')


# Send a GET request to the server
def get_handler(key, host):
    try:
        r = requests.get(f'http://{host}/api/{key}')

        # If key is not present in the server
        if r.status_code == 404:
            print(f'Key {key} not found')
            return
        try:
            # Display the response
            entry = r.json()
            display_response(entry['Key'], entry['Value'])
        except ValueError:
            print('Invalid response from server.')

    except requests.exceptions.ConnectionError:
        print(f"Could not connect to resource at {host}")


def put_handler(key, value, host):
    try:
        payload = {'Key': key, 'Value': value}
        r = requests.post(f'http://{host}/api', json=payload)

    except requests.exceptions.ConnectionError:
        print(f'Could not connect to resource at {host}')


async def watch_handler(host):
    print('connecting...')

    try:
        # Connect to the WS server
        async with websockets.connect(f'ws://{host}/watch') as ws:
            print('connected. Press Ctrl+C to exit')

            # Diplay the message when recieved
            async for message in ws:
                entry = json.loads(message)
                display_response(entry['Key'], entry['Value'])

    except websockets.exceptions.InvalidURI:
        print('Invalid URI')
    except websockets.exceptions.InvalidStatusCode:
        print("Websocket connection not found")
