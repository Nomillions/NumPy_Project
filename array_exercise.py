## Numpy Exercise
import numpy as np

## Step 1: Create a 4x3 array of all 2s
print(
    "-----------------------------------------------   STEP ONE   -----------------------------------------------"
)
twos = np.full((4, 3), 2)
print(twos)
print()

## Step 2: Create a 3x4 array with a range from 0 to 110 where each number increases by 10
print(
    "-----------------------------------------------   STEP TWO   -----------------------------------------------"
)
step1 = np.arange(0, 111, 10).reshape(3, 4)
print(step1)
print()

## Step 3: Change the layout of the above array to be 4x3, store it in a new array
print(
    "-----------------------------------------------   STEP THREE   -----------------------------------------------"
)
step2 = step1.reshape(4, 3)
print(step2)
print()

## Step 4: Multiply every element of the above array by 3 and store the new values in a different array
print(
    "-----------------------------------------------   STEP FOUR   -----------------------------------------------"
)
step3 = step2 * 3
print(step3)
print()

## Step 5: Multiply your array from step one by your array from step 2
print(
    "-----------------------------------------------   STEP FIVE   -----------------------------------------------"
)
"""step4 = twos * step1"""
## This errored out... why?
# because the first is 4x3 and second is 3x4
step4 = twos * step1.reshape(4, 3)
print(step4)
print()

## Step 6: Comment out your code from Step 5 and then multiply your array from step 1 by your array from step 3
print(
    "-----------------------------------------------   STEP SIX   -----------------------------------------------"
)
step5 = twos * step2
print(step5)
## this worked! why?
print()
