import wx
import wx.dataview as dv
import random
import string
from support import *





class MainFrame(wx.Frame):

    # A Frame that says Hello World
    def __init__(self, *args, **kwargs):
        #ensure the parent's __init__ is called
        super(MainFrame, self).__init__(*args, **kwargs)
        self.Xmlpath = None
        self.BinPath = None

        # Create a panel in the frame
        pnl = wx.Panel(self)
        # put some text with a larger bold font on it
        box = wx.BoxSizer(wx.VERTICAL)
        st = wx.StaticText(pnl, -1 , label="Opus Optimization Statistics",  style = wx.ALIGN_CENTER)
        font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.BOLD)
        st.SetFont(font)
        box.Add(st, 1, wx.ALIGN_CENTER,40)
        # Puting the stm logo
        img = wx.Image(get_icon('stm.jpeg'), wx.BITMAP_TYPE_JPEG)
        img.Rescale(40,40)

        self.StmImg = wx.StaticBitmap(pnl,wx.ID_ANY, wx.BitmapFromImage(img))
        #box.Add(self.StmImg,0,wx.ALIGN_LEFT, 5)
        # create the first TextBox
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        l1 = wx.StaticText(pnl, -1, label=" XML location :    ")
        font1 = wx.Font(12, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        l1.SetFont(font1)
        hbox1.Add(l1, 0,  wx.ALIGN_LEFT)
        # including  a control text
        self.t1 = wx.TextCtrl(pnl, -1, size =(20,30) )
        hbox1.Add(self.t1, 1,wx.ALIGN_LEFT)
        #include a button to text1
        self.b1 = wx.Button(pnl,-1, label = "Add")
        hbox1.Add(self.b1, 0, wx.ALIGN_LEFT)

        # create the second TextBox
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        l2 = wx.StaticText(pnl, -1, label=" Binary location : ")
        font2 = wx.Font(12, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        l2.SetFont(font2)
        hbox2.Add(l2, 0, wx.ALIGN_LEFT)
        # including  a control text
        self.t2 = wx.TextCtrl(pnl, -1, size=(20, 30))
        hbox2.Add(self.t2, 1, wx.ALIGN_LEFT)
        # include a button to text1
        self.b2 = wx.Button(pnl, -1, label="Add")
        hbox2.Add(self.b2, 0, wx.ALIGN_LEFT)
        #include process button
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.b3 = wx.Button(pnl, -1, label="Generate")
        self.b4 = wx.Button(pnl, -1, label="Configuration")
        hbox3.Add(self.b3, 0, wx.ALIGN_RIGHT)
        hbox3.Add(self.b4, 0, wx.ALIGN_LEFT)


        box.Add(hbox1, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND,40)
        box.Add(hbox2, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND)
        box.Add(hbox3, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND)

        #include a icone for this frame
        ico = wx.Icon(get_icon('iconmain.png'), wx.BITMAP_TYPE_ICO)

        # put some text with a larger bold font on it
        pnl.SetSizer(box)
        self.makeMenuBar()
        self.CreateStatusBar()
        self.SetStatusText("Welcome to @Opus Optimization statistics")
        self.SetSize(wx.Size(700,250))
        self.SetSizeHintsSz(wx.Size(700, 250), wx.Size(700, 250))
        self.SetIcon(ico)
        self.Bind(wx.EVT_BUTTON,self.ProcessXml_Button,self.b1)
        self.Bind(wx.EVT_BUTTON, self.ProcessBin_Button, self.b2)
        self.Bind(wx.EVT_BUTTON, self.ProcessGenerate_Button, self.b3)
        self.Bind(wx.EVT_BUTTON, self.Config_Button, self.b4)

        # create a menu bar
    def ProcessXml_Button(self, event):
        with wx.FileDialog(self, "Select your XML's Profile file",
                                 wildcard ="XML files (*.xml)|*.xml",
                                 style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            self.Xmlpath = fileDialog.GetPath()

            if self.Xmlpath != None:
                self.t1.AppendText(self.Xmlpath + " ")
                try:
                    with open(self.Xmlpath, 'r' ) as file:
                        print("OK")
                except IOError:
                    self.error_msg = wx.MessageDialog(self, "cannot open file XML file")
                    wx.LogError("cannot open file ")


    def ProcessBin_Button(self, event):

        with wx.FileDialog(self, "Select your binary file",
                           wildcard="Binaries(*.bin, *elf)|*.bin;*.elf",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            self.BinPath = fileDialog.GetPath()


            if self.BinPath != None:
                self.t2.AppendText(self.BinPath + " ")
                try:
                    with open(self.BinPath, 'r' ) as file:
                        print("OK")
                except IOError:
                    self.error_msg = wx.MessageDialog(self, "cannot open file XML file")
                    wx.LogError("cannot open file ")



    def ProcessGenerate_Button(self, event):

        if self.Xmlpath !=None and self.BinPath != None:
            ProsFrame = ProcessingFrame(parent= None)
            ProsFrame.Show()
            ProsFrame.MakeModal(True)
        else:
            Warning_Msg = wx.MessageDialog(self,"!Please add your XML and Binary File")
            Warning_Msg.ShowModal()
            Warning_Msg.Destroy()

    def Config_Button(self, event):
        configframe = ConfigFrame(parent = None)
        configframe.Show()




    def makeMenuBar(self):
        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        Xmlitem = fileMenu.Append(-1, "&Add XML \tCtrl-H",
                                "Select the path of your XML file ")

        Binitem = fileMenu.Append(-1, "&Add Bin \tCtrl-A",
                                "Select the path of your Binary file ")


        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnXml, Xmlitem)
        self.Bind(wx.EVT_MENU, self.OnBin, Binitem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        #close the frame, terminating the applicaiton.
        self.Close(True)

    def OnXml(self, event):
        #openXmlFile
        with wx.FileDialog(self, "Select your XML's Profile file",
                                 wildcard ="XML files (*.xml)|*.xml",
                                 style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            self.Xmlpath = fileDialog.GetPath()

            if self.Xmlpath != None:
                self.t1.AppendText(self.Xmlpath + " ")
                try:
                    with open(self.Xmlpath, 'r' ) as file:
                        print("OK")
                except IOError:
                    self.error_msg = wx.MessageDialog(self, "cannot open file XML file")
                    wx.LogError("cannot open file ")


    def OnBin(self, event):
        #openBinFile
        with wx.FileDialog(self, "Select your binary file",
                           wildcard="Binaries(*.bin, *elf)|*.bin;*.elf",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            self.BinPath = fileDialog.GetPath()

            if self.BinPath != None:
                self.t1.AppendText(self.BinPath + " ")
                try:
                    with open(self.BinPath, 'r' ) as file:
                        print("OK")
                except IOError:
                    self.error_msg = wx.MessageDialog(self, "cannot open file XML file")
                    wx.LogError("cannot open file ")



    def OnAbout(self, event):

        wx.MessageBox("This is @wxPython HelloWorld Sample",
                      "About HelloWorld2",
                      wx.OK | wx.ICON_INFORMATION)


class ConfigFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id =wx.ID_ANY, title = "Configuration",
                          pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # Create a panel in the frame
        configpnl = wx.Panel(self)
        # put some text with a larger bold font on it
        configbox1 = wx.BoxSizer(orient = wx.HORIZONTAL)
        st = wx.StaticText(configpnl, -1, label="Configuration", style=wx.ALIGN_CENTER)
        font = wx.Font(10, wx.ROMAN, wx.NORMAL, wx.BOLD)
        st.SetFont(font)
        configbox1.Add(st, 0, wx.ALIGN_CENTER)
        self.SetSize(wx.Size(700, 360))
        self.Layout()



class ProcessingFrame(wx.Frame):
    def __init__(self, parent):
     wx.Frame.__init__(self, parent, id =wx.ID_ANY, title = "OPUS Results",
                       pos = wx.DefaultPosition, size = wx.DefaultSize ,  style = wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)


     self.SetSizeHintsSz(wx.Size(892, 560),wx.Size(892, 560))

      #create the main process Panel
     ProcessPnl = wx.BoxSizer(wx.VERTICAL)
     DataPanel = wx.FlexGridSizer(0, 1, 0, 0)
     DataPanel.SetFlexibleDirection(wx.BOTH)
     DataPanel.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

     self.m_dataviewCtrl1 = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(892,560),
                                                     dv.DV_MULTIPLE | dv.DV_ROW_LINES | dv.DV_VARIABLE_LINE_HEIGHT)
     self.m_dataviewCtrl1.AppendTextColumn(" Function Name", 0, width=210)
     self.m_dataviewCtrl1.AppendTextColumn("Cycles", 1, width=210, mode=dv.DATAVIEW_CELL_EDITABLE)
     self.m_dataviewCtrl1.AppendDateColumn('Address', 2, width=70, mode=dv.DATAVIEW_CELL_EDITABLE)
     self.data = None;
     self.log = None;
     self.model = MyTreeListModel(data = self.data, log = self.log)
     self.m_dataviewCtrl1.AssociateModel(self.model)


     DataPanel.Add(self.m_dataviewCtrl1,0,wx.EXPAND, 5)

     self.SetSizer(ProcessPnl)
     self.SetSize(wx.Size(700, 360))
     self.Layout()


     self.Bind(wx.EVT_CLOSE,self.OnClose)



    def OnClose(self, event):
        self.MakeModal(False)
        event.Skip()


class MyTreeListModel(dv.PyDataViewModel):
    def __init__(self, data, log):
        dv.PyDataViewModel.__init__(self)
        self.data = data
        self.log = log

        # The objmapper is an instance of DataViewItemObjectMapper and is used
        # to help associate Python objects with DataViewItem objects. Normally
        # a dictionary is used so any Python object can be used as data nodes.
        # If the data nodes are weak-referencable then the objmapper can use a
        # WeakValueDictionary instead. Each PyDataViewModel automagically has
        # an instance of DataViewItemObjectMapper preassigned. This
        # self.objmapper is used by the self.ObjectToItem and
        # self.ItemToObject methods used below.
        self.objmapper.UseWeakRefs(True)

    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return 3

    # Map the data column numbers to the data type
    def GetColumnType(self, col):
        mapper = {0: 'string',
                  1: 'integer',
                  2: 'string',
                  }
        return mapper[col]

    def GetChildren(self, parent, children):
        # The view calls this method to find the children of any node in the
        # control. There is an implicit hidden root node, and the top level
        # item(s) should be reported as children of this node. A List view
        # simply provides all items as children of this hidden root. A Tree
        # view adds additional items as children of the other items, as needed,
        # to provide the tree hierachy.
        ##self.log.write("GetChildren\n")

        # If the parent item is invalid then it represents the hidden root
        # item, so we'll use the genre objects as its children and they will
        # end up being the collection of visible roots in our tree.
        if not parent:
            for genre in self.data:
                children.append(self.ObjectToItem(genre))
            return len(self.data)

        # Otherwise we'll fetch the python object associated with the parent
        # item and make DV items for each of it's child objects.
        node = self.ItemToObject(parent)
        if isinstance(node, Genre):
            for song in node.songs:
                children.append(self.ObjectToItem(song))
            return len(node.songs)
        return 0

    def IsContainer(self, item):
        # Return True if the item has children, False otherwise.
        ##self.log.write("IsContainer\n")

        # The hidden root is a container
        if not item:
            return True
        # and in this model the genre objects are containers
        node = self.ItemToObject(item)
        if isinstance(node, Genre):
            return True
        # but everything else (the song objects) are not
        return False

        # def HasContainerColumns(self, item):

    #    self.log.write('HasContainerColumns\n')
    #    return True

    def GetParent(self, item):
        # Return the item which is this item's parent.
        ##self.log.write("GetParent\n")

        if not item:
            return dv.NullDataViewItem

        node = self.ItemToObject(item)
        if isinstance(node, Genre):
            return dv.NullDataViewItem
        elif isinstance(node, Song):
            for g in self.data:
                if g.name == node.genre:
                    return self.ObjectToItem(g)

    def GetValue(self, item, col):
        # Return the value to be displayed for this item and column. For this
        # example we'll just pull the values from the data objects we
        # associated with the items in GetChildren.

        # Fetch the data object for this item.
        node = self.ItemToObject(item)

        if isinstance(node, Genre):
            # We'll only use the first column for the Genre objects,
            # for the other columns lets just return empty values
            mapper = {0: node.name,
                      1: "",
                      2: "",
                      3: "",
                      4: wx.DateTimeFromTimeT(0),  # TODO: There should be some way to indicate a null value...
                      5: False,
                      }
            return mapper[col]


        elif isinstance(node, Song):
            mapper = {0: node.genre,
                      1: node.artist,
                      2: node.title,
                      3: node.id,
                      4: node.date,
                      5: node.like,
                      }
            return mapper[col]

        else:
            raise RuntimeError("unknown node type")

    def GetAttr(self, item, col, attr):
        ##self.log.write('GetAttr')
        node = self.ItemToObject(item)
        if isinstance(node, Genre):
            attr.SetColour('blue')
            attr.SetBold(True)
            return True
        return False

    def SetValue(self, value, item, col):
        self.log.write("SetValue: %s\n" % value)

        # We're not allowing edits in column zero (see below) so we just need
        # to deal with Song objects and cols 1 - 5

        node = self.ItemToObject(item)
        if isinstance(node, Song):
            if col == 1:
                node.artist = value
            elif col == 2:
                node.title = value
            elif col == 3:
                node.id = value
            elif col == 4:
                node.date = value
            elif col == 5:
                node.like = value


# ----------------------------------------------------------------------

# We'll use instaces of these classes to hold our music data. Items in the
# tree will get associated back to the coresponding Song or Genre object.

class Song(object):
    def __init__(self, id, artist, title, genre):
        self.id = id
        self.artist = artist
        self.title = title
        self.genre = genre
        self.like = False
        # get a random date value
        d = random.choice(range(27)) + 1
        m = random.choice(range(12))
        y = random.choice(range(1980, 2005))
        self.date = wx.DateTimeFromDMY(d, m, y)

    def __repr__(self):
        return 'Song: %s-%s' % (self.artist, self.title)


class Genre(object):
    def __init__(self, name):
        self.name = name
        self.songs = []

    def __repr__(self):
        return 'Genre: ' + self.name








if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
     app = wx.App(False)
     frm = MainFrame(None, title='Opus Optimization Statistics')
     frm.Centre()
     frm.Show()
     app.SetTopWindow(frm)
     app.MainLoop()
