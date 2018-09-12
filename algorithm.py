# This is where the actual sine search algorithm will go.
# I will start off with a couple of test arrays and then may build out the project later.
# IP Chris Morris

test = [1, 3, 7, 9, 13, 25, 78, 103] # array, numbers are sorted

# We want to try to search for a value in this set.

searchForMe = 13

# This will define the algorithm.
def sineSearch(value_to_be_searched):
    # The algorithm will start at the very bottom, but unlike a linear search, it will gradually
    # take bigger steps across the array.
    currentindex = 0
    lowerbound = 0 # this is an index value, NOT an actual value
    upperbound = len(test) - 1 # this is also an index value
    incrementamt = 1
    lastindex = 0
    found = False
    while found is False:
        if test[currentindex] is value_to_be_searched:
            found = True
        else:
            # We have to handle a couple of edge cases in this part of the code.
            # Handle edge cases of:
            # -if we stepped below the minimum bound
        if currentindex < lowerbound:
            # ... figure this out
            # -if we stepped above the maximum bound
        elif currentindex > upperbound:
            # ... figure this out

            # -if we are between the two values where our searched-for value should be and the value
            # isn't actually in the index
        elif incrementamt is 1 and (currentindex is lastindex + 1 or currentindex is lastindex - 1):
            # ... figure this out as well

            # Main case: value isn't found at current index of the array, so take a step slightly
            # bigger than the last step.
        else:
            # ... figure this out... You're leaving a lot of work left to do. (design the implementation with a paper trace from here)


# This is the main program.
sineSearch(searchForMe)
