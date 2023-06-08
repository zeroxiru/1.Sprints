import game
import bots


def main():
    # Instantiate some SpaceBots (use your own SpaceBot class here)
    bot1 = bots.RandomAttacker("Randomizied")
    bot2 = bots.IbrahimAttacker1("IbrahimAttacker1")
    bot3 = bots.IbrahimAttacker2("IbrahimAttacker2")
    bot4 = bots.Room6Attacker("Room6Attacker")
    bot5 = bots.SmartAttacker("SmartAttacker")
    bot_list = [bot1, bot2, bot3, bot4, bot5]

    new_game = game.BattleGame(bot_list)
    new_game.start()


if __name__ == "__main__":
    main()

