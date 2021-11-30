class Collision_manager:
    def __init__(self):
        #List of all the objects present in the actual scene in x axis
        self.objects_list_x = []

        #Final list with the most relevant information for the x axis
        self.collision_list_x = []

    #This function is used to add collidable objects to the list which conyains al the objects of the scene
    def add_collider_x(self, info):
        self.objects_list_x.append(info)