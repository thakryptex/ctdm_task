from django.shortcuts import render
from django.db import connection
from .worker import dictfetchall, colorify_data


def home(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT p.id id1, p.name name1, p.value value1, d.id id2, d.name name2, d.value value2 "
                       "FROM ctdm_person p LEFT JOIN ctdm_newdata d ON p.name = d.name "
                       "UNION ALL "
                       "SELECT p.id id1, p.name name1, p.value value1, d.id id2, d.name name2, d.value value2 "
                       "FROM  ctdm_newdata d LEFT JOIN ctdm_person p ON p.name = d.name "
                       "WHERE  p.name IS NULL;")
        data = dictfetchall(cursor)
        data = colorify_data(data)

    context = {
        'data': data
    }
    return render(request, 'index.html', context)

