toyShop = {
 'dolls': 500,
 'games': ['Guess who?', 'Clue', 'Battleship'],
 'puzzles': ['Star Wars', 'Batman', 'Ironman'],
 "fluffyToy": ["bear", "dog", "cat"]
}

toyShop['puzzles'].remove("Batman")
toyShop['dolls'] += 100

print(toyShop)