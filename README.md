# Historical Battle Simulator (Battle of Plassey)

A Python-based agent-based Monte Carlo simulation for historical battles, starting with the **Battle of Plassey (1757)**. This engine models unit attributes, combat math, morale, weather dynamics (like rainfall disabling artillery), and political variables (such as betrayal mechanics).

Eventually, simulated battle traces will be parsed and animated using **Manim** to create rich visual step-by-step reconstructions.

## Project Structure

```text
plassey_sim/
├── engine/              # Simulation logic (units, battlefield, combat math)
├── campaigns/           # Historical and test battle configurations
├── visuals/             # Manim rendering scripts
├── main.py              # Entry CLI
├── requirements.txt     # Python packages
└── TODO.md              # Project roadmap & checklist
```

## Getting Started

1. Install requirements:
   ```bash
   pip install -r plassey_sim/requirements.txt
   ```

2. Run the simulation CLI:
   ```bash
   python plassey_sim/main.py --mode mc --runs 100
   ```
