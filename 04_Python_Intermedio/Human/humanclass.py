import headclass
import handclass
import armclass
import feetclass
import legclass
import torsoclass


class Human:
    def __init__(self):
        # Crear partes
        head = headclass.Head()

        right_hand = handclass.Hand()
        left_hand = handclass.Hand()

        right_arm = armclass.Arm(right_hand)
        left_arm = armclass.Arm(left_hand)

        right_feet = feetclass.Feet()
        left_feet = feetclass.Feet()

        right_leg = legclass.Leg(right_feet)
        left_leg = legclass.Leg(left_feet)

        # Conectar todo en el torso
        self.torso = torsoclass.Torso(head, right_arm, left_arm, right_leg, left_leg)

    def __str__(self):
        return f"Un Humamo con: \n{self.torso}"