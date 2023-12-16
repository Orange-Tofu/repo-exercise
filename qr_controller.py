import random

content = [
    "https://youtu.be/dQw4w9WgXcQ?si=XatZH3LX2xPvymIh", #Rick Roll
    "https://youtu.be/YLF4sKkUzSQ?si=_hjIoHX62C4S_sbx", #Dilon Ka Shotter
    "https://youtu.be/i1ojUmdF42U?si=NBvGQxKho-qZF2rP", #Emotional Damage
    #Add more here
]

def get_data():
    print(random.choice(content))

get_data()