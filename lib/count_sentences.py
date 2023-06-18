#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")
        
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        if self.value[-1] == ".":
            return True
        else:
            return False
    
    def is_question(self):
        if self.value[-1] == "?":
            return True
        else:
            return False
        
    def is_exclamation(self):
        if self.value[-1] == "!":
            return True
        else:
            return False
        
    def count_sentences(self):
        import re
        split_strings = re.split(r'[.!?]+', self.value)
        while ("" in split_strings):
          split_strings.remove("")
          return len(split_strings)

    def __str__(self):
        return self.value
        