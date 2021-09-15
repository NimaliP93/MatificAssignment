from django.db.models import Window, F, Avg
from django.db.models.functions import PercentRank


def get_players_with_percentile(queryset, percentile):
    queryset = queryset.annotate(Avg('player__score')).annotate(score_percentile=Window(
        expression=PercentRank(),
        order_by=F('player__score__avg').asc()
    ))

    data = []

    for element in queryset:
        print(element.score_percentile)
        if element.score_percentile >= float(percentile):
            data.append(element)

    return data
