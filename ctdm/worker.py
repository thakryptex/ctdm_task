def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def colorify_data(data):
    for d in data:
        color = 'white'
        if d['name1'] != d['name2'] and d['name1'] is None:
            color = 'green'
        elif d['name1'] != d['name2'] and d['name2'] is None:
            color = 'red'
        elif d['value1'] != d['value2']:
            color = 'blue'
        d.update((k, '') for k, v in d.items() if v is None)
        d.update({'color': color})
    return data
