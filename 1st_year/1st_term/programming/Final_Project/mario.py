class Mario:
    #This class stores all the information needed for Mario
    def __init__(self, x:int, y:int, dir:str):
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
        self.sprite = (1, 112, 0, 16, 16)
        self.direction = dir

        #We also assume that Mario will always start with 3 lives
        self.lives = 3

        #This is the size of mario in the x axis
        self.mario_x_size = self.sprite[3]

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

    
    #Approach: connect the first top left to top right and you cannot pass that line
    def collisions(self, size, prohibited_zones_x):        
        self.move()
        for i in prohibited_zones_x:
            if (self.x < i[1]):
                if(self.x + self.mario_x_size < i[0]):
                    self.y += 0
            else:
                self.y += 1

    #The movement is done to move in the x axis
    def move(self):
        self.x += self.acceleration_x

        if(self.acceleration_x > 0):
            self.acceleration_x -= 0.25
        
        if(self.acceleration_x < 0):
            self.acceleration_x += 0.25

    def jump(self, user_input):
        if(user_input == True):
            self.acceleration_y += 1