from app.game import *


def main():
    game = Game()

    while game.running:
        game.update()
    game.savefile.save()


if __name__ == "__main__":
    main()
