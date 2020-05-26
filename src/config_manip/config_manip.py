import yaml

class Config:
    """Class for manipulating config. """
    
    class __Config:
        def __init__(self, fname):
            self.filename = fname
            self.val = {
                "database_filename": "",
                "word_lemmatization_API": "",
                "word_translation_API": "",
                "word_scoring_API": "",
                "logs_file": ""
            }
    inst = None
    def __init__(self, fname):
        """Takes path to the config file as a parameter."""
        if not Config.inst:
            Config.inst = Config.__Config(fname)
        else:
            raise Exception("You tried to instantiate new Config. You can't do such things")
    
    def save(self):
        """Saves current value of config to a file."""
        with open(Config.inst.filename, 'w') as outfile:
            yaml.dump(Config.inst.val, outfile, default_flow_style=False)

    def read(self):
        """Loads config file to a variable."""
        with open(Config.inst.filename, 'r') as infile:
            Config.inst.val = yaml.load(infile, Loader=yaml.FullLoader)

    def get(self):
        """Returns reference to a config file"""
        return Config.inst.val