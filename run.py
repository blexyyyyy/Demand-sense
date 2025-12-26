import subprocess
import sys
import os

def main():
    """
    Run the Streamlit application.
    """
    # Get the absolute path to the directory containing this script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Path to the streamlit app file
    app_path = os.path.join(base_dir, "app", "streamlit_app.py")
    
    # Check if the file exists
    if not os.path.exists(app_path):
        print(f"Error: Could not find application at {app_path}")
        sys.exit(1)
        
    print(f"Starting Streamlit app from: {app_path}")
    
    # Construct the command: python -m streamlit run app/streamlit_app.py
    cmd = [sys.executable, "-m", "streamlit", "run", app_path]
    
    try:
        # Run the command
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Streamlit app: {e}")
        sys.exit(e.returncode)
    except KeyboardInterrupt:
        print("\nStopping Streamlit app...")
        sys.exit(0)

if __name__ == "__main__":
    main()
