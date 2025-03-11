import configparser

import configparser
import os


def get_config():
    """Reads settings from setup.cfg if available."""
    config = configparser.ConfigParser()

    # Possible locations for setup.cfg
    possible_paths = [
        os.path.join(os.getcwd(), "setup.cfg"),  # Current working directory
        os.path.abspath(os.path.join(__file__, "../../../../setup.cfg")),  # Relative to script location
    ]

    for path in possible_paths:
        if os.path.exists(path):
            print(f"✅ Found setup.cfg at: {path}")
            config.read(path)
            return config

    print("❌ setup.cfg not found. Using default settings.")
    return config  # Returns an empty config


def get_license_path():
    """Fetches Aspose license path from setup.cfg or uses a default."""
    config = get_config()
    return config.get("aspose-licenses", "license_file_path", fallback="Aspose.Total.lic")

def use_aspose_license():
    """Checks if Aspose license should be applied (True/False)."""
    config = get_config()
    return config.getboolean("aspose-licenses", "use_aspose_license", fallback=True)  # Defaults to True
