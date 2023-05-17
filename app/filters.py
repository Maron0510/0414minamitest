from django_filters import filters
from django_filters import FilterSet
from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ItemFilter(FilterSet):

    KANRI_CHOICES = (
        ('道央', '道央'),
        ('道南', '道南'),
        ('道東', '道東'),
        ('道北', '道北'),
        ('小樽', '小樽'),
        ('本社', '本社'),
    )

    kanri = filters.ChoiceFilter(label='管理籍', choices=KANRI_CHOICES)
    name = filters.CharFilter(label='製品名', lookup_expr='contains')
    naka = filters.CharFilter(label='中型', lookup_expr='contains')
    hure = filters.CharFilter(label='フレーム', lookup_expr='contains')
    seikei = filters.CharFilter(label='成型機', lookup_expr='contains')
    created_at = filters.CharFilter(label='製造日', lookup_expr='contains')
    memo = filters.CharFilter(label='備考', lookup_expr='contains')

    order_by = MyOrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('kanri', 'kanri'),
            ('name', 'name'),
            ('naka', 'naka'),
            ('hure', 'hure'),
            ('seikei', 'seikei'),
            ('created_at', 'created_at'),
        ),
        field_labels={
            'kanri': '管理籍',
            'name': '製品名',
            'naka': '中型',
            'hure': 'フレーム',
            'seikei': '成型機',
            'created_at': '製造日',
        },
        label='並び順'
    )

    class Meta:

        model = Item
        fields = ('kanri','name','naka', 'hure','seikei','created_at', 'memo',)
