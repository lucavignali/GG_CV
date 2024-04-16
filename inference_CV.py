import sys
import datetime
import time
import subprocess
import os

os.chdir('/home/ubuntu/environment/squeezenet1.1/')

while True:
    
    try:
       
        cmd = ['python', 'imagenet_inference.py']
        output = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output_string = output.stdout.decode("utf-8")
        error_string = output.stderr.decode("utf-8")
        
        
    except Exception as e:
        output_string = "no image file available"
        error_string = "no image file available"
        
    message = f"{output_string}! Current time: {str(datetime.datetime.now())}."
    error_message = f"{error_string}! Current time: {str(datetime.datetime.now())}."
    # Append the message to the log file.
    with open('/tmp/CV.log', 'a') as f:
        print(message, file=f)
    
    with open('/tmp/CV-error.log', 'a') as f:
        print(error_message, file=f)

    time.sleep(1)

