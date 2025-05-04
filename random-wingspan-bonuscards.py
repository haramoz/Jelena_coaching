import random

def generate_bonus_card():
    # Sample bonus card categories and examples
    card_categories = {
        "Nest Type": ["Birds with Bowl Nests", "Birds with Platform Nests", "Birds with Cavity Nests"],
        "Bird Type": ["Birds with Predatory Powers", "Birds that Eat Worms", "Birds that Eat Fish"],
        "Habitat": ["Birds in Forests", "Birds in Wetlands", "Birds in Grasslands"],
        "Eggs": ["Birds that can hold 4+ eggs", "Birds that can hold 3 eggs", "Birds with no egg limit"],
        "Size": ["Birds with Wingspan > 100cm", "Birds with Wingspan < 30cm", "Birds with Wingspan between 50-75cm"],
    }

    # Randomly choose a category
    category = random.choice(list(card_categories.keys()))

    # Randomly choose a bonus card within the category
    bonus_card = random.choice(card_categories[category])

    return {"Category": category, "Bonus Card": bonus_card}

# Generate a random bonus card
if __name__ == "__main__":
    card = generate_bonus_card()
    print(f"Bonus Card Category: {card['Category']}")
    print(f"Bonus Card: {card['Bonus Card']}")
