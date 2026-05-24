from manim import *
import json
import os

class BattleScene(Scene):
    def construct(self):
        # Load trace data
        trace_path = "trace.json"
        if not os.path.exists(trace_path):
            print("No trace.json found. Run the simulation first.")
            return

        with open(trace_path, "r") as f:
            trace = json.load(f)

        max_tick = len(trace) - 1
        if max_tick < 0:
            return

        # Coordinate mapping: from [0, 100] to [-6, 6] in X and [-3.5, 3.5] in Y
        def map_coords(x, y):
            mx = (x / 100.0) * 12 - 6
            my = (y / 100.0) * 7 - 3.5
            return np.array([mx, my, 0])

        # Setup initial dots
        unit_dots = {}
        initial_state = trace[0]["units"]
        
        for u in initial_state:
            color = RED if u["faction"] == "British" else GREEN
            dot = Dot(point=map_coords(u["x"], u["y"]), color=color, radius=0.1)
            unit_dots[u["id"]] = dot
            self.add(dot)

        # Time tracker
        tick_tracker = ValueTracker(0)

        # Updaters for dots
        def create_updater(unit_id):
            def updater(mobj):
                current_tick = int(tick_tracker.get_value())
                if current_tick >= len(trace):
                    current_tick = len(trace) - 1
                
                # Find the unit in this tick
                unit_data = None
                for u in trace[current_tick]["units"]:
                    if u["id"] == unit_id:
                        unit_data = u
                        break
                
                if unit_data:
                    if unit_data["state"] == "dead":
                        mobj.set_opacity(0.2)
                        mobj.set_color(GRAY)
                    else:
                        target_pos = map_coords(unit_data["x"], unit_data["y"])
                        mobj.move_to(target_pos)
            return updater

        for uid, dot in unit_dots.items():
            dot.add_updater(create_updater(uid))

        # Play animation
        duration = max(2.0, max_tick * 0.1) # at least 2 seconds, 0.1s per tick
        self.play(tick_tracker.animate.set_value(max_tick), run_time=duration, rate_func=linear)
        self.wait(1)
