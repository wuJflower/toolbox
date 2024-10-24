import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from capLevel import init_speed_level

ttk.Style().configure("Custom.TButton", background="lightblue",  font=("Arial", 15))


# 创建主窗口
root = tk.Tk()
root.title("工具箱")
root.geometry("500x300")
# 设置背景颜色
root.configure(bg='lightblue')

def open_file_picker():
    file_path = filedialog.askopenfilename()
    input_button.configure(text=file_path)
    file  = filedialog.Open(file_path)

def destroy_root():
    for widget in root.winfo_children():
        widget.destroy()

def back2home():
    # 遍历 root 窗口中的所有子控件并销毁
    destroy_root()
    init_home()

def fix_cap_file():
    destroy_root()
    destroy_button = ttk.Button(root, text="返回", width=10, command=back2home)
    destroy_button.pack(padx=0)

    # 设置大标题
    title_label = ttk.Label(root, text="电容校准文件转换工具", font=("Arial", 14), style="Custom.TButton")
    title_label.pack(pady=10)



    # 输入框和选择按钮
    frame1 = tk.Frame(root)
    frame1.pack(pady=10)
    frame1.configure(bg='lightblue')

    input_button = ttk.Button(frame1, text="输入框", width=20)
    input_button.grid(row=0, column=0, padx=10)

    select_button = ttk.Button(frame1, text="选择", width=10,command=open_file_picker)
    select_button.grid(row=0, column=1, padx=10)

    resize_cap_frame =  ttk.Frame(root)
    resize_cap_frame.pack(pady=10)


    # 提示输入
    instruction_label = ttk.Label(root, text="请输入并联电容:", font=("Arial", 12) )
    instruction_label.pack(pady=10)

    # 容值和数量输入
    frame2 = tk.Frame(root)
    frame2.pack(pady=10)
    frame2.configure(bg='lightblue')

    capacitance_label = ttk.Label(frame2, text="容值/pF", font=("Arial", 12), )
    capacitance_label.grid(row=0, column=0, padx=10)

    quantity_label = ttk.Label(frame2, text="数量", font=("Arial", 12) )
    quantity_label.grid(row=0, column=1, padx=10)


    capacitance_entry = ttk.Entry(frame2, width=15)
    capacitance_entry.grid(row=1, column=0, padx=10)

    quantity_entry = ttk.Entry(frame2, width=15)
    quantity_entry.grid(row=1, column=1, padx=10)

def init_home():
    destroy_root()
    open_fix_cap_button = ttk.Button(root, text="电容文件转换", width=20, command=fix_cap_file) 
    open_fix_cap_button.pack(pady=10)
    
    open_fix_cap_button = ttk.Button(root, text="VPP计算", width=20) 
    open_fix_cap_button.pack(pady=10)
    
    open_fix_cap_button = ttk.Button(root, text="频率等级计算", width=20,) 
    open_fix_cap_button.pack(pady=10)
    
    open_fix_cap_button = ttk.Button(root, text="阻抗计算器", width=20) 
    open_fix_cap_button.pack(pady=10)
    

init_home()


root.mainloop()