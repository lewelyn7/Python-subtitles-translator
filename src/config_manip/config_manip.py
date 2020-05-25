import yaml

class Config:
    class __Config:
        def __init__(self, fname):
            self.filename = fname
            self.val = {
                "database_filename": "",
                "word_lemmatization_API": "",
                "word_translation_API": "",
                "word_scoring_API": ""
            }
    inst = None
    def __init__(self, fname):
        if not Config.inst:
            Config.inst = Config.__Config(fname)
        else:
            raise Exception("You tried to instantiate new Config. You can't do such things")
    
    def save(self):
        with open(Config.inst.filename, 'w') as outfile:
            yaml.dump(Config.inst.val, outfile, default_flow_style=False)

    def read(self):
        with open(Config.inst.filename, 'r') as infile:
            Config.inst.val = yaml.load(infile, Loader=yaml.FullLoader)

    def get(self):
        return Config.inst.val