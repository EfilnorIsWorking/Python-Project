from app.gui import *


class ReinitGUI(GUI):
    def __init__(self, game):
        super().__init__(game)

        self.visible = False

        # gui pos
        self.x = 0
        self.y = 0

        # elements
        self.frmBackground = Frame(self, x=0, y=0, w=self.game.window.w, h=self.game.window.h, color=(20, 20, 20))
        self.frmForm = Frame(self, x=-525/2, y=-600/2, w=525, h=600, parent=self.frmBackground, color=(35, 35, 35))
        self.frmForm.screenAnchor = [0.5, 0.5]

        self.txtForm = Text(self, x=10, y=10, text="Settings", fontSize=50, parent=self.frmForm)

        self.sldMapWidth = Slider(self, x=150, y=200, w=200, caption="Map Width", minVal=32, maxVal=192, parent=self.frmForm, varType=int)
        self.sldMapHeight = Slider(self, x=400, y=200, w=200, caption="Map Height", minVal=32, maxVal=192, parent=self.frmForm, varType=int)

        self.sldBobs = Slider(self, x=150, y=270, w=200, caption="Bobs", minVal=30, maxVal=350, parent=self.frmForm, varType=int)
        self.sldFood = Slider(self, x=400, y=270, w=200, caption="Food", minVal=75, maxVal=600, parent=self.frmForm, varType=int)

        self.sldDayLength = Slider(self, x=150, y=340, w=200, caption="Day Length", minVal=50, maxVal=300, parent=self.frmForm, varType=int)

        self.chkParthenoRepr = Checkbox(self, x=150, y=410, text="Parthenogenesis Reproduction", parent=self.frmBackground)
        self.chkSexualRepr = Checkbox(self, x=150, y=480, text="Sexual Reproduction", parent=self.frmBackground)

        self.btnApply = Button(self, 470, 640, text="Apply", onLeftClick=self.apply, parent=self.frmBackground)
        self.btnClose = Button(self, 280, 640, text="Close", onLeftClick=self.close, bg=(200, 30, 80), hbg=(220, 140, 30), parent=self.frmBackground)

        self.sldMapWidth.curVal = 50
        self.sldMapHeight.curVal = 50
        self.sldFood.curVal = 200
        self.sldBobs.curVal = 50
        self.sldDayLength.curVal = 50

    def apply(self):
        mapW = int(self.sldMapWidth.curVal)
        mapH = int(self.sldMapHeight.curVal)
        bobsAm = int(self.sldBobs.curVal)
        foodAm = int(self.sldFood.curVal)
        dayL = int(self.sldDayLength.curVal)
        parth = self.chkParthenoRepr.value
        sex = self.chkSexualRepr.value

        self.game.reinit(mapW, mapH, bobsAm, foodAm, dayL, parth, sex)
        self.close()

    def close(self):
        self.visible = False
        self.game.menuGUI.visible = True

    def update(self):
        # draw all elements
        self.draw_element(self.frmBackground)
        self.draw_element(self.frmForm)
        self.draw_element(self.txtForm)

        self.draw_element(self.sldMapWidth)
        self.draw_element(self.sldMapHeight)

        self.draw_element(self.sldBobs)
        self.draw_element(self.sldFood)

        self.draw_element(self.sldDayLength)

        self.draw_element(self.chkParthenoRepr)
        self.draw_element(self.chkSexualRepr)

        self.draw_element(self.btnApply)
        self.draw_element(self.btnClose)
