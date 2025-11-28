import os
import pandas as pd
import pickle

# Load dummy model
model = pickle.load(open("model.pkl", "rb"))

INPUT_DIR = "/input/logs"
OUTPUT_FILE = "/output/alerts.csv"

alerts = []

# Read all log files
for file in os.listdir(INPUT_DIR):
    if file.endswith(".log"):
        filepath = os.path.join(INPUT_DIR, file)
        with open(filepath, "r") as f:
            for line in f:
                # Dummy detection rule
                alerts.append({"log_file": file, "line": line.strip(), "prediction": "safe"})

# Save output
df = pd.DataFrame(alerts)
df.to_csv(OUTPUT_FILE, index=False)

print("Alerts saved to /output/alerts.csv")
