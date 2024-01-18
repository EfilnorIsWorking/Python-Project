import pygame
import random
import math

from app.timer import Timer
from app.image import Image

from app.gui import *


# function to clamp float
def clamp(a, mi, ma):
    if a <= mi:
        a = mi
    if a >= ma:
        a = ma
    return a

class BobGUI(GUI):
    def __init__(self, game, bob):
        super().__init__(game)
        self.bob = bob

        # setup UI elements
        self.frame = Frame(self, 0, 0, 250, 300, (64, 64, 64))
        self.entity = Text(self, 10, 10, text="Bob")

        self.energy = Text(self, 10, 50, text="Energy: 100", fontSize=20)
        self.velocity = Text(self, 10, 80, text="Velocity: 1.6", fontSize=20)
        self.mass = Text(self, 10, 110, text="Mass: 10", fontSize=20)
        self.perc = Text(self, 10, 140, text="Perception: 3", fontSize=20)

        self.visible = False

    def update(self):
        if self.visible:
            if self.game.menuGUI.frmMenu.active:
                self.visible = False
        mx, my = pygame.mouse.get_pos()
        if not pygame.Rect(mx-75, my-75, 150, 150).colliderect(self.bob.rect):
            self.visible = False

        if not self.game.renderingEnabled:
            self.visible = False

        # set position
        self.set_position(self.bob.get_position()[0], self.bob.get_position()[1])

        # rendering
        self.draw_element(self.frame)
        self.draw_element(self.entity)

        self.energy.set_text(f"Energy: {int(self.bob.energy)}/{self.bob.maxEnergy}")
        self.velocity.set_text(f"Velocity: {self.bob.velocity}")
        self.mass.set_text(f"Mass: {self.bob.mass}")
        self.perc.set_text(f"Perception: {self.bob.perception}")
        self.draw_element(self.velocity)
        self.draw_element(self.mass)
        self.draw_element(self.energy)
        self.draw_element(self.perc)


# bob entity class
class Bob:
    def __init__(self, game, x, y, generateRandomGenetics=True):
        self.game = game
        self.x = x
        self.y = y

        self.w = 48
        self.h = 48

        # movement
        self.speed = 30 # more = slower (interpolation speed, NOT velocity)
        self.totalMoveX = 0
        self.totalMoveY = 0

        # genetic properties
        self.velocity = 1
        self.mass = 1
        self.perception = 4

        self.energy = 100
        self.maxEnergy = 200

        # state
        self.dead = False
        self.despawned = False
        self.newborn = True
        self.foodTarget = None

        # rect
        self.rect = pygame.Rect(0, 0, 48, 48)

        # init
        if generateRandomGenetics:
            self.random_genetics()
        self.init_gui()
        self.init()

    def random_genetics(self):
        self.velocity = random.randint(8, 20)/10
        self.mass = random.randint(1, 2)/10
        self.perception = random.randint(0, 18)

        self.load_images()

    def load_images(self):
        bobImage = "bob.png"

        if self.velocity >= 1.2 and self.velocity < 1.4:
            bobImage = "bob_blue_1.png"
        elif self.velocity >= 1.4 and self.velocity < 1.6:
            bobImage = "bob_blue_2.png"
        elif self.velocity >= 1.6 and self.velocity < 1.8:
            bobImage = "bob_blue_3.png"
        elif self.velocity >= 1.8 and self.velocity < 2.0:
            bobImage = "bob_blue_4.png"
        elif self.velocity >= 2.0:
            bobImage = "bob_blue_5.png"

        self.img = Image(self.game, f"bob/{bobImage}", 64, 64)
        self.imgShadow = Image(self.game, "bob/bob_shadow.png", 64, 64)
        self.imgDead = Image(self.game, "bob/bob_dead.png", 64, 64)

    def init_gui(self):
        self.gui = BobGUI(self.game, self)
        self.game.add_gui(self.gui)

    def get_position(self):
        return [self.rect.x, self.rect.y]

    def movement(self):
        if self.dead: return

        x = 1
        y = 1

        if self.totalMoveX > 0.2:
            self.x += x / (self.speed / self.game.tickSpeedMult)
            self.totalMoveX -= 1/(self.speed / self.game.tickSpeedMult)
        elif self.totalMoveX < -0.2:
            self.x -= x/(self.speed / self.game.tickSpeedMult)
            self.totalMoveX += 1/(self.speed / self.game.tickSpeedMult)

        if self.totalMoveY > 0.2:
            self.y += y / (self.speed / self.game.tickSpeedMult)
            self.totalMoveY -= 1 / (self.speed / self.game.tickSpeedMult)
        elif self.totalMoveY < -0.2:
            self.y -= y / (self.speed / self.game.tickSpeedMult)
            self.totalMoveY += 1 / (self.speed / self.game.tickSpeedMult)

    def init(self):
        self.load_images()

        self.newbornTimer = Timer(self.game, 10, self.not_newborn, False)
        self.game.add_timer(self.newbornTimer)
        if self.newborn:
            self.newbornTimer.start()

        self.moveTimer = Timer(self.game, 1, self.random_move, True)
        self.moveTimer.start()
        self.game.add_timer(self.moveTimer)

        self.despawnTimer = Timer(self.game, 5, self.despawn, False)
        self.game.add_timer(self.despawnTimer)

        self.resize()

        # movement
        self.movementTimer = Timer(self.game, 5, self.movement, True)
        self.game.add_timer_not_tick(self.movementTimer)
        self.movementTimer.start()

    def resize(self):
        w = 64 * self.mass
        h = 64 * self.mass
        self.w = w
        self.h = h
        self.img.resize(w, h)
        self.imgShadow.resize(w, h)

    def not_newborn(self):
        self.newborn = False

    def despawn(self):
        self.game.remove_gui(self.gui)
        self.despawned = True

    # move the bob
    def move(self, x, y):
        if self.dead: return

        if self.x <= 1.5:
            x = 1
        if self.y <= 1.5:
            y = 1

        if self.x >= self.game.tilemap.sizeWidth-3:
            x = -1
        if self.y >= self.game.tilemap.sizeHeight-3:
            y = -1

        addX = x * self.velocity
        addY = y * self.velocity

        self.totalMoveX += addX
        self.totalMoveY += addY

    def get_food_targets(self):
        foods = []
        for food in self.game.tilemap.foods:
            distX = food.x - self.x
            distY = food.y - self.y
            if distX > -self.perception and distX < self.perception:
                if distY > -self.perception and distY < self.perception:
                    foods.append(food)

        return foods

    def get_hunter_targets(self):
        hunters = []
        for bob in self.game.tilemap.bobs:
            distX = abs(bob.x - self.x)
            distY = abs(bob.y - self.y)
            if distX < self.perception and distY < self.perception:
                if self.mass != 0 and bob.mass != 0:
                    if self.mass/bob.mass <= 0.67:
                        hunters.append(bob)

        return hunters

    def move_to_target(self, target, towards=True):
        xOrY = random.randint(0, 1)

        mult = 1
        if not towards:
            mult = -1

        if xOrY:
            if self.x > target.x:
                self.move(-1*mult, 0)
                return
            if self.x < target.x:
                self.move(1*mult, 0)
                return
        else:
            if self.y > target.y:
                self.move(0, -1*mult)
                return
            if self.y < target.y:
                self.move(0, 1*mult)
                return

    # move x or y
    def random_move(self):
        if self.dead: return

        # substract energy
        self.energy -= self.mass * (self.velocity ** 2)

        # to decide if bob should move to food or randomly move
        moveType = "random"

        if self.foodTarget is None or not self.foodTarget.active:
            foundFoods = self.get_food_targets()

            if len(foundFoods) > 0:
                self.foodTarget = foundFoods[0]
                moveType = "food"
            else:
                moveType = "random"
        else:
            moveType = "food"

        hunters = self.get_hunter_targets()
        if len(hunters) != 0:
            moveType = "survive hunter"

        # finally, move
        if moveType == "food":
            self.move_to_target(self.foodTarget)
        elif moveType == "random":
            mult = random.choice([1, -1])
            if random.randint(0, 1):
                self.move(1*mult, 0)
            else:
                self.move(0, 1*mult)
        elif moveType == "survive hunter":
            self.move_to_target(hunters[0], False)

    # eat a bob
    def eat_bob(self, bob):
        if self.dead: return

        if not bob.dead and not bob.newborn:
            # eat energy
            self.energy += bob.energy
            bob.energy = 0

    def draw(self):
        x = self.x
        y = self.y

        x, y = self.game.tilemap.to_isometric(x, y)

        if not self.dead:
            self.imgShadow.draw(x + 5, y + 5)
            self.img.draw(x, y)
        else:
            self.imgDead.draw(x, y)

    # update rect (for collisions)
    def update_rect(self):
        x = self.x
        y = self.y

        x, y = self.game.tilemap.to_isometric(x, y)
        y = y - self.game.camera.y
        x = x - self.game.camera.x
        x -= 16
        y -= 16

        self.rect = pygame.Rect(x-self.w/2, y-self.h/2, self.w, self.h)

    def reproduce(self):
        if not self.game.parthenoRepr: return
        if self.dead: return

        newBob = Bob(self.game, self.x, self.y)
        newBob.energy = 50
        newBob.newborn = True
        newBob.init()

        self.energy -= 150

        self.game.tilemap.bobs.append(newBob)

    def reproduce_bob(self, bob):
        if not self.game.sexualRepr: return
        if self.dead: return

        if self.energy >= 150 and bob.energy >= 150:
            newBob = Bob(self.game, self.x, self.y, False)
            newBob.energy = 100
            newBob.velocity = (bob.velocity + self.velocity) / 2
            newBob.mass = (bob.mass + self.mass) // 2
            newBob.perception = (bob.perception + self.perception) // 2
            newBob.newborn = True
            newBob.init()

            self.energy -= 100
            bob.energy -= 100

            self.game.tilemap.bobs.append(newBob)

    def update(self):
        if self.despawned: return

        # rendering
        self.update_rect()
        if self.game.renderingEnabled: self.draw()

        # enable GUI if mouse is hovering
        mx, my = pygame.mouse.get_pos()
        if pygame.Rect(mx-75, my-75, 150, 150).colliderect(self.rect):
            self.gui.visible = True
        else:
            self.gui.visible = False

        # eat food
        for food in self.game.tilemap.foods:
            if food.active:
                if food.rect.colliderect(self.rect):
                    maxEat = self.maxEnergy - self.energy
                    toEat = maxEat
                    if toEat >= food.energyGive:
                        toEat = food.energyGive

                    self.energy += toEat
                    food.energyGive -= toEat
                    if food.energyGive <= 0:
                        food.active = False

        # eat bobs
        for bob in self.game.tilemap.bobs:
            if self.rect.colliderect(bob.rect):
                try:
                    if bob.mass/self.mass < 0.67:
                        self.eat_bob(bob)
                        return
                    else: # bob.mass >= self.mass-3:
                        if not bob.newborn:
                            self.reproduce_bob(bob)
                except:
                    pass

        # dead if energy <= 0
        if self.energy <= 0:
            self.energy = 0
            if not self.dead:
                self.despawnTimer.start()
                self.dead = True

        # reproduce if energy capped
        if self.energy >= self.maxEnergy:
            self.reproduce()
