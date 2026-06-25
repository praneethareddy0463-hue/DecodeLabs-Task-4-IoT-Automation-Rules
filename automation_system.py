import random
import time

print("IoT Automation System Started")

for i in range(10):

    temperature = random.randint(25, 40)
    humidity = random.randint(30, 70)
    motion = random.choice(["Detected", "No Motion"])

    print(f"\nTemperature: {temperature} °C")
    print(f"Humidity: {humidity} %")
    print(f"Motion Status: {motion}")

    print("Automation Results:")

    if temperature > 35:
        print(" High Temperature Alert!")

    if humidity < 40:
        print(" Low Humidity Warning!")

    if motion == "Detected":
        print(" Motion Detected - Security Alert!")

    if temperature <= 35 and humidity >= 40 and motion == "No Motion":
        print(" All Conditions Normal")


    time.sleep(2)