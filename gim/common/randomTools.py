from random import Random
class rtl:
    def random_str(self,randomlength=8):
        str = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
        length = len(chars) - 1
        random = Random()
        for i in range(randomlength):
            str+=chars[random.randint(0, length)]
        return str