NORTH = (0,1)
EAST=(1,0)
SOUTH = (0,-1)
WEST = (-1,0)

class Robot :
    def __init__(self,direction=NORTH , x=0 , y=0):
        self.direction=direction
        self.x=x
        self.y=y
        self.instructions = {'A' : self.advance ,
                             'L' : self.turn_left,
                             'R' : self.turn_right 
                             }
        
        self.turning_right = {NORTH: EAST,
                              EAST: SOUTH,
                              SOUTH: WEST,
                              WEST: NORTH}
        
        self.turning_left = {NORTH: WEST,
                             WEST: SOUTH,
                             SOUTH: EAST,
                             EAST: NORTH}
        

    @property 
    def coordinates (self) :
        return (self.x,self.y)
    def turn_left(self) :
        self.direction=self.turning_left[self.direction]


    def turn_right(self) :
        self.direction=self.turning_right[self.direction]    


    def advance (self) :
        moves= {NORTH : 1 , EAST : 1 ,SOUTH : -1 , WEST : -1}
        if self.direction in (NORTH,SOUTH) :
            self.y +=moves[self.direction] 
        if self.direction in (EAST,WEST) :
            self.x +=moves[self.direction] 

    def move (self,directions) :
        for d in directions   :
            self.instructions[d]() 






         
