from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
import sys
from PIL import ImageTk, Image

class moreTab(tk.Tk):
    def __init__(self, ):
        Tk.__init__(self, )
        self.geometry("1350x800")
        self.iconbitmap('Icons-Land-Sport-Soccer-Ball.ico')
        self.title('GORZY BET SOFTWARE')
        container = Frame(self, bg='#c9e3c1')
        container.pack(side="top", fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for q in (pageone, widget):
            frame = q(container, self)
            self.frames[q] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.raise_frame(pageone)

    def raise_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class widget(Frame):
    def __init__(self, master=0, control=0):
        Frame.__init__(self, master, bg='#c9e3c1')
        self.bind("<Button-1>", self.callback1)
        self.heading = Label(self, text='GOZIE BET \nSOFTWARE',
                             font=('Bradley Hand ITC', '25', 'bold'),fg = '#3d7c6f', bd=5, bg='#c9e3c1')
        self.heading.place(x=0, y=0)
        self.graph_heading = Label(self, text='Profit/', font=('Lucida Calligraphy', '15', 'bold'),
                                   fg = '#3d7c6f',bd=5, bg='#c9e3c1')
        self.graph_headingg = Label(self, text='Loss', font=('Lucida Calligraphy', '15', 'bold'),
                                   bd=5, fg ='#ff7171', bg='#c9e3c1')
        self.graph_heading.place(x=930, y=5)
        self.graph_headingg.place(x=1020, y=5)
        # self.graph_heading3 = Label(self, text='', font=('Lucida Calligraphy', '15', 'bold'),
        #                             bd=5, bg='#c9e3c1')
        # self.graph_heading3.place(x=1100, y=5)
        self.amount_played = Label(self, text='Amount', font=('Lucida Calligraphy', '15', 'bold'),
                                   bd=5,fg = '#3d7c6f', bg='#c9e3c1')
        self.amount_played.place(x=710, y=50)
        self.graph_heading1 = Label(self, text='Enter odds', font=('Lucida Calligraphy', '15', 'bold'),
                                    bd=5,fg = '#3d7c6f', bg='#c9e3c1')
        self.graph_heading1.place(x=350, y=10)
        self.m = 0
        n = 2
        ent11 = StringVar()
        ent1 = StringVar()

        self.entrybox = Entry(self, textvariable = ent11, width=10)
        self.entrybox.place(x=10, y=90)
        self.entrybox2 = Entry(self, textvariable = ent1,width=10)
        self.entrybox2.place(x=100, y=90)
        self.vs = Label(self, text='vs', font=('Lucida Calligraphy', '15', 'bold'), bd=5, bg='#c9e3c1')
        self.vs.place(x=60, y=85)

        self.b = ttk.Button(self, text='create more',takefocus=False, width=15, command=self.moving_But)
        self.b.place(x=10, y=120)
        self.photo_home = ImageTk.PhotoImage(file='home-button.png')

        self.b1 = Button(self, image = self.photo_home, border= 0,
                             bg = '#c9e3c1',activebackground ='#c9e3c1',
                         command=lambda: control.raise_frame(pageone)).place(x=1200, y=600)

        # self.b2 = Button(self, text = 'undo boxes', width = 10,command = self.Undo_move)
        # self.b2.place(x =10 , y = 120)
        self.b3 = ttk.Button(self, text='odds', takefocus=False, width=8, command=self.more_odds)
        self.b3.place(x=460, y=85)
        self.b5 = ttk.Button(self, text='compute', takefocus=False,width=10,command=self.computing_odds_frac)
        self.b5.place(x=710, y=120)
        self.b6 =ttk.Button(self, text='Reset', width=7,takefocus=False, command= self.clear_data)
        self.b6.place(x=800, y=120)
        self.b4 = ttk.Button(self, text = 'Restart',takefocus=False, width = 10, command= self.restart_everything)
        self.b4.place(x = 1100, y  = 5)
        ##ODDS LABELS
        self.same_value = StringVar()
        self.same_value1 = StringVar()
        self.same_value2 = StringVar()
        self.same_value3 = StringVar()
        self.oddlabel1 = Entry(self, width=6, textvariable=self.same_value)
        self.oddlabel2 = Entry(self, width=6, textvariable=self.same_value1)
        self.oddlabel3 = Entry(self, width=6, textvariable=self.same_value2)
        self.oddlabel4 = Entry(self, width=6, textvariable=self.same_value3)
        self.oddlabel1.place(x=215, y=60)
        self.oddlabel2.place(x=265, y=60)
        self.oddlabel3.place(x=315, y=60)
        self.oddlabel4.place(x=360, y=60)
        # RESULTS lABEL
        self.winr = Label(self, text='', font=('Lucida Calligraphy', '15', 'bold'), bd=5, bg='#c9e3c1',
                          textvariable=self.same_value)
        self.drawr = Label(self, text='', font=('Lucida Calligraphy', '15', 'bold'), bd=5, bg='#c9e3c1',
                           textvariable=self.same_value1)
        self.loser = Label(self, text='', font=('Lucida Calligraphy', '15', 'bold'), bd=5, bg='#c9e3c1',
                           textvariable=self.same_value2)
        self.othersr = Label(self, text='', font=('Lucida Calligraphy', '15', 'bold'), bd=5, bg='#c9e3c1',
                             textvariable=self.same_value3)
        self.winr.place(x=830, y=40)
        self.drawr.place(x=880, y=40)
        self.loser.place(x=930, y=40)
        self.othersr.place(x=980, y=40)
        ## error labels
        self.errorlab1 = Label(self, text = 'click reset button and enter amount')
        ##ODDS ENTRIES

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
        # TO VALIDATE NUMBER ENTRY
        self.vcmd = (self.register(self.validate_float), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.WinEntry = Entry(self, textvariable=self.wins_var1, validatecommand=self.vcmd, validate='all', width=6)
        self.DrawEntry = Entry(self, textvariable=self.draw_var1, validatecommand=self.vcmd, validate='all', width=6)
        self.LoseEntry = Entry(self, textvariable=self.lose_var1, validatecommand=self.vcmd, validate='all', width=6)
        self.OthersEntry = Entry(self, textvariable=self.others_var1, validatecommand=self.vcmd, validate='all',
                                 width=6)

        self.WinEnt1 = Entry(self, textvariable=self.wins_var, validatecommand=self.vcmd, validate='all', width=6)
        self.DrawEnt1 = Entry(self, textvariable=self.draw_var, validatecommand=self.vcmd, validate='all', width=6)
        self.LoseEnt1 = Entry(self, textvariable=self.lose_var, validatecommand=self.vcmd, validate='all', width=6)
        self.OthersEnt1 = Entry(self, textvariable=self.others_var, validatecommand=self.vcmd, validate='all', width=6)
        self.amount = Entry(self, textvariable=self.amount_var, validatecommand=self.vcmd, validate='all', width=10)
        self.all_amount = Entry(self, width=10)
        ## the entries for matches(Create more)
        self.entrybox = Entry(self, width=10)
        self.entrybox2 = Entry(self, width=10)
        self.vs = Label(self, text='vs', font=('Lucida Calligraphy', '15', 'bold'), fg='#773c00', bd=5,
                        bg='#c9e3c1')
        ##
        self.amount.place(x=710, y=90)
        self.WinEnt1.place(x=210, y=90)
        self.DrawEnt1.place(x=260, y=90)
        self.LoseEnt1.place(x=310, y=90)
        self.OthersEnt1.place(x=360, y=90)


        self.oddEntry = []
        self.oddEntry2 = []
        self.oddEntry3 = []
        self.compt = []
        self.sum_up_row = []
        self.sum_up_row_next = []
        self.odd_Label_Entry = []
        self.odd_Label_Entry_result = []
        self.amount_Entry = []
        self.all_ent_float = []
        self.amount_Entry_float = []
        self.oddEntry_float = []
        self.oddEntry_float1 = []
        self.oddEntry_float2 = []
        self.clear_us = []
        self.var_list = ['q', 'w', 'e', 'r', 't', 'y']

        self.next2row = []
        self.window_w = 1400
        self.window_h = 600
        self.button_x = 10
        self.button_xx = 360
        self.button_oddx = 360
        self.button_y = 110
        self.button_yy = 110
        self.counter = 0
        self.count = 0
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
        self.click_twice = 0
        self.clear_count = 0
        self.answer_next = []
        self.answer_next2 = []
    def computing_odds_frac(self):
        self.b5['state'] = DISABLED
        self.b3.place_forget()
        self.b.place_forget()
        self.answer = []
        self.answer1 = []


        try:
            self.amounts = float(self.amount.get())
            self.wins = float(self.WinEnt1.get())
            self.draw = float(self.DrawEnt1.get())
            self.lose = float(self.LoseEnt1.get())
            self.Other = float(self.OthersEnt1.get())
            self.wins1 = float(self.WinEntry.get())
            self.draw1 = float(self.DrawEntry.get())
            self.lose1 = float(self.LoseEntry.get())
            self.Other1 = float(self.OthersEntry.get())
        except ValueError:
            pass

        # self.second_row = [self.wins1,self.draw1, self.lose1,self.Other1]
        self.list_of_odds = [self.wins, self.draw, self.lose, self.Other]
        # self.list_of_odds_filtered = list(filter(None, self.list_of_odds))
        self.list_of_odds1 = [self.wins1, self.draw1, self.lose1, self.Other1]
        print("odds" , self.list_of_odds,len(self.list_of_odds),'and odds1', self.list_of_odds1,len(self.list_of_odds1) )

        if len(self.oddEntry) != 0:
            ###THIS FOR-LOOP COMPUTES THE ODDS IN THE FIRST ROW
            for i in self.oddEntry:
                self.oddEntry_float1.append(float(i.get()))
            self.list_of_odds.extend(self.oddEntry_float1)
            self.total_of_odds = sum(self.list_of_odds)
            print('self.oddEntry is', self.oddEntry, len(self.oddEntry))
            if self.counter >= 1:
                ## THIS FOR LOOP COMPUTES ODDS FOR THE 2ND ROW :)
                for i in self.oddEntry3:
                    self.oddEntry_float2.append(float(i.get()))
                self.list_of_odds1.extend(self.oddEntry_float2)
                self.total_of_odds1 = sum(self.list_of_odds1)
                print("this is what you seek", self.list_of_odds1)
        if self.count == False:
            ###THIS FOR-LOOP COMPUTES THE ODDS IN THE FIRST ROW
            for i in self.oddEntry:
                self.oddEntry_float1.append(float(i.get()))
            self.list_of_odds.extend(self.oddEntry_float1)
            self.total_of_odds = sum(self.list_of_odds)
            if self.counter >= 1:
                ## THIS FOR LOOP COMPUTES ODDS FOR THE 2ND ROW :)
                try:
                    self.list_of_odds1.extend(self.oddEntry_float2)
                except:
                    pass
                self.total_of_odds1 = sum(self.list_of_odds1)
                print("this is what you seek", self.list_of_odds1)

        for i in self.list_of_odds:
            self.answer.append(((((i ** 2) / self.total_of_odds) * self.amounts))-self.amounts)
        print('this is answer', self.answer, len(self.answer))
        if self.counter >= 1:
            for i in self.list_of_odds1:
                self.answer1.append((((i ** 2) / self.total_of_odds1) * float(self.amount_Entry[0].get()))-float(self.amount_Entry[0].get()))
        print('this is answer1', self.answer1, len(self.answer1))
        for i in self.answer1:
            ## THIS CARRIES THE RESULTS OF THE SECOND ROW
            if i <0 and i != -float(self.amount_Entry[0].get()):
                self.answer_next2.append(Label(self, text="%s" % (str(int((i))).split('.')[0]),
                                           font=('Lucida Calligraphy', '9', 'bold'), fg = 'red', bd=5, bg='#c9e3c1'))
            elif i == -float(self.amount_Entry[0].get()):
                self.answer_next2.append(Label(self, text='',
                                              font=('Lucida Calligraphy', '9', 'bold'), bd=5, bg='#c9e3c1'))
            else:
                self.answer_next2.append(Label(self, text="%s" % (str(int((i))).split('.')[0]),
                                               font=('Lucida Calligraphy', '9', 'bold'), bd=5, fg = '#008080', bg='#c9e3c1'))


        for i in self.answer:
            ## THIS IS THE LABEL THAT CARRIES THE RESULTS OF THE FIRST ROW
            if i < 0 and i != -self.amounts:
                self.answer_next.append(Label(self, text="%s" % str(int((i))).split('.')[0],
                                              font=('Lucida Calligraphy', '9', 'bold'), fg = 'red', bd=5, bg='#c9e3c1'))
            elif i == -self.amounts:
                self.answer_next.append(Label(self, text='',
                                              font=('Lucida Calligraphy', '9', 'bold'), bd=5, bg='#c9e3c1'))
            else:
                self.answer_next.append(Label(self, text="%s" % str(int((i))).split('.')[0],
                                              font=('Lucida Calligraphy', '9', 'bold'), bd=5,fg='#008080', bg='#c9e3c1'))
        self.ty = 780
        for k in self.answer_next:
            ## GEOMETRY POSITIONING OF THE FIRST ROW
            self.ty += 50
            k.place(x=self.ty, y=self.button_yy - 30)
        self.ty = 780
        for k in self.answer_next2:
            ## GEOMETRY POSITIONING OF THE SECOND ROW
            self.ty += 50
            k.place(x=self.ty, y=self.button_yy + 10)
        if self.counter >= 2:
            self.compute_more()

    def compute_more(self):
        ## THIS FUNCTION COMPUTES FROM THE THIRD ROW :)
        self.sum_of_held_odds = []
        self.amount_Entry_next = []
        xd = -1
        xf = -1
        xv = -1
        xvv = 0
        xc = -1
        ss = -1
        self.cd = 0
        self.zz = -1
        self.ratio_odd_and_list = int(len(self.oddEntry2)) // int(len(self.odd_holder))
        if len(self.all_ent) > 0:
            ## IF MORE ODDS CREATED, THIS LOOP CHANGES IT TO FLOAT AND APPENDS IT APPROPRAITELY
            for i in self.all_ent:
                self.all_ent_float.append(float(i.get()))
            for i in self.amount_Entry:
                try:
                    self.amount_Entry_float.append(float(i.get()))
                except ValueError:
                    self.errorlab1.place(x =500, y = self.window_h - 40)

            for i in self.all_ent_float:
                ## THIS LOOP APPENDS THE ODDS INTO A LIST INSIDE IN LIST(SELF.ODD_HOLDER)
                if len(self.odd_holder[self.cd]) <= 3:
                    self.zz += 1
                    self.odd_holder[self.cd].append(self.all_ent_float[self.zz])

                elif len(self.odd_holder[self.cd]) <= 6:
                    self.zz += 1
                    self.cd += 1
                    self.odd_holder[self.cd].append(self.all_ent_float[self.zz])
                elif len(self.odd_holder[self.cd]) <= 9:
                    self.zz += 1
                    self.cd += 1
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
                ## ODDENTRY2 IS HOLDING EXTRA ODDS FROM ODDS BUTTON
                ## THIS RESPONSIBLE FOR THE ODD(EXTRA ODDS) COMPUTATION
                ## FROM THE THIRD ROW
                for i in self.oddEntry2:
                    self.oddEntry_float.append(float(i.get()))
                for i in range(len(self.odd_holder)):
                    xd += 1
                    for i in range(self.ratio_odd_and_list):
                        xf += 1
                        self.odd_holder[xd].append(self.oddEntry_float[xf])

            for i in self.amount_Entry:
                try:
                    self.amount_Entry_next.append(int(i.get()))
                except ValueError:
                    self.errorlab1.place(x = 500, y = self.window_h -20)
            for i in self.odd_holder:
                self.sum_of_held_odds.append(sum(i))
            print('sum of held odds',self.sum_of_held_odds)
            for i in range(len(self.odd_holder)):
                xc += 1
                xv = -1
                xvv += 1

                self.sum_up_row.append([])
                for i in self.odd_holder[xc]:
                    xv += 1

                    self.sum_up_row[xc].append(((((i ** 2) *
                                                  self.amount_Entry_next[xvv]) // self.sum_of_held_odds[xc]))
                                               -self.amount_Entry_next[xvv])
            xvv =0
            for i in range(len(self.sum_up_row)):
                self.sum_up_row_next.append([])
                ss += 1
                xvv +=1
                for i in self.sum_up_row[ss]:
                    if i < 0 and i != -self.amount_Entry_next[xvv] :
                        self.sum_up_row_next[ss].append(Label(self, text="%s" % str(int((i))).split('.')[0],
                                                              font=('Lucida Calligraphy', '9', 'bold'), fg ='red', bd=5, bg='#c9e3c1'))
                    elif i ==  -self.amount_Entry_next[xvv]:
                        self.sum_up_row_next[ss].append(Label(self, text='X',
                                                                  font=('Lucida Calligraphy', '9', 'bold'), fg='#008080',
                                                                  bd=5, bg='#c9e3c1'))
                    else:
                        self.sum_up_row_next[ss].append(Label(self, text="%s" % str(int((i))).split('.')[0],
                                                              font=('Lucida Calligraphy', '9', 'bold'), bd=5,
                                                              bg='#c9e3c1' , fg = '#008080'))
                ssn = 780
                self.button_yy += 40
                for i in self.sum_up_row_next[ss]:
                    ssn += 50
                    i.place(x=ssn, y=self.button_yy + 10)

            print(self.sum_of_held_odds)
            print('this is sum_up_row lists', self.sum_up_row)
            print('this is amount_Entry_next', self.amount_Entry_next)

    def clear_data(self):
        self.b5['state'] = ACTIVE
        ss = -1
        self.ty = 780
        #self.counter = 0
        self.button_yy = 110
        self.clear_count +=1
        self.wins_var.set(0)
        self.draw_var.set(0)
        self.lose_var.set(0)
        self.others_var.set(0)
        self.amount_var.set(0)
        self.wins_var1.set(0)
        self.draw_var1.set(0)
        self.lose_var1.set(0)
        self.others_var1.set(0)
        self.amount_var1.set(0)
        self.errorlab1.place_forget()

        for k in self.answer_next:
            k.place_forget()

        for kk in self.answer_next2:
            kk.place_forget()

        for entry in self.amount_Entry:
            entry.delete(0, "end")

        for entry in self.all_ent:
            entry.delete(0, "end")

        for entry in self.oddEntry:
            entry.delete(0, "end")

        for entry in self.oddEntry2:
            entry.delete(0, "end")


        for entry in self.oddEntry3:
            entry.delete(0, "end")

        for i in range(len(self.sum_up_row)):
            ss +=1
            for labels in self.sum_up_row_next[ss]:
                labels.place_forget()

        self.sum_up_row.clear()
        self.sum_up_row_next.clear()

        try:
            self.answer.clear()
            self.answer1.clear()
            self.answer_next.clear()
            self.answer_next2.clear()
            self.list_of_odds.clear()
            self.list_of_odds1.clear()
            self.oddEntry_float2.clear()
            self.oddEntry_float1.clear()
            self.oddEntry_float.clear()
            self.all_ent_float.clear()
            self.amount_Entry_float.clear()
            self.amount_Entry_next.clear()
            self.sum_of_held_odds.clear()
        except AttributeError:

            print("some parameter is missing")
        print("THIS IS TO TEST DELEETE",(len(self.sum_up_row)))
        self.b.place(x=self.button_x, y=self.button_y + 30)
        for i in self.odd_holder:
            i.clear()
        # self.compt[self.qw] = (([self.all_ent[self.qw]]**2)*self.amount_Entry[self.qw])/self.Sum_Total_list[self.qw]
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

    def restart_everything(self):
        self.b5['state'] = ACTIVE
        ssx = -1
        self.ty = 780
        self.x = -1
        # self.counter = 0
        self.button_yy = 110
        self.clear_count += 1
        self.wins_var.set(0)
        self.draw_var.set(0)
        self.lose_var.set(0)
        self.others_var.set(0)
        self.amount_var.set(0)
        self.wins_var1.set(0)
        self.draw_var1.set(0)
        self.lose_var1.set(0)
        self.others_var1.set(0)
        self.amount_var1.set(0)
        self.errorlab1.place_forget()
        for k in self.answer_next:
            k.place_forget()

        for kk in self.answer_next2:
            kk.place_forget()

        for entry in self.amount_Entry:
            entry.delete(0, "end")

        for entry in self.all_ent:
            entry.delete(0, "end")

        for entry in self.oddEntry:
            entry.delete(0, "end")

        for entry in self.oddEntry2:
            entry.delete(0, "end")

        for entry in self.oddEntry3:
            entry.delete(0, "end")

        for i in range(len(self.sum_up_row)):
            ssx += 1
            for labels in self.sum_up_row_next[ssx]:
                labels.place_forget()

        self.sum_up_row.clear()
        self.sum_up_row_next.clear()

        try:
            self.answer.clear()
            self.answer1.clear()
            self.answer_next.clear()
            self.answer_next2.clear()
            self.list_of_odds.clear()
            self.list_of_odds1.clear()
            self.oddEntry_float2.clear()
            self.oddEntry_float1.clear()
            self.oddEntry_float.clear()
            self.all_ent_float.clear()
            self.amount_Entry_float.clear()
            self.amount_Entry_next.clear()
            self.sum_of_held_odds.clear()
        except AttributeError:
            print("some parameter is missing")
        print("THIS IS TO TEST DELEETE", (len(self.sum_up_row)))
        for i in self.odd_holder:
            i.clear()
        if self.count > 0 or self.counter > 0:
            ## THIS IS RESPONSIBLE FOR THE CLEARING OF
            ## eXTRA ODDS (ODD BUTTON) WIDGETS
            ## FOR THE FIRST AND SECOND ROW
            for i in self.oddEntry:
                i.destroy()
            self.oddEntry.clear()
            for i in self.oddEntry3:
                i.destroy()
            self.oddEntry3.clear()
            for i in self.odd_Label_Entry:
                i.destroy()
            self.odd_Label_Entry.clear()
            for i in self.clear_us:
                i .place_forget()

            for i in self.odd_Label_Entry_result:
                i.place_forget()
            self.odd_Label_Entry_result.clear()
            for i in self.oddEntry3:
                i.destroy()
            for i in self.all_ent:
                i.place_forget()
            self.all_ent.clear()
            for i in self.oddEntry2:
                i.destroy()
            self.oddEntry2.clear()
            self.odd_holder.clear()
            for i in self.amount_Entry:
                i.destroy()
            self.amount_Entry.clear()


            self.b3.place_forget()
            self.b3.place(x =410, y= 85)
            self.b.place_forget()
            self.b.place(x =10, y= 130)
            self.b6.place_forget()
            self.b6.place(x =800, y= 120)
            self.b5.place_forget()
            self.b5.place(x =710, y= 120)
            self.count=0
            self.button_oddx =360
            self.button_y = 110
            self.counter = 0
            try:
                self.errorlab.place_forget()
            except AttributeError:
                pass
        else:
            self.b3.place(x=410, y=85)
            self.b.place(x=10, y=130)
        # self.compt[self.qw] = (([self.all_ent[self.qw]]**2)*self.amount_Entry[self.qw])/self.Sum_Total_list[self.qw]

    def more_odds(self):
        ## this function creates more odds, along the x axis
        self.count += 1
        self.cdx = -1
        count = self.count - 1
        if self.button_oddx < self.window_w - 720:
            self.button_oddx = self.button_oddx + 50
            # self.m is the odd entry widgets created
            self.m = Entry(self,validatecommand=self.vcmd, validate='all', width=6)
            # self.oddm is the result label entry box
            self.oddm = Entry(self, width=6)
            self.oddm.place(x=self.button_oddx, y=60)
            self.odd_Label_Entry.append(self.oddm)
            # for the label results
            self.oddm_results = Label(self, text='', font=('Lucida Calligraphy', '15', 'bold'), bd=5, bg='#c9e3c1')
            self.oddm_results.place(x=self.button_oddx + 620, y=40)
            self.odd_Label_Entry_result.append(self.oddm_results)
            for i in self.var_list:
                i = StringVar()
            if self.count == 1:
                self.odd_Label_Entry_result[count]['textvariable'] = self.var_list[count]
                self.odd_Label_Entry[count]['textvariable'] = self.var_list[count]

            if self.count == 2:
                self.odd_Label_Entry_result[count]['textvariable'] = self.var_list[count]
                self.odd_Label_Entry[count]['textvariable'] = self.var_list[count]
            if self.count == 3:
                self.odd_Label_Entry_result[count]['textvariable'] = self.var_list[count]
                self.odd_Label_Entry[count]['textvariable'] = self.var_list[count]
            if self.count == 4:
                self.odd_Label_Entry_result[count]['textvariable'] = self.var_list[count]
                self.odd_Label_Entry[count]['textvariable'] = self.var_list[count]
            if self.count == 5:
                self.odd_Label_Entry_result[count]['textvariable'] = self.var_list[count]
                self.odd_Label_Entry[count]['textvariable'] = self.var_list[count]
            if self.count == 6:
                self.odd_Label_Entry_result[count]['textvariable'] = self.var_list[count]
                self.odd_Label_Entry[count]['textvariable'] = self.var_list[count]
            self.oddEntry.append(self.m)
            self.m.place(x=self.button_oddx, y=90)
            for i in self.oddEntry:
                i['textvariable'] = DoubleVar()

            self.b3.place_forget()
            self.b3.place(x=self.button_oddx + 50, y=85)
            print(len(self.oddEntry))
            print(len(self.odd_Label_Entry))
        if self.button_oddx >= self.window_w - 750:
            self.b3.place_forget()

    def moving_But(self):
        self.b3.place_forget()
        self.all_entry = []
        if (self.button_y < self.window_h - 50):
            self.counter += 1
            self.button_y = self.button_y + 40
            self.b.place_forget()
            self.b.place(x=self.button_x, y=self.button_y + 30)
            self.b5.place_forget()
            self.b5.place(x=710, y=self.button_y + 30)
            self.b6.place_forget()
            self.b6.place(x=800, y=self.button_y + 30)
            # self.b2.place_forget()
            # self.b2.place(x=10, y=self.button_y + 30)
            self.entrybox = Entry(self, width=10)
            self.entrybox2 = Entry(self, width=10)
            self.vs = Label(self, text='vs', font=('Lucida Calligraphy', '15', 'bold'), fg='#773c00', bd=5,
                            bg='#c9e3c1')
            self.entrybox.place(x=10, y=self.button_y - 20)
            self.entrybox2.place(x=100, y=self.button_y - 20)
            self.vs.place(x=60, y=self.button_y - 25)

            self.WinEntry.place(x=210, y=130)
            self.DrawEntry.place(x=260, y=130)
            self.LoseEntry.place(x=310, y=130)
            self.OthersEntry.place(x=360, y=130)
            clear_us =[self.WinEntry, self.DrawEntry, self.LoseEntry,
                            self.OthersEntry,self.vs, self.entrybox,self.entrybox2]
            self.clear_us.extend(clear_us)
            if len(self.oddEntry) > 0 and self.counter == 1:
                for i in range(len(self.oddEntry)):
                    self.button_xx += 50
                    self.cdx += 1
                    self.oddEntry3.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                    self.oddEntry3[self.cdx].place(x=self.button_xx, y=self.button_y - 20)
                    for i in self.oddEntry3:
                        i['textvariable']=DoubleVar()
                self.button_xx = 360
            print('this is oddEntry3', len(self.oddEntry3))
            print(len(self.odd_holder))
            print(self.odd_holder)
            print(self.counter)
            if self.counter == 2:
                self.odd_holder.append([])
                self.all_ent.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                self.all_ent[0].place(x=210, y=self.button_y - 20)
                self.all_ent[1].place(x=260, y=self.button_y - 20)
                self.all_ent[2].place(x=310, y=self.button_y - 20)
                self.all_ent[3].place(x=360, y=self.button_y - 20)
                for i in self.all_ent:
                    i['textvariable'] = DoubleVar()

                if self.button_xx <= self.button_oddx:
                    self.cdx = -1
                    for i in range(len(self.oddEntry)):
                        self.oddEntry2.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                        self.cdx += 1
                        self.button_xx += 50
                        self.oddEntry2[self.cdx].place(x=self.button_xx, y=self.button_y - 20)
                        for i in self.oddEntry2:
                            i['textvariable'] = DoubleVar()
                    self.button_xx = 360
            elif self.counter == 3:
                self.odd_holder.append([])
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                self.all_ent[4].place(x=210, y=self.button_y - 20)
                self.all_ent[5].place(x=260, y=self.button_y - 20)
                self.all_ent[6].place(x=310, y=self.button_y - 20)
                self.all_ent[7].place(x=360, y=self.button_y - 20)
                for i in self.all_ent:
                    i['textvariable'] = DoubleVar()
                if self.button_xx <= self.button_oddx:
                    for i in range(len(self.oddEntry)):
                        self.button_xx += 50
                        self.cdx += 1
                        self.oddEntry2.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                        self.oddEntry2[self.cdx].place(x=self.button_xx, y=self.button_y - 20)
                        for i in self.oddEntry2:
                            i['textvariable'] = DoubleVar()

                    self.button_xx = 360
            elif self.counter == 4:
                self.odd_holder.append([])
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                self.all_ent[8].place(x=210, y=self.button_y - 20)
                self.all_ent[9].place(x=260, y=self.button_y - 20)
                self.all_ent[10].place(x=310, y=self.button_y - 20)
                self.all_ent[11].place(x=360, y=self.button_y - 20)
                for i in self.all_ent:
                    i['textvariable'] = DoubleVar()
                if self.button_xx <= self.button_oddx:
                    for i in range(len(self.oddEntry)):
                        self.button_xx += 50
                        self.cdx += 1
                        self.oddEntry2.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                        self.oddEntry2[self.cdx].place(x=self.button_xx, y=self.button_y - 20)
                        for i in self.oddEntry2:
                            i['textvariable'] = DoubleVar()
                    self.button_xx = 360
                    print(len(self.oddEntry2))
            elif self.counter == 5:
                self.odd_holder.append([])
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                self.all_ent[12].place(x=210, y=self.button_y - 20)
                self.all_ent[13].place(x=260, y=self.button_y - 20)
                self.all_ent[14].place(x=310, y=self.button_y - 20)
                self.all_ent[15].place(x=360, y=self.button_y - 20)
                for i in self.all_ent:
                    i['textvariable'] = DoubleVar()

                if self.button_xx <= self.button_oddx:
                    for i in range(len(self.oddEntry)):
                        self.button_xx += 50
                        self.cdx += 1
                        self.oddEntry2.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                        self.oddEntry2[self.cdx].place(x=self.button_xx, y=self.button_y - 20)
                        for i in self.oddEntry2:
                            i['textvariable'] = DoubleVar()
                    self.button_xx = 360

            elif self.counter == 6:
                self.odd_holder.append([])
                self.all_ent.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent[16].place(x=210, y=self.button_y - 20)
                self.all_ent[17].place(x=260, y=self.button_y - 20)
                self.all_ent[18].place(x=310, y=self.button_y - 20)
                self.all_ent[19].place(x=360, y=self.button_y - 20)
                for i in self.all_ent:
                    i['textvariable'] = DoubleVar()
                if self.button_xx <= self.button_oddx:
                    for i in range(len(self.oddEntry)):
                        self.button_xx += 50
                        self.cdx += 1
                        self.oddEntry2.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                        self.oddEntry2[self.cdx].place(x=self.button_xx, y=self.button_y - 20)
                        for i in self.oddEntry2:
                            i['textvariable'] = DoubleVar()
                    self.button_xx = 360
            elif self.counter == 7:
                self.odd_holder.append([])
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                self.all_ent.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent[20].place(x=210, y=self.button_y - 20)
                self.all_ent[21].place(x=260, y=self.button_y - 20)
                self.all_ent[22].place(x=310, y=self.button_y - 20)
                self.all_ent[23].place(x=360, y=self.button_y - 20)
                for i in self.all_ent:
                    i['textvariable'] = DoubleVar()
                if self.button_xx <= self.button_oddx:
                    for i in range(len(self.oddEntry)):
                        self.button_xx += 50
                        self.cdx += 1
                        self.oddEntry2.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                        self.oddEntry2[self.cdx].place(x=self.button_xx, y=self.button_y - 20)
                        for i in self.oddEntry2:
                            i['textvariable'] = DoubleVar()
                    self.button_xx = 360
            elif self.counter == 8:
                self.odd_holder.append([])
                self.all_ent.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent[24].place(x=210, y=self.button_y - 20)
                self.all_ent[25].place(x=260, y=self.button_y - 20)
                self.all_ent[26].place(x=310, y=self.button_y - 20)
                self.all_ent[27].place(x=360, y=self.button_y - 20)
                for i in self.all_ent:
                    i['textvariable'] = DoubleVar()
                if self.button_xx <= self.button_oddx:
                    for i in range(len(self.oddEntry)):
                        self.button_xx += 50
                        self.cdx += 1
                        self.oddEntry2.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                        self.oddEntry2[self.cdx].place(x=self.button_xx, y=self.button_y - 20)
                        for i in self.oddEntry2:
                            i['textvariable'] = DoubleVar()
                    self.button_xx = 360
            elif self.counter == 9:
                self.odd_holder.append([])
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent[28].place(x=210, y=self.button_y - 20)
                self.all_ent[29].place(x=260, y=self.button_y - 20)
                self.all_ent[30].place(x=310, y=self.button_y - 20)
                self.all_ent[31].place(x=360, y=self.button_y - 20)
                for i in self.all_ent:
                    i['textvariable'] = DoubleVar()
                if self.button_xx <= self.button_oddx:
                    for i in range(len(self.oddEntry)):
                        self.button_xx += 50
                        self.cdx += 1
                        self.oddEntry2.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                        self.oddEntry2[self.cdx].place(x=self.button_xx, y=self.button_y - 20)
                        for i in self.oddEntry2:
                            i['textvariable'] = DoubleVar()
                    self.button_xx = 360
            elif self.counter == 10:
                self.odd_holder.append([])
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                self.all_ent.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent[32].place(x=210, y=self.button_y - 20)
                self.all_ent[33].place(x=260, y=self.button_y - 20)
                self.all_ent[34].place(x=310, y=self.button_y - 20)
                self.all_ent[35].place(x=360, y=self.button_y - 20)
                for i in self.all_ent:
                    i['textvariable'] = DoubleVar()
                if self.button_xx <= self.button_oddx:
                    for i in range(len(self.oddEntry)):
                        self.button_xx += 50
                        self.cdx += 1
                        self.oddEntry2.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                        self.oddEntry2[self.cdx].place(x=self.button_xx, y=self.button_y - 20)
                        for i in self.oddEntry2:
                            i['textvariable'] = DoubleVar()
                    self.button_xx = 360
                # print('this is the no. items', len(self.all_ent), 'ok')
            elif self.counter == 11:
                self.odd_holder.append([])
                self.all_ent.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                self.all_ent.append(Entry(self, validatecommand=self.vcmd, validate='all',width=6))
                self.all_ent.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent[36].place(x=210, y=self.button_y - 20)
                self.all_ent[37].place(x=260, y=self.button_y - 20)
                self.all_ent[38].place(x=310, y=self.button_y - 20)
                self.all_ent[39].place(x=360, y=self.button_y - 20)
                for i in self.all_ent:
                    i['textvariable'] = DoubleVar()
                if self.button_xx <= self.button_oddx:
                    for i in range(len(self.oddEntry)):
                        self.button_xx += 50
                        self.cdx += 1
                        self.oddEntry2.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                        self.oddEntry2[self.cdx].place(x=self.button_xx, y=self.button_y - 20)
                        for i in self.oddEntry2:
                            i['textvariable'] = DoubleVar()
                    self.button_xx = 360

                print('this is the no. items', len(self.all_ent), 'ok')
                print('this is the no. items', len(self.oddEntry2), 'ok')
            else:
                pass

            if self.counter > 0:
                self.x += 1
                self.amount_Entry.append(Entry(self,validatecommand=self.vcmd, validate='all', width=10))
                self.amount_Entry[self.x].place(x=710, y=self.button_y - 20)
                for i in self.amount_Entry:
                    i["textvariable"] = DoubleVar()
                    if self.clear_count == True:
                        for i in self.amount_Entry:
                              i["textvariable"] = DoubleVar().set('')
        else:
            self.errorlab = Label(self, text="you've reached the limit,\n enter your odds....",
                                  font=('Lucida Calligraphy', '15', 'bold'), fg='#3d7c6f', bd=5,
                                  bg='#c9e3c1')
            self.errorlab.place(x=10, y=self.window_h - 40)


    def callback1(self, event):
        print('you clicked on left frame', event.x, event.y)
        # print(len(self.all_entry))

    def restart_program1(self):
        os.execl(sys.executable, sys.executable, *sys.argv)
class pageone(Frame):
    def __init__(self, master, control):
        Frame.__init__(self, master, bg='#c9e3c1')

        lab = Label(self, text='welcome to \nGORZY BET SOFTWARE',fg = '#3d7c6f', font=('Bradley Hand ITC', '40', 'bold'), bg='#c9e3c1')
        lab.place(x=10, y=10)

        lab1 = Label(self, text='Analyze game', font=('Bradley Hand ITC', '25', 'bold'),fg = '#3d7c6f', bg='#c9e3c1')
        lab1.place(x=1110, y=520)

        lab2 = Label(self, text='About App', font=('Bradley Hand ITC', '25', 'bold'),fg = '#3d7c6f', bg='#c9e3c1')
        lab2.place(x=30, y=520)
        asa = ttk.Style()


        self.photo_info = ImageTk.PhotoImage(file='help-operator.png')
        self.but1 = Button(self, bg='#c9e3c1',cursor = 'circle',activebackground ='#c9e3c1',
                          image = self.photo_info,border = '0',command = self.about_us)
        self.but1.place(x=30, y=560)

       #  text_file = open("C:\\Users\stone's\Desktop\\works.txt")
       #  text1 = text_file.read()
       #

        self.bind("<Button-1>", self.callback1)
        # text11 = Text(self, height = 20, width= 10)
        # text11.place(relx=0.2, rely=0.3)
        self.photo_start = ImageTk.PhotoImage(file='start (1).png')

        but = Button(self, image=self.photo_start,cursor = 'circle',
                     bg='#c9e3c1',activebackground ='#c9e3c1',
                     command=lambda: control.raise_frame(widget))
        but.place(x=1150, y=580)
        but['border']= '0'

        self.photo = ImageTk.PhotoImage(file='goal.png')

        self.help_button =Button(self,image=self.photo,fg = '#c9e3c1',cursor = 'circle',
                                 command = self.how,activebackground ='#c9e3c1', bg= '#c9e3c1')
        self.help_button['border']='0'
        self.help_button.place(relx = 0.02, rely = 0.3)
        self.counting = 1
        self.counting2 = 1
    def about_us(self):
        self.counting2 +=1
        if self.counting2 %2 ==0:
            text_file1 ="""ABOUT APP           """
            text_file = """      \n\nThis desktop app was designed
        using python GUI. It can run
        smoothly on any operating system.
        The creator is CodeHobby.
        Codehobby creates any computer
        application client would need.
        From automation of task to
        analysis of Data.
        Data Structuring is also, another
        task codehobby can handle for you.\n\n
    
        for inquiry:"""
            text_file2 = """\n09090306975 -Livingstone E.V.\nvvictorious99@gmail.com\n"""
            self.tt = Text(self, width=43, height=24, bg='#3d7c6f', fg ='#a3e4c0', font=('Times', '15'))
            self.tt.tag_configure('bold_italics', font=('Bradley Hand ITC', '25','bold'), background='#3d7c6f')
            self.tt.tag_configure('big', font=('Footlight MT Light', 14),foreground = '#008080',background='#d6dfdc')
            self.tt.tag_configure('color', foreground='#008080',
                                font=('Tempus Sans ITC', 15),background='#d6dfdc')
            self.tt.insert(END, text_file1, 'bold_italics')
            self.tt.insert(END, text_file,'color')
            self.tt.insert(END, text_file2,'big')

            self.tt.configure(state = 'disable')
            self.tt.place(relx=0.7, rely=0)
            self.about_clear = ttk.Button(self, text='close', cursor = 'circle',width = 10,takefocus=False, command =self.close_about_page )
            self.about_clear.place(x = 950, y= 500)
        else:
            self.tt.place_forget()
            self.about_clear.place_forget()

    def how(self):
        self.counting +=1

        if self.counting%2 ==0:
            how = """\nThis app is designed to calculate odds with a particular amount.
            -Enter 'zero'(0) for any odd that you intend to leave empty.
            -Create the exact number of matches you intend checking
             their odds.
            -Don't create redundant matches, if you do, click the restart button.\n"""
            how_heading = """" How to use app"""
            self.tt2 = Text(self, width=60, height=8,border ='0',fg ='#a3e4c0', background='#3d7c6f', font=('Times', '15'))
            self.tt2.tag_configure('bold_italics', font=('Bradley Hand ITC', '25', 'bold'), background='#3d7c6f')
            self.tt2.tag_configure('big', font=('Footlight MT Light', 14), foreground='#008080', background='#d6dfdc')
            self.tt2.insert(END, how_heading, 'bold_italics')
            self.tt2.insert(END, how, 'big')
            self.tt2.configure(state='disable')
            self.tt2.place(relx=0.07, rely=0.3)
            print(self.counting, self.counting % 2)

        else:
            self.tt2.place_forget()


        # self.how_clear = ttk.Button(self, text='close', width = 10, command =self.close_how_page )


    def close_about_page(self):
        self.tt.place_forget()
        self.about_clear.place_forget()

    def callback1(self, event):
        print('you clicked on frame', event.x, event.y)


app = moreTab()

app.mainloop()

