from speed_test import SpeedTest
from config import CSV_FILE, TEST_DELAY
from time import sleep
from datetime import datetime


while True:
    try:
        print(datetime.now())
        print("Testing ...")
        
        test = SpeedTest()
        test.test()
        print(test)
        
        print("Writing")
        with open(CSV_FILE, "a") as log_file:
            log_file.write(str(test))
            
        print("Sleeping")
        sleep(TEST_DELAY)
    except Exception as e:
        print(str(e))