from test.recommander import recommendations

# matches = recommendations.topMatches(recommendations.critics, 'Toby', n=3)
# print(matches)

# res = recommendations.getRecommendations(recommendations.critics, 'Toby')
# print(res)

# matches = recommendations.topMatches(recommendations.movies, 'Superman Returns', n=3)
# print(matches)

# sim_items = recommendations.calculateSimilarItems(recommendations.movies, n=3)
# print(sim_items)

sim_items = recommendations.calculateSimilarItems(recommendations.movies, n=10, similarity=recommendations.sim_distance)
re_items = recommendations.getRecommendedItems(recommendations.critics, sim_items, 'Jack Matthews')
print(re_items)
