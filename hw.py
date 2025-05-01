import os
sd=input("Do you want to shutdown your computer? (yes/no):")
if sd=='no':
    exit()
else:
    os.system("Shutdown /s /t 1")