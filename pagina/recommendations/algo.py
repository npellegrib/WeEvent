from random import sample

def do_recomendation(userLikedEvents: dict, allEvents: dict, isAuth: bool) -> dict:
    categoryCounter = {}

    if isAuth is True:
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

        if len(specificEventsMax) >= 3:
            return sample(specificEventsMax, 3)
        else:
            return specificEventsMax
    elif isAuth is False:
        if len(allEvents) >= 3:
            return sample(allEvents, 3)
        else:
            return allEvents


# print(do_recomendation(TEST_EVENTS_LIKES, TEST_ALL_EVENTS))
