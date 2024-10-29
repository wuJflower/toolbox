branchname= freq
remote_url = https://gitee.com/JaFlower/toolbox.git
remote_name = origin
remote_branch = freqSpeedLevel

local_branch = freq


# 添加远程仓库
add_remote:
	git  remote add $(remote_name)  $(remote_url)

# 拉取远程仓库 特定分支到 本地分支
fork_remote:add_remote
	git checkout  -b $(local_branch) $(remote_name)/$(remote_branch)


pull:
	git pull $(remote_name) $(remote_branch)

# 更新 本地仓库到远程仓库
push:pull
	git push $(remote_name)  $(remote_branch)












