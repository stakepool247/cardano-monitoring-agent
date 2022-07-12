from os import path
import configparser
from .args import args

class ConfigParser(configparser.ConfigParser):
    """Can get options() without defaults
    """
    def options(self, section, no_defaults=False, **kwargs):
        if no_defaults:
            try:
                return list(self._sections[section].keys())
            except KeyError:
                raise configparser.NoSectionError(section)
        else:
            return super().options(section, **kwargs)

config = ConfigParser()
config.read(path.join(path.dirname(path.realpath(__file__)), 'default.ini'))
if args.config_file is not None:
    config.read(args.config_file)

# TODO: Validate config
