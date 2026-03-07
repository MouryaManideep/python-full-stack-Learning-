### Day 3 – While loop logic mistake

**What I did**

- Used a `while count >= 0` loop
- Handled `count == 0` inside an `else` block

**Problem**

- Loop logic was correct but fragile
- The loop exit depended indirectly on previous decrements
- Final action was mixed inside the loop

**Fix**

- Simplified loop condition to `while count > 0`
- Moved final action outside the loop

**Lesson**

- Loops should handle repetition only
- Final or one-time actions should be outside the loop

### practice - Hacker Rank Problems

**What I did**

- Took input using map(int, input().split())
- Stored numbers in arr
- Converted A and B into sets
- Iterated over arr

**Problem**

- Misunderstood that sets are unordered and do not support indexing sets using A[i] and B[i]
- Almost used range(m) instead of iterating directly over arr
- learned about map

**Fix**

- Replaced indexed access with membership checking (if i in A)
- Iterated directly over elements in arr
- Used sets correctly for efficient lookup (O(1) time complexity)

**Lesson**

- Sets are for membership testing, not positional access
- Always loop over the actual collection you need to process
- Simpler loops reduce logical mistakes
