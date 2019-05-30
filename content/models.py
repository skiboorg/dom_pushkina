from django.db import models
from pytils.translit import slugify
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField


class News(models.Model):
    short_descr = models.CharField('Короткое описание', max_length=150, blank=False, null=False, default='')
    slug = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField('Картинка превью', upload_to='showcases/', blank=False)
    showcaseFullInfo = RichTextUploadingField('Текст новости', blank=True, null=True)
    created = models.DateField('Дата создания', auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.short_descr)
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return 'Новость - {}'.format(self.short_descr)

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новость"


class PhotoAlbum(models.Model):
    name = models.CharField('Название фотоальбома', max_length=150, blank=False, null=False, default='')
    image = models.ImageField('Обложка альбома', upload_to='Albums/', blank=False)
    name_slug = models.CharField(max_length=150, blank=True, null=True)
    created = models.DateField('Дата создания', auto_now_add=True)
    show_at_homepage = models.BooleanField('Отображать на главной?', default=False)

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(PhotoAlbum, self).save(*args, **kwargs)

    def album_cover(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.image.url))

    def __str__(self):
        return 'Фотоальбом - {}'.format(self.name)

    class Meta:
        verbose_name = "Фотоальбомы"
        verbose_name_plural = "Фотоальбом"


class Photo(models.Model):
    album = models.ForeignKey(PhotoAlbum,
                              blank=True,
                              null=True,
                              on_delete=models.SET_NULL,
                              verbose_name='В альбоме')
    image = models.ImageField('Фотография', upload_to='Photos/', blank=False)

    def image_tag(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.image.url))

    def __str__(self):
        return 'Фото в альбоме - {}'.format(self.album.name)

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"


class callBack(models.Model):
    clientName = models.CharField('Имя', max_length=255, blank=True, null=True)
    clientPhone = models.CharField('Телефон', max_length=255, blank=True, null=True)
    clientEmail = models.CharField('Email', max_length=255, blank=True, null=True)
    clientSite = models.CharField('Адрес сайта', max_length=255, blank=True, null=True)
    comment = models.TextField('Комментарий по клиенту', blank=True, null=True)
    is_done = models.BooleanField('Заявка отработана ?', default=False)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Изменена', auto_now=True)

    def __str__(self):
        return '{} - Заявка на обратный звонок. Отработана :{}'.format(self.created_at, self.is_done)

    class Meta:
        verbose_name = "Заявка на обратный звонок"
        verbose_name_plural = "Заявки на обратный звонок"

