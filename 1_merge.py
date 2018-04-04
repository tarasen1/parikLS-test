def merge_intervals(intervals):
	intervals = sorted(intervals, key = lambda interval: interval[0])
	i=0	
	while i<len(intervals)-1:
		if intervals[i][1] >= intervals[i+1][0]:
			if intervals[i+1][1]>=intervals[i][1]:
				intervals[i] = (intervals[i][0], intervals[i+1][1])
			intervals.pop(i+1)
		else:
			i+=1
	print(intervals)





if __name__ == '__main__':
	merge_intervals([(1,4),(5,6),(3,4),(7,10),(9,13)])
	merge_intervals([(1,3), (4, 6), (1, 7), (9, 10)])  # [(1, 7), (9, 10)]
	merge_intervals([(1,2), (4, 6), (1, 3)])  # [(1, 3), (4, 6)]
	merge_intervals([(9, 10), (8, 10), (0, 1)])  # [(0, 1), (8, 10)]