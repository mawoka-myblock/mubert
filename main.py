import os
import time

import requests
import atexit
import threading
import vlc


def main():

    headers = {'user-agent': 'MubertAndroid'}
    cookies = dict(mat_id="1000000007243347", mat="d073d7a4451ad05d9abf36393.1626432311")
    payload = {"method": "AppGetPages", "params": {"timestamp": 0}, "application": "Mubert", "language": "de",
               "os": "Android", "sandbox": False, "version": "4.2.0"}
    r = requests.post("https://api-app.mubert.com/v2/AppGetPages", json=payload, cookies=cookies, headers=headers)
    print("Startup-shit", r.json())
    r = requests.get("https://stream.mubert.com/b2c/v2?sid=80379", cookies=cookies, headers=headers, stream=True)
    fout = open("mubert.mp3", "ab")
    for line in r.iter_content():
        fout.write(line)
    fout.close()


def play_mp3():
    time.sleep(5)
    # playsound.playsound("mubert.mp3")
    p = vlc.MediaPlayer(f"file://{os.getcwd()}/mubert.mp3")
    p.play()

def delete_file():
    os.remove("mubert.mp3")



if __name__ == "__main__":
    atexit.register(delete_file)
    sound = threading.Thread(target=play_mp3)
    sound.start()
    main()


