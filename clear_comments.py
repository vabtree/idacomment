# Clear all (anterior)comments by funcap using IDAPython (python 2.7.10)

from idaapi import *
from idc import DelExtLnA, SetColor, Refresh, RefreshLists

def refresh_disassembly():
    Refresh()
    return "disassembly"

def refresh_lists():
    RefreshLists()
    return "lists"

def clear_comments():
    ea = idaapi.cvar.inf.minEA   
    while ea != BADADDR:
        DelExtLnA(ea, 0)                    # delete anterior comments
        SetColor(ea, CIC_FUNC, DEFCOLOR)    # set default color of functions and data
        SetColor(ea, CIC_ITEM, DEFCOLOR)
        ea = idaapi.next_head(ea, idaapi.cvar.inf.maxEA)
    
    print "[*] refreshing", refresh_disassembly(), "..ok"
    print "[*] refreshing", refresh_lists(), "..ok"

  # For python 3.x and above - comment above 2 print statements & uncomment next 2 print statements below this line
  # print("[*] refreshing", refresh_disassembly(), "..ok")
  # print("[*] refreshing", refresh_lists(), "..ok")
    return None

clear_comments()    # execute
