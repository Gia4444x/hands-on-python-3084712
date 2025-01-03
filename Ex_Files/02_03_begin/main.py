import statistics as s

NAMES = ["Mark", "Renjun", "Jeno", "Haechan", "Jaemin", "Chenle", "Jisung"]
AGES = [25, 24, 24, 24, 24, 23, 22]

MK = NAMES[0]
RJ = NAMES[1]

MK_RJ = NAMES[:2]
JN_HC = NAMES[2:]
maknaes = NAMES[-2:]
INFJazz = [MK, NAMES[-1]]
REVERSE = NAMES[::-1]
EVERY_OTHER = NAMES[::2]

print(sum(AGES))
print(min(AGES))
print(max(AGES))
print(round(s.mean(AGES), 2))

print(maknaes)
print(INFJazz)
print(REVERSE)

print(f"Show me who's the King!\n {NAMES[0]}")