import sys
import os

# Add project root to Python path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

from grizly_app.app import main

if __name__ == "__main__":
    main()
