import winreg

def add_context_menu():
    # 打开HKEY_CLASSES_ROOT\Directory\Background\shell 键
    key_path = r"Directory\Background\shell\AddToPath"
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path)

    # 设置右键菜单显示的名称
    winreg.SetValue(key, "", winreg.REG_SZ, "添加当前目录到PATH")

    # 设置右键菜单的图标（可选）
    icon_path = "C:\\Windows\\System32\\imageres.dll,-5302"  # 这里使用了一个系统默认图标，你可以替换为自己的图标路径
    winreg.SetValueEx(key, "Icon", 0, winreg.REG_SZ, icon_path)

    # 创建子键command，用于指定要执行的命令
    command_key = winreg.CreateKey(key, "command")

    # 设置要执行的命令，这里是将当前目录添加到系统环境变量PATH中
    command_value = 'setx PATH "%PATH%;%V%" /M'
    winreg.SetValue(command_key, "", winreg.REG_SZ, command_value)

    winreg.CloseKey(key)
    winreg.CloseKey(command_key)

if __name__ == "__main__":
    add_context_menu()