"""
This type stub file was generated by pyright.
"""

from IPython.core.magic import Magics, line_magic, magics_class

"""Implementation of configuration-related magic functions.
"""
reg = ...
@magics_class
class ConfigMagics(Magics):
    def __init__(self, shell) -> None:
        ...
    
    @line_magic
    def config(self, s): # -> None:
        """configure IPython

            %config Class[.trait=value]

        This magic exposes most of the IPython config system. Any
        Configurable class should be able to be configured with the simple
        line::

            %config Class.trait=value

        Where `value` will be resolved in the user's namespace, if it is an
        expression or variable name.

        Examples
        --------

        To see what classes are available for config, pass no arguments::

            In [1]: %config
            Available objects for config:
                AliasManager
                DisplayFormatter
                HistoryManager
                IPCompleter
                LoggingMagics
                MagicsManager
                OSMagics
                PrefilterManager
                ScriptMagics
                TerminalInteractiveShell

        To view what is configurable on a given class, just pass the class
        name::

            In [2]: %config LoggingMagics
            LoggingMagics(Magics) options
            ---------------------------
            LoggingMagics.quiet=<Bool>
                Suppress output of log state when logging is enabled
                Current: False

        but the real use is in setting values::

            In [3]: %config LoggingMagics.quiet = True

        and these values are read from the user_ns if they are variables::

            In [4]: feeling_quiet=False

            In [5]: %config LoggingMagics.quiet = feeling_quiet

        """
        ...
    


