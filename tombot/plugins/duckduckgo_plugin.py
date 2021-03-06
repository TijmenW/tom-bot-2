'''
Provides command for answering queries using the DuckDuckGo API.
'''
import duckduckgo
from tombot.registry import Command, get_easy_logger
from tombot.helper_functions import extract_query


LOGGER = get_easy_logger('plugins.duckduckgo')

@Command(['duckduckgo', 'ddg', 'define'], 'info')
def duckduckgo_cb(bot, message, *args, **kwargs):
    '''
    Answer query using DuckDuckGo.
    '''
    try:
        query = extract_query(message)
        return duckduckgo.get_zci(query)
    except ValueError:
        return 'Sorry, no results.'
    except AttributeError:
        return 'Sorry, no results.'
