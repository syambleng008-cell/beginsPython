print("Greeting as per time:")
import time
timestamp=time.strftime("%H:%M:%S")
print("It's",timestamp," now.")
timestamp=int(time.strftime("%H"))
if timestamp >= 12 and timestamp < 18:
    print("It is",timestamp,"right now so,Good afternoon.")
elif timestamp >= 6 and timestamp < 12:
    print("It is",timestamp,"right now so,Good morning.")
else:
    print("It is",timestamp,"right now so,Good night.")
print("Hour:",timestamp)
timestamp=int(time.strftime("%M"))
print("Minute:",timestamp)
timestamp=int(time.strftime("%S"))
print("Seconds:",timestamp)



