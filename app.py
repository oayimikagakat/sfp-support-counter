import os
from pathlib import Path

ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
if __name__ == '__main__':
    import sys
    sys.path.insert(1, 'src')
    from src import main
    main.main()
