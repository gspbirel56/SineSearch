# This is where the actual sine search algorithm will go.
# I will start off with a couple of test arrays and then may build out the project later.
# IP Chris Morris

test = [1, 3, 7, 9, 13, 25, 78, 103] # array, numbers are sorted

# We want to try to search for a value in this set.

searchForMe = 13

# This will define the algorithm.
def sineSearch(valueToBeSearched):
    # The algorithm will start at the very bottom, but unlike a linear search, it will gradually
    # take bigger steps across the array.
    currentindex = 0
    lowerbound = 0
    upperbound = len(test) - 1
    incrementAmount = 1
    found = False
    while found is False:
        if test[currentindex] is valueToBeSearched:
            found = True
        else
            # We have to handle a couple of edge cases in this part of the code.
            # Handle edge cases of:
            # -if we stepped below the minimum bound
            # -if we stepped above the maximum bound
            # -if we are between the two values where our searched-for value should be and the value
            # isn't actually in the index
            # Main case: value isn't found at current index of the array, so take a step slightly
            # bigger than the last step.

sineSearch(searchForMe)
