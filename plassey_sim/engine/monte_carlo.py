from engine.battlefield import Battlefield

def run_monte_carlo(config_path: str, iterations: int = 1000):
    print(f"Starting Monte Carlo simulation ({iterations} runs)...")
    results = {}
    
    for i in range(iterations):
        battle = Battlefield(config_path)
        
        while not battle.is_battle_over():
            battle.tick()
            # Failsafe to prevent infinite loops during early dev
            if battle.current_tick > 1000:
                break 
                
        winner = battle.get_winner()
        results[winner] = results.get(winner, 0) + 1
        
    print("\n--- Simulation Results ---")
    for faction, wins in results.items():
        win_rate = (wins / iterations) * 100
        print(f"{faction}: {win_rate:.2f}% ({wins} wins)")
