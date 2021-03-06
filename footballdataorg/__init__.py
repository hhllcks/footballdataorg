# logging
# adding NullHandler() to prevent log messages if the user does not want to see them
# see http://docs.python-guide.org/en/latest/writing/logging/#logging-in-a-library
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())
