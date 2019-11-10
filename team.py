# Name:  team.py

import copy
import random


class Team:
    """
    team has a single manager
    team has many players
    team has a ranking in a league
    team plays games against other teams
    """

    def __init__(self, name):
        self.name = name
        self.players = []

        self.wins = 0
        self.losses = 0

        self.money = 1000000

    def weekly_salary(self):
        salary = 0
        for player in self.players:
            salary += player.salary()
            return salary

    def pay_players(self):
        self.money -= self.weekly_salary()

    def rating(self):
        """
        what is the rating of the team
        """
        rating = 0
        for player in self.players:
            rating += player.skill

        return rating

    def __str__(self):
        return f"{self.name} {self.rating()}"


class Game:
    """
    plays a game between two teams
    game belongs to a league
    """

    def __init__(self, league, home_team, away_team):
        self.league = league

        self.home_team = home_team
        self.away_team = away_team

        self.home_team_won = None

        print(f"{self.home_team} vs. {self.away_team}")

    def play(self):
        """
        play the game, return who won
        True means the home team won, False means the away team won
        """
        print("Play begins")

        # insert game here

        print("Play Ends")

        if self.home_team.rating() > self.away_team.rating():
            print(f"{self.home_team} wins.")
            self.home_team_won = True
        else:
            print(f"{self.away_team} wins.")
            self.home_team_won = False


class League:
    """
    league has many teams
    each team is going to have a ranking
    within this league
    """

    def __init__(self, name, teams, players):
        self.name = name
        self.teams = teams
        self.players = players
        self.rounds_played = 0

    def set_teams(self, teams):
        self.teams = teams

    def play_round(self):
        """
        play a round, which is 3 games
        """
        print("Round begins")
        num_teams = len(self.teams)
        num_games = num_teams // 2

        teams_to_play = copy.copy(
            self.teams)  # teams_to_play = self.teams.copy()

        for game_num in range(num_games):
            home_team = random.choice(teams_to_play)
            teams_to_play.remove(home_team)
            away_team = random.choice(teams_to_play)
            teams_to_play.remove(away_team)

            game = Game(self, home_team, away_team)
            game.play()
            self.resolve_game(game)

            print("Round ends")
            self.rounds_played += 1

        # ladder status
        self.ladder()

    def ladder(self):
        for team in sorted(self.teams, key=lambda t: -t.wins):
            print(f"{team}: {team.wins} wins")

    def resolve_game(self, game):
        if game.home_team_won:
            # home team won
            game.home_team.wins += 1
            game.away_team.losses += 1
            game.home_team_won += round(200000 * random.random())
        else:
            # away team won
            game.away_team.wins += 1
            game.home_team.losses += 1
            game.away_team.money += round(200000 * random.random())

        game.home_team.pay_players()
        game.away_team.pay_players()
