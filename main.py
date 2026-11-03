import sys
import os

project_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, project_path)

import importlib
import my_ui

importlib.invalidate_caches() # refresh le check des modules pour mieux reload nos fichiers

importlib.reload(my_ui) # reload my_ui

my_ui.main()