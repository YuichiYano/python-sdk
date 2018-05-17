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
token = "ksf32h8uzJfc3D4%2BHFY8h92JeQS5ZQu3oRwFXGFvFqqzGdzieskSk920B%2B1iuMZWTZxwsDfGLJmefopqBi6txnp7TGgxxL6qRHExFsp0Ic4Mb8PtJ5jAmLemclGaArL1bMp%2F7BqixDHF9fr6Ov9dXEfOk5K%2FCX8StKEVA9Ca6nFuc%2F6ak33ypVYDOWIcgTJYSgDv11NiimkcYByxJMnXebS8h2GNeU6b4HWIHZbKiU1%2FLBgZ2vtnYdsGjhQyQ08xDTEfz0hDetFPCE3IFDTIgt9829hcdX41oW%2FaQE3dKzpC1p%2F%2Bd7bifYR7T5Gl9dq%2BX3hujUiVKO32JVrG2unOGQpxwriktL96V6s15P1OelHNtS36h8kfpy4WpwEwaJj%2BHy8xIO3vucODnLRj9Ig2RHIrmOpD9lpGZYrA3%2Fl2aBf4PlMQeL8reI2D3YHWHYTnvr9yoxUPPTofCHH6DEknXStAYkLVUL4ErNHtDY6a8XXfoP3rP0q%2FQNkgL6%2FvofygxopnBqg251snMiQB1DGbawoshnkXmJs%2BN6pGIvvjy57KetFeWvkiP1a8yR1jt%2FYnffqt33rgIMBD1lM28q%2F4VOMlLOvtKFrxe%2ByQIPWZa7Oj%2FoMXWNetdL%2F3CJgiXXygAPFs6wAUJRLtWeH0bGHhuPIvRls8%2BAtqaVnRhgwXLN4BBiQxl7TC9NQ1oCLcjG1FFCaUPpeqvvB3CWY4SKPaAvU63JZ9Ktq9xYJLUsaAssPxCLcAeNx7D5TKv4jS7rKDyCgc9kJBsXFAeEoOlbBD90Sd1KL%2FVg8%2Fs5gsv3XCXFzcYRFem54WNjhI4oF876cYfCPNh5IGI8bVs0SsIIERXS7izIA1%2BTQpwgnx%2B1D1Hvbe%2BHqaMUTzQrfAnwcYF%2BfWm%2FUUeSOqAZf5o4%2Bons%2FOPPL%2BbKcR6aNZRukWrKLoTMGTlpXLiIqP9yGzo3%2FCkfPZYnYD6Tvf9xFlLjxOlcta5TV%2BvjktxVQzzfSK8vrEuJI%3D"

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
