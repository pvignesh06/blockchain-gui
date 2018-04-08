###########################
#  build your own blockchain from scratch in python3!
#
#   inspired by
#     Let's Build the Tiniest Blockchain In Less Than 50 Lines of Python by Gerald Nash
#     see https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b
#
#
#  to run use:
#    $ python ./blockchain.py

import hashlib as hasher
import datetime as date
import pprint
import image
import time
import Tkinter
from PIL import ImageTk, Image
import tkMessageBox
'''import pygst
pygst.require('0.10')
import gst'''
'''import gobject'''
import os

class Block:
  def __init__( self, index, data, previous_hash ):
    self.index         = index
    self.timestamp     = date.datetime.now()
    self.data          = data
    self.previous_hash = previous_hash
    self.hash          = self.calc_hash()

  def calc_hash( self ):
    sha = hasher.sha256()
    sha.update(str(self.index).encode("utf-8") +
               str(self.timestamp).encode("utf-8") +
               str(self.data).encode("utf-8") +
               str(self.previous_hash).encode("utf-8"))
    return sha.hexdigest()

  def __repr__( self ):
        return "Block< \n  index: {},\n  timestamp: {},\n  data: {},\n  previous_hash: {},\n  hash: {}\t>".format(
          self.index, self.timestamp, self.data, self.previous_hash, self.hash)


  @staticmethod
  def first( data="Genesis" ):
    return Block( 0, data, "0" )

  @staticmethod
  def next( previous, data="Transaction Data..." ):
    return Block( previous.index + 1, data, previous.hash )

root=Tkinter.Tk()
root.title("THE BLOCKCHAIN ")

#####
## let's get started
##   build a blockchain a block at a time

def blockgen():
    def nofbw():
        def center_window(width=300, height=200):
            # get screen width and height
            screen_width = window21.winfo_screenwidth ()
            screen_height = window21.winfo_screenheight ()

            # calculate position x and y coordinates
            x = (screen_width / 2) - (width / 2)
            y = (screen_height / 2) - (height / 2)
            window21.geometry ('%dx%d+%d+%d' % (width, height, x, y))

        window21 = Tkinter.Toplevel ()
        window21.geometry ("500x215")
        Results = Tkinter.Label (window21, text=blockchain)
        Results.grid (row=1, column=1)
        center_window (500, 400)

    def gui():
        window2z = Tkinter.Toplevel ()
        window2z.geometry ("1115x500")
        z12 = Tkinter.Label (window2z, text="DOWNLOAD THE SOFTWARE FROM GIT UP :https://gitup.com/pvignesh06/blockchain-gui\n").pack()
        z122 = Tkinter.Label (window2z, text="DONE BY :\nVIGNESH P\n").pack()
        Bz12 = Tkinter.Button (window2z, text="QUIT", command=quit)
        Bz12.pack ()
        Bz12.place (height=50, width=100, relx=0.42, rely=0.35)

    b0 = Block.first( "Genesis" )
    blockchain=[b0]
    nofbw()
    b1 = Block.next( b0, "Transaction Data..." )
    blockchain = [b1]
    nofbw()
    b2 = Block.next( b1, "Transaction Data......" )
    blockchain = [b2]
    nofbw()
    b3 = Block.next( b2, "More Transaction Data...")
    blockchain = [b3]
    nofbw()
    gui()

#instruction
def instruction():
    window1 = Tkinter.Toplevel ()
    window1.geometry ("1115x500")
    z1 = Tkinter.Label (window1, text="THE BLOCKCHAIN \n INSTRUCTIONS: \n We are on a mission to build a more open, accessible,  and fair financial future, one piece of software at a time.\n Our technology is revolutionizing the financial services industry by empowering millions across the globe to authenticate and transact immediately and without costly intermediaries./"
                                      "\n A global network of computers uses blockchain technology to jointly manage the database that records Bitcoin transactions. That is, Bitcoin is managed by its network, and not any one central authority. \nDecentralization means the network operates on a user-to-user (or peer-to-peer) basis. \n In our project we are just explaining how the block cain works \n so enjoy and lean the this blockchain").grid(row=0,column=0)
    Bz1 = Tkinter.Button (window1, text="OK", command=quit)
    Bz1.pack ()
    Bz1.place (height=50, width=100, relx=0.42, rely=0.35)

#about us
def about_us():
    window2 = Tkinter.Toplevel()
    window2.geometry ("1115x500")
    z2 = Tkinter.Label (window2, text="\t\t\t\t\t\t\t\t\t       THE BLOCKCHAIN\n\t\t\t\t\t\t\t\t\t       ABOUT US\n \t\t\t\t\t\t\t\t\t  This an simple software explains the working of blockchain \n\t\t\t\t\t\t\t\t\t        version:2.0\n\t\t\t\t\t\t\t\t\t       fully based on GUI\n\t\t\t\t\t\t\t\t\t       for more deatils vist:https://github.com/pvignesh06/blockchain-gui").grid (row=0, column=0)
    Bz2 = Tkinter.Button (window2, text="OK", command=quit)
    Bz2.pack ()
    Bz2.place (height=50, width=100, relx=0.45, rely=0.35)

root.geometry("900x500")
#This creates the main window of an application

root.configure(background='grey')

path = "images.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Tkinter.Label(root, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")
B1 = Tkinter.Button(root, text ="INSTRUCTION", command =instruction)
B1.pack()
B1.place( height=50, width=100,relx=0.07, rely=0.81)
B2 = Tkinter.Button(root, text ="START", command =blockgen)
B2.pack()
B2.place( height=50, width=100,relx=0.43, rely=0.81)
B3 = Tkinter.Button(root, text ="ABOUT US", command =about_us)
B3.pack()
B3.place( height=50, width=100,relx=0.75, rely=0.81)

'''
mainloop = gobject.MainLoop()
pl = gst.element_factory_make("playbin", "player")
pl.set_property('uri','file://'+os.path.abspath('intro.mp3'))
pl.set_state(gst.STATE_PLAYING)
mainloop.run()'''

root.mainloop()
######
#  will pretty print something like:
#
#  [Block<
#    index: 0,
#    timestamp: 2017-09-19 19:21:04.015584,
#    data: Genesis,
#    previous_hash: 0,
#    hash: b0cb7953bfad60415ea3b5d3b8015ee22c89d43351ea8f53e5367ee06193b1d3>,
#   Block<
#    index: 1,
#    timestamp: 2017-09-19 19:21:04.015584,
#    data: Transaction Data...,
#    previous_hash: b0cb7953bfad60415ea3b5d3b8015ee22c89d43351ea8f53e5367ee06193b1d3,
#    hash: a87707b2867d28e7367c74e4a2800ec112ea2a8b1517a332ad0b4c49c3b3d60b>,
#   Block<
#    index: 2,
#    timestamp: 2017-09-19 19:21:04.015584,
#    data: Transaction Data......,
#    previous_hash: a87707b2867d28e7367c74e4a2800ec112ea2a8b1517a332ad0b4c49c3b3d60b,
#    hash: 9a8aecdd62da47301502f0079aa1bf24dcf39ad392c723baef6b9bfbc927cf4e>,
#   Block<
#    index: 3,
#    timestamp: 2017-09-19 19:21:04.015584,
#    data: More Transaction Data...,
#    previous_hash: 9a8aecdd62da47301502f0079aa1bf24dcf39ad392c723baef6b9bfbc927cf4e,
#    hash: 5ef442875fb8c3e18d08531f3eba26ea75b608604fa0cc75715d76e15edbb5ea>]
