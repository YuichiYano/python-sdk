from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud.websocket import RecognizeCallback
import sys
import websocket

def on_message(ws, m):
	print("debug:message:1")
	print(m)

def on_error(ws, e):
	print(e)

def on_close(ws):
	print("close")

def on_open(ws):
	print("debug:open:1")
	ws.send('{"action": "start", "content-type": "audio/l16;rate=16000"}')

	with open(join(dirname(__file__), '../resources/speech.wav'), 'rb') as audio_file:
		ws.send(audio_file)

	print("debug:open:2")

ws_url = "wss://stream.watsonplatform.net/speech-to-text/api/v1/recognize"
token = "o4JfL1Gal5yBievjXUue7y1UhI0WYZcIxHKaa5Kci%2FPhZeQPd45dDs1ExPiDRbZNPAxjVEDFx6VHiwd0OeFATZz087vzCBaTaieG7z8kaBznQcNgWafVE%2FlmEb9nS9ZH4fBXUHRKxPuhq6vwRjojBYXcDBcFYxJcENo8zuNKuND8bCm78o1d94DAW0BFUwLiLJ7nDRuDSMoJoiQG0jzP4YlkS0Gum2acmNRg8HHyzJDAGU5BqjWdWE1TcE3aLrANOoRrCVoAqg6WhtGK7Z2aOLU%2FcsnCnWGtCE0GGKutyiO%2FBhAkAZFpHFSDURzwXhHphlVTNXpCByNHuSkBCyMT45BJ5QJmyBQ9utfkHvcYpalArG2KeuCTO92I4TNfZJLLiYkBO0hBQghKS%2BFB6swBcScTRy9uwEDkn1pz55D0o616homoXJuBfV90IcIt8Yos3o%2BcuUlzkvDgiOU%2BD8gVVnkO7%2FtfFaNnRK0khsMtl0aFAj8%2F1%2BlMIBXDCu6UGvrQqsfrhF440RgASXtI6BVgXrTZwVGt5IjTJT2%2FiHBuTRKJQ%2F6gBI%2FbnFEf%2BxnokmzK%2BywKQln8pjfYo0w0zSZ%2BT0la3%2Bv5x4%2FkysX%2Fms84ehyMN7sLVj66lrwtG4gsxXkA%2Bk%2FMN0U6hifkE%2FNYyk%2BMfJ%2BcJm8W0AllPSzIzIRkPXvcR7cadXrvW0lylPeq3a3hSC3B4h9POFkpvlG9ioJ5BUdy%2BhCEGLD3y6JUg1V2lv9ZcleeaFhiIAVmq%2FL1ZOc6JGdTmPMi0HaPTB4CVp0ntnSKVK36O7eVMvGgHWG%2FKhW0hNdXuxPeR01XZTg8VPCoYw1Lbht430c90jZkMSp%2Fo90RgPIx2wq7YBo8OKTio1sxIXrG4rKjtMQRQMKQZq%2BR8KsvD2LLmIOLxIQ%2FOIlAQPG%2Bd7uy9fKkb78MqGIOXYrm3olEzOHxqKPBVt9Yrl9e2Ddrb9tiBuxcFu%2FSD0d7lmZqs6ni7%2FmSkyP7XrvfbBU%3D"

try:
	websocket.enableTrace(True)
	ws = websocket.WebSocketApp(ws_url+"?watson-token=%s" % token,
	 							on_open = on_open,
								on_close = on_close,
								on_message = on_message,
								on_error = on_error)
	ws.run_forever()

except:
	print(err)
