# *-* coding: utf-8 *-*
import wx

# pip install -U wxPython
# app = wx.App()
# win = wx.Frame(None)
# win.Show()
# app.MainLoop()

# app = wx.App()
# win = wx.Frame(None)
# btn = wx.Button(win)
# win.Show()
# app.MainLoop()

# Save按钮被遮盖掉了
# app = wx.App()
# win = wx.Frame(None, title='Simple Editor')
# loadButton = wx.Button(win, label='Open')
# saveButton = wx.Button(win, label="Save")
# win.Show()
# app.MainLoop()

# 设置按钮位置（固定的，不随窗口改变而改变）
# app = wx.App()
# win = wx.Frame(None, title='Simple Editor', size=(410, 335))
# win.Show()
# loadButton = wx.Button(win, label='Open', pos=(225, 5), size=(80, 25))
# saveButton = wx.Button(win, label="Save", pos=(315, 5), size=(80, 25))
# fileName = wx.TextCtrl(win, pos=(5, 5), size=(210, 25))
# contents = wx.TextCtrl(win, pos=(5, 35), size=(390, 260), style=wx.TE_MULTILINE | wx.HSCROLL)   # 联合TE_MULTILINE（垂直滚动条）和HSCROLL（水平滚动条）
# app.MainLoop()

# 使用尺寸器
# app = wx.App()
# win = wx.Frame(None, title='Simple Editor', size=(410, 335))
# bkg = wx.Panel(win)
# loadButton = wx.Button(bkg, label='Open')
# saveButton = wx.Button(bkg, label='Save')
# filename = wx.TextCtrl(bkg)
# contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)
# # wx.EXPAND 标记确保组件会扩展到所分配的空间中
# # wx.LEFT wx.RIGHT wx.TOP wx.BOTTOM wx.ALL 决定边框参数应用于哪儿个边，边框参数用于设置边缘宽度
# hbox = wx.BoxSizer()    # 默认是水平布局
# hbox.Add(filename, proportion=1, flag=wx.EXPAND)            # proportion=1表示水平拉伸时filename获得了全部的额外空间
# hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)
# hbox.Add(saveButton, proportion=0, flag=wx.LEFT, border=5)
#
# vbox = wx.BoxSizer(wx.VERTICAL)
# vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
# vbox.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)
# bkg.SetSizer(vbox)
# win.Show()
#
# app.MainLoop()

# 完整版
# def load(event):
#     file = open(filename.GetValue())
#     contents.SetValue(file.read())
#     file.close()
#
# def save(event):
#     file = open(filename.GetValue(), 'w')
#     file.write(contents.GetValue())
#     file.close()
#
# app = wx.App()
# win = wx.Frame(None, title='Simple Editor', size=(410, 335))
# bkg = wx.Panel(win)
# loadButton = wx.Button(bkg, label='Open')
# loadButton.Bind(wx.EVT_BUTTON, load)
# saveButton = wx.Button(bkg, label='Save')
# saveButton.Bind(wx.EVT_BUTTON, save)
# filename = wx.TextCtrl(bkg)
# contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)
#
# hbox = wx.BoxSizer()
# hbox.Add(filename, proportion=1, flag=wx.EXPAND)
# hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)
# hbox.Add(saveButton, proportion=0, flag=wx.LEFT, border=5)
#
# vbox = wx.BoxSizer(wx.VERTICAL)
# vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
# vbox.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)
# bkg.SetSizer(vbox)
# win.Show()
#
# app.MainLoop()

def hello(event):
    print("Hello World!")
app = wx.App()
win = wx.Frame(None, title="Hello, wxPython!", size=(200, 100))
button = wx.Button(win, label="Hello")
button.Bind(wx.EVT_BUTTON, hello)
win.Show()
app.MainLoop()
