import importlib.util
import subprocess
import sys
from setuptools import setup

def install_if_missing(package, module_name=None):
    """Check if a package is installed; if not, install it."""
    if module_name is None:
        module_name = package.replace("-", "_")  # Convert dashes to underscores

    if importlib.util.find_spec(module_name) is None:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    else:
        print(f"{package} is already installed.")

# List of dependencies
dependencies = [
    ("aspose-cells", "asposecells"),
    ("aspose-words", "asposewords"),
    ("aspose-slides", "asposeslides")
]

# Install missing dependencies before proceeding
for package, module_name in dependencies:
    install_if_missing(package, module_name)

# Now proceed with the actual installation using setup.cfg
setup()
