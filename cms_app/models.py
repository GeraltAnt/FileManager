from django.db import models
from filer.fields.file import FilerFileField

class Site(models.Model):
    name = models.CharField('站点名称', max_length=100)
    description = models.TextField('描述', blank=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, verbose_name='所属站点')
    name = models.CharField('物品名称', max_length=100)
    description = models.TextField('描述', blank=True)

    def __str__(self):
        return self.name

class BusinessProcess(models.Model):
    name = models.CharField('流程阶段名称', max_length=100)
    order = models.PositiveIntegerField('阶段顺序')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class ProcessFile(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='所属物品')
    process = models.ForeignKey(BusinessProcess, on_delete=models.CASCADE, verbose_name='业务流程')
    file = FilerFileField(related_name='process_files', verbose_name='文件', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item.name} - {self.process.name}"
