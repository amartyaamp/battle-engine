import math
import random

class Unit:
    def __init__(self, config: dict):
        self.id = config["id"]
        self.faction = config["faction"]
        self.x = config["x"]
        self.y = config["y"]
        self.hp = config["hp"]
        self.morale = config["morale"]
        self.speed = config["speed"]
        self.range = config["range"]
        self.accuracy = config["accuracy"]
        self.state = "idle"  # idle, moving, firing, routing, dead

    def distance_to(self, other_unit) -> float:
        return math.sqrt((self.x - other_unit.x)**2 + (self.y - other_unit.y)**2)

    def is_alive(self) -> bool:
        return self.hp > 0 and self.morale > 0.1

    # TODO: Implement move_towards(target)
    # TODO: Implement fire_at(target)
