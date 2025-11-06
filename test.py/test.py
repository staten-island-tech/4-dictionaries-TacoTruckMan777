item = {
    "name": "Cards",
    "price": 7.99,
    "department": "Games",
    "description": "Deck for playing cards."
}

{
    "name": "pie",
    "price": 14.99,
    "department": "Food",
    "description": "Heals Hp to full."
}

{
    "name": "over priced cards",
    "price": 35.99,
    "department": "Games",
    "description": "Deck for playing cards but expensived."
}

{
    "name": "1st Edition Charzard PSA 10",
    "price": 575000.00,
    "department": "Charzard",
    "description": "good investment."
}

{
    "name": "magic cards",
    "price": 67.67,
    "department": "Games",
    "description": "cards for playing magic the gathering."
}

for index, item in enumerate(item):
    print(index, ":", item["name"])

cart