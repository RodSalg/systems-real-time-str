import math

'''

    Student: Thiago Rodrigo Monteiro Salgado
    Professor: Dr. Lucas Cordeiro

    Federal University of Amazonas

    Real Time Systems - Master's degree subject

    to execute just put your tasks on list with dictionary with a name, period and computation time.

'''

tasks = [
    {"name": "A", "T": 25, "C": 10},
    {"name": "B", "T": 25, "C": 8},
    {"name": "C", "T": 50, "C": 5},
    {"name": "D", "T": 50, "C": 4},
    {"name": "E", "T": 100, "C": 2},
]

periods = [t["T"] for t in tasks]

TCS = math.gcd(*periods)
TCP = math.lcm(*periods)

print("System Cycle Time TCS =", TCS)
print("TCP =", TCP)
print()

for time in range(0, TCP, TCS):
    print(f"Time {time}:")
    for t in tasks:
        if time % t["T"] == 0:
            print(f"   Execute {t['name']} for {t['C']} units")
    print()
