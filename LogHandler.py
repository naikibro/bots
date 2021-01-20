# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 12:39:51 2021

@author: Vaanaiki
"""

import datetime

class LogHandler:
    
    def __init__(self):
        
        self.log = "log.txt"
        
    def logit(self):
    
        log_time = datetime.datetime.now()    
        
        file = open("log.txt", "a+")
        file.writelines("\n"+str(log_time.year)+str(log_time.month)+str(log_time.day)+"--"+str(log_time.hour)+"-"+str(log_time.minute)+" : "+self.text)
        file.close()
       
    