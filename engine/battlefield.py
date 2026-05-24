import json
from engine.unit import Unit

class Battlefield:
    def __init__(self, config_path: str):
        self.units = []
        self.current_tick = 0
        self.load_config(config_path)

    def load_config(self, config_path: str):
        with open(config_path, 'r') as f:
            data = json.load(f)
            for unit_data in data["units"]:
                self.units.append(Unit(unit_data))

    def tick(self):
        """Advances the battle by one unit of time."""
        self.current_tick += 1
        
        # --- Historical Events ---
        # Rain Event: Disable Bengal Artillery (Siraj didn't cover his powder)
        is_raining = (20 <= self.current_tick <= 30)
        
        # Betrayal Event: Mir Jafar abandons the field
        if self.current_tick == 50:
            for unit in self.units:
                if unit.commander == "Mir Jafar":
                    unit.morale = 0.0 # Force route
                    unit.state = "routing"
        
        for unit in self.units:
            if not unit.is_alive():
                continue
                
            if is_raining and unit.faction == "Bengal" and unit.type == "artillery":
                unit.state = "idle"
                continue # Artillery cannot act in rain
                
            # Target selection: Find closest alive enemy
            closest_enemy = None
            min_dist = float('inf')
            
            for other in self.units:
                if other.faction != unit.faction and other.is_alive():
                    dist = unit.distance_to(other)
                    if dist < min_dist:
                        min_dist = dist
                        closest_enemy = other
                        
            if closest_enemy:
                # Combat / Movement phase
                if min_dist <= unit.range:
                    unit.fire_at(closest_enemy)
                else:
                    unit.move_towards(closest_enemy.x, closest_enemy.y)
            else:
                unit.state = "idle"

    def is_battle_over(self) -> bool:
        alive_factions = {u.faction for u in self.units if u.is_alive()}
        return len(alive_factions) <= 1
        
    def get_winner(self) -> str:
        alive_factions = list({u.faction for u in self.units if u.is_alive()})
        if len(alive_factions) == 1:
            return alive_factions[0]
        elif len(alive_factions) == 0:
            return "Draw"
        return "Unknown"

    def get_state(self) -> dict:
        return {
            "tick": self.current_tick,
            "units": [
                {
                    "id": u.id,
                    "faction": u.faction,
                    "x": u.x,
                    "y": u.y,
                    "hp": u.hp,
                    "state": u.state
                }
                for u in self.units
            ]
        }
