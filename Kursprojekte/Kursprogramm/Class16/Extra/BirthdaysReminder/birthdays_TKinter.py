import datetime
import operator
import tkMessageBox
import Tkinter as tk

if __name__ == '__main__':
    birthdates = {'Patrick':datetime.date(1987, 8, 22),
                  'Markus': datetime.date(1984, 4, 1),
                  'Stefan': datetime.date(1983, 6, 7),
                  'MarkusW': datetime.date(1982, 8, 3),
                  'Leni': datetime.date(1990, 12, 11)}

    days_left_dict = {}
    today = datetime.datetime.now().date()

    for k,v in birthdates.iteritems():
        age_this_year = today.year - v.year
        days_left = (datetime.date(today.year,v.month,v.day) - today).days
        if days_left > 0:
            days_left_dict[k] = days_left

    sorted_x = sorted(days_left_dict.items(), key=operator.itemgetter(1))


    if len(sorted_x)>0:
        msg = "This is a list of the next birthdays of your friends: \n"
        for k,v in sorted_x:
            msg += "%20s (%s), %i days\n"%(k,birthdates[k].isoformat(),v)
        root = tk.Tk()
        root.withdraw()
        tkMessageBox.showinfo('Upcoming Birthdays',msg)
