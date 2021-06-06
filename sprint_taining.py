markerCount = 5
sprints = [2, 4, 1, 3]
print("Rounds: ", 5)
print("Sprint: ", sprints)
incremental = [0] * (markerCount + 2)
for i in range(len(sprints)):
	if i < len(sprints) - 1:
		start = min(sprints[i], sprints[i + 1])
		end   = max(sprints[i], sprints[i + 1])
		# print(start, end)
		incremental[start] = incremental[start] + 1
		incremental[end + 1]= incremental[end + 1] - 1

scores = [0] * (markerCount + 1)
# print(/scores)
score = 0

for i in range(markerCount + 1):
	score = score + incremental[i]
	scores[i] = score
print("Sprint Path: ", [0,1,2,3,4,5])
print("Sprint Count: ", scores)
