class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture_line = "*" * self.width + '\n'
        return picture_line * self.height
    
    def get_amount_inside(self, shape):
        width_amount = self.width // shape.width
        height_amount = self.height // shape.height

        return width_amount * height_amount

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

    def __str__(self):
        return f"Square(side={self.width})"


# Test
rec = Rectangle(3,4)
area = rec.get_area()
sq = Square(10)
print(rec.get_picture())
print(sq)