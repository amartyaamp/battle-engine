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
        # TODO: Implement target selection
        # TODO: Implement movement phase
        # TODO: Implement firing/combat phase

    def is_battle_over(self) -> bool:
        # TODO: Return True if only one faction remains alive/non-routed
        return False
        
    def get_winner(self) -> str:
        # TODO: Return the name of the winning faction
        return "Unknown"
