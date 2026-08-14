import sys
import os
import site


if sys.prefix != sys.base_prefix:
    # Virtual env, to quit use "deactivate" in the shell
    print("MATRIX STATUS: Welcome to the construct\n")
    
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}\n")

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")

    print("Package installation path:")
    print(site.getsitepackages()[0])
    
else:
    # Global env
    print("MATRIX STATUS: You're still plugged in\n")
    
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install\n.")

    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate\n") #On UNIX

    print("Then run this program again")