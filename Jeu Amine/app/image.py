import pygame
import pygame._sdl2 as sdl2

# directory for images
IMAGES_DIRECTORY = "src/img/"


# custom image loading class
class Image:
    def __init__(self, game, path, w=64, h=64):
        self.game = game
        self.w = w
        self.h = h

        self.anchor = [0.5, 0.5]

        # load & set proper size (important: convert_alpha() for huge performance improvement)
        self.img = pygame.image.load(IMAGES_DIRECTORY + path).convert_alpha()
        self.resize(w, h)

        if self.game.gpuAcceleration:
            self.get_sdl_texture()

        self.sdlTex = None

    def get_sdl_texture(self):
        try:
            self.sdlTex = sdl2.Texture.from_surface(self.game.renderer, self.img)
        except:
            pass

    def resize(self, w, h):
        self.w = w
        self.h = h

        # scale image
        self.img = pygame.transform.scale(self.img, (self.w, self.h))

        # sdl2 tex?
        if self.game.gpuAcceleration:
            self.get_sdl_texture()

    def draw(self, x, y):
        # blit image on window surface
        x = x - self.game.camera.x
        y = y - self.game.camera.y
        x = x - self.w * self.anchor[0]
        y = y - self.h * self.anchor[1]

        # dont draw if not in screen
        if x < -self.w or y < -self.h:
            return
        if x > self.game.window.w or y > self.game.window.h:
            return

        # blit
        if not self.game.gpuAcceleration:
            self.game.screen.blit(self.img, (x, y))
        else:
            if self.sdlTex is not None:
                self.sdlTex.draw(dstrect=(x, y))
            else:
                self.get_sdl_texture()
