#Food club grabber
#ask for and get paste the page info
#weed out the arenas pirates and odds
#output a formatted text with the info
#
from tkinter import *
import re

def getPirates():
   ps = pageSource.get()
   ps2 = (re.sub(r'<.*?>',' ',ps))
  # ps3 = (re.sub(r'{.*?}','',ps2))
  # print (ps2)
   indexStart = ps2.find("NeoPoints per bet,")
   indexEnd = ps2.find("Winnings Calculator")
   ps3 = ps2[indexStart:indexEnd]
   #print (ps2[indexStart:indexEnd])
   #print (indexStart)
   #print (indexEnd)
   ps3=ps3.strip()
   #print (ps3)
  ## arenas = [["Shipwreck"],["Lagoon"],["Treasure Island"],["Hidden Cove"],["Harpoon Harry's"]]
##   allPirates =["Lucky McKyriggan", "Franchisco Corvallio", "Ol' Stripey", "Squire Venable",
##         "Peg Leg Percival","Puffo the Waister","Ned the Skipper", "Buck Cutlass",
##         "Gooblah the Grarrl","Federismo Corvallio","Bonnie Pip Culliford", "Orvinn the First Mate",
##         "The Tailhook Kid", "Stuff-A-Roo","Captain Crossblades","Scurvy Dan the Blade",
##         "Fairfax the Deckhand","Admiral Blackbeard","Sir Edmund Ogletree","Young Sproggie"]
##   currentPirates= []

   allPirates =["Lucky", "Franchisco", "Stripey", "Venable",
         "Peg","Puffo","Ned", "Buck",
         "Gooblah","Federismo","Bonnie", "Orvinn",
         "Tailhook", "Stuff-A-Roo","Crossblades","Dan",
         "Fairfax","Blackbeard","Edmund","Sproggie"]
   allOdds = ['2;','3;','4;','5;','6;','7;','8;','9;','10;','11;','12;','13;']
   currentPirates= []
   currentOdds = []


   ps4 = (re.sub(' +',' ',ps3))
   ##filter(lambda z: z in ps4, allPirates)
   ps5 = ps4.split()
  # print (ps4)
   
   ##ps5 =(re.sub(r'<.*?>','',ps4))
   for x in ps5:
      if x in allPirates:
         currentPirates.append(x)
   for y in ps5:
      if y in allOdds:
         currentOdds.append(y.replace(';',''))

  # print(currentPirates)
   #print(currentOdds)
   aString = ["Shipwreck | ","Lagoon | ","Treasure Island | ", "Hidden Cove | ", "Harpoon Harry's | "]
   b = 0
   currInd = 0
  
       
   for c in aString:
      print('\n')
      print (c, end = '')
      b=0
      while b <= 3:
         print(currentPirates[currInd], end = '/')
         currInd += 1
         b += 1

   currInd = 0
   posit = 0
   
   for v in currentOdds:
      print('\n')
      b = 0
      posit = 0
      if currInd >= len(currentOdds):
         break
      while b <= 3  and currInd < len(currentOdds):
         print(currentOdds[currInd], end = '/')
         posit += (1/int(currentOdds[currInd]))
         currInd += 1
         b += 1

      if posit < 1 :
         print('(+)')
      elif posit  == 1:
         print('(0)')
      else :
        print('(-)')
   
   
##start at shipwreck end at max bet
## for every string in betwwen the start and end find any of these
#pirates or arenas and put that pirate into the pirates array of that arena
##find the odds of said pirate and put into odds arr*make sure the first pirate foun
# is put into the array and not the other way around only need 4 loops
##for arena in arenas
##i = 0
##   while i < 3
##   #find the pirates put in arenas

    
          
master = Tk()
Label(master, text ="Paste page source here:").grid(row=0)
pageSource= Entry(master)
pageSource.grid(row = 0, column=1)

Button(master, text ='Quit', command = master.destroy).grid(row=3, column=0, sticky = W, pady=4)
Button(master, text = 'Go', command = getPirates).grid(row=3, column=1, sticky = W, pady = 4)




mainloop()
