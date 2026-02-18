"""
Pytest configuration and shared fixtures.

This file:
- Sets up Python path to include src/ directory
- Provides shared fixtures for all tests
"""
import sys
from pathlib import Path

# Add project root and src/ to Python path for imports
PROJECT_ROOT = Path(__file__).parent.parent
SRC_DIR = PROJECT_ROOT / "development_tutor"
# Add both project root and src to path
# This allows imports like "from src.core.config import ..."
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))
