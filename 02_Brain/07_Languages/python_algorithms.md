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

## Two Pointers Pattern
**Concept**: Use two indices (pointers) to traverse an array or string, typically to compare elements from different positions simultaneously. Common strategies include:
-   **Converging**: One pointer at start (left), one at end (right), moving towards each other (e.g., Palindrome, Two Sum sorted).
-   **Parallel**: Both start at 0, one moves faster (e.g., Cycle Detection, Remove Duplicates).

### Valid Palindrome (LeetCode #125)
**Problem**: Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring case.

**Approach**: Two pointers converging from both ends.
*   **Time Complexity**: O(n) (traversing strictly once).
*   **Space Complexity**: O(1) (pointers only).

**Key Insight**: Filtering non-alphanumeric characters on the fly avoids creating a new string (O(n) space).

```python
def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    
    while left < right:
        # Move left pointer forward until alphanumeric char found
        while left < right and not s[left].isalnum():
            left += 1
        # Move right pointer backward until alphanumeric char found
        while left < right and not s[right].isalnum():
            right -= 1
            
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
        
    return True
```

## Sliding Window Pattern
**Concept**: Maintain a subset of elements (a "window") that satisfies a specific condition. As the window moves or expands over the data, updates are made in O(1) time.

### Best Time to Buy and Sell Stock (LeetCode #121)
**Problem**: Find maximum profit from a list of daily stock prices (buy once, sell once).

**Approach**: Dynamic Sliding Window (Left=Buy, Right=Sell).
*   **Time Complexity**: O(n)
*   **Space Complexity**: O(1)

**Key Insight**: We don't need a nested loop. We update the **minimum price seen so far** as we iterate.

```python
def maxProfit(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price  # Found a new lowest buying point
        elif price - min_price > max_profit:
            max_profit = price - min_price  # Found a new max profit
            
    return max_profit
```


