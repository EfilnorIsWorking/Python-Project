import pygame


class Food:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y

        # properties
        self.initialEnergyGive = 100
        self.energyGive = self.initialEnergyGive
        self.rect = pygame.Rect(self.x, self.y, 48, 48)

        self.active = True

    # update rectangle (for collisions)
    def update_rect(self):
        x = self.x
        y = self.y

        x, y = self.game.tilemap.to_isometric(x, y)
        y = y - self.game.camera.y
        x = x - self.game.camera.x
        x -= 16
        y -= 16

        self.rect = pygame.Rect(x, y, 48, 48)

    def init(self):
        pass

    def draw(self):
        if not self.active: return

        x = self.x
        y = self.y

        x, y = self.game.tilemap.to_isometric(x, y)
        x -= 4
        y -= 6

        if self.energyGive == self.initialEnergyGive:
            self.game.imgFoodShadow.draw(x+5, y+5)
            self.game.imgFood.draw(x, y)
        else:
            self.game.imgFoodLeftoverShadow.draw(x+5, y+5)
            self.game.imgFoodLeftover.draw(x, y)

    def update(self):
        if not self.active: return

        self.update_rect()
        if self.game.renderingEnabled: self.draw()
