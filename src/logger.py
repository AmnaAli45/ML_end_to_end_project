# this is the file code writes whats happening when the code runs (helpful in finding errors)

import os
import sys
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_S')}.log" # log file ka naam kis format mein hona hai 
# datetime.now() -- > current time at which code is running
# strftime('%m_%d_%Y_%H_%M_S') --> converts the date and time in the given format
# .log --> to add .log at the end of file name

log_path = os.path.join(os.getcwd(),"logs", LOG_FILE) # path where the log file is stored
# os.grtcwd() --> path of current folder ... 
# "logs" --> cretae the folder named logs in current folder
# LOG_FILE --> create the file inside logs folder with the name stored in LOG_FILE variable
# is path k according ..folder aur file ne create hona hai

os.makedirs(log_path,exist_ok = True) # to make directory according to the path stored in log_path 
# exist_ok = True --> if the folder already exist don't give n error

LOG_FILE_PATH = os.path.join(log_path ,LOG_FILE)


logging.basicConfig(
 filename=LOG_FILE_PATH, # save all log messages in this file
 format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", # it defines how each message looks
 level =  logging.INFO # Record only INFO and higher-level logs
)
 # %(asctime)s --> Prints date and time
 # %(lineno)d --> shows line number where an error occured
 # %(name)s --> identifies which module create the logs
 # %(levelname)s --> log levels
 # %(message)s --> actual log message you wrote

 # Final log output looks like this: 
 # [2025-02-15 14:35:12] 44 main - INFO - Data loading started
