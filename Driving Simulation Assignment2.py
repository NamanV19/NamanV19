Initial_Velocity = 0
Speed_Limit = 60
Time_On_Road = int(input("Enter time on road"))
Acceleration = int(input("Enter acceleration"))
Distance = int(input("Enter Distance"))
Time = 1
Speed = 0
Speed = Initial_Velocity + Acceleration*Time_On_Road

if Speed > 60:
    print("The person went over the speed limit. Max speed was " + str(Speed))
else:
    print("The person did not go over the speed limit. Max speed was" + str(Speed))

while Time <= Time_On_Road:

 Distance = Initial_Velocity*Time + 0.5*Acceleration*Time*Time
 Distance = Distance/10
 print("Duration: " +str(Time) + " Distance: " + int(Distance)*"*")

 Time = Time + 1

Distance = Distance*10
print("The person reached the destination. Distance travelled " + str(Distance))


