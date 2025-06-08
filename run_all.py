import subprocess
import sys  # To get current Python interpreter

print("🚀 Training the model...")
subprocess.run([sys.executable, "train.py"], check=True)

print("✅ Training complete. Starting the app...")
subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"], check=True)
