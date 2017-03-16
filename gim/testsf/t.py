# -*- coding: utf-8 -*-
import re

string = "通过对开元技校基站与四监狱远端端间新建无线链路。经过测试该无线链路通信稳定可靠，用1024字节，ping了340次，已接收到340次，无丢失，延时最短为5ms，最长为6ms，平均为50ms。用32字节，ping了340次，已接收到340次，无丢失，最短延时为5ms，最长为6ms，平均是5ms。在开元技校基站与四监狱远端之间完成网络互联，满足设计要求，可以投入正常使用"

result = re.findall(".*平均为(.*)ms.*", string)
print result[0]
a = result[0]
print a[:a.find('。')-2]
for x in result:
    print x
    # '某某内容'



