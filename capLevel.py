def init_speed_level(root,ttk):
    for widget in root.winfo_children():
        widget.destroy()
    open_fix_cap_button = ttk.Button(root, text="电容文件转换", width=20) 
    open_fix_cap_button.pack(pady=10)
    
    open_fix_cap_button = ttk.Button(root, text="VPP计算", width=20) 
    open_fix_cap_button.pack(pady=10)
    
    open_fix_cap_button = ttk.Button(root, text="频率等级计算", width=20) 
    open_fix_cap_button.pack(pady=10)
    
    open_fix_cap_button = ttk.Button(root, text="阻抗计算器", width=20) 
    open_fix_cap_button.pack(pady=10)