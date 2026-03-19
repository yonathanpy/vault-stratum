import importlib

class Engine:
    def __init__(self):
        self.modules = {}

    def load(self, name):
        module = importlib.import_module(f"modules.{name}")
        self.modules[name] = module

    def run(self, name, target):
        if name not in self.modules:
            return "Module not loaded"
        return self.modules[name].run(target)
