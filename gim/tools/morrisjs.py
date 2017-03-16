#encoding: utf-8
import sys
class chart:
    def bar(self,ele,data,lab):
        js = '$(function() {'
        js += 'Morris.Bar({'
        js += "element: '"+ele+"',"
        js += 'data: ['
        for c in data:
            js += "{y:'"+c[1]+"',"
            js += 'a:'+str(c[0])+'},'
        js = js[:len(js)-1]
        js += '],'
        js += "xkey: 'y',ykeys: ['a'],"
        js += "labels: ['"+lab+"'],"
        js += "hideHover: 'auto',resize: true});});"
        print js
        return js
    def area(self,ele,data,lab):
        js = '$(function() {'
        js += 'Morris.Area({'
        js += "element: '"+ele+"',"
        js += 'data: ['
        for c in data:
            js += "{period:'"+str(c[0]).replace('-',' ')+"',"
            js += 'je:'+str(c[1])+'},'
        js = js[:len(js)-1]
        js += '],'
        js += "xkey: 'period',ykeys: ['je'],"
        js += "labels: ['"+lab+"'],"
        js += "pointSize: 2,hideHover: 'auto',resize: true});});"
        print js
        return js
    def save(self,name,context):
        fp = sys.path[0]+'/static/data/'+name+'.js'
        file_object = open(fp, 'w')
        file_object.write(context)
        file_object.close( )
