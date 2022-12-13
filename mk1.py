import random
import pandas as pd

dfActors = pd.read_csv('actors.csv')
saved_columnAct = dfActors.Name 
actors_list = saved_columnAct.values.tolist()

dfDirectors = pd.read_csv('directors.csv')
saved_columnDir = dfDirectors.Name 
directors_list = saved_columnDir.values.tolist()

franchise = ['Star Wars', 'Marvel', 'Indiana Jones', 'DC', 'Pokémon', 'Mario', 'Captain Crunch', 'Fortnite', 'Star Trek', 'Paw Patrol', "JoJo's Byzarre Adventure", 'Chainsaw Man', 'Matrix', 'Jurassic Park', 'Berserk', 'Devil May Cry', 'Venom', 'Spider-Man', 'Avengers', 'Twin Peaks', 'Pingu']
character = ['Venom', 'Batman', 'Spider-Man', 'Anakin Skywalker', 'Darth Vader', 'Jotaro Kujo', 'Guts', 'Captain America', 'Jonathan Joestar', 'Denji', 'Dale Cooper', 'Makima', 'Doom Guy', 'Indiana Jones', 'Superman', 'Pingu', 'Link', 'Princess Zelda', 'Princess Peach', 'Mario', 'Luigi']

actortwt = random.randrange(len(actors_list))
directortwt = random.randrange(len(directors_list))
franchisetwt = random.randrange(len(franchise))
charactertwt = random.randrange(len(character))
