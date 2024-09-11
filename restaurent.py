import sys
from datetime import datetime
from tkinter import *
from tkinter import messagebox, ttk


def main():
    win=Tk()
    app=LoginPage(win)
    win.mainloop()


class LoginPage():
    def __init__(self,win):
        self.win=win
        self.win.geometry("1350x750+0+0")
        self.win.title("Restaurent Management System")
        
        self.title_label=Label(self.win,text="Restaurent Management System",font=('Arial',35,'bold'),bg="cyan",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)
        
        self.main_frame=Frame(self.win,bg="lightgrey",bd=6,relief=GROOVE)
        self.main_frame.place(x=250,y=150,width=800,height=450)
        
        self.login_lbl=Label(self.main_frame,text="LOGIN",bd=6,relief=GROOVE,anchor=CENTER,bg="lightgrey",font=('sans-serif',25,'bold'))
        self.login_lbl.pack(side=TOP,fill=X)
        
        self.entry_frame=LabelFrame(self.main_frame,text="Enter Details",bd=6,relief=GROOVE,bg="lightgrey",font=('sans-serif',18))
        self.entry_frame.pack(fill=BOTH,expand=TRUE)
        
        # =============================variables======
        
        username=StringVar()
        password=StringVar()
        
        self.entus_lbl=Label(self.entry_frame,text="Enter username",bg="lightgrey",font=('sans-serif',15))
        self.entus_lbl.grid(row=0,column=0,padx=2,pady=2)
        
        self.entus_ent=Entry(self.entry_frame,font=('sans-serif',15),bd=6,textvariable=username)
        self.entus_ent.grid(row=0,column=1,padx=2,pady=2)
        
        
        self.entpass_lbl=Label(self.entry_frame,text="Enter password",bg="lightgrey",font=('sans-serif',15))
        self.entpass_lbl.grid(row=1,column=0,padx=2,pady=2)
        
        self.entpass_ent=Entry(self.entry_frame,font=('sans-serif',15),bd=6,textvariable=password)
        self.entpass_ent.grid(row=1,column=1,padx=2,pady=2)
        
        # ==========functions=======
        
        
        def check_login():
            if username.get() =="krish" and password.get()=="1234":
                self.Billing_btn.config(state="normal")
            else:
                pass
        def reset():        
            username.set("")
            password.set("")
            
            
        def billing_sect():
            self.newWindow=Toplevel(self.win)
            self.app=Window2(self.newWindow)
        # ========== BUTTONS=======

        self.button_frame=LabelFrame(self.entry_frame,text="options",font=('Arial',15),bg="lightgrey",bd=7,relief=GROOVE)
        self.button_frame.place(x=20,y=100,width=730,height=85)
        
        
        self.login_btn=Button(self.button_frame,text="Login",font=('Arial',15),bd=5,width=15,command=check_login)
        self.login_btn.grid(row=0,column=0,padx=20,pady=2)
        
        self.Billing_btn=Button(self.button_frame,text="Billing",font=('Arial',15),bd=5,width=15,command=billing_sect)
        self.Billing_btn.grid(row=0,column=1,padx=20,pady=2,)
        self.Billing_btn.config(state="disabled")
        
        self.reset_btn=Button(self.button_frame,text="Reset",font=('Arial',15),bd=5,width=15,command=reset)
        self.reset_btn.grid(row=0,column=2,padx=20,pady=2)
        
        
class Window2():
    def __init__(self,win):
    
        self.win=win
        self.win.geometry("1350x750+0+0")
        self.win.title("Restaurent Management System")
        
        
        self.title_label=Label(self.win,text="Restaurent Management System",font=('Arial',35,'bold'),bg="cyan",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)
        
        # =========variables====
        cust_nm=StringVar()
        cust_cot=StringVar()
        date_pr=StringVar()
        item_pur=StringVar()
        item_qty=StringVar()
        cone=StringVar()  
        bill_no=StringVar()
        
        
        date_pr.set(datetime.now())
        
        
        total_list=[]
        self.grand_total=0
        
        
        # =========entry==========================
        
        self.entry_frame=LabelFrame(self.win,text="Enter Details",bd=7,relief=GROOVE,bg="lightgrey",font=('sans-serif',20))
        self.entry_frame.place(x=20,y=95,width=500,height=550)
        
        self.bill_no_lbl=Label(self.entry_frame,text="Bill Number",font=('Arial',15),bg="lightgrey")
        self.bill_no_lbl.grid(row=0,column=0,padx=20,pady=2)
        
        self.bill_no_ent=Entry(self.entry_frame,bd=5,textvariable=bill_no,font=('Arial',15))
        self.bill_no_ent.grid(row=0,column=1,padx=20,pady=2)
        
        
        self.cust_no_lbl=Label(self.entry_frame,text="Customer Name",font=('Arial',15),bg="lightgrey")
        self.cust_no_lbl.grid(row=1,column=0,padx=20,pady=2)
        
        self.cust_no_ent=Entry(self.entry_frame,bd=5,textvariable=cust_nm,font=('Arial',15))
        self.cust_no_ent.grid(row=1,column=1,padx=20,pady=2)
        
        
        self.cust_cont_lbl=Label(self.entry_frame,text="Contact Number",font=('Arial',15),bg="lightgrey")
        self.cust_cont_lbl.grid(row=2,column=0,padx=20,pady=2)
        
        self.cust_cont_ent=Entry(self.entry_frame,bd=5,textvariable=cust_cot,font=('Arial',15))
        self.cust_cont_ent.grid(row=2,column=1,padx=20,pady=2)
        
        self.date_lbl=Label(self.entry_frame,text="Date",font=('Arial',15),bg="lightgrey")
        self.date_lbl.grid(row=3,column=0,padx=20,pady=2)
        
        self.date_ent=Entry(self.entry_frame,bd=5,textvariable=date_pr,font=('Arial',15))
        self.date_ent.grid(row=3,column=1,padx=20,pady=2)
        
        self.Item_Purchased_lbl=Label(self.entry_frame,text="Item Purchased",font=('Arial',15),bg="lightgrey")
        self.Item_Purchased_lbl.grid(row=4,column=0,padx=20,pady=2)
        
        self.Item_Purchased_ent=Entry(self.entry_frame,bd=5,textvariable=item_pur,font=('Arial',15))
        self.Item_Purchased_ent.grid(row=4,column=1,padx=20,pady=2)
        
        
        self.Item_qty_lbl=Label(self.entry_frame,text="Item Quantity",font=('Arial',15),bg="lightgrey")
        self.Item_qty_lbl.grid(row=5,column=0,padx=20,pady=2)
        
        self.Item_qty_ent=Entry(self.entry_frame,bd=5,textvariable=item_qty,font=('Arial',15))
        self.Item_qty_ent.grid(row=5,column=1,padx=20,pady=2)
        
        
        self.cost_one_lbl=Label(self.entry_frame,text="Cost of One",font=('Arial',15),bg="lightgrey")
        self.cost_one_lbl.grid(row=6,column=0,padx=20,pady=2)
        
        self.cost_one_ent=Entry(self.entry_frame,bd=5,textvariable=cone,font=('Arial',15))
        self.cost_one_ent.grid(row=6,column=1,padx=20,pady=2)
        
        # ===============Functions==================
        def default_bill():
            self.bill_txt.insert(END,"\n\t\t\t\t Krish Restaurent ")
            self.bill_txt.insert(END,"\n\t\t\t 7 street,near Airport,rajkot")
            self.bill_txt.insert(END,"\n\t\t\t Contact - +917778814270")
            self.bill_txt.insert(END,"\n================================================================================")
        
        
        def genbill():
            if  cust_nm.get()=="" or (cust_cot.get()=="" or len(cust_cot.get())!=10):
                messagebox.showerror("Error!","Please fill the fields correctly",parent=self.win)
            else:

                    self.bill_txt.insert(END,f"\nBilling Number: {bill_no.get()}")
                    self.bill_txt.insert(END,f"\nCustomer Name: {cust_nm.get()}")
                    self.bill_txt.insert(END,f"\nCustomer Contact: {cust_cot.get()}")
                    self.bill_txt.insert(END,f"\nDate :{date_pr.get()}")
                    self.bill_txt.insert(END,"\n================================================================================")
                    self.bill_txt.insert(END,"\nProduct Name\t\t        Quantity\t\t         Per Cost\t\t        Total")
                    self.bill_txt.insert(END,"\n================================================================================")

                    self.add_btn.config(state="normal")
                    self.total_btn.config(state="normal")
        def clear_func():
            cust_nm.set("")
            cust_cot.set("")
            item_pur.set("")
            item_qty.set("")
            cone.set("")
            
        def reset_func():
            total_list.clear()
            self.grand_total=0
            self.total_btn.config(state="disabled")
            self.add_btn.config(state="disabled")
            self.save_btn.config(state="disabled")
            self.bill_txt.delete("1.0",END)
            default_bill()
            
        def add_func():
            if item_pur.get()=="" or item_qty.get()=="":
                messagebox.showerror("Error!","Please fill the fields correctly",parent=self.win)
            else:
                
                    qty=int(item_qty.get())
                    cones=int(cone.get())
                    total=qty * cones
                    total_list.append(total)
                    self.bill_txt.insert(END,f"\n{item_pur.get()}\t\t            {item_qty.get()}\t\t           \tRs.{cone.get()}\t\t      \tRs.{total}")
                    
            
        def total_func():
            for item in total_list:
                self.grand_total +=item
                
                
            self.bill_txt.insert(END,"\n================================================================================")
            self.bill_txt.insert(END,f"\n\t\t\t\t\t\t\tGrand total : Rs.{self.grand_total}")
            self.bill_txt.insert(END,"\n================================================================================")
            self.save_btn.config(state="normal")

        def save_func():
            user_choice=messagebox.askyesno("Confirm?",f"Do you want to save the bill {bill_no.get()}",parent=self.win)
            
            if user_choice>0:
                self.bill_content=self.bill_txt.get("1.0",END)
                try:
                    
                    con=open(f"D:/sujanproject/Python/bills/" + str(bill_no.get())+ ".txt","w")
                except exception as e:
                    messagebox.showerror("Error!",f"Error due to {e}")
                con.write(self.bill_content)
                con.close()
                messagebox.showinfo("Success!",f"Bill {bill_no.get()} has been saved successfully",parent=self.win)
            else:
                return
            
        
        # ================Buttons=========
        
        self.button_frame=LabelFrame(self.entry_frame,bd=5,text="Options",bg="lightgrey",font=('Arial',15))
        self.button_frame.place(x=20,y=280,width=440,height=220)
        
        
        self.add_btn=Button(self.button_frame,bd=2,text="add",width=18,height=3,command=add_func)
        self.add_btn.grid(row=0,column=0,padx=4,pady=2)
        self.add_btn.config(state="disabled")
        
        self.generate_btn=Button(self.button_frame,bd=2,text="generate",width=18,height=3,command=genbill)
        self.generate_btn.grid(row=0,column=1,padx=4,pady=2)
        
        self.Clear_btn=Button(self.button_frame,bd=2,text="Clear",width=18,height=3,command=clear_func)
        self.Clear_btn.grid(row=0,column=2,padx=4,pady=2)
        
        self.total_btn=Button(self.button_frame,bd=2,text="total",width=18,height=3,command=total_func)
        self.total_btn.grid(row=1,column=0,padx=4,pady=2)
        self.total_btn.config(state="disabled")

        
        self.reset_btn=Button(self.button_frame,bd=2,text="reset",width=18,height=3,command=reset_func)
        self.reset_btn.grid(row=1,column=1,padx=4,pady=2)
        
        self.save_btn=Button(self.button_frame,bd=2,text="save",width=18,height=3,command=save_func)
        self.save_btn.grid(row=1,column=2,padx=4,pady=2)
        self.save_btn.config(state="disabled")

        
        
        
        # ========Bill frame=======
        
        self.bill_frame=LabelFrame(self.win,text="Bill Area",font=('Arial',18),bg="lightgrey",bd=8,relief=GROOVE)
        self.bill_frame.place(x=575,y=95,width=680,height=550)
        
        
        self.y_scroll=Scrollbar(self.bill_frame,orient="vertical")
        self.bill_txt=Text(self.bill_frame,bg="white",yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_txt.yview)
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.bill_txt.pack(fill=BOTH,expand=TRUE)
        
        
        default_bill()

if __name__=="__main__":
    main()
    
