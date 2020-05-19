from __future__ import print_function
import json

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    # Python 2.x fallback
    from argparse import Namespace

def j2o(data_str):
    return json.loads(data_str, object_hook=lambda d: Namespace(**d))