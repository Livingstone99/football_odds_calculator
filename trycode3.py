from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
import sys


class moreTab(tk.Tk):

    def __init__(self, ):
        Tk.__init__(self, )
        self.geometry("1350x800")
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
        self.heading = Label(self, text='GAME ANALYSIS',
                             font=('Bradley Hand ITC', '25', 'bold'), bd=5, bg='#c9e3c1')
        self.heading.place(x=0, y=0)
        self.graph_heading = Label(self, text='Profit/', font=('Lucida Calligraphy', '15', 'bold'),
                                   bd=5, bg='#c9e3c1')
        self.graph_headingg = Label(self, text='Loss', font=('Lucida Calligraphy', '15', 'bold'),
                                   bd=5, fg ='red', bg='#c9e3c1')
        self.graph_heading.place(x=930, y=5)
        self.graph_headingg.place(x=1020, y=5)
        # self.graph_heading3 = Label(self, text='', font=('Lucida Calligraphy', '15', 'bold'),
        #                             bd=5, bg='#c9e3c1')
        # self.graph_heading3.place(x=1100, y=5)
        self.amount_played = Label(self, text='Amount', font=('Lucida Calligraphy', '15', 'bold'),
                                   bd=5, bg='#c9e3c1')
        self.amount_played.place(x=710, y=5)
        self.graph_heading1 = Label(self, text='Enter odds', font=('Lucida Calligraphy', '15', 'bold'),
                                    bd=5, bg='#c9e3c1')
        self.graph_heading1.place(x=350, y=0)
        self.m = 0
        n = 2
        self.entrybox = Entry(self, width=10)
        self.entrybox.place(x=10, y=90)
        self.entrybox2 = Entry(self, width=10)
        self.entrybox2.place(x=100, y=90)
        self.vs = Label(self, text='vs', font=('Lucida Calligraphy', '15', 'bold'), bd=5, bg='#c9e3c1')
        self.vs.place(x=60, y=85)

        self.b = ttk.Button(self, text='create more', width=15, command=self.moving_But)
        self.b.place(x=10, y=120)
        self.b1 = ttk.Button(self, text='start page', width=15, command=lambda: control.raise_frame(pageone)).place(x=1200,
                                                                                                                y=640)
        # self.b2 = Button(self, text = 'undo boxes', width = 10,command = self.Undo_move)
        # self.b2.place(x =10 , y = 120)
        self.b3 = ttk.Button(self, text='odds', width=8, command=self.more_odds)
        self.b3.place(x=560, y=100)
        self.b5 = ttk.Button(self, text='compute', width=10,command=self.computing_odds_frac)
        self.b5.place(x=550, y=15)
        self.b6 =ttk.Button(self, text='Reset', width=7, command= self.restart_program1)
        self.b6.place(x=660, y=15)
        # self.b4 = ttk.Button(self, text = 'close App', width = 10, command= self.destroy())
        # self.b4.place(x = 1100, y  = 5)
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

        self.list_of_odds = [self.wins, self.draw, self.lose, self.Other]
        self.list_of_odds1 = [self.wins1, self.draw1, self.lose1, self.Other1]

        if len(self.oddEntry) != 0:
            ###THIS FOR-LOOP COMPUTES THE ODDS IN THE FIRST ROW
            for i in self.oddEntry:
                self.oddEntry_float1.append(float(i.get()))
            self.list_of_odds.extend(self.oddEntry_float1)
            self.total_of_odds = sum(self.list_of_odds)
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
                self.answer_next2.append(Label(self, text='X',
                                              font=('Lucida Calligraphy', '9', 'bold'), fg='black', bd=5, bg='#c9e3c1'))
            else:
                self.answer_next2.append(Label(self, text="%s" % (str(int((i))).split('.')[0]),
                                               font=('Lucida Calligraphy', '9', 'bold'), bd=5, bg='#c9e3c1'))


        for i in self.answer:
            ## THIS IS THE LABEL THAT CARRIES THE RESULTS OF THE FIRST ROW
            if i < 0 and i != -self.amounts:
                self.answer_next.append(Label(self, text="%s" % str(int((i))).split('.')[0],
                                              font=('Lucida Calligraphy', '9', 'bold'), fg = 'red', bd=5, bg='#c9e3c1'))
            elif i == -self.amounts:
                self.answer_next.append(Label(self, text='X',
                                              font=('Lucida Calligraphy', '9', 'bold'), fg='black', bd=5, bg='#c9e3c1'))
            else:
                self.answer_next.append(Label(self, text="%s" % str(int((i))).split('.')[0],
                                              font=('Lucida Calligraphy', '9', 'bold'), bd=5, bg='#c9e3c1'))
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
        print('this is the odd', len(self.oddEntry2), '\nand this is the number of list', len(self.odd_holder))
        xd = -1
        xf = -1
        xv = -1
        xvv = 0
        xc = -1
        ss = -1

        self.ratio_odd_and_list = int(len(self.oddEntry2)) // int(len(self.odd_holder))
        print('this is the ratio', self.ratio_odd_and_list)
        if len(self.all_ent) > 0:
            ## IF MORE ODDS CREATED, THIS LOOP CHANGES IT TO FLOAT AND APPENDS IT APPROPRAITELY
            for i in self.all_ent:
                self.all_ent_float.append(float(i.get()))
            for i in self.amount_Entry:
                self.amount_Entry_float.append(float(i.get()))
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
                for i in self.oddEntry2:
                    self.oddEntry_float.append(float(i.get()))
                for i in range(len(self.odd_holder)):
                    xd += 1
                    for i in range(self.ratio_odd_and_list):
                        xf += 1
                        self.odd_holder[xd].append(self.oddEntry_float[xf])
            for i in self.amount_Entry:
                self.amount_Entry_next.append(int(i.get()))
            for i in self.odd_holder:
                self.sum_of_held_odds.append(sum(i))
                print(self.sum_of_held_odds)
            for i in range(len(self.odd_holder)):
                xc += 1
                xv = -1
                xvv += 1
                print('for list in holder', xc)
                self.sum_up_row.append([])
                for i in self.odd_holder[xc]:
                    xv += 1
                    print('held odds', xv)
                    print('index for amount', xvv)
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
                                                                  font=('Lucida Calligraphy', '9', 'bold'), fg='black',
                                                                  bd=5, bg='#c9e3c1'))
                    else:
                        self.sum_up_row_next[ss].append(Label(self, text="%s" % str(int((i))).split('.')[0],
                                                              font=('Lucida Calligraphy', '9', 'bold'), bd=5,
                                                              bg='#c9e3c1'))
                ssn = 780
                self.button_yy += 40
                for i in self.sum_up_row_next[ss]:
                    ssn += 50
                    i.place(x=ssn, y=self.button_yy + 10)

            print(self.sum_of_held_odds)
            print('this should be lists', self.sum_up_row)
            print('this for amount', self.amount_Entry_next)

    def clear_data(self):
        ss = -1
        self.clear_count +=1
        self.wins_var.set('')
        self.draw_var.set('')
        self.lose_var.set('')
        self.others_var.set('')
        self.amount_var.set('')
        self.wins_var1.set('')
        self.draw_var1.set('')
        self.lose_var1.set('')
        self.others_var1.set('')
        self.amount_var1.set('')

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

    def more_odds(self):
        ## this function creates more odds, along the x axis
        self.count += 1
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
        self.b3.destroy()
        self.all_entry = []
        if (self.button_y < self.window_h - 50):
            self.counter += 1
            self.button_y = self.button_y + 40
            self.b.place_forget()
            self.b.place(x=self.button_x, y=self.button_y + 30)
            # self.b2.place_forget()
            # self.b2.place(x=10, y=self.button_y + 30)
            self.entrybox = Entry(self, width=10).place(x=10, y=self.button_y - 20)
            self.entrybox2 = Entry(self, width=10).place(x=100, y=self.button_y - 20)
            self.vs = Label(self, text='vs', font=('Lucida Calligraphy', '15', 'bold'), fg='#773c00', bd=5,
                            bg='#c9e3c1').place(x=60, y=self.button_y - 25)

            self.WinEntry.place(x=210, y=130)
            self.DrawEntry.place(x=260, y=130)
            self.LoseEntry.place(x=310, y=130)
            self.OthersEntry.place(x=360, y=130)
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
                self.all_ent.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
                self.all_ent.append(Entry(self,validatecommand=self.vcmd, validate='all', width=6))
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
                                  font=('Lucida Calligraphy', '15', 'bold'), fg='#773c00', bd=5,
                                  bg='#c9e3c1').place(x=10, y=self.window_h - 40)


    def callback1(self, event):
        print('you clicked on left frame', event.x, event.y)
        # print(len(self.all_entry))

    def restart_program1(self):
        os.execl(sys.executable, sys.executable, *sys.argv)
class pageone(Frame):
    def __init__(self, master, control):
        Frame.__init__(self, master, bg='#c9e3c1')
        self.canvas = Canvas(self, width=200, height=100)

        self.canvas.place(x=10, y=10)
        self.line_horizontal = self.canvas.create_line(10, 10, 12, 10)
        lab = Label(self, text='welcome to Game Analysis', font=('Bradley Hand ITC', '40', 'bold'), bg='#c9e3c1')
        lab.place(x=10, y=10)
        # img = PhotoImage(file = 'forward.png')
        but = ttk.Button(self, text='start', width = 15, command=lambda: control.raise_frame(widget))
        but.place(x=1150, y=580)

        lab1 = Label(self, text='Analyze game', font=('Bradley Hand ITC', '25', 'bold'), bg='#c9e3c1')
        lab1.place(x=1110, y=520)

        lab2 = Label(self, text='About App', font=('Bradley Hand ITC', '25', 'bold'), bg='#c9e3c1')
        lab2.place(x=30, y=520)
        but1 = ttk.Button(self, text="click...",command = self.about_us, width = 15)
        but1.place(x=30, y=560)

        def restart_program1(self):

            self.python = sys.executable
            os.execl(self.python, self.python, *sys.argv)

        self.bind("<Button-1>", self.callback1)

    def about_us(self):
        text_file = open("C:\\Users\stone's\Desktop\\works.txt")
        text1 = text_file.read()
        Label(self, text="%s" % (text1), font=('Bradley Hand ITC', '25', 'bold'), bg='#c9e3c1').place(x=30, y=100)

    def callback1(self, event):
        print('you clicked on left frame', event.x, event.y)


app = moreTab()

app.mainloop()

