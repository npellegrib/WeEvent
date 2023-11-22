from random import sample

def do_recomendation(userLikedEvents: dict, allEvents: dict) -> dict:
    categoryCounter = {}

    if len(userLikedEvents) == 0:
        return {'msg':'user has no likes'}
    else:
        # Get tha category of the events that user liked and count how many of each category are
        for i in range(len(userLikedEvents)):
            for event in allEvents:
                if event['id'] == userLikedEvents[i]['id']:
                    category = event['category']
                    categoryCounter[category] = categoryCounter.get(category, 0) + 1

        # Take all events with the category that has more likes, if there is a tie it returns all categories involved
        maxQuantity = max(categoryCounter.values())
        maxAmmountCategories = [categoria for categoria, cantidad in categoryCounter.items() if cantidad == maxQuantity]
        specificEventsMax = [evento for evento in allEvents if evento['category'] in maxAmmountCategories]

        # return the results

        if len(specificEventsMax) >= 4:
            return sample(specificEventsMax, 4)
        else:
            return specificEventsMax


# print(do_recomendation(TEST_EVENTS_LIKES, TEST_ALL_EVENTS))
