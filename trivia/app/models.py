from django.db import models
class Name(models.Model):
    your_Name = models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.your_Name
class Cricketer(models.Model):
    choice_type=(
        ('Sachin_Tendulkar','Sachin_Tendulkar'),
        ('Virat_Kolli','Virat_Kolli'),
        ('Adam_Gilchirst','Adam_Gilchirst'),
        ('Jacques_Kallis','Jacques_Kallis')
    )
    best_Cricketer = models.CharField(choices=choice_type,max_length=30)
    def __str__(self):
        return self.best_Cricketer    
class Flag(models.Model):
    choice_type=(
        ('White','White'),
        ('Yellow','Yellow'),
        ('Orange','Orange'),
        ('Green','Green')
    )
    indian_National_Flag = models.CharField(choices=choice_type,max_length=30)
    def __str__(self):
        return self.indian_National_Flag       
class Finish(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    nameforo = models.ForeignKey(Name,on_delete=models.CASCADE,related_name='nameforo')
    cricketerforo = models.ForeignKey(Cricketer,on_delete=models.CASCADE,related_name='cricketerforo')
    flagforo = models.ForeignKey(Flag,on_delete=models.CASCADE,related_name='flagforo')
    def __str__(self):
        return str(self.nameforo)
class Summary(models.Model):
    finishfor = models.ForeignKey(Finish,on_delete=models.CASCADE,related_name='finishfor')
    namefor = models.ForeignKey(Name,on_delete=models.CASCADE,related_name='namefor')
    cricketerfor = models.ForeignKey(Cricketer,on_delete=models.CASCADE,related_name='cricketerfor')
    flagfor = models.ForeignKey(Flag,on_delete=models.CASCADE,related_name='flagfor')
    def __str__(self):
        return str(self.namefor)