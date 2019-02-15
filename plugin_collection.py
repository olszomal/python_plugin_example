class Plugin:
    """Base class that each plugin must inherit from. within this class
    you must define the methods that all of your plugins must implement
    """

    def __init__(self):
        pass

    def perform_operation(self, argument):
        """The method that we expect all plugins to implement. This is the
        method that our framework will call
        """
        raise NotImplementedError




class PluginCollection:
    """Upon creation, this class will read the plugins folder for modules
    that contain a class definition that is inheriting from the Plugin class
    """

    def __init__(self, plugin_folder):
        """Constructor that initiates the reading of all available plugins
        when an instance of the PluginCollection object is created
        """
        self.plugin_folder = plugin_folder
        self.walk_folder()

    def walk_folder(self):
        pass