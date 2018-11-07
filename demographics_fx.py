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

def getStateName(code):
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    return states[code]

def getCounty(name,counties):
    for county in counties:
        if county["County"] == name:
            return county

def getStateInfo(state, counties):
    sdata = {}

    tPop = 0
    oPop = 0
    nCount = 0

    whites = 0
    blacks = 0
    asians = 0
    latinos = 0
    others = 0

    for county in counties:
        if county["State"] == state:
            nCount += 1
            p = county["Population"]["2014 Population"]
            oPop += county["Population"]["2010 Population"]

            w = int(county["Population"]["2014 Population"] * (county["Ethnicities"]["White Alone, not Hispanic or Latino"]/100))
            b = int(county["Population"]["2014 Population"] * (county["Ethnicities"]["Black Alone"]/100))
            a = int(county["Population"]["2014 Population"] * (county["Ethnicities"]["Asian Alone"]/100))
            l = int(county["Population"]["2014 Population"] * (county["Ethnicities"]["Hispanic or Latino"]/100))
            o = int(p - (w+b+a+l))

            # print(o)

            tPop += p
            whites += w
            blacks += b
            asians += a
            latinos += l
            others += o

    # print(whites)
    # print(blacks)
    # print(asians)
    # print(latinos)
    # print(others)

    whitePercent = (whites/tPop)*100
    blackPercent = (blacks/tPop)*100
    asianPercent = (asians/tPop)*100
    latinoPercent = (latinos/tPop)*100
    otherPercent = (others/tPop)*100

    popInc = tPop - oPop

    sdata["population"] = tPop
    sdata["num_counties"] = nCount
    sdata["population_increase"] = popInc
    sdata["white_percent"] = whitePercent
    sdata["afam_percent"] = blackPercent
    sdata["asian_percent"] = asianPercent
    sdata["latino_percent"] = latinoPercent
    sdata["other_percent"] = otherPercent

    return sdata
