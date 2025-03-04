# This is Task 6
""" 42. Merge Intervals
 Objective   : Merge overlapping intervals in a list of intervals.
 Input       : A list of intervals where each interval is represented as a pair of integers [start,end][start, end][start,end].
 Output      : A list of merged intervals.
 Hint        : Sort the intervals by start time and merge if the start of the current interval is less
                than or equal to the end of the previous one."""
def merge_intervals(a):
    if not a :
        return []
    a.sort( key=lambda x: x[0])
    merged = [a[0]]

    for start ,end in a[1:]:
        last_end = merged[-1][1]

        if start <= last_end :
            merged[-1][1] = max(last_end , end)
        else :
            merged.append([start,end])
    return  merged

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))