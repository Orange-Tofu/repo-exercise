import random

content = [
    "https://youtu.be/dQw4w9WgXcQ?si=XatZH3LX2xPvymIh", #Rick Roll
 "https://youtu.be/i1ojUmdF42U?si=NBvGQxKho-qZF2rP", #Emotional Damage
    
#Add more links to memes here in the given format
]

def get_data():
    return random.choice(content)
