#! /usr/bin/env python
#
# OldMonk Auto trading Bot
# Desc: Main File implements Bot
# Copyright 2018, Joshith Rayaroth Koderi. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
import time
import pkgutil
import pprint
import sys
from decimal import *
import argparse
import os

from flask import Flask, request, send_from_directory

from utils import getLogger
from utils.readconf import readConf
from dateparser import conf

log = getLogger ('UI')
log.setLevel(log.CRITICAL)

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'web/static')

def server_main ():
    app = Flask(__name__, root_path='web/', static_url_path='/web/')

    @app.route('/js/<path:path>')
    def send_js(path):
        return send_from_directory('js', path)
    @app.route('/')
    def root():
        return app.send_static_file('index.html')
    
    log.debug ("starting server..")
    app.run()
    log.error ("server finished!")
        
def arg_parse ():
    parser = argparse.ArgumentParser(description='OldMonk Auto Trading Bot UI Server')

    parser.add_argument('--version', action='version', version='%(prog)s 0.0.1')
    parser.add_argument("--clean", help='Clean states and exit. Clear all the existing states', action='store_true')
#     parser.add_argument("--config", help='OldMonk Global config file')
#     parser.add_argument("--backtesting", help='do backtesting', action='store_true')
    
    args = parser.parse_args()
    
    if (args.clean):
        exit (0)
#     if (args.backtesting):              
#         log.debug ("backtesting enabled")       
#         sims.backtesting_on = True
#     else:
#         log.debug ("backtesting disabled")       
#         sims.backtesting_on = False        
#                  
#     if (args.config):
#         log.debug ("config file: %s"%args.config)
#         if False == load_config (args.config):
#             log.critical ("Config parse error!!")
#             parser.print_help()
#             exit(1)
#         else:
#             log.debug ("config loaded successfully!")
# #             exit (0)
#     else:
#         parser.print_help()
#         exit(1)

######### ******** MAIN ****** #########
if __name__ == '__main__':
    
    arg_parse()
    
    getcontext().prec = 8 #decimal precision
    
    print("Starting OldMonk UI server..")
    
    try:
        log.debug ("Starting Main forever loop")
        server_main ()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()
    except:
        print ("Unexpected error: ",sys.exc_info())
        raise
    #'''Not supposed to reach here'''
    print("\nOldMonk UI Server end")
    

#EOF
