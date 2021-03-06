"""Build full release.
Loose files are packed into a bsa and version numbers are added."""
import config
import logging
import release
import shutil

logger = logging.getLogger(release.__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
handler = logging.FileHandler("{}.log".format(release.__name__), "w")
handler.setFormatter(formatter)
logger.addHandler(handler)
try:
    flags = release.ArchiveFlags()
    flags.check_misc = True
    flags.check_retain_directory_names = True
    flags.check_retain_file_names = True
    release.build_release(dir_src=config.DIR_REPO_LE,
                          temp_alt=config.DIR_TEMP_ALT,
                          arch_exe=config.ARCH_EXE_LE,
                          arch_flags=flags,
                          trim_fomod=True,
                          warn_readmes=False)
    shutil.copytree(config.DIR_SCRIPTS_LE, config.DIR_SCRIPTS_SE)
    release.build_release(dir_src=config.DIR_REPO_SE,
                          temp_alt=config.DIR_TEMP_ALT,
                          arch_exe=config.ARCH_EXE_SE,
                          arch_flags=flags,
                          trim_fomod=True,
                          warn_readmes=False)
    shutil.rmtree(config.DIR_SCRIPTS_SE)
except Exception as error:
    logger.exception(error)
