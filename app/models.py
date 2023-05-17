from django.db import models
from django.core import validators


class Item(models.Model):

    KANRI_CHOICES = (
        ('道央', '道央'),
        ('道南', '道南'),
        ('道東', '道東'),
        ('道北', '道北'),
        ('小樽', '小樽'),
        ('本社', '本社'),
    )
    hoka_CHOICES = (
        (True, '自社'),
        (False, '他社'),
    )
    ZUMEN_CHOICES = (
        (True, 'あり'),
        (False, 'なし'),
    )

    kanri = models.CharField(
        verbose_name='管理籍',
        max_length=10,
        choices=KANRI_CHOICES,
        default='道央'
    )

    name = models.CharField(
        verbose_name='製品名',
        max_length=200,
        unique=True,
    )
    naka = models.CharField(
        verbose_name='中型',
        max_length=200,
    )
    hure = models.CharField(
        verbose_name='フレーム',
        max_length=200,
        validators=[validators.RegexValidator(regex=r'^[a-zA-Z0-9_@\-\.]+$')]
    )
    idou = models.IntegerField(
        verbose_name='フレーム高さ移動側',
        default=0
    )
    kotei = models.IntegerField(
        verbose_name='フレーム高さ固定側',
        default=0
    )
    tori = models.DecimalField(
        verbose_name='取数',
        default=0,
        max_digits=5,
        decimal_places=1,
    )
    metuke = models.DecimalField(
        verbose_name='目付',
        default=0,
        max_digits=5,
        decimal_places=1,
    )
    hoka = models.BooleanField(
        verbose_name='他社金型',
        choices=hoka_CHOICES,
        default=True
    )
    seikei = models.CharField(
        verbose_name='成型機',
        max_length=200,
    )
    zumen = models.BooleanField(
        verbose_name='製品図面',
        choices=ZUMEN_CHOICES,
        default=True
    )
    memo = models.TextField(
        verbose_name='備考',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='製造日',
        #auto_now_add=True
    )
    
    # hureを大文字に変換する
    #def save(self, *args, **kwargs):
        #self.hure = self.hure.upper()
        #super().save(*args, **kwargs)

    # 以下は管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'

