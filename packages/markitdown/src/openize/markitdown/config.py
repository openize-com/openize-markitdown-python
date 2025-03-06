import configparser
import os

# Import Aspose libraries
try:
    import aspose.words as aw
    import aspose.cells as ac
    import aspose.slides as asl

except ImportError:
    print("Warning: Some Aspose libraries are not installed.")

class Config:
    USE_ASPOSE_LICENSE = False  # Default: No license
    LICENSE_FILE_PATH = "Aspose.Total.lic"  # Default license file name

    @staticmethod
    def load_config():
        """Load settings from setup.cfg"""
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), "../../setup.cfg"))

        if "aspose-licenses" in config:
            Config.USE_ASPOSE_LICENSE = config["aspose-licenses"].getboolean("use_aspose_license", False)
            Config.LICENSE_FILE_PATH = config["aspose-licenses"].get("license_file_path", "Aspose.Total.lic")

    @staticmethod
    def set_aspose_license():
        """Apply Aspose license to all supported products"""
        if not Config.USE_ASPOSE_LICENSE:
            print("Aspose license is disabled. Using evaluation mode.")
            return

        try:
            license_path = Config.LICENSE_FILE_PATH
            print(f"Applying Aspose license from {license_path}")

            # Set license for all available Aspose products
            for lib in [aw, ac, asl]:
                if lib:
                    try:
                        license = lib.License()
                        license.set_license(license_path)
                        print(f"License applied for {lib.__name__}")
                    except Exception as e:
                        print(f"Warning: Could not set license for {lib.__name__}. {e}")

        except Exception as e:
            print(f"Error: Failed to apply Aspose license. {e}")

# Load config and apply license at startup
Config.load_config()
Config.set_aspose_license()
