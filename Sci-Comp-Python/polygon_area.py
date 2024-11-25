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
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        string = ""
        for _ in range(self.width):
            string += "*"
        string += "\n"
        string *= self.height
        return string
    
    def get_amount_inside(self, shape):
        count = 0
        for _ in range(self.height // shape.height):
            for _ in range(self.width // shape.width):
                count += 1
        return count

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
    
    def set_side(self, side):
        self.width = side
        self.height = side

    set_width = set_side
    set_height = set_side

    def __str__(self):
        return f"Square(side={self.width})"
