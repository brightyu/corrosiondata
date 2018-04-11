from django.db import models
from django.http import Http404
from django.shortcuts import get_object_or_404

class BaseManager(models.Manager):
    def get_or_none(self, *args, **kwargs):
        try:
            return self.get(*args, **kwargs)
        except self.model.DoesNotExist:
            return None

    def get_or_404(self, *args, **kwargs):
        try:
            return self.get(*args, **kwargs)
        except self.model.DoesNotExist:
            raise Http404('您查找的 {t} 并不存在。（查询参数 {a} {k}）'.format(t=self.model.__name__, a=args or '', k=kwargs or ''))


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    objects = BaseManager()

    class Meta:
        abstract = True

    def toArray(self):
        self.created = self.created.isoformat(' ')
        self.modified = self.modified.isoformat(' ')
        return model_to_dict(self)

class Environment(BaseModel):
    environmentid = models.IntegerField()
    time = models.DateField()
    location = models.CharField(max_length=40)
    sunshine = models.CharField(max_length=40)
    hcl = models.CharField(max_length=40)
    so2 = models.CharField(max_length=40)
    ph = models.CharField(max_length=40)
    rain = models.CharField(max_length=40)


class Chemical(BaseModel):
    chemicalid = models.IntegerField()
    chemicalname = models.CharField(max_length=40)
    P = models.CharField(max_length=40)
    C = models.CharField(max_length=40)
    S = models.CharField(max_length=40)
    Cu = models.CharField(max_length=40, default=3.2)
    Si = models.CharField(max_length=40)

class CorrosionResult(BaseModel):
    corrosionid = models.IntegerField()
    environmentid = models.IntegerField()
    chemicalid = models.IntegerField()
    starttime = models.DateField()
    endtime = models.DateField()
    corrosionrate = models.CharField(max_length=40)

    @property
    def material(self):
        return Chemical.objects.filter(chemicalid = self.chemicalid)

    @property
    def environment(self):
        return Environment.objects.filter(environmentid = self.environmentid)
