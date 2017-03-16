from django.db import models

# Create your models here.

class erp_data(models.Model):
    rq = models.CharField(max_length = 150,null=True)
    gys = models.CharField(max_length = 150,null=True)
    djbh = models.CharField(max_length = 150,null=True)
    shbz = models.CharField(max_length = 2,null=True)
    gbbz = models.CharField(max_length = 2,null=True)
    wlmc = models.CharField(max_length = 150,null=True)
    ggxh = models.CharField(max_length = 150,null=True)
    sl = models.CharField(max_length = 150,null=True)
    dw = models.CharField(max_length = 150,null=True)
    jhrq = models.CharField(max_length = 150,null=True)
    bb = models.CharField(max_length = 150,null=True)
    ywy = models.CharField(max_length = 150,null=True)
    ghjg = models.CharField(max_length = 150,null=True)
    wlcdm = models.CharField(max_length = 150,null=True)
    hsdj = models.CharField(max_length = 150,null=True)
    dj = models.CharField(max_length = 150,null=True)
    jshj = models.CharField(max_length = 150,null=True)
    bm = models.CharField(max_length = 150,null=True)
    cydw = models.CharField(max_length = 150,null=True)
    fjs = models.CharField(max_length = 150,null=True)
    btfjs = models.CharField(max_length = 150,null=True)
    slsl = models.CharField(max_length = 150,null=True)
    tlsl = models.CharField(max_length = 150,null=True)
    zxbgbh = models.CharField(max_length = 150,null=True)
    jhlb = models.CharField(max_length = 150,null=True)
    # timestamp = models.DateTimeField()
# class city(models.Model):
#     name = models.CharField(max_length = 150,null=True)
#     lo = models.CharField(max_length = 150,null=True)
#     la = models.CharField(max_length = 150,null=True)
# class product(models.Model):
#     name = models.CharField(max_length = 150,null=True)
class worklog(models.Model):
    project = models.CharField(max_length = 150,null=True)
    people = models.CharField(max_length = 150,null=True)
    rq = models.CharField(max_length = 150,null=True)
    site = models.CharField(max_length = 150,null=True)
class commreport(models.Model):
    project = models.CharField(max_length = 150,null=True)
    product = models.CharField(max_length = 150,null=True)
    rq = models.CharField(max_length = 150,null=True)
    site = models.CharField(max_length = 150,null=True)
    ping = models.CharField(max_length = 150,null=True)
    avg = models.CharField(max_length = 150,null=True)
