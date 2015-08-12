from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'
    
    cat_num = models.CharField(max_length=255, unique=True)
    cat_alp = models.CharField(max_length=255, unique=True)
    cat_name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return u'%s' % (self.cat_name)
        #return u'%s-%s-%s' % (self.cat_num, self.cat_alp, self.cat_name)

class Coverage(models.Model):
    cov_num = models.CharField(max_length=255, unique=True)
    cov_alp = models.CharField(max_length=255, unique=True)
    cov_name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return u'%s' % (self.cov_name)
        #return u'%s-%s-%s' % (self.cov_num, self.cov_alp, self.cov_name)

class Source(models.Model):
    src_num = models.CharField(max_length=255, unique=True)
    src_alp = models.CharField(max_length=255, unique=True)
    src_name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return u'%s' % (self.src_name)
        #return u'%s-%s-%s' % (self.src_num, self.src_alp, self.src_name)

class Year(models.Model):
    year_num = models.IntegerField() # models.IntegerField(default=0)
    year_alp = models.CharField(max_length=255)
    year_name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return u'%s' % (self.year_name)
        #return u'%s-%s-%s' % (str(self.year_num), self.year_alp, self.year_name)

class Main(models.Model):
    category = models.ForeignKey(Category)
    coverage = models.ForeignKey(Coverage)
    source = models.ForeignKey(Source)
    year = models.ForeignKey(Year)
    basename = models.CharField(max_length=255)
    
    def __unicode__(self):
        return u'%s-%s-%s-%s-%s' % (
            self.category.cat_num,
            self.coverage.cov_num,
            self.source.src_num,
            str(self.year.year_num),
            self.basename
        )