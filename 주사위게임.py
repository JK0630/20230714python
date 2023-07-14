import numpy as np
import cv2 as cv
import random as rd


class Player:
    def __init__(self, id):
        self.id = id
        self.coins = 10
        self.score = 0

    def roll_dice(self):
        dice1 = rd.randint(1, 6)
        dice2 = rd.randint(1, 6)
        total = dice1 + dice2

        if dice1 == dice2:
            dice3 = rd.randint(1, 6)
            dice4 = rd.randint(1, 6)
            total += dice3 + dice4

        return total

    def play_turn(self):
        if self.coins > 0:
            self.coins -= 1
            return self.roll_dice()
        else:
            self.coins = rd.randint(1, 10)
            return -1


class Game:
    def __init__(self, num_players):
        self.players = [Player(i) for i in range(num_players)]

    def play_round(self):
        round_results = []

        for player in self.players:
            result = player.play_turn()
            if result != -1:
                round_results.append((player, result))

        if len(round_results) > 0:  
            round_results.sort(key=lambda x: x[1])
            min_val = round_results[0][1]
            max_val = round_results[-1][1]

            for player, result in round_results:
                if result == min_val:
                    player.score -= 30
                elif result == max_val:
                    player.score += result * 2
                else:
                    player.score += result

                player.score = max(0, min(player.score, 1000))


    def display_scores(self):
        box = np.zeros((600, 1200, 3), dtype=np.uint8)
        bar_width = 1200 // len(self.players)
        bar_gap = 2  # 막대 사이의 간격을 설정 (픽셀 단위)

        # 1등인 플레이어 찾기
        max_score = max(player.score for player in self.players)
        first_place_players = [player for player in self.players if player.score == max_score]

        for i, player in enumerate(self.players):
            bar_height = int(player.score * 0.6)

            # 1등인 플레이어의 막대를 빨간색으로 그리기
            if player in first_place_players:
                color = (0, 0, 255)  # 빨간색
            else:
                color = (0, 255, 255)  # 노란형광색

            cv.rectangle(box, (i * bar_width + bar_gap, 600 - bar_height), ((i + 1) * bar_width - 1, 600), color, -1)

        cv.imshow("Scores", box)
        cv.waitKey(1)


    def play_game(self):
        while not any(player.score >= 1000 for player in self.players):
            self.play_round()
            self.display_scores()
            cv.waitKey(100)

        winner = max(self.players, key=lambda x: x.score)
        print(f"Player {winner.id} wins with a score of {winner.score}")
        cv.destroyAllWindows()


if __name__ == "__main__":
    game = Game(50)
    game.play_game()
