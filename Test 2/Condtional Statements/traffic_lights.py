# Implement a traffic light simulator (Red, Yellow, Green).
import random

light = ["red" , "yellow", "green"]
traffic_light = random.choice(light)

if traffic_light == "red":
    print("Red")
elif traffic_light == "yellow":
    print("Yellow")
elif traffic_light == "green":
    print("Green")

print("'stop' - red \n'ready' - yellow \n'go' - green")

while bool(traffic_light) == True:
    user_input = str(input("Follow the traffic lights: ")).lower()
    if user_input == "stop" and traffic_light == "red":
        print("ready for the next signal.")
    elif user_input == "ready" and traffic_light == "yellow":
        print("Be ready. Start your vehicle.")
    elif user_input == "go" and traffic_light == "green":
        print("Go to your destination.")
    else:
        print("You jumped the traffic lights. Follow the rules.")
    break 