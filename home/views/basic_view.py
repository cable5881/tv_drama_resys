from django.db.models import Q
from django.shortcuts import render, redirect

from meiju.models.drama import Drama
from meiju.models.drama_type import DramaType


def to_index(request):
    latest_drama_list = Drama.objects.order_by('-year')[:6]

    types = DramaType.objects

    sci_magic_types = types.filter(Q(type='奇幻') | Q(type='科幻') | Q(type='灾难'))
    sci_magic_dramas = Drama.objects.filter(
        Q(types=sci_magic_types[0]) |
        Q(types=sci_magic_types[1]) |
        Q(types=sci_magic_types[2])
    ).distinct()
    sci_magic_new_dramas = sci_magic_dramas.order_by('-year', '-avg_rating')[:6]
    sci_magic_top10_dramas = sci_magic_dramas.order_by('-avg_rating')[:10]

    supernatural_scary_types = types.filter(Q(type='恐怖') | Q(type='惊悚'))
    supernatural_scary_dramas = Drama.objects.filter(
        Q(types=supernatural_scary_types[0]) |
        Q(types=supernatural_scary_types[1])
    ).distinct()
    supernatural_scary_new_dramas = supernatural_scary_dramas.order_by('-year', '-avg_rating')[:6]
    supernatural_scary_top10_dramas = supernatural_scary_dramas.order_by('-avg_rating')[:10]

    urban_emotional_types = types.filter(Q(type='喜剧') | Q(type='家庭') | Q(type='爱情'))
    urban_emotional_dramas = Drama.objects.filter(
        Q(types=urban_emotional_types[0]) |
        Q(types=urban_emotional_types[1]) |
        Q(types=urban_emotional_types[2])
    ).distinct()
    urban_emotional_new_dramas = urban_emotional_dramas.order_by('-year', '-avg_rating')[:6]
    urban_emotional_top10_dramas = urban_emotional_dramas.order_by('-avg_rating')[:10]

    crime_historic_types = types.filter(Q(type='传记') | Q(type='历史') | Q(type='犯罪'))
    crime_historic_dramas = Drama.objects.filter(
        Q(types=crime_historic_types[0]) |
        Q(types=crime_historic_types[1]) |
        Q(types=crime_historic_types[2])
    ).distinct()
    crime_historic_new_dramas = crime_historic_dramas.order_by('-year', '-avg_rating')[:6]
    crime_historic_top10_dramas = crime_historic_dramas.order_by('-avg_rating')[:10]

    return render(request, 'home/index.html', {
        'sci_magic_new_dramas': sci_magic_new_dramas,
        'sci_magic_top10_dramas': sci_magic_top10_dramas,
        'supernatural_scary_new_dramas': supernatural_scary_new_dramas,
        'supernatural_scary_top10_dramas': supernatural_scary_top10_dramas,
        'urban_emotional_new_dramas': urban_emotional_new_dramas,
        'urban_emotional_top10_dramas': urban_emotional_top10_dramas,
        'crime_historic_new_dramas': crime_historic_new_dramas,
        'crime_historic_top10_dramas': crime_historic_top10_dramas,
    })
