#coding:utf8
from bs4 import BeautifulSoup
import requests,re,time
from django.db import connection
import gim.common.file_processing as cfp
from django.http import HttpResponse
import sd
def snn(request):
    cursor = connection.cursor()
    cursor.execute("select distinct site from gim_commreport where site='印度哈兹拉港'")
    rst = cursor.fetchall()
    # code = '#coding:utf8\r\n'
    # code += 'sll = {}\r\n'
    code = ''
    for row in rst:
        site = row[0]
        hk = sd.sll.has_key(site)
        print site + ':'+str(hk)
        if  hk == False:
            url = 'http://zhannei.baidu.com/cse/search?q=%s&click=1&entry=1&s=5624957645465903891&nsid='%(site)
            # print url
            try:
                # time.sleep(10)
                r = requests.get(url)
                r.encoding = 'utf-8'
                doc = r.text
                # print doc
                href = []
                pagesoup = BeautifulSoup(doc, 'lxml')
                for link in pagesoup.find_all(name='a', attrs={"href": re.compile(r'^http:')}):
                    # print type(link)
                    # print link.get('href')
                    h = link.get('href')
                    if h.find('city') > 0:
                        # print h
                        href.append(h)
                # print len(href)
                if len(href) > 0:
                    if href[0].find('earthol') > 0:
                        # time.sleep(10)
                        r = requests.get(href[0])
                        r.encoding = 'utf-8'
                        doc = r.text
                        spos = doc.find('include.js"></script>')+21
                        epos= doc.find('</head>')
                        newdoc = doc[spos:epos].replace('<script type="text/javascript">','').replace('</script>','')
                        x = newdoc.split(';')[0].split('=')[1].replace(' ','')
                        y = newdoc.split(';')[1].split('=')[1].replace(' ','')
                        coor = x+','+y
                        #
                        code += "sll[u'%s'] = '%s'\r\n"%(site,coor)
                    else:
                        print '00000000000'+site
                else:
                    print '111111111'+site
            except Exception, e:
                # print Exception, ":", e

                print '22222222222'+site
                pass
    print code
    cf = cfp.fp()
    path = cf.cur_file_dir() + '/gim/datastore/sd.py'
    # print path
    file_object = open(path, 'a')
    file_object.write(code)
    file_object.close()
    return HttpResponse('Sync success')