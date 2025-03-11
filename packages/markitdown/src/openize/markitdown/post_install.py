import os
import configparser

CONFIG_FILE = os.path.expanduser("../../../setup.cfg")

def ask_license():
    """Prompt the user for license details after installation."""
    print("\n🔹 Do you want to use an Aspose license? (yes/no)")
    use_license = input("Enter your choice: ").strip().lower()

    if use_license in ["yes", "y"]:
        license_path = input("Enter the full path to the Aspose license file: ").strip()
    else:
        license_path = ""

    save_config(use_license == "yes", license_path)

def save_config(use_license, license_path):
    """Save user preferences to a config file."""
    config = configparser.ConfigParser()
    config["Aspose"] = {
        "use_license": str(use_license),
        "license_path": license_path
    }

    with open(CONFIG_FILE, "w") as configfile:
        config.write(configfile)

    print(f"\n✅ Configuration saved to {CONFIG_FILE}")

if __name__ == "__main__":
    ask_license()
