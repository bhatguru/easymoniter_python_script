# easymoniter_python_script

Easy moniter is a python script which is the commandline version of easy moniter gui app which you can find in my erlier repository.

This script will moniter the cpu and memory utilization and prints the value continuesly on commandline, once you configure email details in hostconfiguration file it will notify you by email when the cpu or memory reaches threshold level. By default threshold level is set to 90% you can change that in the script.

Interval is nothing but it is the time defference for sending a mail when threshold level is reached that will keep on notifying you depending on intervals you have provided.

Easy moniter script has dependency of hostconfiguration.txt file, which stores informations about esource email, password and target email and intervels as you can see in hostconfiguration file or in easy moniter.py file which is commented.

Edit the host configuration file with rightfull informations and check it out.
