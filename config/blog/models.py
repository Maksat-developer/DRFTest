from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self) -> str:
        return f"Category name: {self.name}"
    



class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Цена', default=00.00)
    created_at = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self) -> str:
        return f"Product name {self.name}"
    


 
