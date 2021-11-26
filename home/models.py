from django.db import models

class Paciente(models.Model):
    name=models.CharField(max_length=50)
    
    class Meta:
        verbose_name = ("Paciente")
        verbose_name_plural = ("Pacientes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Paciente_detail", kwargs={"pk": self.pk})

class Tessiu(models.Model):
    temperatura = models.FloatField()
    color = models.FloatField()
    inflamation = models.FloatField(verbose_name="Inflamacion")
    name = models.ForeignKey(Paciente,blank=True, null=True,verbose_name="Nombre", on_delete=models.CASCADE)
    #fieldName = models.ManyToManyField(RelatedModel)
    #fieldName = models.OneToOneField(RelatedModel, on_delete=models.CASCADE)
     
    class Meta:
        verbose_name = ("Tejido")
        verbose_name_plural = ("Tejidos")

    def __str__(self):
        if self.name is not None:
            return str(self.temperatura) + "   " 
        else:
           return str(self.temperatura)   
    

    def get_absolute_url(self):
        return reverse("Tessiu_detail", kwargs={"pk": self.pk})


