"""
 - Logging allows you to report progress and problems in your code
 - With logging you can leave a trail of breadcrumbs so you can
   determine the cause
 - Logging gives you information of which parts of your code have
   executed, and what problems may have arisen
 - Levels: Debug, Info, Warning, Error, Critical
"""

import logging

print(dir(logging))
#  - The entries in all caps are constants
#  - The capitalized items are classes
#  - The items that start with a lower case are methods

# Create and configure logger
logging.basicConfig(filename=)

