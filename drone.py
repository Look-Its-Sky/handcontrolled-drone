import CoDrone

class Drone:
    drone = None

    def __init__(self):
        self.drone = CoDrone.CoDrone()
        self.drone.pair(self.drone.Nearest)
        self.takeoff()
        self.land()

    def takeoff(self):
        self.drone.takeoff()

    def land(self):
        self.drone.land()

    def estop(self):
        self.drone.emergency_stop()

    def disconnect(self):
        self.drone.close()

    def move(self, vec):
        pass