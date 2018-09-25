import matplotlib.pyplot as plt
Initial_Velocity = 0
Speed_Limit = 60
Time_On_Road = int(input("Enter time on road"))
Acceleration = int(input("Enter acceleration"))
Distance = int(input("Enter Distance"))
Time = 1
Speed = 0
Speed = Initial_Velocity + Acceleration*Time_On_Road
x=[]
y=[]
for i in range(int(Time_On_Road)):
    s = (1/2)*Acceleration* ((i)**2)
    Star_no = s // 5
    print("Duration : ",i," Distance : ",end="")
    for j in range ( int(Star_no)):
        print("*",end="")
    print("\n")
    x.append(i)
    y.append(s)
plt.plot(x,y)
plt.show()