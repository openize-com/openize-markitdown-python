import configparser

def get_config():
    """Reads settings from setup.cfg"""
    config = configparser.ConfigParser()
    config.read("../../setup.cfg")
    return config

def get_license_path():
    """Fetches Aspose license path from setup.cfg or uses a default."""
    config = get_config()
    return config.get("aspose", "license_path", fallback="Aspose.Total.lic")

def use_aspose_license():
    """Checks if Aspose license should be applied (True/False)."""
    config = get_config()
    return config.getboolean("aspose", "use_aspose_license", fallback=True)  # Defaults to True
