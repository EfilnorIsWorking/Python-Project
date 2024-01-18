import pygame
import pygame._sdl2 as sdl2


# window class
class Window:
    def __init__(self, game):
        self.game = game

        # win settings
        self.title = "Isometric Bob Game"
        self.icon = pygame.image.load("src/img/icon.png")
        self.w = 800
        self.h = 800

        # init window
        if not self.game.gpuAcceleration:
            self.normal_init()
        else:
            self.gpu_init()

        # setup game clock
        self.clock = pygame.time.Clock()
        self.tickFPS = 360
        self.fps = 0
        self.deltaTime = 0

        # mouse position saving
        self.mouseDownPos = [0, 0]
        self.mouseUpPos = [0, 0]

    def normal_init(self):
        self.screen = pygame.display.set_mode((self.w, self.h), pygame.SCALED | pygame.RESIZABLE | pygame.WINDOWPOS_CENTERED)
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(self.icon)

    def gpu_init(self):
        pygame.display.set_mode((self.w, self.h), pygame.SCALED | pygame.RESIZABLE | pygame.WINDOWPOS_CENTERED)
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(self.icon)
        self.win = pygame.Window.from_display_module()
        self.renderer = sdl2.Renderer.from_window(self.win)
        self.screen = self.win.get_surface()

    def handle_events(self):
        if not self.game.running: return

        for event in pygame.event.get():
            # quit the game
            if event.type == pygame.QUIT:
                self.game.running = False
                return

            # mouse events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    self.mouseDownPos = [mx, my]

                    # update move pos in camera
                    self.game.camera.moveCurrentPos = [mx, my]

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    self.mouseUpPos = [mx, my]

        # clear screen
        color = (156, 213, 226)
        if not self.game.renderingEnabled:
            color = (0, 0, 0)

        if not self.game.gpuAcceleration:
            self.screen.fill(color)
        else:
            self.renderer.clear()
            self.renderer.draw_color = color
            self.renderer.fill_rect((0, 0, self.w, self.h))

    def update(self):
        # update the window
        if not self.game.gpuAcceleration:
            pygame.display.update()
        else:
            self.renderer.present()

        # tick clock
        self.deltaTime = self.clock.tick(self.tickFPS)
        self.fps = self.clock.get_fps()

        # DEBUG: framerate in caption
        # pygame.display.set_caption(f"FPS: {int(self.fps)}")
