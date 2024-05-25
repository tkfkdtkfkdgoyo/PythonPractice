class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def set_demension(self, legth, width): # setter
        self.length = length
        self.width = width

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def area(self): # 넓이
        return self.length * self.width

    def perimeter(self): # 둘레
        return 2 * (self.length + self.width)

    def print(self):
        print("Rectangle: length = ", self.length, ", width = ", self.width, ", area = ", self.area(), ", perimeter = ", self.perimeter())

class Box(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width) # 부모 클래스 생성자 호출
        self.height = height

    def set_dimension(self, length, width, height): # 부모 클래스의 set_dimension 메소드를 오버라이딩
        self.length = length
        self.width = width
        self.height = height

    def get_heigth(self):
        return self.height

    def area(self):
        return 2 * (self.length * self.width + self.width * self.height + self.height * self.length)

    def volume(self):
        return self.length * self.width * self.height

    def print(self):
        print("Box: length = ", self.length, ", width = ", self.width, ", height = ", self.height, ", area = ", self.area(), ", volume = ", self.volume())

if __name__ == "__main__":
    r = Rectangle(10, 20)
    r.print()

    b = Box(10, 20, 30)
    b.print()
