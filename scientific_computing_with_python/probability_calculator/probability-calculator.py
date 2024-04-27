import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def get_contents(self):
        return self.contents
    
    def draw(self, amount):
        if amount >= len(self.contents):
            return self.contents
        
        result=[]
        for _ in range(amount):
            random_ball = random.choice(self.contents)
            self.contents.remove(random_ball)
            result.append(random_ball)

        return result
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        draw = hat_copy.draw(num_balls_drawn)
        if compare_draw(draw, expected_balls):
            count += 1
    return count/num_experiments

def compare_draw(draw, expected):
    for color, count in expected.items():
        if draw.count(color) < count:
            return False
    return True

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=40,
                  num_experiments=2000)
                
print(probability)