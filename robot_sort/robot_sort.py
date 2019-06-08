class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        #  1)  Determine if the robot's SORT mode light is on, which allows it to enter the SORT loop.
        # print("Let's check to see if the robot's SORT mode light is even turned on, otherwise it can't begin to sort anything! \n")
        # print("If the robot's SORT mode light is 'True', it can enter the SORT loop! \n")
        # print("If the robot's SORT mode light is 'False', it CAN'T start sorting yet! \n")
        # print("Robot's SORT mode light: ", self.light_is_on(), "\n")
        # if self.light_is_on() == True:
        #     #  2)  If the robot's SORT mode light is on, proceed to step 4.
        #     pass
        # else: 
            #  3)  If the robot's SORT mode light is NOT on, turn it on to enter the SORT loop.
            # print("Since the robot's SORT mode light isn't turned on yet, let's do that FIRST so it can enter the SORT loop! \n")
        self.set_light_on()
        print("*******INITIAL turning on of the robot's SORT mode light: ", self.light_is_on())
            # print("Now that the robot's SORT mode light is turned on, it can jump into the SORT loop! \n")
        while self.light_is_on() == True:
                #  4)  Turn off the robot's light to remain inside this SORT loop.
                # print("Now that the robot has entered the SORT loop, let's turn off it's SORT mode light so that it can keep sorting in this loop! \n")
            
            #  5)  Determine if the robot can move left or right, which 
            #      signifies where the robot is located in the list and 
            #      whether there are still items to be sorted.
            #  6a) If the robot can move left AND right, the robot is 
            #      positioned somewhere in the middle of the list and 
            #      may continue sorting.
            #  6b) If the robot can only move LEFT, then the robot has 
            #      reached the end of the list and can no longer sort.
            #  6c) If the robot can only move RIGHT, this signifies 
            #      that the robot is positioned at the beginning of the 
            #      list (l[0]) and may continue sorting.
            # print("Great! Now, let's figure out where the robot is located in the list! \n")
            # print("The Robot's Current Ability to Move Left: ", self.can_move_left())
            print("The Robot's Current Ability to Move Right: ", self.can_move_right(), "\n")
            # print("In it's current position, if the robot can move, both, LEFT and RIGHT, it is positioned somewhere in the middle of the list! \n")
            # print("However, if the robot can ONLY move to the LEFT, it is positioned at the FIRST index of the list! \n")
            # print("But don't forget that that the robot can KEEP sorting in this list as long as it has the ability to move to the RIGHT! \n")
            # print("And if the robot can ONLY move to the RIGHT, it is positioned at the LAST index of the list! \n")
            while self.can_move_right() == True:
                self.set_light_off()
                print("Robot's SORT mode light has been shut OFF because it entered the CAN_MOVE_RIGHT While loop!")
                print("The robot's current position within the list: ", robot._position, "\n")
                self.swap_item()
                print(f"The robot has PICKED UP an item at the {robot._position} index! \n")
                self.move_right()
                print(f"The robot is NOW at the {robot._position} position within the list. \n")
                    #  7)   To begin sorting, we must compare the value of the item
                    #       in the robot's hand with the item in front of it. If a
                    #       swap is performed, we will turn on the robot's SORT mode
                    #       light to allow it to enter the SORT loop again.
                    # print("Now that we know the robot is positioned at the FIRST index of the list, let's start sorting as we move to the RIGHT! \n")
                    #  8a)  If the item in the robot's hand is GREATER than the item 
                    #       in front of the robot, it will swap those two items and 
                    #       then move LEFT to drop off the LESSER item at the previous 
                    #       position.
                if self.compare_item() == 1:
                    print("The robot was holding something GREATER than what was in front of it. SWAPPPPPPP! \n")
                    self.swap_item()  
                    self.move_left()
                    self.swap_item()
                    self.set_light_on()
                    print("The robot's SORT mode light has been turned ON because of a GREATER to LESSER item SWAP + DROP OFF!")
                    self.move_right()
                    #  8c)  If the item in the robot's hand is EQUAL to the item in front
                    #       of the robot, it will move RIGHT to the next position without
                    #       swapping anything.
                elif self.compare_item() == 0: 
                    self.move_left()
                    self.swap_item()
                    self.move_right()
                elif self.compare_item() == -1: 
                    self.move_left()
                    self.swap_item()
                    self.move_right()
                #  9)  When the robot reaches the end of the list and still has it's SORT mode light
                #      on, the robot will keep moving LEFT, without sorting anything, until it is back 
                #      to the FIRST index of the list again, where it will pass throughth the list for
                #      another round of sorting again!
                # print("Now that we know the robot is positioned at the LAST index of the list, let's have it return to the FIRST index to keep sorting! \n")
                if self.can_move_right() == False:
                    while self.can_move_left() == True and self.light_is_on() == True:
                        self.move_left()                        

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`
    # l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65]
    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)