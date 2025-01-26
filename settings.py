import ollama

class Settings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Settings, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return

        self._initialized = True
        self.selected_model = None
        try:
            self.models = ollama.list()['models']
        except Exception as e:
            print(f"Could not get list of Ollama models due to exception: {e}")
            self.models = []    # initialize empty list and continue
        # Create a dict with the name of the model as key
        self.models_dict = { item['model']: item for item in self.models }
        self.models_list = list(self.models_dict.keys())
        if self.models and len(self.models) > 0:
            self.selected_model = self.models[0]

    def set_model(self, name: str):
        self.selected_model = self.models_dict[name]

    def get_model_name(self):
        return self.selected_model['model']
