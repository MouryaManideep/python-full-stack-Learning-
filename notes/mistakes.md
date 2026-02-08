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
