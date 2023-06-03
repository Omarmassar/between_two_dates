# This code calculates the duration (hours: minutes) between tow dates

#enter hours and minutes of first date
[H1,M1]=[int(input("enter hours of first date: ")),int(input("enter minutes of first date: "))]

#enter hours and minutes of second date
[H2,M2]=[int(input("enter hours of second date: ")),int(input("enter minutes of second date: "))]


#conditions to calculate the difference
if H1 < H2 and M1 < M2:
    H,M=[H2-H1,M2-M1]
    print(H,"h",M,"m")
elif H1 < H2 and M1 > M2:
    H,M=[H2-H1-1,60-M1+M2]
    print(H,"h",M,"m")
elif H1 > H2 and M1 < M2:
    H,M=[24-H1+H2,M2-M1]
    print(H,"h",M,"m")
elif H1 > H2 and M1 > M2:
    H,M=[23-H1+H2,60-M1+M2]
    print(H,"h",M,"m")
else:
    print("Error, please try again")




