import json

def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    lowest = counties[0]["County"]

    for county in counties:
        lowest = county["County"] if county["County"] < lowest else lowest

    return lowest


def county_most_under_18(counties):
    """Return the name and state of a county ("<county name>, <state>") with the highest percent of under 18 year olds."""
    highest = counties[0]

    for county in counties:
        highest = county if county["Age"]["Percent Under 18 Years"] > highest["Age"]["Percent Under 18 Years"] else highest

    return [highest["County"], highest["State"]]

def getStates(counties):
    states = []
    for county in counties:
        if county["State"] not in states:
            states.append(county["State"])

    return states

def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""
    highest = 0

    for county in counties:
        highest = county["Age"]["Percent Under 18 Years"] if county["Age"]["Percent Under 18 Years"] > highest else highest

    return highest

def most_under_18(counties):
    """Return a list with the name and state of a county ("<county name>, <state>") and the percent of under 18 year olds for a county with the highest percent of under 18 year olds."""
    highest = counties[0]

    for county in counties:
        highest = county if county["Age"]["Percent Under 18 Years"] > highest["Age"]["Percent Under 18 Years"] else highest

    return [highest["County"], highest["State"], highest["Age"]["Percent Under 18 Years"]]

def state_with_most_counties(counties):
    """Return a state that has the most counties."""
    states = {}

    for county in counties:
        state = county["State"]
        if state not in states:
            states[state] = 1
        else:
            states[state] += 1

    max = 0
    res = "CA"

    for state, cNum in states.items():
        if cNum > max:
            res = state

    return res

def getCounties(state, counties):
    countiesOut = []

    for county in counties:
        if county["State"] == state:
            countiesOut.append(county["County"])

    return countiesOut

def getVeterans(county, state, counties):
    for countyL in counties:
        if countyL["County"] == county and countyL["State"] == state:
            return countyL["Miscellaneous"]["Veterans"]

    return -1

def total_foreign_born(state, counties):
    total = 0

    for county in counties:
        if county["State"] == state:
            percent_foreign = float(county["Miscellaneous"]["Foreign Born"])/100
            total_pop = float(county["Population"]["2010 Population"])
            total += (percent_foreign * total_pop)

    return int(total)

def greatest_building_permits_per_housing_unit(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""
    max = 0

    for county in counties:
        try:
            val = county["Miscellaneous"]["Building Permits"]/county["Housing"]["Housing Units"]
        except ZeroDivisionError as e:
            pass

        max = val if val > max else max

    return max
