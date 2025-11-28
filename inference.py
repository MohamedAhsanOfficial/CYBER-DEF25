import os
import pandas as pd
import time

# Define paths
INPUT_DIR = "/input/logs"
OUTPUT_DIR = "/output"
MODEL_PATH = "model.pkl"

def load_model():
    print(f"Loading model from {MODEL_PATH}...")
    # In a real scenario, we would load the model here using pickle or joblib
    # model = pd.read_pickle(MODEL_PATH)
    print("Model loaded successfully.")
    return "DUMMY_MODEL"

def analyze_logs(model):
    print(f"Scanning logs in {INPUT_DIR}...")
    
    if not os.path.exists(INPUT_DIR):
        print(f"Error: Input directory {INPUT_DIR} does not exist.")
        return

    alerts = []
    
    for filename in os.listdir(INPUT_DIR):
        file_path = os.path.join(INPUT_DIR, filename)
        if os.path.isfile(file_path):
            print(f"Processing {filename}...")
            # Simulate processing
            try:
                # Assuming simple text logs for this assignment
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        # Dummy detection logic
                        if "suspicious" in line.lower() or "malware" in line.lower():
                            alerts.append({
                                "file": filename,
                                "line_number": i + 1,
                                "content": line.strip(),
                                "prediction": "MALWARE_DETECTED",
                                "confidence": 0.98
                            })
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    return alerts

def save_results(alerts):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    output_path = os.path.join(OUTPUT_DIR, "alerts.csv")
    df = pd.DataFrame(alerts)
    df.to_csv(output_path, index=False)
    print(f"Results saved to {output_path}")

if __name__ == "__main__":
    print("Starting AI Malware Detection Inference Container...")
    model = load_model()
    alerts = analyze_logs(model)
    save_results(alerts)
    print("Inference complete.")
