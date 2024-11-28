branchname= freq
remote_url = https://gitee.com/JaFlower/toolbox.git
remote_name = origin
remote_branch = freqSpeedLevel

local_branch = feature-freqSpeedLevel



# 添加远程仓库
add_remote:
	git  remote add $(remote_name)  $(remote_url)

# 拉取远程仓库 特定分支到 本地分支
fork_remote:add_remote
	git checkout  -b $(local_branch) $(remote_name)/$(remote_branch)
switch_branch:
	git checkout $(local_branch)

pull:
	git pull $(remote_name) $(remote_branch)

# 更新 本地仓库到远程仓库
push:pull
	git push $(remote_name)  $(remote_branch)













# 通过代理ttkbootstrap 库安装
ttkbootstrap:
	pip install ttkbootstrap  -i https://pypi.tuna.tsinghua.edu.cn/simple

messagebox:
	pip install  tkmessagebox  -i https://pypi.tuna.tsinghua.edu.cn/simple

# 生成exe可执行文件,相对路径
main_file = main.py
exe_file_name = ToolBox.exe



open:
	./dist/$(exe_file_name)
exe:
	pip install pyinstaller
	pyinstaller --onefile --noconsole  -n  $(exe_file_name) $(main_file) 
# vsc 插件
# git-commit-lint-vscode