class Player:
    def __init__(self):
        #pygame.sprite.Sprite.__init__(self)
        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        self.frame = 0 # count frames

    def control(self,x,y):
        """ control player movement """
        self.movex += x
        self.movey += y

    def update(self):
        """ Update sprite position"""
        self.rect.x = self.rect.x + self.movex  
        self.rect.y = self.rect.y + self.movey
        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]