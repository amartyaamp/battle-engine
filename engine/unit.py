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
        self.type = config.get("type", "infantry")
        self.commander = config.get("commander", "None")
        self.state = "idle"  # idle, moving, firing, routing, dead

    def distance_to(self, other_unit) -> float:
        return math.sqrt((self.x - other_unit.x)**2 + (self.y - other_unit.y)**2)

    def is_alive(self) -> bool:
        return self.hp > 0 and self.morale > 0.1

    def move_towards(self, target_x: float, target_y: float):
        self.state = "moving"
        dx = target_x - self.x
        dy = target_y - self.y
        dist = math.sqrt(dx**2 + dy**2)
        
        if dist > 0:
            # Move up to self.speed towards the target
            step = min(self.speed, dist)
            self.x += (dx / dist) * step
            self.y += (dy / dist) * step

    def fire_at(self, target):
        self.state = "firing"
        dist = self.distance_to(target)
        
        # Accuracy falloff: accuracy halves at max range
        effective_accuracy = self.accuracy * (1.0 - (dist / self.range) * 0.5)
        
        # RNG check for hit
        if random.random() < effective_accuracy:
            # Hit! Apply damage and morale shock
            damage = random.randint(10, 20)
            target.hp -= damage
            
            morale_damage = random.uniform(0.05, 0.15)
            target.morale -= morale_damage
            
            # Check state changes
            if target.hp <= 0:
                target.state = "dead"
            elif target.morale <= 0.1:
                target.state = "routing"
