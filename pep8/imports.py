# Part 1 Imports
import collections  # imports always at the top of a file

# do this
from os import chdir, chflags, chown
# not this
from os import *  # not this

# Why? If we were to import another package above that used the same name as a module in os, we'd get a conflict.
# It's best to stay as explicit as possible.

# Do this
import os
import collections
import multiprocessing

#not this
#import os, collections, multiprocessing

# I have to comment that last line out, AutoPep8 won't let me save if the 3 imports are on the same line.

# Which order should we import packages?

# 1. Standard Library Imports
# 2. Related Third Party Imports
# 3. Local Application / Library Specific Imports
