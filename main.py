
import subprocess

def run_script(script_name):
    try:
        result = subprocess.run(["nix-shell", "dev.nix", "--run", f"python3 {script_name}"], capture_output=True, text=True, check=True)
        print(f"Successfully ran {script_name}")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}:")
        print(e.stderr)
        exit(1)

if __name__ == "__main__":
    run_script("data_ingestion.py")
    run_script("data_preprocessing.py")
    run_script("model_training.py")
