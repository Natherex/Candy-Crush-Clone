import random
import stdarray
import stddraw as sd
import picture


class Jewel:

    def __init__(self):
        """
        creates a random jewel with index between 1-6. Each index contains a unique color and image.
        """
        self.index = random.randint(1, 6)
        self.matched = False
        if self.index == 1:
            self.color = "blue"
            self.image = "blue.jpg"
        if self.index == 2:
            self.color = "purple"
            self.image = "purple.jpg"
        if self.index == 3:
            self.color = "red"
            self.image = "red.jpg"
        if self.index == 4:
            self.color = "yellow"
            self.image = "yellow.jpg"
        if self.index == 5:
            self.color = "green"
            self.image = "green.jpg"
        if self.index == 6:
            self.color = "orange"
            self.image = "orange.jpg"

    def draw(self, x, y):
        """
        draws the Jewel onto the screen at location (x,y)
        """
        image = picture.Picture(self.image)
        sd.picture(image, x+.5, y+.5)
