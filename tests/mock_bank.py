#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from src.bank import Bank
from mock import MagicMock


thing = Bank()
