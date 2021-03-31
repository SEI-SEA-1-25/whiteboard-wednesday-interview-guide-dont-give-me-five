# Whiteboard Wednesday - Interview Guide - Don't Give Me Five

## Intro

This is a good general set of steps to follow to guide someone through your problem.

You'll also find some solutions embedded at the end of this doc. You can refer to them here, or in this repo's `solution.py` file.

## Guide To Guiding

- If they get stuck with saving the values, remind them that they can make a list out of those strings with split.
  - If they ask how to use it, you can tell them that it is a method you can use on strings, and that if you give it no arguments it splits the string on the spaces.
    - If they're stuck on what splitting on spaces means: it means they get a list of _words_ from the string the user typed in.
    - If they're stuck on how to use the string method, just let them know they can write `.split()` after a string to make it a list of words.
- If they get stuck with solving this like a math problem, ask them if converting to a string might help.
  - If they can't see how it helps, ask them about ways you could compare the two strings.
  - If they're not seeing the "one string is inside another string" point, you can ask them, "Is one of these strings inside the other?"
  - If they get the concept that they can check whether a string is inside another string, but don't know how to do it in Python, you can suggest they pseudocode it... no need to teach them `in`! (The syntax of particular Python tasks is not what this is about.)
- There are two major conversions that happen in this one. If they fail to convert one, give them some breathing room to do so; only if they think they're done but they've missed a conversion, then walk through the code with them and show them (kindly!) what would happen.
- Conversions to watch for:
  - converting the input to numbers for `range` or a loop
  - converting the current num to a string when checking if it includes a 5
- At the end, if you see they would not get the last number in the range, e.g., given 3 and 6 they would only hit 3 and 4 and 5 (a common problem - range is _exclusive_, and with a loop it's easy to stop if the current num is one _less_ than the max), point it out! Ask them with a simple example: with 2 and 3 as your inputs, walk through the code with them.
  - If they still don't see it, ask them about how their particular solution handles it. Specifically: if they're using range, ask them if `range` goes up to AND INCLUDES the last number or not. If they're using a loop, ask whether their last number would meet the condition. **This isn't a quiz**, just asking them to think about it! If they don't know the answer, you can give it. (The internet would!)

## Solution(s)

```python
num1, num2 = input("What range should we cover? (separate the numbers with a space)").split()
num1 = int(num1)
num2 = int(num2)

# main solution
for num in range(num1, num2 + 1):
  if ("5" in str(num)) == False:
    print(num)

# using while loop instead of range
num = num1
while num <= num2:
  if ("5" in str(num)) == False:
    print(num)

  num += 1

# using `not` instead of `== False`
for num in range(num1, num2 + 1):
  if not "5" in str(num):
    print(num)

# with fancy inline number conversions (doesn't need lines 2-3)
for num in range(int(num1), int(num2) + 1):
  if ("5" in str(num)) == False:
    print(num)
```
