from tkinter import *
from tkinter import ttk, messagebox #PopUp Error
import csv
from datetime import datetime



GUI =Tk()
GUI.title('โปรแกรมยบันทึกค่าใช้จ่าย v.1.0')
GUI.geometry('800x700+500+300')

########### Menu #############
menubar = Menu(GUI)
GUI.config(menu=menubar)

# File menu
filemenu = Menu(menubar)
menubar.add_cascade(label='File',menu=filemenu) #เพิ่มเมนูใหม่เข้าไป
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Export to Googlesheet')

# Help
def About():
        messagebox.showwarning('About','สวัสดีครับ โปรแกรมนี้คือโปรแกรมบันทึกข้อมูล\nสนใจบริจาคเราไหม ขอ 1 BTC ก็พอแล้ว\nฺBTC Adress: abc')
helpmenu = Menu(menubar)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)

# Donate
donatemenu = Menu(menubar)
menubar.add_cascade(label='Donate',menu=donatemenu)

########################

Tab = ttk.Notebook(GUI) #เอา Notebook ไปใส่ใน GUI
T1 = Frame(Tab) #เอา Frame ไปใส่ใน Tab ขยาย => T1 = Frame(Tab,width=400,height=400)
T2 = Frame(Tab)  #เอา Frame ไปใส่ใน Tab
Tab.pack(fill=BOTH,expand=1) #x มาจาก import * ขยายเต็มจอ

icon_t1 = PhotoImage(file='insert.png')#.subsample(2) = ย่อรูปตามขนาดเท่า
icon_t2 = PhotoImage(file = 'list.png')
icon_t3 = PhotoImage(file = 'save.png')



Tab.add(T1,text= f'{"เพิ่มค่าใช้จ่าย":^{30}}',image = icon_t1,compound='left') #ทำให้ Tab ยาวเท่ากัน จาก 30 ตัวอักษร
Tab.add(T2,text= f'{"ค่าใช้จ่าทั้งหมด":^{30}}',image = icon_t2,compound='left') #ทำให้ Tab ยาวเท่ากัน จาก 30 ตัวอักษร

#f1 = Frame(GUI)
f1 =Frame(T1)
#f1.place(x=100,y=50)
f1.pack() 

FONT1 = (None,20)

days = {'Mon':'จันทร์',
        'Tue':'อังคาร',
        'Wed':'พุธ',
        'Thu':'พฤหัสบดี',
        'Fri':'ศุกร์',
        'Sat':'เสาร์',
        'Sun':'อาทิตย์'}

def Save(event=None):
        expense = v_expense.get()
        price = v_price.get()
        emt = v_emt.get()
        if expense=='' :
                print('No Dara')
                messagebox.showwarning('Error','กรุณากรอกค่าใช้จ่าย')
                return
        elif price =='':
                messagebox.showwarning('Error','กรุณากรอกราคา')
                return
        elif emt == '':
                messagebox.showwarning('Error','กรุณากรอกจำนวน')              
                return

        try: 
           total = float(price)*float(emt)
           text = 'รายการ: {} ราคา: {}\n'.format(expense,price)
           text = text+ 'จำนวน: {} รวมทั้งหมด: {} บาท'.format(emt,total)
           print('รายการ : {}  ราคา: {} บาท\nจำนวน:  {} ชิ้น  ราคารวม: {} บาท '.format(expense,price,emt,total))
          
           d = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
           v_result.set(text+"\n"+d)
           v_expense.set(' ')
           v_price.set(' ')
           v_emt.set(' ')

           today = datetime.now().strftime('%a') # days['Mon'] = 'จันทร์'
           stamp = datetime.now()
           print(today)
           # dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
           dt = stamp.strftime('%Y-%m-%d %H:%M:%S')
           transactionID = stamp.strftime('%Y%m%d%H%M%f') #เป็นการสร้างไอดี จากสันเดอืนปี ชัวโมงนาทีวินาที f เป็นระดับไมโควินาที

           dt = days[today] + '-' + dt
           with open('data2.csv','a' ,encoding='utf-8',newline='') as  f:  
             fw = csv.writer(f) 
             data =  [transactionID,dt,expense,price,emt,total]
             fw.writerow(data)

        # ทำให้เคอเซอร์กลับไปตำแหน่งช่องกรอก E1
           E1.focus()
           update_table() #เพื่ออัพเดตข้อมูล
        except:
                print('Error')
                # messagebox.showerror('Error','กรุณากรอกข้อมูลให่ คุณกรอกตัวเลขผิด')
                messagebox.showwarning('Error','กรุณากรอกข้อมูลให่ คุณกรอกตัวเลขผิด')
                #messagebox.showinfo('Error','กรุณากรอกข้อมูลให่ คุณกรอกตัวเลขผิด')
                v_expense.set(' ')
                v_price.set(' ')
                v_emt.set(' ')

# ทำให้สามารถกด enter ได้
GUI.bind('<Return>', Save) #ต้องพิมใน def Save(event=None) ด้วย

icon_t4 = PhotoImage(file = 'Submarine.png')
Mainicon = Label(f1,image=icon_t4) 
Mainicon.pack()


L = Label(f1,text = 'รายการซื้อเรือดำน้ำของนายตู่', font=FONT1).pack()
v_expense = StringVar()
E1 = ttk.Entry(f1,textvariable = v_expense,font=FONT1)
E1.pack()


L = Label(f1, text="ราคา (บาท)",font=FONT1).pack()
v_price = StringVar()
E2 = ttk.Entry(f1,textvariable=v_price,font=FONT1)
E2.pack()

L = Label(f1,text='จำนวน' ,font=FONT1).pack()
v_emt = StringVar()
E3 = ttk.Entry(f1,textvariable= v_emt,font=FONT1)
E3.pack()

b2 = ttk.Button(f1,text=f'{"Save": >{10}}',image=icon_t3,compound='left',command=Save) # text=f'{"Save": >{10}}' = ให้ข้อความห่างจากด้านขวา 10 ตัวอักษร
b2.pack(ipadx=20,ipady=10,pady=20) #pady=20 ห่างจาก lable ข้างบน 20


v_result =StringVar()
v_result.set('------ผลลัพธ์-------')
result = Label(f1, textvariable = v_result,font=FONT1,fg='green')
result.pack(pady=20)
#icon_t5 = PhotoImage(file = 'nayok2.png')
#n = Label(f1,image=icon_t5,compound='left')
#n.pack()


##################### TAB2 #####################

def read_csv():
        with open('data2.csv',newline="",encoding="utf-8") as f: #ให้เปิดไฟล์ csv ตัวนี้ขึ้นมาแล้วต้องชื่อเล่นมันว่า f
            fr = csv.reader(f)
        #นอกจาก with สามารถทำแบบข้างล่างได้
        #f = open('savedata.csv',newline="",encoding="utf-8")
        #fr = csv.reader(f)
        #f.close()     
            data = list(fr)
            # print(data)
            # print('-------')
            # print(data[0][0])

             #for d in data: #วิธีที่ 1
              #   print(d[0]) #1 คือตำแหน่งในลิสที่ 1

            # for a,b,c,d,e in data: วิธีที่ 2
            #     print(d)
        return data
            
# tabel

L = Label(T2,text = 'ตารางแสดงผลลัพธ์', font=FONT1).pack()

header = ['รหัสรายการ','วัน-เวลา','รายการ','ค่าใช้จ่าย','จำนวน','รวม']
reuslttabel = ttk.Treeview(T2,columns=header,show='headings',heigh=50) # เอาไปใส่ใน tab2 headings คือเพื่อให้ไม่มีการย่อลงมาได้
reuslttabel.pack()

# for i in range(len(header)): วิธีที่ 1
#         reuslttabel.heading(header[i],text=header[i])

# reuslttabel.heading(header[0],text=header[0])  วิธีที่ 2
# reuslttabel.heading(header[1],text=header[1])
# reuslttabel.heading(header[2],text=header[2])
# reuslttabel.heading(header[3],text=header[3])
# reuslttabel.heading(header[4],text=header[4])

for h in header: #วิธีที่ 3
        reuslttabel.heading(h,text=h)


headerwidth = [140,200,100,80,80,80] # กำหนดค่าความกว้าง
for h,w in zip(header,headerwidth): #เป็นการจับคู่
        reuslttabel.column(h,width=w)

#reuslttabel.insert('','end',value=['จันทร์','น้ำส้ม','30','3','60'])

def DeleteRecord():
        check = messagebox.askyesno('confirm?','คุณต่้องการลบข้อมูลใช่หรือไม่')
        print('Yes/No',check)
        

        if check==True:
           print('delete')     
           select = reuslttabel.selection()
           #print(select)
           data = reuslttabel.item(select) #เรียกดูข้อมูลใน reuslttabel
           data = data['values'] #values เป็น key
           transactionID= data[0] #ค้นหาข้อมูลตำแหน่งที่ 0
           #print(transactionID)
           del alltransaction[str(transactionID)] #delete data in dict
           #print(alltransaction)
           updateCSV()
           update_table()
        else:
                print('cencel')

BDeldata = ttk.Button(T2,text='delete',command=DeleteRecord) #เอาไปใส่ใน T2 command คือการเรียกใช้ฟังกันอะไร
BDeldata.place(x=50,y=550)



alltransaction = {} #สร้างเพื่อเก็บ id ของข้อมูลเพื่อเอามาไว้ลบ         

def updateCSV():
        with open('data2.csv','w',newline="",encoding="utf-8") as f: # w save ทับข้อมูลที่มีอยู่
            fw = csv.writer(f)
            # เตรียมข้อมูลออกมาจาก alltransaction ให้กลายเป็น list
            data = list(alltransaction.values()) #แปลง dict ให้กลายเป็นลิส
            fw.writerows(data) #ลิสซ้อนลิส [[],[],[]] multiple line from nested list
            print('Table was updated')
            

def update_table():
    reuslttabel.delete(*reuslttabel.get_children()) #ลบข้อมูลก่อนที่จะอัพเดตข้อมูล *เป็นการลบแบบรัวๆ หรือลบแบบ for ลูป
    # for c in reuslttabel.get_children():
    #     reuslttabel.delete(c)
    try: #ดักจับถ้าไม่มีไฟล์
       data = read_csv()
       for d in data:
           #สร้าง transaction data
           alltransaction[d[0]] = d # d[0] = transactionID
           reuslttabel.insert('',0,value=d) #เพิ่ม data ตำแหน่งแรก
       print(alltransaction)
    except Exception as e:
        print('No File')

update_table()




GUI.bind('<Tab>',lambda x: E2.focus())
GUI.mainloop()
