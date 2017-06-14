import logging
import simplejson as json

# Initialize what's won't change in the function before the function definition
# To avoid doing it at each function call and to persist existing connections
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):

	logger.info('Launched with event: '+json.dumps(event))

	return {
		'code': 200,
		'results': 'A nice API'
	}

