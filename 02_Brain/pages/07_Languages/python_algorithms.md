---
tags:
  - languages
---

# Python Algorithms & Interview Prep

## Contains Duplicate (LeetCode #217)
**Problem**: Given an integer array, return `true` if any value appears at least twice.

**Approach**: Use a HashSet to track seen elements.
*   Time Complexity: O(n)
*   Space Complexity: O(n)

**Key Insight**: Trading space for time by using a HashSet for O(1) lookups.

```python
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

### Related
- [[java]]
