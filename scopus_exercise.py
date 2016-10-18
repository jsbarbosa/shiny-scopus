# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 14:15:04 2016

@author: juan
"""

import requests
import json
#from my_scopus import MY_API_KEY

from scopus.scopus_api import ScopusAbstract

ab = ScopusAbstract("2-s2.0-84930616647")
print(ab.bibtex)
print(ab.ris)