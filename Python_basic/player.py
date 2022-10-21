class Player:
    def __init__(
            self,
            nickname: str,
            players_color: str,
            points: float = 0
    ):
        self.nickname = nickname
        self.badge_color = players_color
        self.points = points

    def increase_points(self, extra_points):
        self.points += extra_points


print("please, create a Player")

nickname = input("Nickname: ")
players_color = input("Your favourite color: ")

player_1 = Player(nickname=nickname, players_color=players_color)

print("Your current stats: ")
print(player_1.nickname)
print(player_1.badge_color)


player_1.increase_points(420)
print(player_1.points)


class Round:
    pass
