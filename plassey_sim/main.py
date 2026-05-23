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
        print("Single run mode (with JSON tracing) is not yet implemented.")
        # TODO: Implement single run with JSON trace export

if __name__ == "__main__":
    main()
