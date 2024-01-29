from app.game import *


def main():
    game = Game()

    while game.running:
        game.update()
    


if __name__ == "__main__":
    main()
  