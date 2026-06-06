aspects = {
    "Room": [
        "room",
        "bed",
        "washroom"
    ],

    "Service": [
        "service",
        "waiter",
        "staff"
    ],

    "Food": [
        "food",
        "taste",
        "meal"
    ],

    "Location": [
        "location",
        "place",
        "market"
    ],

    "Cleanliness": [
        "clean",
        "dirty",
        "hygiene"
    ]
}

def detect_aspects(text):

    found = []

    text = text.lower()

    for aspect, words in aspects.items():

        for word in words:

            if word in text:
                found.append(aspect)
                break

    return found