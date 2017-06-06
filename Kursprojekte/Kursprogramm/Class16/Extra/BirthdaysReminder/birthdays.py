import datetime
import operator

if __name__ == '__main__':
    birthdates = {'Patrick':datetime.date(1987, 8, 22),
                  'Reini': datetime.date(1979, 12, 17),
                  'Boxi': datetime.date(1982, 1, 12),
                  'Thomas': datetime.date(1975, 11, 16),
                  'Marko': datetime.date(1989, 10, 21)}

    days_left_dict = {}
    today = datetime.datetime.now().date()

    for k,v in birthdates.iteritems():
        age_this_year = today.year - v.year
        days_left = (datetime.date(today.year,v.month,v.day) - today).days
        if days_left > 0:
            days_left_dict[k] = (days_left, v)

    sorted_x = sorted(days_left_dict.items(), key=operator.itemgetter(1))
    print sorted_x
