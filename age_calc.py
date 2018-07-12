from datetime import datetime
new=datetime.now()
print(new)
old=input("Enter your date of birth(dd mm yyyy) :- ")
dob=datetime.strptime(old,"%d %m %y")
print(dob)
#y=new.year-dob.year

if new.month>dob.month:
    m=new.month-dob.month
elif new.month<dob.month:
    if new.day>dob.day:
        m=new.month-dob.month+12
    elif new.day<dob.day:
        m=new.month-dob.month+11
    
'''        
d=new.day-dob.day
h=new.hour-dob.hour
mn=new.minute-dob.minute
s=new.second-dob.second
ms=new.microsecond-dob.microsecond

print("Here is your age stats :- ")
print("Years :- ",y)
print("Months :- ",m)
print("Days :- ",d)
print("Hours :- ",h)
print("Minutes :- ",mn)
print("Seconds :- ",s)
print("Microseconds :- ",ms)
print()
'''
d=(new-dob).days
yr=d//365
mon=yr*12+m
hr=d*24
min=hr*60
sec=min*60
ms=sec*1000
mics=sec*1000000
print("Here is your age calculation :- ")
print("Age in years :- ",yr)
print("Age in months :- ",mon)
print("Age in days :- ",d)
print("Age in hours :- ",hr)
print("Age in minutes :- ",min)
print("Age in seconds :- ",sec)
print("Age in milliseconds :- ",ms)
print("Age in microseconds :- ",mics)