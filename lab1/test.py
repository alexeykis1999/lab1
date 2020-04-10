import csv

def csv_reader(file):

    reader = csv.reader(file)
    call_duration = 0
    sms_number = 0
    for i in reader:
        if i[1] == "933156729": 
            call_duration+=float(i[3])
            sms_number+=int(i[4])

    call_price = call_duration * 2
    if sms_number > 10:
        sms_price = sms_number - 10
    else:
        sms_price = 0

    print("Price:",sms_price + call_price)    

with open ("data.csv", "r") as fob:
    csv_reader(fob)
