# menu

import subprocess as sb
#import pywhatkit as py
print("""
Press 1: to run date command
Press 2: to run docker commands
Press 3: to play song on you tube
Press 4: to run a ml code based on Simple linear Regression
Enter your hours of study (x)
""")
print(" Enter your choice : ")

ip = input()
print(type(ip))

if int(ip) == 1:
    d = sb.getoutput("date")
    print(d)
elif int(ip) == 2:
    docker = sb.getoutput("docker ps -a")
    print(docker)
elif int(ip) == 3:
    print(" Enter your song name : ")
    song = input()
    py.playonyt("song")
elif int(ip) == 4:
    print(" Enter hrs of study : ")
else:
    print("invalid input")
