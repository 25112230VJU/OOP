#bai1
seconds = 42 * 60 + 42
print("Seconds",seconds)

#bai2
miles = 10 / 1.61
print("Miles",miles)

#bai3
time = 42 + 42/60
pace = time / miles
paceminutes = int (pace)
paceseconds = (pace - paceminutes) * 60
speed = miles / (time / 60)
print("Average pace (time per mile in minutes and seconds : )" , paceminutes , "minutes" , paceseconds , "seconds")
print("Average speed (miles per hour : )" , speed , "miles/hour")
