from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from django.utils.html import mark_safe

# Create your models here.
User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, уместен ли торг')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Пользователь')
    image = models.ImageField('Изображение', upload_to = 'advertisements/')
    @admin.display(description='дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    @admin.display(description='дата обновления')
    def update_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: purple; font-weight: bold;">Сегодня в {}</span>', updated_time
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    # def get_avatar(self):
    #     if self.image == '1':
    #         return '/static/img/advd.png'
    #     return self.image.url
    
    # @admin.display(description='миниатюра')
    # def avatar_tag(self):
    #     return format_html('<img src="%s" width="50" height="50" />' % self.get_avatar())

    @admin.display(description='миниатюра')
    def show_mini_image(self):
        if self.image == '1':
            return '/static/img/advd.png'
        return format_html('<img src="{}" width="50" height="50" />', self.image.url)

    def get_absolut_url(self):
        return reverse('adv-detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'advertisements'
    
    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price}'