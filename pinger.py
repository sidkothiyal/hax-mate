import daemon
from requests import post, get
import time

server_ip = "https://postman-echo.com/post"  #'127.0.0.1'

with daemon.DaemonContext():
	while True:
		ip = get('http://jsonip.com').json()['ip']
		print post(server_ip, data={'ip': ip}).json()
		time.sleep(600)
