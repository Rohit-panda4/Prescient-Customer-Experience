
import subprocess
import sys
import os
import platform
import shutil


def run_script(script_name):
    """Run a script in a platform-appropriate way.

    On Unix-like systems try to run the script inside `nix-shell dev.nix` (original
    behaviour). On Windows (or when `nix-shell` isn't available) run the script
    using the current Python interpreter (sys.executable). Scripts are executed
    from the repository directory so relative imports work.
    """
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(repo_dir, script_name)

    # Prefer nix-shell on non-Windows systems if it's available
    use_nix = platform.system() != "Windows" and shutil.which("nix-shell") is not None

    if use_nix:
        cmd = ["nix-shell", "dev.nix", "--run", f"python3 {script_path}"]
    else:
        # Fall back to the current Python executable (works in virtualenvs on Windows)
        cmd = [sys.executable, script_path]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"Successfully ran {script_name}")
        if result.stdout:
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}:")
        if e.stderr:
            print(e.stderr)
        else:
            print(e.output)
        exit(1)

if __name__ == "__main__":
    run_script("data_ingestion.py")
    run_script("data_preprocessing.py")
    run_script("model_training.py")
    run_script("generate_predictions.py")
