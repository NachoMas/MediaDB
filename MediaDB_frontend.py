#!/usr/bin/python

import wx
import wx.grid
import os
import sqlite3
import gettext

cw = os.path.abspath(os.curdir)
dbPath = "/home/nacho/Documents/Personal_info/MultimediaDB/MultimediaMasFunke.db"

def connect():#this is the sqlite3 connection
    #con_str=cwd + '/Data/file.db'
    con_str = dbPath
    cnn = sqlite3.connect(con_str)
    return cnn
    cnn.close()

def data_rows_count():# to count the rows in the database
    con = connect()
    cur=con.cursor()
    cur.execute("SELECT * FROM Films")
    rows=cur.fetchall()
    i=0
    for r in rows:
        i+=1
    return i

class MyFrame(wx.Frame):# this is the parent frame
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.frame_1_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(1, _("Index"), "", wx.ITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu,_("Media DB"))
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(2, _("Films"), "", wx.ITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu,_("About"))
        self.SetMenuBar(self.frame_1_menubar)
        self.__set_properties()
        self.__do_layout()
        #self.Bind(wx.EVT_MENU, self.open_dialog, id=1)
        #self.Bind(wx.EVT_MENU,self.open_dialog1,id =2)

    def __set_properties(self):
        self.SetTitle(_("MediaDB"))
        self.SetSize((555, 444))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer_1)
        self.Layout()

if __name__ == "__main__":
    gettext.install("MediaDB")
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
