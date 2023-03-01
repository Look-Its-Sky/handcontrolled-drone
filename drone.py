from codrone_edu.drone import *

class Dronee:
    drone = None
    testMode = False
    height = 100
    heightModifier = 1000
    power = 1

    def __init__(self):
        if not self.testMode:
            self.drone = Drone()
            self.drone.pair()
            self.drone.takeoff()

    def takeoff(self):
        self.drone.takeoff()

    def land(self):
        self.drone.land()

    def estop(self):
        self.drone.emergency_stop()

    def disconnect(self):
        self.drone.close()

    def move(self, vec, threshold):
        if not self.testMode:
            # if not vec: #and self.drone.is_flying():
            #     self.land()
            #     return
            
            # elif vec and not self.drone.is_flying():
            #     self.takeoff()
            #     self.drone.go_to_height(self.height)

            if (self.drone and vec) or self.testMode:
                #x axis
                if vec[0] > 0 and vec[0] >= threshold: #turn right
                    self.drone.turn_right()

                elif vec[0] < 0 and vec[0] <= threshold: #turn left
                    self.drone.turn_left()

                #y axis
                if vec[1] > 0 and vec[1] >= threshold: #up
                    self.height += self.heightModifier

                elif vec[1] < 0 and vec[1] <= threshold: #down
                    self.height -= self.heightModifier
                    
                    if self.height == 0:
                        self.height = 30

                #z axis
                if vec[2] > 0 and vec[2] >= threshold: #forward
                    print("Moving Forward!")
                    self.drone.set_pitch(30)
                    self.drone.move(self.power)
                                    
                elif vec[2] < 0 and vec[2] <= threshold: #backward
                    print("Moving Backward!")
                    
            elif self.drone and not vec:
                #self.land()
                pass