"""Global variables for Quest Markers Restored build system"""
import os

DIR_REPO = "C:\\Users\\user\\Documents\\GitHub\\quest-markers-restored"
"""Directory where the git repository for Quest Markers Restored is stored."""

DIR_REPO_LE = os.path.join(DIR_REPO, "Legendary Edition")
"""Directory where all mod files for Legendary Edition are stored."""

DIR_SCRIPTS_LE = os.path.join(DIR_REPO_LE, "Quest Markers Restored", "Scripts")
"""Directory where all papyrus scripts for Legendary Edition are stored."""

DIR_REPO_SE = os.path.join(DIR_REPO, "Special Edition")
"""Directory where all mod files for Special Edition are stored."""

DIR_SCRIPTS_SE = os.path.join(DIR_REPO_SE, "Quest Markers Restored", "Scripts")
"""Directory where all papyrus scripts for Special Edition are stored."""

DIR_TEMP_ALT = "C:\\Windows\\Temp"
"""Directory where temporary files can be stored.
The path must not contain a directory that ends with "Data"."""

DIR_SKYRIM_LE = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Skyrim"
"""Directory where Skyrim Legendary Edition is installed."""

DIR_SKYRIM_SE = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Skyrim Special Edition"
"""Directory where Skyrim Special Edition is installed."""

ARCH_EXE_LE = os.path.join(DIR_SKYRIM_LE, "Archive.exe")
"""Path to Archive.exe for Legendary Edition"""

ARCH_EXE_SE = os.path.join(DIR_SKYRIM_SE, "Tools\\Archive\\Archive.exe")
"""Path to Archive.exe for Special Edition"""
