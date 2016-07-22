# -*- coding: UTF-8 -*-
import renpy.store as store
import renpy.exports as renpy
from text_default_phrases import phrases
default_phrase = 'I have no phrase on this language so bye...'
class Outputable(object):
    language = None
    @classmethod
    def set_lang(cls, lang):
        if lang == None:
            lang = 'english'
        cls.language = lang
    def __init__(self, name, other_info):
        self.name = name
        self.other_info = other_info
    def get_phrase(self):
        try:
            my_phrase = phrases[self.language][self.other_info]
        except KeyError:
            my_phrase = default_phrase
        return unicode(my_phrase)
    def description(self):
        wellcome_text = self.get_phrase()
        return self.name + ': ' + wellcome_text