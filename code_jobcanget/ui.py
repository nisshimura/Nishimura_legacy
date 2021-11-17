    # def load_ui(self, loading):
    #     if loading == True:
    #         application = wx.App()
    #         frame = wx.Frame(None, wx.ID_ANY, 'LoadingStatus', size=(300, 200))

    #         panel = wx.Panel(frame, wx.ID_ANY)

    #         s_text_1 = wx.StaticText(panel, wx.ID_ANY, 'Loading...')

    #         layout = wx.BoxSizer(wx.VERTICAL)
    #         layout.Add(s_text_1)

    #         panel.SetSizer(layout)

    #         frame.Show()
    #         application.MainLoop()
    #     else:
    #         application = wx.App()
    #         frame = wx.Frame(None, wx.ID_ANY, 'LoadingStatus', size=(300, 200))

    #         panel = wx.Panel(frame, wx.ID_ANY)

    #         s_text_1 = wx.StaticText(panel, wx.ID_ANY, 'Complete! Good job!')

    #         layout = wx.BoxSizer(wx.VERTICAL)
    #         layout.Add(s_text_1)

    #         panel.SetSizer(layout)

    #         frame.Show()
    #         application.MainLoop()