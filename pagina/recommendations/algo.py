from random import sample

TEST_ALL_EVENTS = [
    {"id": "1", "name": "Evento 1", "category": "Cultura"},
    {"id": "2", "name": "Evento 2", "category": "Fiesta"},
    {"id": "3", "name": "Evento 3", "category": "Tecnología"},
    {"id": "4", "name": "Evento 4", "category": "Deporte"},
    {"id": "5", "name": "Evento 5", "category": "Conferencia"},
    {"id": "6", "name": "Evento 6", "category": "Cultura"},
    {"id": "7", "name": "Evento 7", "category": "Fiesta"},
    {"id": "8", "name": "Evento 8", "category": "Tecnología"},
    {"id": "9", "name": "Evento 9", "category": "Deporte"},
    {"id": "10", "name": "Evento 10", "category": "Conferencia"},
    {"id": "11", "name": "Evento 11", "category": "Cultura"},
    {"id": "12", "name": "Evento 12", "category": "Fiesta"},
    {"id": "13", "name": "Evento 13", "category": "Tecnología"},
    {"id": "14", "name": "Evento 14", "category": "Deporte"},
    {"id": "15", "name": "Evento 15", "category": "Conferencia"},
    {"id": "16", "name": "Evento 16", "category": "Cultura"},
    {"id": "17", "name": "Evento 17", "category": "Fiesta"},
    {"id": "18", "name": "Evento 18", "category": "Tecnología"},
    {"id": "19", "name": "Evento 19", "category": "Deporte"},
    {"id": "20", "name": "Evento 20", "category": "Conferencia"}
]


TEST_EVENTS_LIKES = [
    {"id": "1"},
    {"id": "6"},
    {"id": "11"},
    {"id": "19"},
    {"id": "14"},
    {"id": "9"}
]

def do_recomendation(userLikedEvents: dict, allEvents: dict) -> dict:
    categoryCounter = {}

    if len(userLikedEvents) == 0:
        return {"msg":"user has no likes"}
    else:
        # Get tha category of the events that user liked and count how many of each category are
        for i in range(len(userLikedEvents)):
            for event in allEvents:
                if event["id"] == userLikedEvents[i]["id"]:
                    category = event["category"]
                    categoryCounter[category] = categoryCounter.get(category, 0) + 1

        # Take all events with the category that has more likes, if there is a tie it returns all categories involved
        maxQuantity = max(categoryCounter.values())
        maxAmmountCategories = [categoria for categoria, cantidad in categoryCounter.items() if cantidad == maxQuantity]
        specificEventsMax = [evento for evento in allEvents if evento["category"] in maxAmmountCategories]

        # return the results
        if len(maxAmmountCategories) == 1:
            return sample(specificEventsMax, 4)
        elif len(maxAmmountCategories) > 1:
            #TODO
            return sample(specificEventsMax, 4)
        else:
            return {'error':'an error has ocurred'}

print(do_recomendation(TEST_EVENTS_LIKES, TEST_ALL_EVENTS))
