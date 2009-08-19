#!/usr/bin/env python
"""
    Ruxxer
        The Fuzzing Language.
"""
# Ruxxer is dependent on ply2.3 or greater.
from lib.rux1_0 import *
from lib.rux_ui import *
from lib.rux_grammar import *
import socket

def main_exec():
    """
        Main execution location.
    """
    start_gui()

if __name__ == "__main__":
    main_exec()

