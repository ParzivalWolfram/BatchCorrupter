"""
BatchCorrupt v0.379a, release "Slow improvements, but years later... better late than never?"
by Parzival Wolfram (parzivalwolfram@gmail.com)
Released under <LICENSE>, head to <URL> to read it

Decent CLI coming soon.
This currently only replaces bytes with other bytes, now with flaky addition or subtraction. Additional modes coming... soon? Maybe?

so i've come back to this like a year later and i wanna die way more now, so i did a shit job at annotating it. it also corrupted itself at one point (probably more) so comments may have small issues

don't worry, past me, it's 2022 now and none of this is okay, but i'm still learning how min() and max() work so it's probably fine
"""

#2/21/2022: i made this :)
debug = False
superdebug = False

#3/12/22: mmm yes built-in logging
logging = False
logName = "../corrupter.log"
logFileHandle = 0

import sys #we need this for one fucking thing and it's not able to be from-imported
from datetime import date
from time import time
if sys.version_info[0] >= 3: #so we don't eat shit in Py3 but we stay Py2 compatible because fuck maintaining this twice just for my XP fuckery
        raw_input = input #you're fucking gay and you know it, py3



#3/12/22: adding this entire block for basic flag passing for things like debugging and self-logging
argvlist = sys.argv
if "python" in argvlist[0]: #check for "python <scriptname>" as well as just <scriptname>
        del argvlist[1]
del argvlist[0]
for argvbuf in argvlist: #this isn't i because this is actually optimization of a block i wrote like 20 minutes ago so it's not i for code reuse reasons
        tempflag = False
        if "--log=" in argvbuf: #check logging before debug flags in case custom lig name has "-v" or "-vv" in it
                logName = argvbuf.strip("--log=")
                tempflag = True
        if "--log" in argvbuf:
                logging = True
                logFileHandle = open(logName,"w+")
                logFileHandle.write("==================================================================")
                logFileHandle.write(str(date.fromtimestamp(time())))
                logFileHandle.write("==================================================================")
        if "--super" in argvbuf or "--superdebug" in argvbuf: #superdebug is DEADLY if you have logging on too!!!
                superdebug = True
        if "-vv" in argvbuf and not tempflag: #don't try to check for short flags in the custom path, dumbass
                superdebug = True
        if "-v" in argvbuf and not tempflag: #this one still catches -vv, can you tell me why? :)
                debug = True
        if "--debug" in argvbuf or "--verbose" in argvbuf: #check for standard debug flag
                debug = True

def sendLog(inputString): #3/12/22: logging is nice, my code does not
        stringType = inputString[:4]
        if stringType == "DEBUG" and debug:
                print(inputString)
                if logging:
                        logFileHandle.write(inputString)
        elif stringType == "SUPER" and superdebug:
                print(inputString)
                if logging:
                        logFileHandle.write(inputString)
        elif stringType != "DEBUG" and stringType != "SUPER":
                print(inputString)
                if logging:
                        logFileHandle.write(inputString)



"""3/12/22: fuck it. user's responsibility.

def warnUser(): #why the loops have to look like this i'll never fucking know, you'd think there'd be a better way
        print("\n\n\n\n\n!!!!!!!!!!!!!!!!!!WARNING WARNING WARNING!!!!!!!!!!!!!!!!!!\nYOU ARE NOT RUNNING THIS SCRIPT INSIDE A WHITELISTED DIRECTORY\nTHIS SCRIPT CAN EASILY HOSE A SYSTEM\n\nENSURE YOU MEAN TO RUN THIS SCRIPT IN THIS FOLDER,\nTHEN TYPE \"I AGREE\" AT THE NEXT PROMPT.") #fuck readability, this is about LINE COUNT, motherfucker, scrollbars exist and you need to start fucking using them!
        while True:
                if str(raw_input("\n\nTYPE \"I AGREE\" TO CONTINUE.\nInput> ")).lower() == "i agree": #"if \"i agree\" in" is a shit solution, what am i, high?                                maybe
                        break
                print("\n\nTRY AGAIN.")

if cwd[:5] != "/home" and cwd[0] != "~" and cwd[:4] != "/tmp" and cwd[:8] != "C:\\Users" and cwd[:12] != "C:\\Documents": #if we're not running from somewhere that's usually fairly safe...
        warnUser() #freak the fuck out.
        #why this doesn't always detect properly is fucking beyond me
"""

import os
cwd = str(os.getcwd()) #why can't this be "getcd?"
if debug: #3/11/22: might as well add these to debug strings already here too
        sendLog("DEBUG: cwd="+cwd)

import random #import trimming needs done you fat fuck
if debug: #3/11/22: might as well add these to debug strings already here too, electric boogaloo
        sendLog("DEBUG: argv="+str(sys.argv))
        sendLog("DEBUG: basefile="+str(os.path.basename(__file__)))

def recursive():
        return sorted([os.path.join(root, name) for root, dirs, files in os.walk('.') for name in files]) #walks the entire folder tree from current dir downward, returns list of paths. 2/21/2022: now sorted for fun
def standard():
        return [f for f in os.listdir('.') if os.path.isfile(f)] #returns list of files in current folder only

def corrupt(fileName):
        if fileName == "corrupter.py": #this is for dev purposes
                return 0
        try: #i forgot why this try/except block is here but i'm gonna assume "because Windows"
                fileHandle = open(fileName,"rb+") #yes, this lets us read and write binary without truncating the file. Why? Ask the Python Foundation.
        except Exception:
                return e
        fileSize = os.stat(fileName).st_size #it's like 4 lines to get this using the actual file's data and discrepancies are rare nowadays so fuck it, good enough
        skip = random.randint(128,1024) #PRNG is the spice of life and i'm tired of pretending it's not
        seek = random.randint(16, 256)
        
        method = random.randint(0,1) #3/11/22: added byte modification as well as overwriting, finally

        if debug:
                sendLog("DEBUG: fileName="+str(fileName)+";fileSize="+str(fileSize)+";skip="+str(skip)+";seek="+str(seek)+";method="+str(method))

        fileHandle.seek(skip,0) #it defaults to mode 0 for the seek but i've gotta be sure, also the vars are named after dd, yes, stop asking
        loopnum = 0
        while fileHandle.tell() <= fileSize:
                if not method:
                        rolledByte = random.randint(0,255)
                else:
                        try:
                                rolledByte = abs(ord(fileHandle.read(1))+random.randint(-10,10))%256 #3/11/22: i hope this works?
                                fileHandle.seek(-1,1)
                        except: #3/11/22: apparently not always, so fall back if needed
                                rolledByte = random.randint(0,255)
                        
                if superdebug: #2/21/2022: THIS WILL FILL A DRIVE VERY FAST.
                        sendLog("SUPER: rolledByte="+str(rolledByte)+" at "+str(fileHandle.tell())+" in mode "+str(method))
                if sys.version_info[0] >= 3: #breaks in py3 so we're checking for it
                        fileHandle.write(bytes([rolledByte])) #2/21/2022: hey dumbass, bytes(int) writes out a 0-fill of int LENGTH, not the int itself. that's gotta be an iterable to work how you want it.
                else:
                        fileHandle.write(chr(rolledByte))
                fileHandle.seek(seek,1)
                loopnum += 1
        fileHandle.flush() #on some OSes and/or Python versions you have to flush AND close or it doesn't flush because mmhmm sure why not?
        fileHandle.close()
        sendLog(str(fileName)+": corrupted "+str(loopnum)+" bytes out of "+str(fileSize)+" total, corrupted "+str(float(float(loopnum)/float(fileSize))*100)+"%.")
        return 0

while True: #this is the worst and i have yet to find a less ugly way of doing infinite looping user input validation, it makes me sad too
        try:
                prompt = int(raw_input("\n\nPlease input file handler to use.\n1 - Standard (all files in this folder)\n2 - Recursive (all files in this folder PLUS all subfolders)\n0 - Exit\n\nInput> "))
        except:
                pass
        if prompt == 0 or prompt == 1 or prompt == 2:
                break
        print("\n\nPlease try again.")

if prompt==0:
        exit(0)
elif prompt==1:
        fileArray = standard() #why bother putting some flag on which to use when this is extendable, more compact and less stupid, EARLIER ME, YOU IDIOT???
elif prompt==2:
        fileArray = recursive()
else:
        print("Internal error 374. Please report.") #this should never be hit, as we did validation, but this is here in case either Python bites it or I break the validation somehow. Or both! 
        exit(374) #number pulled out of ass, no significance
for f in fileArray:
        if str(f) != './'+str(os.path.basename(__file__)) and str(f) != "corrupter.py": #it would be bad if we corrupted whatever we're currently running from, so try not to
                errorCheck = corrupt(f) #this is also terrible
                if logging:
                        logFileHandle.flush()
                if errorCheck != 0:
                        print("Internal error has occured:\n\nFile I/O error\n\nPlease contact author and attach \"error.bin\".") #this error handler is really bad, fix immediately
                        errorDump = open("error.bin","w")
                        errorDump.append(str(errorCheck))
                        errorDump.flush()
                        errorDump.close()

if logging:
        logFileHandle.flush()
        logFileHandle.close()
# just exit i'm tired and it's like 5AM i need sleep
