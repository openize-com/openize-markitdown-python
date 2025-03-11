import aspose.words as aw
import aspose.cells as ac
import aspose.slides as asl
import logging
from config_loader import get_license_path, use_aspose_license

class LicenseManager:
    """Manages the application of Aspose licenses for different file format APIs."""

    def __init__(self):
        """Initialize LicenseManager with license settings."""
        self.license_path = get_license_path()
        self.use_license = use_aspose_license()

    def apply_license(self):
        """Apply the Aspose license if enabled in setup.cfg."""
        if not self.use_license:
            logging.info("Aspose license is disabled in setup.cfg. Running in free mode.")
            return

        try:
            license_files = [aw.License(), ac.License(), asl.License()]
            for license in license_files:
                license.set_license(self.license_path)
            logging.info(f"Aspose license applied from {self.license_path}")
        except Exception as e:
            logging.warning(f"Failed to apply Aspose license: {e}")

# Usage example:
# license_manager = LicenseManager()
# license_manager.apply_license()

