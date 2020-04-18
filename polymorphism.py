'''Polymorphic Classes'''
class Square:
    side = 5     
    def calculate_area(self):
        return self.side * self.side

class Triangle:
    base = 5
    height = 4
    def calculate_area(self):
        return 0.5 * self.base * self.height

sq = Square()
tri = Triangle()
print("Area of square: ", sq.calculate_area())
print("Area of triangle: ", tri.calculate_area())

for obj in (sq, tri):
    print(obj.calculate_area())

'''Polymorphism with Functions'''

def find_area_of_shape(obj):
    return obj.calculate_area()

sq = Square()
tri = Triangle()

print('find_area_of_shape sq', find_area_of_shape(sq))
print('find_area_of_shape tri', find_area_of_shape(tri))