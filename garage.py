class GarageOutOfSpaceError(BaseException):
    pass

class Floor(object):
    def __init__(self):
        self.max_cars = 0
        self.num_cars = 0

    def get_num_cars(self):
        return self.num_cars

    def has_place_available(self):
        if self.max_cars > self.num_cars:
            return True
        return False

    def set_max_cars(self, max):
        self.max_cars = max

    def remove_car(self):
        self.num_cars -= 1

    def add_car(self):
        if self.max_cars == self.num_cars:
            return False
        self.num_cars += 1
        return True

class Garage(object):
    def __init__(self):
        self.floors = []
        self.current_floor = 0

    def add_floor(self, fl):
        self.floors.append(fl)

    def _first_available_floor(self):
        for f in self.floors:
            if f.has_place_available():
                return f
        raise GarageOutOfSpaceError("No more space to park")

    def add_car(self):
        floor = self._first_available_floor()
        floor.add_car()
    
    def trace(self):
        cars = []
        for f in self.floors:
            cars.append(f.get_num_cars())
        return cars

    def remove_car_from_floor(self, floor:int):
        self.floors[floor].remove_car()

if __name__ == "__main__":

    import unittest

    class ParkingManagementtestcase(unittest.TestCase):
        def setUp(self):

            g = Garage()

            f1 = Floor()
            f1.set_max_cars(20)
            g.add_floor(f1)
            f2 = Floor()
            f2.set_max_cars(20)
            g.add_floor(f2)
            f3 = Floor()
            f3.set_max_cars(12)
            g.add_floor(f3)
            f4 = Floor()
            f4.set_max_cars(20)
            g.add_floor(f4)

            self.g = g

        def test_adding_removing_cars(self): 
            for c in range(25):
                self.g.add_car()
            self.assertEqual(self.g.trace(), [20,5,0,0])

            self.g.remove_car_from_floor(0)
            self.assertEqual(self.g.trace(), [19,5,0,0])

            self.g.add_car()
            self.g.add_car()
            self.g.add_car()
            self.assertEqual(self.g.trace(), [20,7,0,0])

            self.g.remove_car_from_floor(1)
            for c in range(35):
                self.g.add_car()
            self.assertEqual(self.g.trace(), [20,20,12,9])

            self.g.remove_car_from_floor(1)
            self.assertEqual(self.g.trace(), [20,19,12,9])

            with self.assertRaises(GarageOutOfSpaceError): 
                    for c in range(35):
                        self.g.add_car()
            
    unittest.main()