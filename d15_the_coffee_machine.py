# 3 Flavours - espresso, latte, cappuccino.
# Coin Operated / Note Operated.
# Notes accepted - 10, 20, 50, 100
# report input prints all resources left and money earned.

drinks = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
            "milk":0
        },
        "price":50,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "coffee":24,
            "milk":150,
        },
        "price":120,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "coffee":24,
            "milk":100,
        },
        "price":280,
    },
}

machine_storage = {
    "water":300,
    "milk":200,
    "coffee":100,
}

cash_box = 0

notes_accepted = [10, 20, 50, 100]


