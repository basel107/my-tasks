import json
from pathlib import Path


config_path = Path("config.json")
with config_path.open("r") as f:
    config = json.load(f)

print("Config loaded:", config)

results = {
    "model_name": config["model_name"],
    "epochs": config["epochs"],
    "final_loss": 0.123,
    "final_accuracy": 0.94,
    "config_used": config
}

print("Training results simulated.")

results_path = Path("results.json")
with results_path.open("w") as f:
    json.dump(results, f, indent=4)

print("Results saved to results.json")