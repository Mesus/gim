#coding:utf8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import common.file_processing as cfp
import common.read_office as o
import common.time_correlation as tt
from datastore.mongo_init import *
from models import *
from django.db import connection
import common.randomTools as rt
import tools.morrisjs as m
from django.contrib import auth
from datastore.sd import sll
import re
# Create your views here.
def index(request):
    # m = request.GET.get('msg')
    return render(request, 'index.html')
def async(request):
    rootDir = '/opt/p4d2'
    fp = cfp.fp()
    fp.fdt(rootDir)
    office = o.office()
    for fl in fp.fileList:
        fex = fp.file_extension(fl)
        if 'docx' in fex:
            doc = office.read_docx(fl)
            entry = {}
            entry['name'] = fp.file_name(fl)
            entry['content'] = doc
            entry['time'] = tt.timeTools().ctwithymdhms()
            insert_doc('doc',entry)
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
                        ed = erp_data(rq=d[0],gys=d[1],djbh=d[2],shbz=d[3],
                                      gbbz=d[4],wlmc=d[5],ggxh=d[6],sl=d[7],
                                      dw = d[8],jhrq=d[9],bb=d[10],ywy=d[11],
                                      ghjg=d[12],wlcdm=d[13],hsdj=d[14],dj=d[15],
                                      jshj=d[16],bm=d[17],cydw=d[18],fjs=d[19],
                                      btfjs=d[20],slsl=d[21],tlsl=d[22],
                                      zxbgbh=d[23],jhlb=d[24])
                        ed.save()
            insert_multi_docs('xls',entryList)
    return HttpResponse('Sync success')
def ghpd(request):
    name = 'ghpd'
    cursor = connection.cursor()
    cursor.execute("select count(gys),gys from gim_erp_data group by 2 order by 1 desc limit 0,10")
    row = cursor.fetchall()
    mj = m.chart()
    con = mj.bar(name,row,'供货总数')
    mj.save(name,con)
    context = {}
    context['flagjs'] = name+'.js'
    return render(request,'ghpd.html',context)
def cgje(request):
    name = 'cgje'
    cursor = connection.cursor()
    cursor.execute("select sum(dj),gys from gim_erp_data group by 2 order by 1 desc limit 0,5")
    row = cursor.fetchall()
    mj = m.chart()
    con = mj.bar(name,row,'采购金额')
    mj.save(name,con)
    context = {}
    context['flag'] = name
    return render(request,'cgje.html',context)
def dppd(request):
    name = 'dppd'
    cursor = connection.cursor()
    cursor.execute("select count(wlmc),wlmc from gim_erp_data where length(wlmc)>0 group by 2 order by 1 desc limit 0,10")
    row = cursor.fetchall()
    mj = m.chart()
    con = mj.bar(name,row,'单品数量')
    mj.save(name,con)
    context = {}
    context['flag'] = name
    return render(request,'dppd.html',context)
def dpje(request):
    name = 'dpje'
    cursor = connection.cursor()
    cursor.execute("select sum(dj),wlmc from gim_erp_data where length(wlmc)>0 group by 2 order by 1 desc limit 0,5")
    row = cursor.fetchall()
    mj = m.chart()
    con = mj.bar(name,row,'单品金额')
    mj.save(name,con)
    context = {}
    context['flag'] = name
    return render(request,'dpje.html',context)
def jeqs(request):
    name = 'jeqs'
    cursor = connection.cursor()
    cursor.execute("select distinct substr(rq,1,7),sum(dj) from gim_erp_data where id<>8168 group by 1 order by 1")
    row = cursor.fetchall()
    mj = m.chart()
    con = mj.area(name,row,'金额')
    # mj.save(name,con)
    context = {}
    context['flag'] = name
    return render(request,'jeqs.html',context)
def wqbg(request):
    rootDir = '/opt/p4d2'
    fp = cfp.fp()
    fp.fdt(rootDir)
    office = o.office()
    body = ''
    for fl in fp.fileList:
        fex = fp.file_extension(fl)
        if 'docx' in fex:
            doc = office.read_docx(fl)
            tr = '<tr class="gradeA">'
            p = doc[0]
            pa = p.split('|')
            title = pa[0]+pa[1]
            pal = len(pa)
            dw = pa[pal-4].split(' ')
            qz = pa[pal-3].replace('签字：','').replace(' ','')
            rq = pa[pal-2].replace('日期：','').replace(' ','')
            print title,dw[0],dw[2],qz,rq
            t = doc[1]
            name = t.cell(0,1).text
            num = t.cell(1,1).text
            fzr = t.cell(2,1).text
            print name,num,fzr
            tr += '<td>'+title+'</td>'

    context = {}
    return render(request,'wqbg.html')
def menu(request):
    return render(request,'menu.html')
def map(request):
    allfun = ''
    myInterval = ''
    city = queryCity()
    prod = queryProd()
    m = mi()
    r3 = rt.rtl()
    i = 0
    j = 1000
    for r in city:
        nf = ''
        funname = r3.random_str()+'()'
        nf = m.replace('name',funname).replace('title',r[0]).replace('l1',r[1]).replace('l2',r[2]).replace('h1',prod[i])
        allfun += nf
        myInterval += 'setTimeout("'+funname+'",'+str(j)+');\r\n'
        i += 1
        j += 4000
    # print allfun
    print myInterval
    context = {}
    context['interval'] = myInterval
    context['sfun'] = allfun
    return render(request,'mblocation.html',context)
def queryCity():
    cursor = connection.cursor()
    cursor.execute("select field2,field3,field4 from area where cast(field1 as int)%30=0")
    row = cursor.fetchall()
    return row
def queryProd():
    cursor = connection.cursor()
    cursor.execute("select field2 from prod")
    row = cursor.fetchall()
    prod = []
    for r in row:
        prod.append(r[0])
    return prod
def mi():
    miw = '''function name{
            var marker = new MMarker(
                    new MPoint(l1,l2),
                    new MIcon("/static/1.png", 34, 34),
                    new MInfoWindow("title", "h1")
            );
            maplet.setIwStdSize(200,100);
            maplet.addOverlay(marker);
            marker.openInfoWindow();
        }'''
    return miw

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    # username = request.GET['username']
    # password = request.GET['password']
    print username+'    '+password
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        return nav(request)
    else:
        context = {}
        context['error'] = '''<div class="alert alert-danger alert-dismissible" style="z-index:9999;" role="alert">
  <button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
  用户名或密码错误！
</div>'''
        return render(request, 'index.html',context)

def charts(request):
    y = ''
    try:
        y = request.GET['year']
    except:
        y = '2013'
    print y
    ser = ''
    cursor = connection.cursor()
    for m in range(1,13):
        year = ''
        if m < 10:
            year = y+'-0'+str(m)
        else:
            year = y+'-'+str(m)
        sql = 'select sum(dj),gys from gim_erp_data where substr(rq,1,7)="'+year
        sql += '" group by 2 order by cast(sum(dj) as real) desc limit 0,1'
        #print sql
        cursor.execute(sql)
        row = cursor.fetchall()
        for r in row:
            ser += "['"+r[1]+"',"+str(r[0])+'],'
    ser = ser[:len(ser)-1]
    print ser
    context = {}
    context['sss'] = ser
    context['yyy'] = y

    return render(request,'charts.html',context)
def sub_charts(request):
    year = request.GET['y']
    month = request.GET['m']
    month = int(month)+1
    gys = request.GET['g']
    cursor = connection.cursor()
    sql = 'select substr(rq,6,5),wlmc,dj,djbh,ggxh from gim_erp_data where cast(substr(rq,6,2) as int)=' + str(month)
    sql += ' and substr(rq,0,5)="'+year
    sql += '" and gys="'+gys +'"'
    # #print sql
    cate = ''
    setr = ''
    cursor.execute(sql)
    row = cursor.fetchall()
    for r in row:
        print r[0]+'    '+r[1]+'    '+r[2]+'    '+r[3]+'    '+r[4]
        cate += r[0] +','
        setr += r[1] + ',' + r[2] +';'
    cate = cate[:len(cate)-1]
    setr = setr[:len(setr)-1]
    ret = cate + '|' + setr
    return HttpResponse(ret)
def charts_right(request):
    y = ''
    try:
        y = request.GET['year']
    except:
        y = '2013'
    ser = ''
    cursor = connection.cursor()
    sql = 'select sum(dj),gys from gim_erp_data where substr(rq,1,4)="'+y
    sql += '" group by 2 order by cast(sum(dj) as real) desc limit 0,5'
    #print sql
    cursor.execute(sql)
    row = cursor.fetchall()
    c = ''
    for r in row:
        c += "'"+r[1]+"',"
        ser += "['"+r[1]+"',"+str(r[0])+'],'
    c = c[:len(c)-1]
    ser = ser[:len(ser)-1]
    print ser
    context = {}
    context['categ'] = c
    context['sss'] = ser
    context['yyy'] = y

    return render(request,'charts_right.html',context)
def scr(request):
    year = request.GET['y']
    month = request.GET['m']
    month = int(month)+1
    gys = request.GET['g']
    cursor = connection.cursor()
    sql = 'select rq,wlmc,dj from gim_erp_data where substr(rq,1,4)="' + year
    sql += '" and gys="'+gys
    sql += '" group by 1'
    #print sql
    cate = ''
    setr = ''
    cursor.execute(sql)
    row = cursor.fetchall()
    for r in row:
        # print r[0]+'    '+r[1]+'    '+r[2]+'    '+r[3]+'    '+r[4]
        cate += r[0] +','
        setr += r[1] + ',' + r[2] +';'
    cate = cate[:len(cate)-1]
    setr = setr[:len(setr)-1]
    ret = cate + '|' + setr
    return HttpResponse(ret)
def nav(request):
    return render(request,'nav.html')
def createData(request):
    from tests import GimTestCase
    g = GimTestCase()
    # # g.tranStruct()
    g.tranStruct_CR()
    print 'Endddddddddddddddddddd'
    return HttpResponse('Success')
def wlframe(request):
    context = {}
    type = request.GET['t']
    if type == 'report':
        context['fl'] = '/bmcr'
        context['fr'] = '/r2'
    if type == 'log':
        context['fl'] = '/lm'
        context['fr'] = '/rwl'
    return render(request,'mapFrame.html',context)
def right_worklog(request):
    context = {}
    cursor = connection.cursor()
    #年度
    sql = 'select distinct substr(rq, 1, 4) from gim_worklog'
    cursor.execute(sql)
    row = cursor.fetchall()
    print row[0]
    context['ystart'] = row[0][0]
    context['yend'] = row[len(row)-1][0]
    #人数
    sql = 'select count(distinct people) from gim_worklog'
    cursor.execute(sql)
    row = cursor.fetchall()
    context['peoplenum'] = row[0][0]
    #Chart
    sql = 'select count(distinct site),people from gim_worklog group by 2 order by 1 desc limit 0,7'
    #print sql
    cate = ''
    setr = ''
    cursor.execute(sql)
    rowm = cursor.fetchall()
    for r in rowm:
        cate += "'"+r[1]+"',"
        setr += "['" + r[1] + "'," + str(r[0]) + '],'
    cate = cate[:len(cate) - 1]
    setr = setr[:len(setr) - 1]
    context['categ'] = cate
    context['sss'] = setr
    #
    #涉及地区
    sql = 'select count(distinct site) from gim_worklog'
    cursor.execute(sql)
    row = cursor.fetchall()
    context['cs'] = row[0][0]
    #
    #
    p4s = people4site(rowm[0][1])
    context['downCate'] = p4s[0]
    context['downData'] = p4s[1]

    return render(request,'wl_right.html',context)
def people4site(p):
    cursor = connection.cursor()
    sql = 'select distinct site from gim_worklog where people = "%s"'%(p)
    #print sql
    cursor.execute(sql)
    row = cursor.fetchall()
    cate = ''
    data = ''
    i = 1
    for r in row:
        cate += "'"+r[0]+"',"
        data += str(i) + ','
    cate = cate[:len(cate) - 1]
    data = data[:len(data) - 1]
    return cate,data
def ajax_p4s(request):
    p = request.GET['p']
    p4s = people4site(p)
    ret = p4s[0].replace("'",'') + '|' + p4s[1]
    return HttpResponse(ret)
#@De
# def bmap_worklog(request):
#     year = request.GET['y']
#     fp = cfp.fp()
#     obj = fp.open('gzrz.bw')
#
#     j = 1000
#     myInterval = ''
#     for line in obj.readlines():
#         if len(line) > 0 and line.find("日期") > 0:
#             print line
#             arr = line.split(';')
#             for cell in arr:
#                 tmp = cell.split(':')
#                 if len(tmp) > 1:
#                     name = tmp[0]
#                     value = tmp[1]
#                     if name == '日期':
#                         # print value
#                         # print value.find(year)
#                         if value.find(year) < 0:
#                             break
#                     if name == '地点':
#                         print value
#                         myInterval += 'setTimeout("addMarker(point,' + "'" + value + "','" + line.replace('\r\n','') + "')" + '",' +str(j) + ');\r\n'
#                         j += 3000
#
#     content = {}
#     content['fill'] = myInterval
#     return render(request,'logMap.html',content)
def bmap_worklog(request):
    w = ' where people = "'
    try:
        y = request.GET['p']
        w += y + '"'
    except:
        w = ''
    cursor = connection.cursor()
    sql = 'select project,people,rq,site from gim_worklog'+w
    #print sql
    cursor.execute(sql)
    row = cursor.fetchall()
    j = 1000
    myInterval = ''
    for r in row:
        if len(r[3]) > 0:
            line = '项目名称:'+r[0]+';人员:'+r[1]+';日期:'+r[2]+';地点:'+r[3]+';'
            # myInterval += 'setTimeout("addMarker(point,' + "'" + r[3] + "','" + line + "')" + '",' + str(j) + ');\r\n'
            myInterval += 'addMarker(point,' + "'" + r[3] + "','" + line + "')" + ';\r\n'
            j += 3000
    content = {}
    content['fill'] = myInterval
    print myInterval
    content['zoom'] = 6
    return render(request,'logMap.html',content)
def right_report(request):
    context = {}
    cursor = connection.cursor()
    #年度
    sql = "select distinct substr(rq, 1, 4) from gim_commreport where rq <> '' order by cast(substr(rq, 1, 4) as int)"
    cursor.execute(sql)
    row = cursor.fetchall()
    print row[0]
    context['ystart'] = row[0][0]
    context['yend'] = row[len(row)-1][0]
    #年度列表
    select = ''
    for r in row:
        select += '<option>%s</option>' % (r[0])
    context['sel_y'] = select
    #
    #人数
    sql = 'select count(distinct project) from gim_commreport'
    cursor.execute(sql)
    row = cursor.fetchall()
    context['peoplenum'] = row[0][0]
    #Chart
    sql = "select count(distinct project),substr(rq, 1, 4) from gim_commreport where rq <> '' group by 2"
    #print sql
    cate = ''
    setr = ''
    cursor.execute(sql)
    rowm = cursor.fetchall()
    for r in rowm:
        cate += "'"+r[1]+"',"
        setr += "['" + r[1] + "'," + str(r[0]) + '],'
    cate = cate[:len(cate) - 1]
    setr = setr[:len(setr) - 1]
    context['categ'] = cate
    context['sss'] = setr
    #
    #涉及地区
    year = rowm[0][1]
    p4y = project4year(year)
    context['cs'] = p4y[2]
    #
    #
    context['downCate'] = p4y[0]
    context['downData'] = p4y[1]
    context['ott'] = year + '年工程地区分布'

    return render(request,'cr_right.html',context)

def project4year(year):
    cursor = connection.cursor()
    sql = 'select distinct site from gim_commreport where substr(rq,1,4)="%s"'%(year)
    #print sql
    cursor.execute(sql)
    row = cursor.fetchall()
    cate = ''
    data = ''
    i = 1
    for r in row:
        cate += "'"+r[0]+"',"
        data += str(i) + ','
    cate = cate[:len(cate) - 1]
    data = data[:len(data) - 1]
    return cate,data,len(row)
def ajax_p4y(request):
    y = request.GET['y']
    p4y = project4year(y)
    ret = p4y[0].replace("'",'') + '|' + p4y[1]  + '|' + str(p4y[2])
    print ret
    return HttpResponse(ret)
def bmap_commreport(request):
    # y = ''
    w = ' where substr(rq,1,4) = "'
    try:
        y = request.GET['year']
        w += y + '"'
    except:
        w = ''
    cursor = connection.cursor()

    sql = 'select distinct site from gim_commreport'
    #print sql
    cursor.execute(sql)
    row = cursor.fetchall()
    for rr in row:
        if sll.has_key(rr[0]) == False:
            print rr[0]

    sql = 'select project,product,rq,site,ping from gim_commreport'+w
    ##print sql
    cursor.execute(sql)
    row = cursor.fetchall()
    myInterval = ''
    for r in row:
        if len(r[3]) > 0:
            print r
            if r[4] == None:
                line = '<p>项目名称:'+r[0]+'</p><p>产品:'+r[1]+'</p><p>日期:'+r[2]+'</p><p>地点:'+r[3]+'</p>'
            else:
                line = '<p>项目名称:'+r[0]+'</p><p>产品:'+r[1]+'</p><p>日期:'+r[2]+'</p><p>地点:'+r[3]+'</p><p>PING'+r[4]+'</p>'
            print r[3]
            jwd = sll[r[3]].split(',')
            print jwd[0],jwd[1]
            myInterval += '[%s,%s,"%s"],'%(jwd[0],jwd[1],line)
    content = {}
    content['fill'] = myInterval[:len(myInterval)-1]
    content['zoom'] = 5
    return render(request,'crMap.html',content)
def ysxg(request):
    context = {}
    cursor = connection.cursor()
    #Chart
    sql = "select count(ping),'ping' from gim_commreport"
    #print sql
    cate = ''
    setr = ''
    cursor.execute(sql)
    rowm = cursor.fetchall()
    for r in rowm:
        cate += "'"+r[1]+"',"
        setr += "['" + r[1] + "'," + str(r[0]) + '],'
    cate = cate[:len(cate) - 1]
    setr = setr[:len(setr) - 1]
    context['categ'] = cate
    context['sss'] = setr
    #
    #涉及地区
    yb = ysxg_bottom('avg')
    context['downCate'] = yb[0]
    context['downData'] = yb[1]
    context['eff'] = '平均'
    return render(request,'ysxg.html',context)
def ajax_ysxg_bottom(request):
    t = request.GET['t']
    yb = ysxg_bottom(t)
    ret = yb[0].replace("'",'') + '|' + yb[1]
    print ret
    return HttpResponse(ret)
def ysxg_bottom(type):
    sql = 'select %s,project from gim_commreport where %s notnull'%(type,type)
    cursor = connection.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()
    c = ''
    d = ''
    for r in row:
        c += "'"+r[1]+"',"
        # print r[0]
        # dr = re.findall(".*了(.*)次.*", r[0].encode('utf-8'))
        # print dr
        # d += dr[0] + ','
        d += r[0] + ','
    c = c[:len(c) - 1]
    d = d[:len(d) - 1]
    return c, d