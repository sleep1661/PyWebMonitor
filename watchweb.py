import ConfigParser

URL = 'url'
REGEX = 'regex'
CONDITION = 'condition'
MAIL_RECEIVER = 'mail_receiver'
MAIL_MSG = 'mail_msg'
INTERVAL_SECONDS = 'interval_seconds'
WATCH_WEBS = 'watchweb.ini'

def get_watch_webs():
	config = ConfigParser.ConfigParser()
	config.read(WATCH_WEBS)
	return [dict(config.items(section)) for section in config.sections()]


if __name__ == '__main__':
	get_watch_web()
