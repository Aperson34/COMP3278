import datetime
insert = 'INSERT INTO CourseClass (course_id, class_id, class_date, class_time, class_end_time, class_venue, zoomlink, is_tutorial) VALUES ('
first = datetime.datetime(2023,9,5)
for i in range(0,14):
  print(insert+f'"8", "{i+1}", "{first + datetime.timedelta(days = (i-i%2)*7+2*(i%2))}", "12:30:00", "13:20:00", "CPD2.16", "https://hku.zoom.us/j/93189128050?pwd=RVZjcnl0anVDbW5OT0EzSXRON3lFdz09", False);')