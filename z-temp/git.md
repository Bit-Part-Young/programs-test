---
title: git 使用
top: false
cover: false
toc: true
mathjax: true
summary: git 使用
tags:
  - git
categories:
  - 科研工具
date: 2023-07-22 15:56:30
password:
---

# 介绍

分布式版本控制系统（无法对 office 文档格式进行版本控制），程序员必备


参考资料：
>[Git 备忘清单 & git cheatsheet & Quick Reference](https://wangchujiang.com/reference/docs/git.html)
>[git.txt](https://github.com/skywind3000/awesome-cheatsheets/blob/master/tools/git.txt)
>[GitHub - jaywcjlove/git-tips: 这里是我的笔记，记录一些git常用和一些记不住的命令。](https://github.com/jaywcjlove/git-tips)
>[GitHub - 521xueweihan/git-tips: :trollface:Git的奇技淫巧](https://github.com/521xueweihan/git-tips)
>[Git • Linux tutorial](https://pranabdas.github.io/linux/git)
>[十分钟学会正确的github工作流，和开源作者们使用同一套流程\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV19e4y1q7JJ/)
>[GitHub - hongiii/gitNotes\_from\_Liao: 从廖老师网站上总结的Git笔记，对常见命令进行了总结。](https://github.com/hongiii/gitNotes_from_Liao)
>[Git 重学指南 - Git 重学指南](https://git-remake.wybxc.cc/index.html)




---
---

# 使用

## 配置文件

### `.gitconfig`

- windows `.gitconfig` 路径：`git\etc\gitconfig`
- linux `.gitconfig` 路径：`~/.gitconfig`

```bash
[user]
        name = XXX
        email = XXX@email.com
[init]
        defaultBranch = main
[credential]
        helper = cache --timeout 300000
        # 可添加
        # helper = store --file ~/.git-credentials

```



---

### `.git-credential`

待写



---

### `.gitignore`

忽略文件，可在 repo 根目录或其他子目录创建多个 `.gitignore` 文件


若在 `.gitignore` 添加忽略文件后不起作用，可使用如下命令：
```bash
git rm --cached file
```


不同编程语言的 `.gitignore` 模板
>[GitHub - github/gitignore: A collection of useful .gitignore templates](https://github.com/github/gitignore)


仅 git 克隆部分文件
>[如何使用 Git 只克隆部分文件 | 猎人杂货铺](https://hunterx.xyz/git-sparse-checkout.html#more)


- [ ] .gitattributes 文件的含义是什么？
>[.gitattributes](https://github.com/esemble/simpy/blob/master/.gitattributes)



---

## 多账号 ssh 配置

多账号 ssh 配置作用：
- 多账号管理：通过配置 config 文件，可以方便地管理访问多个仓库时使用的不同账号；
- 通过 ssh 协议，可以免密访问、克隆远程仓库，以及 git 操作（clone、pull 和 push 等）。


生成密钥，将 `id_rsa.gitee.pub` 和 `id_rsa.github.pub` 文件中的内容添加到 github 和 gitee 中的 SSH keys（SSH 公钥）中；
```bash
ssh-keygen -t rsa -f ~/.ssh/id_rsa.gitee -C "XXX@email.com"

ssh-keygen -t rsa -f ~/.ssh/id_rsa.github -C "XXX@email.com"
```


`~/.ssh/config` 文件配置
```bash
# github
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa.github

# gitee
Host gitee.com
    Port 22
    HostName gitee.com
    User git
    IdentityFile ~/.ssh/id_rsa.gitee

# gitlab
Host gitlab.com
    Port 22
    HostName gitlab.com
    User git
    IdentityFile ~/.ssh/id_rsa.gitlab

```


测试
```bash
ssh -T git@github.com

ssh -T git@gitee.com

ssh -T git@gitlab.com
```


若返回信息，则配置成功
```txt
Hi XXX! You've successfully authenticated, but GitHub does not provide shell access.

Hi XXX! You've successfully authenticated, but GITEE.COM does not provide shell access.
```


注：
- 超算平台中的登陆节点禁止对外的 ssh，无法使用 git 交互环境，建议在 pc 本地或者实验室工作站（manager 和 master）使用。
- 超算平台进行以上设置会出现以下报错：
```bash
ssh: connect to host github.com port 22: Network is unreachable
```

- pi 有时候能通过 ssh 连上 github。
- `~/.ssh/config` 文件出现 `Bad owner or permissions` 错误的解决办法：文件权限位问题，设置 config 文件权限为 `600` （chmod 命令）。



---

### 将 repo 的 remote origin 由 https 改为 ssh 或 token 形式

之后进行 push、pull 等操作时，将默认通过 SSH 协议,并使用 SSH keys 进行身份验证，不需要再输入用户名和密码。

在该 repo 目录中的 `.git/config` 文件找到 `[remote "origin"]` 选项，将 URL 后的 https 地址改成 ssh 形式或带 token 的地址

```bash
# 原
url = https://github.com/user/repo.git

# ssh形式
url = git@gitee.com:user/repo.git
url = git@github.com:user/repo.git

# 带token形式
url = https://user:token@github.com/user/repo.git
url = https://user:token@gitee.com/user/repo.git
```



---

## github 需要用到 token 的地方

github 从 2021 年开始不再支持输入账号和密码的形式进行验证，改为 token。

- git 操作（push）
- 图床
- 与 gitee 进行 repo 同步



---

## 为 repo 创建 gh-pages 分支并 deploy

一般通过第三方的 Github Actions repo
>[GitHub - peaceiris/actions-gh-pages: GitHub Actions for GitHub Pages 🚀 Deploy static files and publish your site easily. Static-Site-Generators-friendly.](https://github.com/peaceiris/actions-gh-pages)

>[GitHub Marketplace · Actions to improve your workflow · GitHub](https://github.com/marketplace?type=actions)



---

## gitee 与 github、gitlab 之间互相同步

**gitee 可以直接从 github 和 gitlab 中导入 repo**

>[仓库镜像管理（Gitee<->Github 双向同步） | Gitee 产品文档](https://help.gitee.com/repository/settings/sync-between-gitee-github)
>[Gitlab、Github、Gitee之间的代码同步\_gitea 和gitee能同步吗\_李·逍遥的博客-CSDN博客](https://blog.csdn.net/lianwen1314/article/details/106384595)



---

## 基本使用

- 注册 gitee 或 github 账户
- 配置 gitee 或 github 的 SSH（id_rsa.gitee、id_rsa.github）
- 配置 git（.gitconfig）
- 新建 repo

```bash
git init
git add README.md
git commit -m "first commit"

# github
git remote add origin git@github.com:username/repo.git
# git remote add origin https://github.com/username/repo.git

# gitee
git remote add origin git@gitee.com:username/repo.git
# git remote add origin https://gitee.com/username/repo.git

git push -u origin main
```


- 本地已有 git repo

```bash
git remote add origin git@github.com:username/repo.git
git push -u origin main
```



---

## 开发使用

>[GitHub - firstcontributions/first-contributions: 🚀✨ Help beginners to contribute to open source projects](https://github.com/firstcontributions/first-contributions)


```bash
1.git clone // 到本地  
2.git checkout -b xxx 切换至新分支xxx  
（相当于复制了remote的仓库到本地的xxx分支上  
3.修改或者添加本地代码（部署在硬盘的源文件上）  
4.git diff 查看自己对代码做出的改变  
5.git add 上传更新后的代码至暂存区  
6.git commit 可以将暂存区里更新后的代码更新到本地git  
7.git push origin xxx 将本地的xxxgit分支上传至github上的git  
-----------------------------------------------------------  
（如果在写自己的代码过程中发现远端GitHub上代码出现改变）  
1.git checkout main 切换回main分支  
2.git pull origin master(main) 将远端修改过的代码再更新到本地  
3.git checkout xxx 回到xxx分支  
4.git rebase main 我在xxx分支上，先把main移过来，然后根据我的commit来修改成新的内容  
（中途可能会出现，rebase conflict -----》手动选择保留哪段代码）  
5.git push -f origin xxx 把rebase后并且更新过的代码再push到远端github上  
（-f ---》强行）  
6.原项目主人采用pull request 中的 squash and merge 合并所有不同的commit  
----------------------------------------------------------------------------------------------  
远端完成更新后  
1.git branch -d xxx 删除本地的git分支  
2.git pull origin master 再把远端的最新代码拉至本地
```




---
---

## 常用命令

### config

```bash
# 查看设置
git config --list

# 全局设置 git
git config --global user.name "username"
git config --global user.email "user@email.com"

# 取消设置
git config --global --unset user.name
git config --global --unset user.email
```



---

### add

---

### commit

---

### push

---

### pull

```bash
# 建立版本库
git init

# 将更新的文件加入版本库缓存区
git add * 

# 进行 Commit, 每一次 Commit 就相当于保存一份备份, 作为时间线的一个节点
git commit -m "message" 

# 查看完整时间线, 方便进行版本回退
git log 

# 进行版本回退, 即返回你保存的某个备份, <commit_id> 是你使用 git log 看见的 ID 值
git reset --hard <commit_id> 

# 将 GitHub 上的代码仓库给 Clone 下来
git clone <url> 

# 拉取远程分支(团队其他人可能修改了代码), 如果有冲突, 解决冲突
git pull 

# 推送分支到远程分支, 进行团队同步
git push 


git status --short --branch
```


---

### branch

```bash
git branch 

git branch -a

git brach -u

git branch -m

# 删除前会提醒是否进行分支的合并
git branch -d branch-name

# 强制删除
git branch -D branch-name
```


---

### checkout

```bash
git checkout


git checkout -b
```


---

### remote

```bash
git remote prune origin

# 查看远程分支
git remote show origin
```


---

### fetch

---

### tag

打标签 tag
```bash
# 列出现有标签
git tag

# 新建标签
git tag v1.0.0

# 新建带注释标签
git tag -a v1.0.0 -m 'Nb-Si projects scripts until on 20230723'

# 推送单个tag到orgin源上
git push origin v1.0.0

# 将本地所有的标签都推送到远程仓库
git push origin --tags



# 删除标签
git tag -d v0.1

# 删除远程标签
git push origin :refs/tags/v1.0.0

# 获取远程所有内容包括tag
git pull --all

# 列出标签及其注释
git tag -ln

# 查看具体某个标签信息
git show v1.0.0
```


---

### log

日志 log
```bash
# 查看提交日志
git log

# 以一行的形式显示提交日志,并显示缩短的 commit id
git log --oneline

# 显示倒数第几条log
git log -num

# 查看含有 "update" 关键字的提交日志
git log --grep=update

# 查看所有分支的所有操作记录
git reflog

# 美观的 git log 输出样式 参考 zsh git alias
git log --graph --pretty="%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%ar) %C(bold blue)<%an>%Creset" --stat
```



---

### diff

---

### status

---

### stash

git stash 命令用于在不提交当前工作目录的情况下,将当前的修改保存起来,以便后续恢复。

它的主要用途有:

1. 当你正在开发功能,需要切换分支修复 bug 或 pull request 时,可以用 git stash 暂存当前的修改,待修复 bug 后再恢复这些修改继续开发。

2. 当你代码修改到一半,还不想提交,但是需要拉取最新的远程代码时,可以用 git stash 暂存当前的修改,拉取代码后再恢复这些修改。

git stash 的常用命令:
```bash
# 将当前修改暂存到 stash 栈中
git stash

# 包括 untracked 的文件
git stash -u

# 恢复 stash 中的最近一次暂存，并从 stash 栈中删除
git stash pop

# 恢复 stash 中的最近一次暂存,但不从 stash 栈中删除
git stash apply

# 显示 stash 中的所有暂存
git stash list

# 清空 stash 中的所有暂存
git stash clear

# 从 stash 中创建一个新的分支
git stash branch <branch> 

# 删除 stash 中的最近一次暂存
git stash drop
```


所以 git stash 可以让我们灵活地在功能开发和 bug 修复之间切换,提高效率。正确使用可以避免许多不必要的提交或代码丢失。



---

## oh-my-zsh 中 git 插件 git 命令相关 alias

```bash
# git add 相关
ga='git add'
gaa='git add --all'
gapa='git add --patch'
gau='git add --update'
gav='git add --verbose'
gwip='git add -A; git rm $(git ls-files --deleted) 2> /dev/null; git commit --no-verify --no-gpg-sign --message "--wip-- [skip ci]"'


# git commit 相关
gc='git commit --verbose'
'gc!'='git commit --verbose --amend'
gca='git commit --verbose --all'
'gca!'='git commit --verbose --all --amend'
gcam='git commit --all --message'
'gcan!'='git commit --verbose --all --no-edit --amend'
'gcans!'='git commit --verbose --all --signoff --no-edit --amend'
gcas='git commit --all --signoff'
gcasm='git commit --all --signoff --message'
gcmsg='git commit --message'
'gcn!'='git commit --verbose --no-edit --amend'
gcs='git commit --gpg-sign'
gcsm='git commit --signoff --message'
gcss='git commit --gpg-sign --signoff'
gcssm='git commit --gpg-sign --signoff --message'
gwip='git add -A; git rm $(git ls-files --deleted) 2> /dev/null; git commit --no-verify --no-gpg-sign --message "--wip-- [skip ci]"'


# git push 相关
ggpush='git push origin "$(git_current_branch)"'
git-svn-dcommit-push='git svn dcommit && git push github $(git_main_branch):svntrunk'
gp='git push'
gpd='git push --dry-run'
gpf='git push --force-with-lease'
'gpf!'='git push --force'
gpoat='git push origin --all && git push origin --tags'
gpod='git push origin --delete'
gpsup='git push --set-upstream origin $(git_current_branch)'
gpsupf='git push --set-upstream origin $(git_current_branch) --force-with-lease'
gpu='git push upstream'
gpv='git push --verbose'


# git pull 相关
ggpull='git pull origin "$(git_current_branch)"'
gl='git pull'
gluc='git pull upstream $(git_current_branch)'
glum='git pull upstream $(git_main_branch)'
gpr='git pull --rebase'
gup='git pull --rebase'
gupa='git pull --rebase --autostash'
gupav='git pull --rebase --autostash --verbose'
gupom='git pull --rebase origin $(git_main_branch)'
gupomi='git pull --rebase=interactive origin $(git_main_branch)'
gupv='git pull --rebase --verbose'


# git checkout 相关
gcb='git checkout -b'
gcd='git checkout $(git_develop_branch)'
gcm='git checkout $(git_main_branch)'
gco='git checkout'
gcor='git checkout --recurse-submodules'


# git reset相关
gpristine='git reset --hard && git clean --force -dfx'
grh='git reset'
grhh='git reset --hard'
groh='git reset origin/$(git_current_branch) --hard'
gru='git reset --'
gunwip='git rev-list --max-count=1 --format="%s" HEAD | grep -q "\--wip--" && git reset HEAD~1'


# git status 相关
gsb='git status --short --branch'
gss='git status --short'
gst='git status'


# git diff 相关
gd='git diff'
gdca='git diff --cached'
gdcw='git diff --cached --word-diff'
gds='git diff --staged'
gdt='git diff-tree --no-commit-id --name-only -r'
gdup='git diff @{upstream}'
gdw='git diff --word-diff'


# git tag 相关
gtl='gtl(){ git tag --sort=-v:refname -n --list "${1}*" }; noglob gtl'
gts='git tag --sign'
gtv='git tag | sort -V'


# git remote 相关
gr='git remote'
gra='git remote add'
grmv='git remote rename'
grrm='git remote remove'
grset='git remote set-url'
grup='git remote update'
grv='git remote --verbose'


# git config 相关
gcf='git config --list'


# git rm 相关
grm='git rm'
grmc='git rm --cached'
gwip='git add -A; git rm $(git ls-files --deleted) 2> /dev/null; git commit --no-verify --no-gpg-sign --message "--wip-- [skip ci]"'

```




---
---

# 其他用法

### 删除本地及对应的远程分支

```bash
# 删除本地分支
# 强制删除
git branch -D local-branch

# 删除对应的远程分支
git push origin :remote-branch
git push origin --delete remote-branch


# 示例：
git branch -D feature
git push origin :feature

git remote prune origin   # 该命令的作用主要是使本地的跟踪分支列表与远程保持一致，删除那些远程分支已经不存在而本地还保留的跟踪记录
```



---

## 忽略文件的权限变化

```bash
git config core.fileMode false
```



---

## 显示本地分支相关联的远程分支的跟踪情况

列出当前仓库中所有分支的信息，包括每个分支的名称、关联的远程分支、远程分支的提交和本地分支的提交。

```bash
git branch -vv
```



---

## 提交空文件夹

在空文件夹中建立一个文件 `.gitkeep`, 之后空文件夹可以提交。



---

## clone 多个分支

```bash
git clone -b <branch1> -b <branch2> <url>
```



---

## 下载单个文件

打开单个文件，点击 "Raw"，用 wget 下载单个文件
```bash
# gitee
wget https://gitee.com/Devkings/oh_my_zsh_install/raw/master/install.sh -O install.sh

# github
wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O install.sh

# gist
wget https://gist.githubusercontent.com/user/GIST_ID/raw/filename -O filename
```



---

## git 设置 alias

>[查看历史 - Git 重学指南](https://git-remake.wybxc.cc/%E5%82%A8%E5%AD%98%E5%BA%93/%E6%9F%A5%E7%9C%8B%E5%8E%86%E5%8F%B2.html)

```bash
# 设置之后直接使用 git ls
git config --global alias.ls "log --no-merges --color --graph --date=format:'%Y-%m-%d %H:%M:%S' --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cd) %C(bold blue)<%an>%Creset' --abbrev-commit"
```



---

## github 加速下载

可以在 github url 前面加上 `https://ghproxy.com/`
```bash
git clone https://ghproxy.com/https://github.com/tommason14/lammps.vim.git
```



---

## 规范式 commit

gitmoji-cli：git commit 时使用 emoji
>[GitHub - carloscuesta/gitmoji-cli: A gitmoji interactive command line tool for using emojis on commits. 💻](https://github.com/carloscuesta/gitmoji-cli)
>[gitmoji 速查表 - Git 重学指南](https://git-remake.wybxc.cc/%E9%99%84%E5%BD%95/gitmoji-%E9%80%9F%E6%9F%A5%E8%A1%A8.html)



---

## 查看两个星期内的改动

```bash
git whatchanged --since='2 weeks ago'
```



---

## `git status` 中文乱码

```bash
git config --global core.quotepath false
```

## 创建发行版（Releases）

待写



---

## 新建孤立分支

与当前的主分支无继承关系




---
---

# 可能会遇到的问题

## 问题 1

```bash
Switched to branch 'main'
Your branch is based on 'origin/master', but the upstream is gone.
(use "git branch --unset-upstream" to fixup) 
```

（ChatGPT 生成）
- 如果你不再需要跟踪远程分支,可以运行 `git branch --unset-upstream` 来取消设置跟踪关系,这样本地分支就会成为一个独立分支。
- 如果你还需要跟踪远程分支，只是远程分支被删除或重命名了，你可以重新设置跟踪关系:

```
git branch -u origin/新分支名 主分支

git branch -u origin/main main
```

- 如果远程仓库 itself 消失了，你需要先添加一个新的远程仓库，然后重新设置跟踪关系:

```
git remote add origin 新仓库地址
git branch -u origin/主分支名 主分支
```



---

## 问题 2

windows git 出现如下问题：
```bash
fatal: unable to access https://github.com/MatMLlab/SEN_model.git/': Recv failure: Connection was reset
```

解决方法：
- 可以尝试添加 user 选项的 name 和 email config 信息
- 网络问题，可尝试重启电脑



---

## 问题 3

```bash
fatal: unable to access 'https://gitee.com/mirrors/oh-my-zsh.git/': Failed to connect to 172.22.240.1 port 10811 after 132492 ms: Connection timed out
```

解决方法：可以修改 git 的代理
```bash
git config --global http.proxy ""
git config --global https.proxy ""
```



---

## `git commit` 提交者信息填错

```bash
git commit --amend --author='Author Name <email@address.com>'

# 可能需要设置文本编辑器
git config --global core.editor vim
```

显示 git 配置文件的路径
```bash
git config --list --show-origin
```



---

## 其他问题

- github 和 gitee 中的 md 文档无法渲染 `\begin{}` 等 LaTeX 命令
- github 可以渲染 Front-Matter，gitee 暂不行
