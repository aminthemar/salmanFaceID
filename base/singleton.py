class Singleton(object):
    __instance = None
    initialized = False

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.initialized:
            return
        self.initialized = True
