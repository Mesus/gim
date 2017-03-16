import jieba
class nlp:

    def word_frequency(self,text):
        from collections import Counter

        words = [word for word in jieba.cut(text, cut_all=True) if len(word) >= 2]
        c = Counter(words)
        l = []
        for word_freq in c.most_common(50):
            word, freq = word_freq
            # print type(word)
            xxx = word.encode('utf-8')
            # print xxx
            xxx = xxx.decode('utf-8')
            print xxx,freq
            t = (xxx,freq)
            l.append(t)
        return l