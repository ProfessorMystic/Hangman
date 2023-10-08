import random  # using random function to randomly select word for hangman


# defining a function which randomly selects a word from a list
def getword():
    wordlist = ["acid", "adept", "apple", "apricot", "ardent", "assassin", "authority", "autocracy", "autonomy",
                "bagel", "bakery", "balloon", "beautiful", "beetle", "benevolent", "best", "bottom", "bread",
                "bumblebee", "butterfly",
                "candy", "cereal", "chat", "choreography", "clutch", "contagious", "courage", "craving", "cucumber",
                "dance", "dark", "deafened", "depraved", "derisive", "diplomat", "dumbfounded", "dystopia",
                "eating", "edibles", "ephemeral", "estrogen", "ether", "entrenched",
                "factual", "forget", "folly", "freedom",
                "generous", "ghost", "glorious", "gorgeous", "greatness",
                "hardiness", "handful", "head", "height",
                "ideology", "idiom", "idleness", "idolatry", "inept", "italicize",
                "jealous", "jester", "joke", "jolly", "joyful",
                "ketchup", "kindhearted", "kinesiology", "kindle",
                "laugh", "leader", "linger", "lullaby",
                "magnanimous", "masterful", "magnificent", "meditation", "mechanical", "mindful", "monopoly", "mustard",
                "malignant", "malevolent",
                "necessary", "neither", "nice", "nuisance", "nullify",
                "odyssey", "optimal", "optimistic", "orange", "overwhelming",
                "painful", "parent", "partially", "pasta", "pastor", "pediatrician", "philosophy", "plane", "priest",
                "pudding", "psychology",
                "quantum", "quarantine", "quarrel", "quarterback", "quickly",
                "radiation", "radical", "radio", "ratify", "rent", "reprehensible",
                "sabre", "sapling", "satisfiable", "seed", "sufficient", "superfluous",
                "taciturn", "tactful", "tarnished", "testosterone", "tether", "tower", "turning", "train", "truck",
                "underworld", "underwhelming", "university", "utopia",
                "vain", "vanity", "veal", "vehicle", "velvet",
                "watch", "weightlifting", "wilderness", "wonderful", "world",
                "xerox", "xenon", "xylitol",
                "yesterday", "youthful",
                "zealous", "zebra"]
    return random.choice(wordlist).upper()  # capitalize word for less confusion in game
