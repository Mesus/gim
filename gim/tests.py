#coding:utf8
from django.test import TestCase
import common.file_processing as cfp
from bson.objectid import ObjectId
import common.read_office as o
import common.time_correlation as tt
from datastore.mongo_init import *
import jieba,sys,re
# from models import *
from django.db import connection

# Create your tests here.
class GimTestCase():
    def async(self):
        rootDir = '/opt/p4d2'
        fp = cfp.fp()
        fp.fdt(rootDir)
        office = o.office()
        for fl in fp.fileList:
            fex = fp.file_extension(fl)
            if 'docx' in fex:
                doc = office.read_docx(fl)
                seg_list = jieba.cut(doc, cut_all=False)
                fa = str(sys.path[0]).replace('frame/gim','frame')+'/static/data/area.nd'
                file_object = open(fa)
                area = file_object.read()
                for seg in seg_list:
                    if area.find(seg) > 0:
                        print seg
                # p = doc[0]
                # pa = p.split('|')
                # title = pa[0]+pa[1]
                # pal = len(pa)
                # dw = pa[pal-4].split(' ')
                # qz = pa[pal-3].replace('签字：','').replace(' ','')
                # rq = pa[pal-2].replace('日期：','').replace(' ','')
                # print title,dw[0],dw[2],qz,rq
                # t = doc[1]
                # name = t.cell(0,1).text
                # num = t.cell(1,1).text
                # fzr = t.cell(2,1).text
                # print name,num,fzr
                # entry = {}
                # entry['name'] = fp.file_name(fl)
                # entry['content'] = doc
                # entry['time'] = tt.timeTools().ctwithymdhms()
                # insert_doc('doc',entry)
            if 'xls' in fex:
                xlsList = office.read_excel(fl)
                entryList = []
                for xls in xlsList:
                    entry = {}
                    entry['name'] = fp.file_name(fl)
                    entry['content'] = xls
                    entry['time'] = tt.timeTools().ctwithymdhms()
                    entryList.append(entry)
                    sheets = str(xls).split('\r\n')
                    for rows in sheets:
                        d = str(rows).split(',')
                        # print rows
                        if str(rows).find('合计') < 0:
                            print rows
                            # ed = erp_data(rq=d[0],gys=d[1],djbh=d[2],shbz=d[3],
                            #               gbbz=d[4],wlmc=d[5],ggxh=d[6],sl=d[7],
                            #               dw = d[8],jhrq=d[9],bb=d[10],ywy=d[11],
                            #               ghjg=d[12],wlcdm=d[13],hsdj=d[14],dj=d[15],
                            #               jshj=d[16],bm=d[17],cydw=d[18],fjs=d[19],
                            #               btfjs=d[20],slsl=d[21],tlsl=d[22],
                            #               zxbgbh=d[23],jhlb=d[24])
    def getdoc(self):
        coll = db['doc']
        col = coll.find()
        print col
        return col
    def queryCity(self):
        cursor = connection.cursor()
        cursor.execute("select field2,field3,field4 from area where cast(field1 as int)%30=0")
        row = cursor.fetchall()
        return row
    def queryProd(self):
        cursor = connection.cursor()
        cursor.execute("select field2 from prod")
        row = cursor.fetchall()
        return row
    def tsbg(self):
        rootDir = '/home/vicent/PycharmProjects/aztsbg/n'
        fp = cfp.fp()
        fp.fdt(rootDir)
        office = o.office()
        data = ''
        for fl in fp.fileList:
            fex = fp.file_extension(fl)
            print fex
            if '.docx' == fex:
                fn = fp.file_name(fl)
                print '====='+fl
                site = self.splitName(fn)
                data += '地点:' + site + ';'
                pn = fn.replace('安装调试报告.docx','')
                data += '项目名称:' + pn + ';'

                # doc = office.read_docx2(fl)
                # try:
                #     tab = doc.tables[0]
                #     rows = len(tab.rows)
                #     cols = len(tab.columns)
                #     for r in range(0, rows):
                #         for c in range(0, cols):
                #             if str(tab.cell(r, c).text).find('完成日期') > 0:
                #                 t = tab.cell(r, c + 1).text
                #                 data += '日期:' + t + ';'
                # except:
                #     print 'error'
                ddoc = office.read_docx2(fl)
                para_arr = ddoc.paragraphs
                rq = para_arr[len(para_arr)-1].text
                rq = str(rq).replace('日','').replace('期','').replace('：','').replace(' ','')
                data += '日期:' + rq + ';'
                fullText = office.read_docx(fl)
                arr = fullText.split('，')
                for cell in arr:
                    # print cell
                    if cell.find('北京国基科技提供的') > 0:
                        cpmc = re.sub(u'[\u4e00-\u9fa5]+', '', cell)
                        data += '产品名称:' + cpmc + ';'
                        break
                result = re.findall(".*ping(.*)次.*", fullText.encode('utf-8'))
                data += 'ping:' + result[0] + ';'
                # for x in result:
                #     data += x
                # data += ';'
                re2 = re.findall(".*平均为(.*)ms.*", fullText.encode('utf-8'))
                a = re2[0]
                avg = a[:a.find('。') - 2]
                data += 'avg:' + avg + ';'
                data += '\r\n'
                # print data
                # print '___________________'
        fp.save('tsbg_1.bw', data)
    def splitName(self,fn):

        zhPattern = re.compile(u'[\u4e00-\u9fa5]+.*')
        content = fn.replace('售','')
        match = zhPattern.search(content.decode('utf-8'))
        site = ''
        if match:
            area = match.group(0)
            # print '有中文：%s' % (area,)
            # print content[:content.find(area)]
            m = re.compile('[1-9]+').search(area)
            if m:
                n = m.group(0)
                site =  area[:area.find(n)]
        else:
            print '没有包含中文'
        return site
    def worklog(self):
        rootDir = '/home/vicent/PycharmProjects/gzbg'
        fp = cfp.fp()
        fp.fdt(rootDir)
        office = o.office()
        content = ''
        for fl in fp.fileList:
            fex = fp.file_extension(fl)
            if 'docx' in fex:
                print fl
                parag = office.read_docx2parag(fl)
                # h1 = parag[0].text
                # print h1
                doc = office.read_docx2(fl)
                for index in range(0,len(doc.tables)):
                    data = ''
                    tab = doc.tables[index]
                    rows = len(tab.rows)
                    cols = len(tab.columns)
                    for r in range(0,rows):
                        for c in range(0,cols):
                            if tab.cell(r,c).text == '地点':
                                t = tab.cell(r,c+1).text
                                data += '地点:' + t + ';'
                            if tab.cell(r,c).text == '项目名称':
                                t = tab.cell(r,c+1).text
                                data += '项目名称:' + t + ';'
                            if tab.cell(r,c).text == '人员':
                                t = tab.cell(r,c+1).text
                                data += '人员:' + t + ';'
                            if tab.cell(r, c).text == '日期':
                                t = tab.cell(r, c + 1).text
                                data += '日期:' + t + ';'
                    print data
                    content += data + '\r\n'
        fp.save('gzrz.bw',content)

                # b_time = tab.cell(0,1).text
                # b_area = tab.cell(0, 3).text
                # b_name = tab.cell(1, 1).text
                # b_crew = tab.cell(1, 3).text
                # print b_time+'  '+b_area+'  '+b_name+'  '+b_crew
                #     print '================'
    def tranStruct(self):
        from models import worklog
        year = '2015'
        fp = cfp.fp()
        obj = fp.open('gzrz.bw')
        for line in obj.readlines():
            if len(line) > 0 and line.find("日期") > 0:
                rid = {}
                print line
                arr = line.split(';')
                for cell in arr:
                    tmp = cell.split(':')
                    if len(tmp) > 1:
                        name = tmp[0]
                        value = tmp[1]
                        if name == '日期':
                            print value
                            # print value.find(year)
                            # if value.find(year) < 0:
                            #     break
                            rid['rq'] = value
                        if name == '地点':
                            print value
                            rid['dd'] = value
                        if name == '项目名称':
                            print value
                            rid['mc'] = value
                        if name == '人员':
                            print value
                            rid['ry'] = value
                if len(rid) == 4:
                    p = worklog(project=rid['mc'],people=rid['ry'],site=rid['dd'],rq=rid['rq'])
                    p.save()
    def tranStruct_CR(self):
        from models import commreport
        year = '2015'
        fp = cfp.fp()
        obj = fp.open('tsbg_1.bw')
        for line in obj.readlines():
            if len(line) > 0 and line.find("日期") > 0:
                rid = {}
                print line
                arr = line.split(';')
                for cell in arr:
                    tmp = cell.split(':')
                    if len(tmp) > 1:
                        name = tmp[0]
                        value = tmp[1]
                        if name == '日期':
                            print value
                            # print value.find(year)
                            # if value.find(year) < 0:
                            #     break
                            rid['rq'] = value
                        if name == '地点':
                            print value
                            rid['dd'] = value
                        if name == '项目名称':
                            print value
                            rid['mc'] = value
                        if name == '产品名称':
                            print value
                            rid['cp'] = value
                        if name == 'ping':
                            print value
                            rid['ping'] = value
                        if name == 'avg':
                            print value
                            rid['avg'] = value
                if len(rid) == 5:
                    p = commreport(project=rid['mc'],product=rid['cp'],site=rid['dd'],rq=rid['rq'],ping=rid['ping'],avg=rid['avg'])
                    p.save()
if __name__=='__main__':
    g = GimTestCase()
    # g.async()
    # for r in g.queryCity():
    #     print r[0]+'    '+r[1]+'    '+r[2]
    # for w in g.queryProd():
    #     print w[0]
    g.tsbg()
    # g.worklog()
    # g.tranStruct()
    g.tranStruct_CR()


