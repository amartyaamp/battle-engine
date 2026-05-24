import argparse
from engine.monte_carlo import run_monte_carlo

def main():
    parser = argparse.ArgumentParser(description="Historical Battle Simulator")
    parser.add_argument("--mode", choices=["single", "mc"], default="single", help="Run a single trace or a Monte Carlo batch")
    parser.add_argument("--config", default="campaigns/dummy_test.json", help="Path to battle config JSON")
    parser.add_argument("--runs", type=int, default=100, help="Number of runs for Monte Carlo mode")
    
    args = parser.parse_args()

    if args.mode == "mc":
        run_monte_carlo(args.config, args.runs)
    else:
        from engine.battlefield import Battlefield
        import json
        
        print(f"Running single trace for {args.config}...")
        battle = Battlefield(args.config)
        trace = []
        
        # Record initial state
        trace.append(battle.get_state())
        
        while not battle.is_battle_over():
            battle.tick()
            trace.append(battle.get_state())
            if battle.current_tick > 1000:
                break
                
        winner = battle.get_winner()
        print(f"Battle over in {battle.current_tick} ticks. Winner: {winner}")
        
        trace_file = "trace.json"
        with open(trace_file, "w") as f:
            json.dump(trace, f, indent=2)
        print(f"Trace saved to {trace_file}")

if __name__ == "__main__":
    main()
