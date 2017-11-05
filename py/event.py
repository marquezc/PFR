# ---
# event.py
# ---

import os
import filestr

def event_path(date, ev_num):
    return (filestr.base_pri_dir + '/events/ev-' + date + '-' + ev_num)

def main():

    ev_path = event_path('171022', str(0)) 
    print(ev_path) 
    print(os.path.exists(ev_path))
   

main()

