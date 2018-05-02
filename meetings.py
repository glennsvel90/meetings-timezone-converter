import datetime
import pytz

Other_Timezones = [pytz.timezone('US/Pacific'),
pytz.timezone('Europe/London'),
pytz.timezone('Asia/Calcutta'),
pytz.timezone('UTC'),
pytz.timezone('Asia/Jerusalem'),
pytz.timezone('Asia/Hong_Kong'),
pytz.timezone('Africa/Lagos')
]

fmt = '%a %b %d  %I:%M %p %Z%z'

while True:
    date_input = input("When is your meeting? Please use MM/DD/YYYY HH:MM am/pm format. ")
    try:
        # try turning a string to a datetime
        local_date = datetime.datetime.strptime(date_input, '%m/%d/%Y %I:%M %p')
    except ValueError:
        print("{} doesn't seem to be a valid date & time.".format(date_input))
    # if "try" runs smoothly, then after that, the "else" happens.
    else:
        local_date = pytz.timezone('US/Eastern').localize(local_date)
        utc_date = local_date.astimezone(pytz.utc)
        output = []
        for timezone in Other_Timezones:
            output.append(utc_date.astimezone(timezone))
        for appointment in output:
            print(appointment.strftime(fmt))
        break
