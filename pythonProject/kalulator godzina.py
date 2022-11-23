response=input("What time is now?")
hr=int(response)
response=input("Set the number of hours to wait")
wt=int(response)
a=(hr+wt)%24
print("Alarm time is set to:",a)