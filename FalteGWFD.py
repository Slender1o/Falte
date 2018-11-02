'''
    Writer: Martin Belt
    Date: 10/14/18
    Time: 6:47 PM CST
    Program: txt.exe

    Code development: George W. F. Downing
    Joined: 10/25/18
    Time: 9:05 AM CST
'''
import time
import random
import sys
raceList = ["Orc","Human","Elf","Dwarf"]
positive = ["Yes","yes","Sure","sure","ok","OK","Ok","oK",
            "Okay","okay","Y","y","K","k","KK","kk","Kk","kK"]
def wait(wait,NS):
    time.sleep(wait)
    if NS == False:
        print ("\n" * 64)

def dprint(s,ND):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)
    print("\n\n")

def raceI(WTR,CLTHSM,CLTHSF,RCE,INTRO):
    WTR = str(WTR)
    CLTHSM = str(CLTHSM)
    CLTHSF = str(CLTHSF)
    INTRO = str(INTRO)
    dprint(INTRO+RCE[2]+" .")
    while urmom == 'strait':
        dprint(" You can't help but feel nauseous while in the "+WTR+" of water.\n")
        dprint("Would you like to get out?")
        response = input("\n\n>")
    
        if response in positive:
            dprint("You get out of the water. ")
            wait(3,True)
            if  gender == 'Female':
                dprint(CLOTHSF)
            else:
                dprint(CLOTHSM)
            urmom = ("gay")
            wait(10,False)
        else:
            dprint("Despite the Nausea, you think that you should stay in the water for a little while longer.\n")
            wait(3,True)
    
#main intro
                
print ("\n" * 64)

dprint ("You are surrounded in darkness. Everything that you see is dark and confusing.")

wait(6,True)

dprint("A warm light surrounds you and you hear a voice:")

wait(3,True)

dprint("Who are you, Adventurer? What is your proper name?")
Name = input("\n\n>")

wait(3,True)
print ("\n\n")
dprint("..and your nickname, " + Name + "?")
nickName = input("\n\n>")

wait(1,True)

dprint(Name + "...that is a good, strong name. ")

dprint("You have a choice, " + nickName + ". You can become the fabled hero of Falte or you can die in the process.")

dprint(" I will now transport you into the country of Falte...\n")

wait(10,False)

dprint("You wake up in a pool of soothing water. Your memory is hazy, at best, and you can't seem to figure out where you are.")

dprint(" As you look around, you can't seem to figure out what your body looks like. You concentrate...")

wait(3,False)

dprint("As you inspect what little you can see of your body, you remember that you are...")
dprint("What is your gender?")
gender = input("\n\n>")

if gender == 'Female':
    dprint("You remember your feminine charms and whims.")
    wait(2,True)
    dprint("You are a woman.")
if gender == 'Male':
    dprint("You remember your manly muscles and all your feats of strength.")
    wait(2,True)
    dprint("You are a man.")

wait(6,False)

#pick your poison

for i in range(0,3):
  dprint(raceList[i],"\n")
    
dprint("What is your race, " + Name + "?\n")
race = input("\n\n>")
print ("\n\n")
dprint("Yes. That's right. You're a(n) " + race + ".")

wait(6,False)

if race == 'Elf':

    raceI("pool","There is a tunic and a pair of boots.","There is a dress, a hair clip and a pair of boots.",

        ["Elf","elf","Elven","elven"],"You look around and see that you are in a tent with guards standing outside. They are ")
