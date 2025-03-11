from setuptools import setup
from setuptools.command.install import install
import subprocess


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        print("\n🚀 Running custom post-installation script...")  # Display confirmation
        install.run(self)  # Run the standard install first
        print("\n✅ Setup.py executed successfully!\n")  # Confirm setup execution

        # Run post-install script
        subprocess.call(["python", "-m", "openize.markitdown.post_install:ask_license"])


setup(
    setup_requires=['setuptools'],
    cmdclass={'install': PostInstallCommand},
)
