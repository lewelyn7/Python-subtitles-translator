import abc
class conjugationAPI(abc.ABC):
    def is_vowel(self, c):
        if c == 'a':
            return True
        elif c == 'e':
            return True
        elif c == 'i':
            return True
        elif c == 'o':
            return True
        elif c == 'u':
            return True
        elif c == 'y':
            return True
        else:
            return False

    def is_verb_regular(self, verb, normal_form):
        print("normal form " + normal_form)
        if normal_form + 'ed' == verb:
            return True
        elif normal_form + 'd' == verb:
            return True
        elif normal_form + 'ing' == verb:
            return True
        elif normal_form + 's' == verb:
            return True
        elif normal_form + 'es' == verb:
            return True
        elif normal_form[-1] == 'e' and normal_form[0:-1] + 'ing' == verb:
            return True
        elif self.is_vowel(normal_form[-2]):
            if not self.is_vowel([-1]):
                if normal_form + normal_form[-1] + 'ing' == verb:
                    return True
                elif normal_form + normal_form[-1] + 'ed' == verb:
                    return True
        elif normal_form[-1] == 'y':
            if not self.is_vowel(normal_form[-2]):
                if normal_form[0:-1] + 'ied' == verb:
                    return True
        else:
            return False

    def is_noun_regular(self, word, normal):
        if word == normal + "s":
            return True
        elif word == normal + "es":
            return True
        else:
            return False