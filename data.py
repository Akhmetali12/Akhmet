from datetime import datetime, timedelta
current_date = datetime.now()
new_date = current_date - timedelta(days=5)
print(current_date.strftime("%Y-%m-%d"))
print(new_date.strftime("%Y-%m-%d")) 


from datetime import datetime, timedelta
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday: ", yesterday.strftime("%Y-%m-%d"))
print("Today: ", today.strftime("%Y-%m-%d"))
print("Tomorrow: ", tomorrow.strftime("%Y-%m-%d"))


from datetime import datetime
current_datetime = datetime.now()
current_datetime_no_microseconds = current_datetime.replace(microsecond=0)
print(current_datetime)
print(current_datetime_no_microseconds) 


from datetime import datetime
date1 = datetime(2024, 6, 20, 12, 0, 0)
date2 = datetime(2024, 6, 25, 12, 0, 0) 
difference = date2 - date1
difference_in_seconds = difference.total_seconds()
print(difference_in_seconds) 


