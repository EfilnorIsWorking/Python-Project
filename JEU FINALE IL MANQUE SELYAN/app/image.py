import pygame
import pygame._sdl2 as sdl2

# directory for images
IMAGES_DIRECTORY = "src/img/"


# custom image loading class
class Image:
    def __init__(self, game, path, w=64, h=64):
        self.game = game
        self.path = path

        # set width, height
        self.w = w
        self.h = h

        self.zoom = 1

        # anchor
        self.anchor = [0.5, 0.5]

        # load img
        self.load()

    def load(self):
        # load & set proper size (important: convert_alpha() for huge performance improvement)
        self.img = pygame.image.load(IMAGES_DIRECTORY + self.path).convert_alpha()
        self.resize(self.w, self.h)

        # get new sdl texture if gpuAcceleration is enabled
        if self.game.gpuAcceleration:
            self.get_sdl_texture()

        self.sdlTex = None

    # get SDL texture
    def get_sdl_texture(self):
        try:
            self.sdlTex = sdl2.Texture.from_surface(self.game.renderer, self.img)
        except:
            pass

    # resize image
    def resize(self, w, h):
        self.w = w
        self.h = h

        # scale image
        self.img = pygame.transform.scale(self.img, (self.w * self.zoom, self.h * self.zoom))

        # sdl2 tex?
        if self.game.gpuAcceleration:
            self.get_sdl_texture()

    # draw the image on the coords
    def draw(self, x, y):
        # blit image on window surface
        x = x - self.game.camera.x
        y = y - self.game.camera.y
        # calculate with anchor
        x = x - self.w * self.anchor[0]
        y = y - self.h * self.anchor[1]

        # check correct zoom
        if self.zoom != self.game.camera.zoom:
            self.zoom = self.game.camera.zoom
            self.load()
            self.resize(self.w, self.h)

        zoom = self.game.camera.zoom
        # dont draw if not in screen
        if x < -self.w*zoom or y < -self.h*zoom:
            return
        if x > self.game.window.w/zoom or y > self.game.window.h/zoom:
            return

        # blit
        if not self.game.gpuAcceleration:
            self.game.screen.blit(self.img, (x * self.game.camera.zoom, y * self.game.camera.zoom))
        else:
            if self.sdlTex is not None:
                self.sdlTex.draw(dstrect=(x * self.game.camera.zoom, y * self.game.camera.zoom))
            else:
                self.get_sdl_texture()
