from math import sqrt

# Returns a distance-based similarity score for person1 and person2


def sim_distance(prefs, person1, person2):
    # Get the list of shared_items
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    # if they have no ratings in common, return 0
    if len(si) == 0:
        return 0

    # Add up the squares of all the differences
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2)
                          for item in prefs[person1] if item in prefs[person2]])

    return 1 / (1 + sum_of_squares)


# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(prefs, p1, p2):
    # Get the list of mutually rated items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    # if they are no ratings in common, return 0
    if len(si) == 0:
        return 0

    # Sum calculations
    n = len(si)

    # Sums of all the preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    # Sums of the squares
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])

    # Sum of the products
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    # Calculate r (Pearson score)
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0

    r = num / den

    return r


# Returns the best matches for person from the prefs dictionary.
# Number of results and similarity function are optional params.
def topMatches(prefs, item, n=6, similarity=sim_pearson):
    scores = [(similarity(prefs, item, other), other)
              for other in prefs if other != item]
    scores.sort()
    scores.reverse()
    return scores[0:n]


def calculateSimilarItems(prefs, n=6, similarity=sim_pearson):
    result = {}

    for item in prefs:
        scores = topMatches(prefs, item, n=n, similarity=similarity)
        result[item] = scores
    return result


def getRecommendedItemsByUserReviews(item_match, user_ratings):
    scores = {}
    total_sim = {}

    for (item, rating) in user_ratings.items():
        for (similarity, item2) in item_match[item]:

            if item2 in user_ratings:
                continue

            scores.setdefault(item2, 0)
            scores[item2] += similarity * rating

            total_sim.setdefault(item2, 0)
            total_sim[item2] += similarity

    rankings = [(item, score / total_sim[item]) for item, score in scores.items()]

    rankings.sort()
    rankings.reverse()
    return rankings



