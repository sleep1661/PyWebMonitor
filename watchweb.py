import ConfigParser
import codecs

URL = 'url'
REGEX = 'regex'
CONDITION = 'condition'
MAIL_RECEIVER = 'mail_receiver'
MAIL_MSG = 'mail_msg'
INTERVAL_SECONDS = 'interval_seconds'
WATCH_WEBS = 'watchweb.ini'

def get_watch_webs():
	config = ConfigParser.ConfigParser()
	config.readfp(codecs.open(WATCH_WEBS, "r", encoding='utf-8'))
	return [dict(config.items(section)) for section in config.sections()]


if __name__ == '__main__':
	get_watch_web()
