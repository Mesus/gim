#encoding: utf-8
import read_office,jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.font_manager import *
import nlp_processing
ro = read_office.office()
# print ro.read_docx(ur'/home/vicent/Documents/1.docx')
# ro.read_excel(ur'/home/vicent/惠州农场2016020111每日采收表.xlsx')
def h():
    myfont = FontProperties(fname='/usr/share/fonts/truetype/wqy/wqy-microhei.ttc')
    l = []
    l.append(ro.read_docx(ur'/home/vicent/施工报告.docx'))
    word_list = [" ".join(jieba.cut(sentence)) for sentence in l]
    new_text = ' '.join(word_list)
    wordcloud = WordCloud(font_path="/usr/share/fonts/truetype/wqy/wqy-microhei.ttc", background_color="black").generate(new_text)
    plt.subplot(211)
    plt.title(u'word',fontproperties=myfont)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

if __name__=='__main__':
    # h()
    nlp = nlp_processing.nlp()
    text = ro.read_docx(ur'/home/vicent/施工报告.docx')
    nlp.word_frequency(text)