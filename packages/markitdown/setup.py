
from setuptools import setup
from setuptools.command.install import install
import subprocess

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)  # Run the standard install first
        subprocess.call(["python", "post_install.py"])  # Run post-install script

setup(
    setup_requires=['setuptools'],
    cmdclass={'install': PostInstallCommand},
)
