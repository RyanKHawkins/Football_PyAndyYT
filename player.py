# Name:  player.py

import random


class Player:
    """
    player is on a single team, with many other players
    players play in a game for a team
    """

    def __init__(self, name, skill):
        self.name = name

        # player skill ranking
        self.skill = skill

    def salary(self):
        return 5000 + self.skill * 100

    def __str__(self):
        return f'{self.name}, Skill: {self.skill}, Salary: {self.salary()}'


def generate_player():
    first_names = [
        'Noah', 'Emma', 'Liam', 'Olivia', 'Ethan', 'Ava', 'Mason', 'Sophia',
        'Lucas', 'Isabella', 'Oliver', 'Mia', 'Aiden', 'Charlotte', 'Elijah',
        'Amelia', 'James', 'Harper', 'Benjamin', 'Abigail', 'Logan', 'Emily',
        'Jacob', 'Madison', 'Jackson', 'Ella', 'Michael', 'Lily', 'Carter',
        'Avery', 'Daniel', 'Evelyn', 'Luke', 'Sofia', 'William', 'Aria',
        'Alexander', 'Riley'
    ]

    first_name = random.choice(first_names)
    last_name = random.choice(first_names)

    full_name = f"{first_name} {last_name}"

    # generate skill and salary
    skill = 10 + random.randint(10, 100)
    return Player(full_name, skill)
