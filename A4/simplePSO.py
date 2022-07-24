def cost(x, y):
    return 4 * x**2 - 2.1 * x**4 + (x**6)/3 + x*y - 4 * y**2 + 4 * y**4


class Particle:
    def __init__(self, x, y, x_velocity, y_velocity):
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity


print(cost(0.089840, -0.712659))
