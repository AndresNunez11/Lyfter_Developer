class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

    def __str__(self):
        return f"Torso con: \n{self.head},\n{self.right_arm},\n{self.left_arm}, \n{self.right_leg}, \n{self.left_leg}"