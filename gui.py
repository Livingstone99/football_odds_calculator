from tkinter import *
import tkinter as tk
import sys
import os



def restart_program():
     os.execl(sys.executable, sys.executable, *sys.argv)


# from tkFileDialog   import askopenfilename
import math


# master = Tk()
#root.resizable(False, False)
#root.iconbitmap('Custom-Icon-Design-Flatastic-4-Hot.ico')
class moreTab(tk.Tk):

    def __init__(self,):
        Tk.__init__(self,)
        self.geometry("1400x600")
        container = Frame(self, bg='#c9e3c1')
        container.pack(side = "top", fill = 'both', expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.frames = {}
        for q in (pageone, widget):
            frame = q(container,self)
            self.frames[q] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.raise_frame(widget)
    def raise_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
class widget(Frame):
    def __init__(self, master = 0, control= 0):
        Frame.__init__(self, master,bg='#c9e3c1')
        self.bind("<Button-1>",self.callback1)
        self.heading = Label(self, text='GAME ANALYSIS',
                             font=('Bradley Hand ITC', '25', 'bold'),  bd=5, bg='#c9e3c1')
        self.heading.place(x=0, y=0)
        self.graph_heading = Label(self, text='Result', font=('Lucida Calligraphy', '15', 'bold'),
                                    bd=5, bg='#c9e3c1')
        self.graph_heading.place(x=930, y=5)
        self.graph_heading3 = Label(self, text='Profit/Gain', font=('Lucida Calligraphy', '15', 'bold'),
                                    bd=5, bg='#c9e3c1')
        self.graph_heading3.place(x=1100, y=5)
        self.amount_played = Label(self, text='Amount', font=('Lucida Calligraphy', '15', 'bold'),
                                    bd=5, bg='#c9e3c1')
        self.amount_played.place(x=710, y=5)
        self.graph_heading1 = Label(self, text='Enter odds', font=('Lucida Calligraphy', '20', 'bold'),
                                    bd=5, bg='#c9e3c1')
        self.graph_heading1.place(x=420, y=0)
        self.m = 0
        n = 2
        self.entrybox = Entry(self, width = 10)
        self.entrybox.place(x = 10, y = 90)
        self.entrybox2 = Entry(self, width = 10)
        self.entrybox2.place(x = 100, y = 90)
        self.vs = Label(self, text = 'vs',font=('Lucida Calligraphy', '15', 'bold'), bd=5, bg='#c9e3c1' )
        self.vs.place(x = 60, y = 85)

        self.wins_var = DoubleVar()
        self.draw_var = DoubleVar()
        self.lose_var = DoubleVar()
        self.amount_var = DoubleVar()
        self.others_var = DoubleVar()
        self.wins_var1 = DoubleVar()
        self.draw_var1 = DoubleVar()
        self.lose_var1 = DoubleVar()
        self.amount_var1 = DoubleVar()
        self.others_var1 = DoubleVar()
        self.vcmd = (self.register(self.validate_float), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.WinEntry = Entry(self, textvariable=self.wins_var1, validatecommand=self.vcmd, validate='all', width=6)
        self.DrawEntry = Entry(self, textvariable=self.draw_var1, validatecommand=self.vcmd, validate='all', width=6)
        self.LoseEntry = Entry(self, textvariable=self.lose_var1, validatecommand=self.vcmd, validate='all', width=6)
        self.OthersEntry = Entry(self, textvariable=self.others_var1, validatecommand=self.vcmd, validate='all',
                                 width=6)
        self.instruct = Label(self, text=' enter your odds',
                              font=('Bradley Hand ITC', '15', 'bold'), fg='#773c00', bd=5, bg='#c9e3c1')
        self.instruct.place(x=0, y=25)
        self.heading = Label(self, text='',
                             font=('Lucida Calligraphy', '15', 'bold', 'underline'), fg='#773c00', bd=5, bg='#c9e3c1')
        self.heading.place(x=30, y=60)
        self.graph_heading = Label(self, text='profit or loss', font=('Lucida Calligraphy', '15', 'bold', 'underline'),
                                   fg='#773c00', bd=5, bg='#c9e3c1')
        self.graph_heading.place(x=600, y=0)
        m = 0
        n = 2
        self.entrybox = Entry(self, width = 5).place(x = 10, y = 50)
        self.entrybox2 = Entry(self, width = 3).place(x = 50, y = 50)
        self.vs = Label(self, text = 'vs',fg='#773c00', bd=5, bg='#c9e3c1' ).place(x = 30, y = 50)

        self.b3 = Button(self, text='odds', width=5, command=self.more_odds)
        self.b3.place(x=560, y=100)
        self.b5 = Button(self, text='compute', width=5, command=self.compute_more)
        self.b5.place(x=600, y=15)
        self.oddEntry = []
        self.oddEntry2 = []
        self.compt = []
        self.sum_up_row = []
        self.odd_Label_Entry = []
        self.amount_Entry = []
        self.all_ent_float = []
        self.amount_Entry_float = []
        self.oddEntry_float = []
        self.window_w = 1400
        self.window_h = 600
        self.button_x = 10
        self.button_xx = 360
        self.button_oddx = 360
        self.button_y = 110
        self.button_yy = 110
        self.counter = 0
        self.xm = -1
        self.xmm = -1
        self.nm = 0
        self.x = -1
        self.zz = -1
        self.cd = 0
        self.cdx = -1
        self.mm = 0
        self.n = 1
        self.t = 2
        self.q = 3
        self.ls = 520
        self.all_ent = []
        self.odd_holder = []
        self.b = Button(self, text='create more', width=10, command=self.moving_But)
        self.b.place(x=self.button_x, y=120)
        #Button(self.left, text='GO', command=self.createMore).place(x=274, y=33)
    def callback1(self,event):
        print('you clicked on left frame', event.x,event.y)
    def callback2(self,event):
        print('you clicked on right frame', event.x,event.y)

    def more_odds(self):
        if self.button_oddx < self.window_w - 720:
            self.button_oddx = self.button_oddx + 50
            self.m = Entry(self, width=6)
            self.oddm = Entry(self, width=6)

            self.oddm.place(x=self.button_oddx, y=60)
            self.odd_Label_Entry.append(self.oddm)
            self.oddEntry.append(self.m)
            self.m.place(x=self.button_oddx, y=90)
            self.b3.place_forget()
            self.b3.place(x=self.button_oddx + 50, y=85)
        if self.button_oddx >= self.window_w - 750:
            self.b3.place_forget()
    # def createMore(self):
    #     for i in range(1, 11):
    #         m = 55
    #         m += 20
    #         Label(self, text=i, fg='#773c00', bg='#c9e3c1').place(x=2, y=m)
    def validate_float(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        # action=1 -> insert
        if (action == '1'):
            if text in '0123456789.-+':
                try:
                    float(value_if_allowed)
                    return True
                except ValueError:
                    return False
            else:
                return False
        else:
            return True

    def compute_more(self):
        self.sum_of_held_odds =[]
        self.amount_Entry_next = []
        print('this is the odd',len(self.oddEntry2),  '\nand this is the number of list',len(self.odd_holder))
        xd = -1
        xf = -1
        xv = -1
        xvv = 0
        xc = -1
        self.ratio_odd_and_list = int(len(self.oddEntry2))//int(len(self.odd_holder))
        print('this is the ratio',self.ratio_odd_and_list)
        if len(self.all_ent) > 0:
            for i in self.all_ent:
                self.all_ent_float.append(float(i.get()))
            for i in self.amount_Entry:
                self.amount_Entry_float.append(float(i.get()))
            for i in self.all_ent_float:
                if len(self.odd_holder[self.cd]) <= 3:
                    self.zz +=1
                    self.odd_holder[self.cd].append(self.all_ent_float[self.zz])

                elif len(self.odd_holder[self.cd])<=6:
                    self.zz +=1
                    self.cd +=1
                    self.odd_holder[self.cd].append(self.all_ent_float[self.zz])
                elif len(self.odd_holder[self.cd])<=9:
                    self.zz +=1
                    self.cd +=1
                    self.odd_holder[self.cd].append(self.all_ent_float[self.zz])
                elif len(self.odd_holder[self.cd]) <= 12:
                    self.zz += 1
                    self.cd += 1
                    self.odd_holder[self.cd].append(self.all_ent_float[self.zz])
                elif len(self.odd_holder[self.cd]) <= 15:
                    self.zz += 1
                    self.cd += 1
                    self.odd_holder[self.cd].append(self.all_ent_float[self.zz])
                elif len(self.odd_holder[self.cd]) <= 18:
                    self.zz += 1
                    self.cd += 1
                    self.odd_holder[self.cd].append(self.all_ent_float[self.zz])
            if len(self.oddEntry2) > 0:
                for i in self.oddEntry2:
                    self.oddEntry_float.append(float(i.get()))
                for i in range(len(self.odd_holder)):
                    xd +=1
                    for i in range(self.ratio_odd_and_list):
                        xf +=1
                        self.odd_holder[xd].append(self.oddEntry_float[xf])

            print(len(self.odd_holder))
            print(self.odd_holder)
            for i in self.amount_Entry:
                self.amount_Entry_next.append(int(i.get()))
            for i in self.odd_holder:
                self.sum_of_held_odds.append(sum(i))
                print(self.sum_of_held_odds)
            for i in range(len(self.odd_holder)):
                xc +=1
                xv = -1
                xvv +=1
                print('for list in holder', xc)
                self.sum_up_row.append([])
                for i in self.odd_holder[xc]:

                    xv +=1
                    print('held odds',xv)
                    print('index for amount', xvv)
                    self.sum_up_row[xc].append(((i**2)*self.amount_Entry_next[xvv])//self.sum_of_held_odds[xc])

            print(self.sum_of_held_odds)
            print('this should be lists', self.sum_up_row)
            print('this for amount', self.amount_Entry_next)

    def moving_But(self):

        self.all_entry = []
        if (self.button_y < self.window_h - 50):
            self.counter += 1
            self.button_y = self.button_y + 40
            self.b.place_forget()
            self.b.place(x=self.button_x, y=self.button_y + 30)
            # self.b2.place_for get()
            # self.b2.place(x=10, y=self.button_y + 30)
            self.entrybox = Entry(self, width=10).place(x=10, y=self.button_y - 20)
            self.entrybox2 = Entry(self, width=10).place(x=100, y=self.button_y - 20)
            self.vs = Label(self, text='vs', font=('Lucida Calligraphy', '15', 'bold'), fg='#773c00', bd=5,
                            bg='#c9e3c1').place(x=60, y=self.button_y - 25)

            self.WinEntry.place(x=210, y=130)
            self.DrawEntry.place(x=260, y=130)
            self.LoseEntry.place(x=310, y=130)
            self.OthersEntry.place(x=360, y=130)
            print(len(self.odd_holder))
            print(self.odd_holder)
            print(self.counter)
            if self.counter == 2:
                self.odd_holder.append([])
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent[0].place(x=210, y=self.button_y - 20)
                self.all_ent[1].place(x=260, y=self.button_y - 20)
                self.all_ent[2].place(x=310, y=self.button_y - 20)
                self.all_ent[3].place(x=360, y=self.button_y - 20)
                print(len(self.odd_holder))
                print(self.odd_holder)
                print(self.counter)
                if self.button_xx <= self.button_oddx:
                    for i in range(len(self.oddEntry)):
                        self.button_xx +=50
                        self.cdx +=1
                        self.oddEntry2.append(Entry(self, width = 6))
                        self.oddEntry2[self.cdx].place(x = self.button_xx, y = self.button_y -20)
                    self.button_xx = 360
            elif self.counter == 3:
                self.odd_holder.append([])
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent[4].place(x=210, y=self.button_y - 20)
                self.all_ent[5].place(x=260, y=self.button_y - 20)
                self.all_ent[6].place(x=310, y=self.button_y - 20)
                self.all_ent[7].place(x=360, y=self.button_y - 20)
                print(len(self.odd_holder))
                print(self.odd_holder)
                print(self.counter)
                if self.button_xx <= self.button_oddx:
                    for i in range(len(self.oddEntry)):
                        self.button_xx +=50
                        self.cdx +=1
                        self.oddEntry2.append(Entry(self, width = 6))
                        self.oddEntry2[self.cdx].place(x = self.button_xx, y = self.button_y -20)
                    self.button_xx = 360
            elif self.counter == 4:
                self.odd_holder.append([])
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent[8].place(x=210, y=self.button_y - 20)
                self.all_ent[9].place(x=260, y=self.button_y - 20)
                self.all_ent[10].place(x=310, y=self.button_y - 20)
                self.all_ent[11].place(x=360, y=self.button_y - 20)
                print(len(self.odd_holder))
                print(self.odd_holder)
                # print(self.counter)
                if self.button_xx <= self.button_oddx:
                    for i in range(len(self.oddEntry)):
                        self.button_xx +=50
                        self.cdx +=1
                        self.oddEntry2.append(Entry(self, width = 6))
                        self.oddEntry2[self.cdx].place(x = self.button_xx, y = self.button_y -20)
                    self.button_xx = 360
                    print(len(self.oddEntry2))
            elif self.counter == 5:
                self.odd_holder.append([])
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent[12].place(x=210, y=self.button_y - 20)
                self.all_ent[13].place(x=260, y=self.button_y - 20)
                self.all_ent[14].place(x=310, y=self.button_y - 20)
                self.all_ent[15].place(x=360, y=self.button_y - 20)
                if self.button_xx <= self.button_oddx:
                    for i in range(len(self.oddEntry)):
                        self.button_xx += 50
                        self.cdx += 1
                        self.oddEntry2.append(Entry(self, width=6))
                        self.oddEntry2[self.cdx].place(x=self.button_xx, y=self.button_y - 20)
                    self.button_xx = 360

            elif self.counter == 6:
                self.odd_holder.append([])
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent[16].place(x=210, y=self.button_y - 20)
                self.all_ent[17].place(x=260, y=self.button_y - 20)
                self.all_ent[18].place(x=310, y=self.button_y - 20)
                self.all_ent[19].place(x=360, y=self.button_y - 20)
                if self.button_xx <= self.button_oddx:
                    for i in range(len(self.oddEntry)):
                        self.button_xx += 50
                        self.cdx += 1
                        self.oddEntry2.append(Entry(self, width=6))
                        self.oddEntry2[self.cdx].place(x=self.button_xx, y=self.button_y - 20)
                    self.button_xx = 360
            elif self.counter == 7:
                self.odd_holder.append([])
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent[20].place(x=210, y=self.button_y - 20)
                self.all_ent[21].place(x=260, y=self.button_y - 20)
                self.all_ent[22].place(x=310, y=self.button_y - 20)
                self.all_ent[23].place(x=360, y=self.button_y - 20)
                if self.button_xx <= self.button_oddx:
                    for i in range(len(self.oddEntry)):
                        self.button_xx += 50
                        self.cdx += 1
                        self.oddEntry2.append(Entry(self, width=6))
                        self.oddEntry2[self.cdx].place(x=self.button_xx, y=self.button_y - 20)
                    self.button_xx = 360
            elif self.counter == 8:
                self.odd_holder.append([])
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent[24].place(x=210, y=self.button_y - 20)
                self.all_ent[25].place(x=260, y=self.button_y - 20)
                self.all_ent[26].place(x=310, y=self.button_y - 20)
                self.all_ent[27].place(x=360, y=self.button_y - 20)
                if self.button_xx <= self.button_oddx:
                    for i in range(len(self.oddEntry)):
                        self.button_xx += 50
                        self.cdx += 1
                        self.oddEntry2.append(Entry(self, width=6))
                        self.oddEntry2[self.cdx].place(x=self.button_xx, y=self.button_y - 20)
                    self.button_xx = 360
            elif self.counter == 9:
                self.odd_holder.append([])
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent[28].place(x=210, y=self.button_y - 20)
                self.all_ent[29].place(x=260, y=self.button_y - 20)
                self.all_ent[30].place(x=310, y=self.button_y - 20)
                self.all_ent[31].place(x=360, y=self.button_y - 20)
                if self.button_xx <= self.button_oddx:
                    for i in range(len(self.oddEntry)):
                        self.button_xx += 50
                        self.cdx += 1
                        self.oddEntry2.append(Entry(self, width=6))
                        self.oddEntry2[self.cdx].place(x=self.button_xx, y=self.button_y - 20)
                    self.button_xx = 360
            elif self.counter == 10:
                self.odd_holder.append([])
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent[32].place(x=210, y=self.button_y - 20)
                self.all_ent[33].place(x=260, y=self.button_y - 20)
                self.all_ent[34].place(x=310, y=self.button_y - 20)
                self.all_ent[35].place(x=360, y=self.button_y - 20)
                if self.button_xx <= self.button_oddx:
                    for i in range(len(self.oddEntry)):
                        self.button_xx += 50
                        self.cdx += 1
                        self.oddEntry2.append(Entry(self, width=6))
                        self.oddEntry2[self.cdx].place(x=self.button_xx, y=self.button_y - 20)
                    self.button_xx = 360
                # print('this is the no. items', len(self.all_ent), 'ok')
            elif self.counter == 11:
                self.odd_holder.append([])
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent.append(Entry(self, width=6))
                self.all_ent[36].place(x=210, y=self.button_y - 20)
                self.all_ent[37].place(x=260, y=self.button_y - 20)
                self.all_ent[38].place(x=310, y=self.button_y - 20)
                self.all_ent[39].place(x=360, y=self.button_y - 20)
                if self.button_xx <= self.button_oddx:
                    for i in range(len(self.oddEntry)):
                        self.button_xx += 50
                        self.cdx += 1
                        self.oddEntry2.append(Entry(self, width=6))
                        self.oddEntry2[self.cdx].place(x=self.button_xx, y=self.button_y - 20)
                    self.button_xx = 360

                print('this is the no. items', len(self.all_ent), 'ok')
                print('this is the no. items', len(self.oddEntry2), 'ok')
            else:
                pass
            if self.counter > 0:
                self.x += 1
                self.amount_Entry.append(Entry(self, width=10))
                self.amount_Entry[self.x].place(x=710, y=self.button_y - 20)
        else:
            self.errorlab = Label(self, text="you've reached the limit,\n enter your odds....",
                                  font=('Lucida Calligraphy', '15', 'bold'), fg='#773c00', bd=5,
                                  bg='#c9e3c1').place(x=10, y=self.window_h - 40)
        self.b3.place_forget()
            # if len(self.oddEntry)>0:
            #     if self.button_xx <=self.button_oddx:
            #
            #         self.button_xx +=50
            #         self.oddEntry.append(self.oddm)
            #         self.oddm.place(x= self.button_xx, y = self.button_y)
        # if self.oddEntry[0]:
        #     self.oddEntry.append(self.oddm)
        #     self.place(x=410, y = self.button_y)
        # if self.oddEntry[1]:
        #     self.oddEntry.append(self.oddm)
        #     self.place(x=460, y = self.button_y)

                # for i in range(len(self.oddEntry)):
                #     self.oddEntry.append(self.oddm)
                #     self.oddm.place(x= self.button_xx, y = self.button_y)

            # if self.button_xx <= self.button_oddx:
            #     self.button_oddx +=50
            #     self.button_xx +=50
            #     self.nm +=1
            #     self.oddEntry.append(self.oddm)
            #     self.oddEntry[1].place(x=self.button_xx, y=self.button_y - 20)
                # except IndexError:
                #     pass
                # try:
                #     self.oddEntry[1] = Entry(self, width=6)
                #     self.oddEntry[1].place(x=460, y=self.button_y - 20)
                # except IndexError:
                #     pass
                # try:
                #     self.oddEntry[2] = Entry(self, width=6)
                #     self.oddEntry[2].place(x=510, y=self.button_y - 20)
                # except IndexError:
                #     pass
            # try:
            #     self.oddEntry[3] = Entry(self, width=6)
            #     self.oddEntry[3].place(x=560, y=self.button_y - 20)
            # except IndexError:
            #     pass
            # try:
            #     self.oddEntry[4] = Entry(self, width=6)
            #     self.oddEntry[4].place(x=610, y=self.button_y - 20)
            #
            # except IndexError:
            #     pass
            # try:
            #     self.oddEntry[5] = Entry(self, width=6)
            #     self.oddEntry[5].place(x=660, y=self.button_y - 20)
            #
            # except IndexError:
            #     pass

    # def CountWig(self):
    #     self.textvar = StringVar()
    #     self.textvar.set("")
    #     Entry(self, width = 4).place(x=8,y= 10)
    #     #Entry(self.left, width = 4).place(x=8,y= 15)
    # def CreateTab(self):
    #    self.count = self.CountWig()
    #    return self.count
    # def MovingButton(self):
    #     n = 2
    #     n+=5
    #     show = Button(self, text='GO', command=self.CountWig).place(x=6, y=n)
    #     return show


#to restart programme
    def restart_program(self):
        os.execl(sys.executable, sys.executable, *sys.argv)

class pageone(Frame):
    def __init__(self, master, control):

        Frame.__init__(self,master,bg='#c9e3c1')

        lab = Label(self, text = 'welcome to Game Analysis',font=('Bradley Hand ITC', '40', 'bold') ,bg='#c9e3c1')
        lab.place(x = 10, y = 10)
        #img = PhotoImage(file = 'forward.png')
        but = Button(self, text = 'start',  command  = lambda: control.raise_frame(widget))
        but.place(x = 1150, y = 560)

        lab1 = Label(self, text = 'Analyze game', font = ('Bradley Hand ITC', '25', 'bold'),bg='#c9e3c1')
        lab1.place(x = 1110, y = 520)

        lab2 = Label(self, text = 'About App', font = ('Bradley Hand ITC', '25', 'bold'),bg='#c9e3c1')
        lab2.place(x = 30, y = 520)
        but1 = Button(self, text="click...")
        but1.place(x=30, y=560)

        self.bind("<Button-1>", self.callback1)
    def callback1(self, event):
        print('you clicked on left frame', event.x, event.y)
b = moreTab()


b.mainloop()
# redundant stuffs
# self.draw_amount1 = ((self.draw1**2)/self.total_of_odds1)*float(self.amount_Entry[0].get())
            # self.lose_amount1 = ((self.lose1**2)/self.total_of_odds1)*float(self.amount_Entry[0].get())
            # self.other_amount1 = ((self.Other1**2)/self.total_of_odds1)*float(self.amount_Entry[0].get())
            # self.asssd = [self.win_amount1, self.draw_amount1, self.lose_amount1, self.other_amount1]
            # self.odd_win1 = Label(self, text="%s" % str(int((self.win_amount1))).split('.')[0],
            #                       font=('Lucida Calligraphy', '9', 'bold'), bd=5, bg='#c9e3c1')
            # self.odd_draw1 = Label(self, text="%s" % str(int((self.draw_amount1))).split('.')[0],
            #                        font=('Lucida Calligraphy', '9', 'bold'), bd=5, bg='#c9e3c1')
            # self.odd_lose1 = Label(self, text="%s" % str(int((self.lose_amount1))).split('.')[0],
            #                        font=('Lucida Calligraphy', '9', 'bold'), bd=5, bg='#c9e3c1')
            # self.odd_others1 = Label(self, text="%s" % str(int((self.other_amount1))).split('.')[0],
            #                          font=('Lucida Calligraphy', '9', 'bold'), bd=5, bg='#c9e3c1')
            # self.assdd = [self.odd_win1, self.odd_draw1, self.odd_lose1, self.odd_others1]
            # for kk in self.assdd:
            #     self.ty += 50
            #     kk.place(x=self.ty, y=self.button_yy + 20)
        # print(self.answer)
# self.asd = [ self.win_amount ,self.draw_amount,self.lose_amount,self.other_amount ]

# self.odd_win = Label(self, text="%s" % str(int((self.win_amount))).split('.')[0],
#                      font=('Lucida Calligraphy', '9', 'bold'), bd=5, bg='#c9e3c1')
# self.odd_draw = Label(self, text="%s" % str(int((self.draw_amount))).split('.')[0],
#                       font=('Lucida Calligraphy', '9', 'bold'), bd=5, bg='#c9e3c1')
# self.odd_lose = Label(self, text="%s" % str(int((self.lose_amount))).split('.')[0],
#                       font=('Lucida Calligraphy', '9', 'bold'), bd=5, bg='#c9e3c1')
# self.odd_others = Label(self, text="%s" % str(int((self.other_amount))).split('.')[0],
#                         font=('Lucida Calligraphy', '9', 'bold'), bd=5, bg='#c9e3c1')


# self.assd = [self.odd_win, self.odd_draw, self.odd_lose, self.odd_others]
