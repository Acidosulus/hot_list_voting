
import requests
import logging


import time
import datetime
import logging
from click import echo, style  

logging.basicConfig(level=logging.INFO, filename="log.html",filemode="a", format="%(asctime)s %(levelname)s %(message)s")


def addSecs(tm, secs):
	fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
	fulldate = fulldate + datetime.timedelta(seconds=secs)
	return fulldate.time()


def rq ():
	orq = requests.post(
		'https://www.hot-list.ru/voting-api.php',
		data={
			'command': 'vote',
			'userip': '185.112.225.153',
			'mode': 'music',
			'act': 'hit-na-veka-2024',
			'secpoll': 'd9afa34fe1f6ef9ce305b62826195a1b',
			'imgid': "music-3309"
		}
	)
	echo(style(text=orq.text, fg='bright_blue'))
	logging.info(orq.text)
	print()
	print()
	orq = requests.post(
		'https://www.hot-list.ru/voting-api.php',
		data={
			'command': 'vote',
			'userip': '185.112.225.153',
			'mode': 'music',
			'act': 'music-legends',
			'secpoll': '2b22a7f01105ba2eefbf00b0239fd9f2',
			'imgid': "music-2204"
		}
	)
	echo(style(text=orq.text, fg='bright_red'))
	logging.info(orq.text)
	print()
	print()
	orq = requests.post(
		'https://www.hot-list.ru/voting-api.php',
		data={
			'command': 'vote',
			'userip': '185.112.225.153',
			'mode': 'music',
			'act': 'hit-na-veka-2024',
			'secpoll': 'd9afa34fe1f6ef9ce305b62826195a1b',
			'imgid': "music-3957"
		}
	)
	echo(style(text=orq.text, fg='bright_green'))
	logging.info(orq.text)
	print()
	print()
	orq = requests.post(
		'https://www.hot-list.ru/voting-api.php',
		data={
			'command': 'vote',
			'userip': '185.112.225.153',
			'mode': 'music',
			'act': 'music-legends',
			'secpoll': '2b22a7f01105ba2eefbf00b0239fd9f2',
			'imgid': "music-3694"
		}
	)
	echo(style(text=orq.text, fg='bright_cyan'))
	logging.info(orq.text)
	print()
	print()
	orq = requests.post(
		'https://www.hot-list.ru/voting-api.php',
		data={
			'command': 'vote',
			'userip': '185.112.225.153',
			'mode': 'music',
			'act': 'hit-na-veka-2024',
			'secpoll': 'd9afa34fe1f6ef9ce305b62826195a1b',
			'imgid': "music-4209"
		}
	)
	echo(style(text=orq.text, fg='bright_cyan'))
	logging.info(orq.text)
	print()
	print()


delay = 65*60
if delay == 0:
	rq()
else:
	while True:
		logging.info('')
		rq()
		logging.info('')
		echo(style(text=f'sleep until {addSecs(datetime.datetime.now().time(), delay)}', bg='bright_black', fg='bright_cyan'))
		time.sleep(delay)