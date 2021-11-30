from collisionManager import Collision_manager
import common_values

class Mario:
    #This class stores all the information needed for Mario
    def __init__(self, x:int, y:int, dir:str, collision_manager:Collision_manager):
        #This method creates the Mario object
        #param x the starting x of Mario
        #param y the starting y of Mario
        #param dir a string to store the initial direction of Mario.

        self.x = x
        self.y = y

        #Acceleration will be the variable which makes possible the slip
        self.acceleration_x = 0
        self.acceleration_y = 0

        #Here we are assuming Mario will be always placed at the first
        #bank at first position and it will have fixed size
        self.sprite = (0, 0, 112, 16, 16, 12)
        self.direction = dir

        #We also assume that Mario will always start with 3 lives
        self.lives = 3

        #This is the size of mario in the x axis
        self.mario_x_size = self.sprite[3]
        self.mario_y_size = self.sprite[4]

        #This is are the obstales which mario can collide with
        self.objects = collision_manager.objects_list_x
    
    def obstacles_updater(self, collision_manager:Collision_manager):
        self.objects = collision_manager.objects_list_x

    def accelerate(self, direction: str, size: int, prohibited_zones: list):
        """ This is an example of a method that moves Mario, it receives the
        direction and the size of the board"""
        # Checking the current horizontal size of Mario to stop him before
        # he reaches the right border
        if direction.lower() == 'right' and self.x < size - self.mario_x_size and ([self.x + 1, self.y] not in prohibited_zones):
            self.acceleration_x += 1

        elif direction.lower() == 'left' and self.x > 0 and ([self.x -1, self.y] not in prohibited_zones):
            # I am assuming that if it is not right it will be left
            self.acceleration_x -= 1

    
    #Approach: Check if the exists a block  under mario
    def collisions(self):
     #This algorithm is done to establish the bounds where mario can collide--------------
        falling = True
        self.collading_with_mario = ["down"]

        for i in self.objects:
            if self.y + self.sprite[4] == i[1] and self.x + self.sprite[3] >= i[0] and self.x <= i[0] + i[3]:
                falling = False
                self.collading_with_mario.append(i[2])

            if self.y + self.sprite[4] >= i[1] and self.y <= i[1] + i[4] and (self.x == i[0] + i[3] or self.x + self.sprite[3] == i[0]):
                self.acceleration_x = 0
        
        if (falling and self.acceleration_y  == 0):
            self.acceleration_y = 0
            self.y += 1

        print(self.acceleration_x)
        #return self.collading_with_mario

    #The movement is done to move in the x axis
    def move(self):
        self.x += self.acceleration_x

        if(self.acceleration_x > 0):
            self.acceleration_x -= 0.25
        
        if(self.acceleration_x < 0):
            self.acceleration_x += 0.25

        if(self.acceleration_y != 0):
            self.y -= common_values.gravity

        if(self.acceleration_y > 0):
            self.acceleration_y -= 0.25
        
        if(self.acceleration_y < 0):
            self.acceleration_y += 0.25

    #The jump is done to
    def jump(self, user_input):
        if (user_input):
            self.acceleration_y -= 8