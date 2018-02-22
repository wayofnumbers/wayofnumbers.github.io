'''  calculate word count'''
import math
import bs4
from pelican import signals


def is_visible(element):
    '''tell whether text has tags'''
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif isinstance(element, bs4.element.Comment):
        return False
    elif element.string == "\n":
        return False
    return True


def filter_visible_text(page_texts):
    '''remove tags etc.'''
    return filter(is_visible, page_texts)

WPM = 200
WORD_LENGTH = 5

def count_words_in_text(text_list, word_length):
    '''count words'''
    total_words = 0
    for current_text in text_list:
        total_words += len(current_text)/word_length
    return total_words

def estimate_reading_time(content_object):
    '''estimate the reading time of an article'''
    if content_object._content is not None:
        content = content_object._content

        filtered_text = filter_visible_text(content)
        total_words = count_words_in_text(filtered_text, WORD_LENGTH)
        minutes = int(math.ceil(total_words/WPM))
        if minutes == 0:
            minutes = 1

        content_object.readtime = {
            "minutes": minutes,
        }


def register():
    '''api'''
#    signals.content_object_init.connect(estimate_reading_time)
    signals.content_object_init.connect(estimate_reading_time)
