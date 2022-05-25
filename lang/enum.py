from enum import Enum
class Worker(Enum):
	MGR = 1
	SUPT = 2
	REG = 3
	CASUAL = 4
	IGNOREME = 4 # dupes silently ignored(!)

print("By name")
print(Worker.REG)
print(Worker.MGR.name)

print("By Iteration")
for w in Worker:
	print(w)
