#coding: utf-8
import os,sys
class fp:
    def __init__(self):
        print ''
    fileList = []
    #File dictory
    def fdt(self,rootDir):
        for lists in os.listdir(rootDir):
            path = os.path.join(rootDir,lists)
            print path
            if os.path.isdir(path):
                self.fdt(path)
            else:
                self.fileList.append(path)
    def file_extension(self,path):
        return os.path.splitext(path)[1]
    def file_name(self,path):
        return os.path.basename(path)
    def save(self,name,context):
        spath = sys.path[0].replace('frame/gim','frame')
        fp = spath +'/static/data/'+name
        file_object = open(fp, 'w')
        file_object.write(context)
        file_object.close()
    def open(self,name):
        spath = sys.path[0].replace('frame/gim','frame')
        fp = spath + '/static/data/' + name
        file_object = open(fp, 'rb')
        return file_object