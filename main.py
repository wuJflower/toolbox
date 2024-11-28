import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from capLevel import init_speed_level

import re
import os
import platform

from enum import Enum

# data

#func
# global var
content = []
single_cal_file = []
single_cap = []
cap_value_list = []
cap_file_read = False
cap_index = 0

file_path = ""

# 密码确认页面打开页面索引
# 创建枚举类型 0,VPP;1，速度等级；2，阻抗计算；from enum import Enum
# 新增 需要鉴权页面则需要新增枚举类型

class PAGE_INDEX(Enum):
    PAGE_INDEX_VPP = 0
    PAGE_INDEX_SPEED_LEVEL = 1
    PAGE_INDEX_IMPEDANCE_CALCULATION = 2

page_index = PAGE_INDEX.PAGE_INDEX_VPP.value


FILE_SHOW_INDEX = 999
LABEL_INPUT_FILE = 1000

# 创建主窗口
root = ttk.Window(themename="superhero")
root.title("工具箱")
# 获取屏幕分辨率
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 设置窗口大小为屏幕宽度的 80% 和高度的 60%
window_width = int(screen_width * 0.8)
window_height = int(screen_height * 0.6)
root.geometry(f"{window_width}x{window_height}")
# 设置最小尺寸
root.wm_minsize(int(window_width*0.5), int(window_height*0.5))


root.configure(bg='lightblue') 

# root.resizable(False, True)

# 左右布局
left = tk.Frame(root, bg='lightblue')
right = tk.Frame(root)

cap_list_frame = tk.Frame(right)


cap_inpout = tk.Frame(right)
frame = ttk.Frame(right)
cap_list = [(0,frame)]
cap_sum_label = ttk.Label(right,text="")

input_file_name = ttk.Label(right, text="暂未输入文件", width=40)

left.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
right.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)

root.grid_rowconfigure(0,weight=1)



# 打开单电容校准文件、多电容校准文件，
# 多电容校准文件，只计算保存第一个电容的校准数据
def open_file_picker():
    file_path = filedialog.askopenfilenames(
        title="选择txt 格式的校准文件",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        global cap_file_read
        cap_file_read = True

        
        global cap_list
        
        # 修复重复创建text_widget bug
        for i in cap_list:
            if i[0] == FILE_SHOW_INDEX:
                list_index = cap_list.index(i)
                i[1].destroy()
                cap_list.pop(list_index)
            if i[0] == LABEL_INPUT_FILE:
                pass

        # bug，暂时无法提取文件名，用于显示
        # fix 修复提取文件名
        if(os.path.splitext(os.path.basename(file_path[0]))[1].lower() != ".txt"):
            messagebox.showerror("错误", "请选择txt格式的电容校准文件")
            return
        messagebox.showinfo("提示", "已选择文件："+os.path.splitext(os.path.basename(file_path[0]))[0].lower()+os.path.splitext(os.path.basename(file_path[0]))[1].lower())
        global input_file_name
        input_file_name.config(text=os.path.splitext(os.path.basename(file_path[0]))[0].lower()+os.path.splitext(os.path.basename(file_path[0]))[1].lower())
        
        with open(file_path[0], 'r') as file:
            # 单电容校准文件格式
            # 数字 + 100个编码器位置 + 100个电容值位置
            # 读第101行到201行的数据
            global content
            global single_cal_file

            content = file.readlines()
            single_cal_file = content[0:201]

            text_widget = ttk.Text(right, wrap=WORD,width=40,height=10)
            
            cap_list.append((FILE_SHOW_INDEX,text_widget))

            text_widget.pack(pady=10)
            content = [line.strip() for line in content]
            text_widget.insert(END, "\n".join(content))


def destroy_root(self):
    for widget in self.winfo_children():
        widget.destroy()

def back2home():
    # 遍历 root 窗口中的所有子控件并销毁
    destroy_root(right)
    init_home()

def create_fix_cap_page():
    destroy_root(right)
    cap_file_read = False
    global cap_index
    cap_index = 0
    global file_path
    file_path = ""


    head = tk.Frame(right)
    head.pack(pady=10)

    # 设置大标题
    title_label = ttk.Label(head, text="单电容校准文件转换工具 V0.1.0", font=("Arial", 14))
    title_label.grid(row=0, column=0, padx=10)

    destroy_button = ttk.Button(head, text="X", width=10, command=back2home)
    destroy_button.grid(row=0, column=1, padx=10)

    # 输入框和选择按钮
    frame1 = tk.Frame(right)
    frame1.pack(pady=10)

    global input_file_name
    # 这个Label可用于展示
    input_file_name = ttk.Label(frame1, text="暂未输入文件", width=40)

    # 保存句柄，在打开文件后更新文件名
    global cap_list
    cap_list.append((LABEL_INPUT_FILE,input_file_name))


    input_file_name.grid(row=0, column=0, padx=10)

    select_button = ttk.Button(frame1, text="1、选择", width=10,command=open_file_picker)
    select_button.grid(row=0, column=1, padx=10)

    resize_cap_frame =  ttk.Frame(root)
    resize_cap_frame.grid(row=1,column=0)

    # 1、检验 选择的校准文件内容适合正确
   



    # 提示输入
    instruction_label = ttk.Label(right, text="请输入并联电容:", font=("Arial", 12) )
    instruction_label.pack(pady=10)

    # 容值和数量输入
    cap_inpout = tk.Frame(right)
    cap_inpout.pack(pady=10)

    capacitance_label = ttk.Label(cap_inpout, text="容值/pF", font=("Arial", 12), )
    capacitance_label.grid(row=0, column=0, padx=10)

    quantity_label = ttk.Label(cap_inpout, text="数量", font=("Arial", 12) )
    quantity_label.grid(row=0, column=1, padx=10)


    capacitance_entry = ttk.Entry(cap_inpout, width=15)
    capacitance_entry.grid(row=1, column=0, padx=10)

    quantity_entry = ttk.Entry(cap_inpout, width=15)
    quantity_entry.grid(row=1, column=1, padx=10)

    add = ttk.Button(cap_inpout,text="2、添加",width= 10,command= lambda :add_cap(capacitance_entry.get(),quantity_entry.get()))
    add.grid(row=1 , column = 2,pady=10)

    add = ttk.Button(cap_inpout,text="3、计算并保存",width= 15,command= lambda :cal_and_save(capacitance_entry.get(),quantity_entry.get()))
    add.grid(row=2 , column = 2,pady=10)

    open = ttk.Button(cap_inpout,text="4、打开文件",width= 10,command= lambda:open_file(file_path))
    open.grid(row=2 , column = 1,pady=10)


    # grid 格局占据一整行，固定电容总和位置
    global cap_sum_label
    cap_sum_label = ttk.Label(cap_inpout, text="并联电容容值总和：", font=("Arial", 12) )
    cap_sum_label.grid(row=3, column=0, columnspan=3, padx=10)

    global cap_list_frame
    cap_list_frame = ttk.Frame(cap_inpout)
    cap_list_frame.grid(row=4 ,column=0,columnspan=3,pady=10)
    

    # 2、点击按钮计算并联电容的容值C1 pF

    # 3、把校准文件的自101行开始，每一行加上C1*1000


def open_file(file_path:str):
    if file_path == "":
        messagebox.showwarning("提示", "请先打开校准文件 并点击 `计算并保存` ")
        return
    if platform.system() == "Windows":
        os.system(f"notepad {file_path}")
    return

def add_cap(cap_val:str , count :str):

    """  校验 """
    """ 输入数据要求
     cap_val 为非负数即可
      count  必须为非负整数 """
    
    if cap_val == "" or count == "":
        messagebox.showwarning("提示", "请输入容值和数量")
        return
    
    # 检测机制不完全，待解决；”123\"" 这种情况也能通过
    if  re.match(r'^-?\d*\.\d+$', cap_val) == False or re.match(r'^-?\d*\.\d+$', count)== False :
        messagebox.showwarning("提示", "请输入正确的数字")
        return
    

    """ # Model """
    
    global cap_index
    cap_index += 1
    index = cap_index
    cap_value_list.append([(index,cap_val,count)])
    
    """ # View """
    # 这个 页面 和 显示校准文件 形成左右布局，待更改
    # 需要固定和 显示校准文件关系
    # bug
    frame = ttk.Frame(cap_list_frame)
    # 全局链表便于页面增删
    # 可以考虑 全局所有页面都存储起来，然后通过index来删除（解决 button 不能传 Frame参数
    global cap_list
    cap_list.append((index,frame))

    ttk.Label(frame,text=cap_val, width=15).grid(row=0, column=0, padx=10)

    ttk.Label(frame,text=count, width=15).grid(row=0, column=1, padx=10)

    ttk.Button(frame,text="删除",width= 10,command= lambda:delete_frame(index)).grid(row=0 , column = 2,pady=10)
    frame.pack(pady=10)

# 删除指定页面组件
def delete_frame(index:int):
    # Model

    global cap_list

    for i in cap_list:
        if i[0] == index:
            list_index = cap_list.index(i)
            i[1].destroy()
            cap_list.pop(list_index)

    # bug 删除了组件但是没有删除数据
    global cap_value_list
    for i in cap_value_list:
        if i[0][0] == index :
            val_index = cap_value_list.index(i)
            cap_value_list.pop(val_index)


# 计算并联总容值
def cal_and_save(cap_val:str , count :str):
    
    if cap_file_read == False:
        # 用提示框提示请先打开校准文件
        messagebox.showwarning("提示", "请先打开校准文件")
        return
    # 断言 assert 校验输入参数str 是否都是数字，不是则提示
    # 待解决 检测字符串是否是数字
    # assert cap_val.isdigit() == True and count.isdigit() == True, "请输入整数"


    # Model
    global content
    # 1、所有并联电容值总和

    total_of_parallel_caps  = 0.0
    # 计算cap的和
    for i in cap_value_list:
        # bug 第一个电容值的小数位会被忽略,只要小数点后三位
        total_of_parallel_caps += round(float(i[0][1]),3)*float(i[0][2])*1000

    total_of_parallel_caps = int(total_of_parallel_caps)

    # 2、计算并联电容综合 依次加到电容值上
    cap_start_line = 101
    cap_end_line = 200


    # bug  重复点击会在上次结果进行累积计算
    # 直接用原始数据做 计算
    for i in range(cap_start_line,cap_end_line-1):
        single_cal_file[i]=str(int(content[i])+total_of_parallel_caps)+"\n"
    # 最后一个 不需要换行
    single_cal_file[cap_end_line]=str(int(content[cap_end_line])+total_of_parallel_caps)
        
    # view
    global cap_sum_label
    cap_sum_label.config(text=f"并联电容容值总和：{total_of_parallel_caps}")

    
    
    #Control
    # Save to file
    # 保存content 变量 到txt文件
    # 打开保存文件对话框
    global file_path
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",                # 默认文件扩展名
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],  # 文件类型
        title="保存文件"
    )
    # 检查用户是否选择了文件路径
    if file_path:
        # 将内容保存到指定路径
        with open(file_path, "w") as file:
            # 清空file
            file.writelines("")
            # 把数据写入file
            file.writelines(single_cal_file)
     


def create_vpp_page():
    destroy_root(right)
    head = tk.Frame(right)
    head.pack(pady=10)

    # 设置大标题
    title_label = ttk.Label(head, text="VPP计算工具", font=("Arial", 14) )
    title_label.grid(row=0, column=0, padx=10)

    destroy_button = ttk.Button(head, text="X", width=10, command=back2home)
    destroy_button.grid(row=0, column=1, padx=10)

    # 设置大标题
    title_label = ttk.Label(head, text="待开发", font=("Arial", 14) , bootstyle=DANGER)
    title_label.grid(row=1, column=0, padx=10)

def create_speed_level():
    destroy_root(right)
    
    head = tk.Frame(right)
    head.pack(pady=10)

    # 设置大标题
    title_label = ttk.Label(head, text="速度等级计算工具", font=("Arial", 14))
    title_label.grid(row=0, column=0, padx=10)

    destroy_button = ttk.Button(head, text="X", width=10, command=back2home)
    destroy_button.grid(row=0, column=1, padx=10)

    frame1 = tk.Frame(right)
    frame1.pack(pady=2)

    tk.Label(frame1, text="输入频率/Mhz:").grid(row=0, column=0, padx=10)
    tk.Entry(frame1, width=20,validate="key").grid(row=0, column=1, padx=10)


    frame2 = tk.Frame(right)
    frame2.pack(pady=2)

    tk.Label(frame2).grid( row=0, column=0, padx=10)
    
def create_z_cal():
    
    destroy_root(right)
    
    head = tk.Frame(right)
    head.pack(pady=10)

    # 设置大标题
    title_label = ttk.Label(head, text="阻抗计算器", font=("Arial", 14))
    title_label.grid(row=0, column=0, padx=10)

    destroy_button = ttk.Button(head, text="X", width=10, command=back2home)
    destroy_button.grid(row=0, column=1, padx=10)

def open_page():
    if page_index == PAGE_INDEX.PAGE_INDEX_VPP.value:
        create_vpp_page()
    elif page_index == PAGE_INDEX.PAGE_INDEX_SPEED_LEVEL.value:
        create_speed_level()
    elif page_index == PAGE_INDEX.PAGE_INDEX_IMPEDANCE_CALCULATION.value:
        create_z_cal()
    pass

def create_auth_page(index ):
    
    destroy_root(right)

    # 校验输入index在PAEGE_INDEX范围内
    if index < 0 or index >= len(PAGE_INDEX):
        messagebox.showwarning("提示", "打开错误页面")


    # Model 层
    global page_index
    page_index = index

    # View 层
    head = tk.Frame(right)
    head.pack(pady=10)
    
    
    title_label = ttk.Label(head, text="请输入密码", font=("Arial", 14))
    title_label.grid(row=0, column=0, padx=10)
    destroy_button = ttk.Button(head, text="X", width=10, command=back2home)
    destroy_button.grid(row=0, column=1, padx=10)

    body = tk.Frame(right)
    body.pack(pady=2)

    ttk.Label(body,text="密码：").grid(row=0,column=0,padx=10)
    pwd_entry = ttk.Entry(body, width=20)
    ttk.Button(body,text="打开",command=open_page).grid(row=0,column=1,padx=10)

    


def init_home():
    destroy_root(left)
    open_fix_cap_button = ttk.Button(left, text="单电容文件转换", width=20, command=create_fix_cap_page) 
    open_fix_cap_button.pack(pady=10)
    
    open_fix_cap_button = ttk.Button(left, text="VPP计算(待完成)", width=20,command=lambda: create_auth_page(PAGE_INDEX.PAGE_INDEX_VPP.value)) 
    open_fix_cap_button.pack(pady=10)
    
    open_fix_cap_button = ttk.Button(left, text="频率等级计算(待完成)", width=20, command=lambda: create_auth_page(PAGE_INDEX.PAGE_INDEX_SPEED_LEVEL.value)) 
    open_fix_cap_button.pack(pady=10)
    
    open_fix_cap_button = ttk.Button(left, text="阻抗计算器(待完成)", width=20,command=lambda: create_auth_page(PAGE_INDEX.PAGE_INDEX_IMPEDANCE_CALCULATION.value)) 
    open_fix_cap_button.pack(pady=10)

    ttk.Label(left, text="Power By WuWei",foreground="#FAF0E6",font=("Helvetica", 16)).pack(side="bottom", pady=(0, 30))
    

init_home()


class FreqLevelWidget:
    # 创建私有变量 频率 freq 和等级 level，
    def __init__(self, freq=13.56):
        self.freq = freq
        self.valid_level = []
    
    # 创建UI界面
    def crt_ui(self):
        # 显示当前频率 单位MHz
        freq_label = ttk.Label(right, text="当前频率: " + str(self.freq) + " MHz")
        freq_label.grid(row=0, column=0, padx=10, pady=10)

        # 输入框，用于输入频率
        freq_entry = ttk.Entry(right, width=20)
        freq_entry.grid(row=0, column=1, padx=10, pady=10)

        # 频率速度等级列表
        

        

        # 按钮点击事件，更新频率并计算等级
        def update_freq():
            self.freq = float(freq_entry.get())
            self.cal_freq_level()
            # 添加符合条件的 速度等级 和频率 组合到 列表
            


        pass

    # 计算得出
    def cal_freq_level(self):
        pass


root.mainloop()