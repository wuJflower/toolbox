import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from capLevel import init_speed_level

ttk.Style().configure("Custom.TButton", background="lightblue",  font=("Arial", 15))

# data

speed_levels  = [0,0,0,0,0,0,0,0,0]
level_str =tk.StringVar()
level_str.set("有效速度等级：")
#func


# 创建主窗口
root = tk.Tk()
root.title("工具箱")
root.geometry("500x300")
root.configure(bg='lightblue')

root.resizable(False, False)

# 左右布局
left = tk.Frame(root, bg='lightblue')
left.pack(side=tk.LEFT, padx=2, pady=10)
right = tk.Frame(root, bg='lightblue',bd=5,relief="ridge")
right.pack(side=tk.RIGHT,padx=10, pady=2)



def open_file_picker():
    file_path = filedialog.askopenfilename()
    input_button.configure(text=file_path)
    file  = filedialog.Open(file_path)

def destroy_root(self):
    for widget in self.winfo_children():
        widget.destroy()

def back2home():
    # 遍历 root 窗口中的所有子控件并销毁
    destroy_root(right)
    init_home()

def fix_cap_file():
    destroy_root(right)

    head = tk.Frame(right)
    head.pack(pady=10)

    # 设置大标题
    title_label = ttk.Label(head, text="电容校准文件转换工具", font=("Arial", 14), style="Custom.TButton")
    title_label.grid(row=0, column=0, padx=10)

    destroy_button = ttk.Button(head, text="X", width=10, command=back2home)
    destroy_button.grid(row=0, column=1, padx=10)

    # 输入框和选择按钮
    frame1 = tk.Frame(right)
    frame1.pack(pady=10)
    frame1.configure(bg='lightblue')

    input_button = ttk.Button(frame1, text="输入框", width=20)
    input_button.grid(row=0, column=0, padx=10)

    select_button = ttk.Button(frame1, text="选择", width=10,command=open_file_picker)
    select_button.grid(row=0, column=1, padx=10)

    resize_cap_frame =  ttk.Frame(root)
    resize_cap_frame.pack(pady=10)


    # 提示输入
    instruction_label = ttk.Label(right, text="请输入并联电容:", font=("Arial", 12) )
    instruction_label.pack(pady=10)

    # 容值和数量输入
    frame2 = tk.Frame(right)
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

def create_vpp_page():
    destroy_root(right)
    head = tk.Frame(right)
    head.pack(pady=10)

    # 设置大标题
    title_label = ttk.Label(head, text="VPP计算工具", font=("Arial", 14), style="Custom.TButton")
    title_label.grid(row=0, column=0, padx=10)

    destroy_button = ttk.Button(head, text="X", width=10, command=back2home)
    destroy_button.grid(row=0, column=1, padx=10)





# 定义验证函数
def validate_input(freq):
    if freq.isdigit() == True :
        level = 0
        index = 0
        # 待修复bug
        while(float(freq * pow(2,level)) <50):
            speed_levels[index] = level
            index += 1
            current=level_str.get()
            level_str.set(current + str(level) + ",")
            level += 1

        return True
    return False  # 仅当输入是数字时返回 True

# 注册验证函数
vcmd = (root.register(validate_input), '%P')  # '%P' 表示输入后的内容

def create_speed_level():
    destroy_root(right)
    
    head = tk.Frame(right)
    head.pack(pady=10)

    # 设置大标题
    title_label = ttk.Label(head, text="速度等级计算工具", font=("Arial", 14), style="Custom.TButton")
    title_label.grid(row=0, column=0, padx=10)

    destroy_button = ttk.Button(head, text="X", width=10, command=back2home)
    destroy_button.grid(row=0, column=1, padx=10)

    frame1 = tk.Frame(right)
    frame1.pack(pady=2)

    tk.Label(frame1, text="输入频率/Mhz:").grid(row=0, column=0, padx=10)
    tk.Entry(frame1, width=20,validate="key", validatecommand=vcmd).grid(row=0, column=1, padx=10)


    frame2 = tk.Frame(right)
    frame2.pack(pady=2)

    tk.Label(frame2, textvariable=level_str).grid( row=0, column=0, padx=10)
    



def init_home():
    destroy_root(left)
    open_fix_cap_button = ttk.Button(left, text="电容文件转换", width=20, command=fix_cap_file) 
    open_fix_cap_button.pack(pady=10)
    
    open_fix_cap_button = ttk.Button(left, text="VPP计算", width=20,command=create_vpp_page) 
    open_fix_cap_button.pack(pady=10)
    
    open_fix_cap_button = ttk.Button(left, text="频率等级计算", width=20, command=create_speed_level) 
    open_fix_cap_button.pack(pady=10)
    
    open_fix_cap_button = ttk.Button(left, text="阻抗计算器", width=20) 
    open_fix_cap_button.pack(pady=10)
    

init_home()


root.mainloop()