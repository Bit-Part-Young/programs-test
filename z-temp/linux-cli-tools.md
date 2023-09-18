---
title: Linux终端工具
top: false
cover: false
toc: true
mathjax: true
summary: Linux终端工具
tags:
  - Linux
categories:
  - 科研工具
password:
---

# 介绍

>[GitHub - ibraheemdev/modern-unix: A collection of modern/faster/saner alternatives to common unix commands.](https://github.com/ibraheemdev/modern-unix)


终端工具安装方式：
- Linux 端：ubuntu（apt、snap 等）、archlinux(pacman、yay 等)；
- Windows 端：scoop；
- 程序端：Python（pip）、Rust（cargo）；
- web.sh 网站（后三者可以在无 root 权限情况下安装）；
- 源码编译
- …

>[webinstall.dev](https://webinstall.dev/)




---
---

# 常用终端工具

## zsh、ohmyzsh

>[GitHub - ohmyzsh/ohmyzsh: 🙃 A delightful community-driven (with 2,100+ contributors) framework for managing your zsh configuration. Includes 300+ optional plugins (rails, git, macOS, hub, docker, homebrew, node, php, python, etc), 140+ themes to spice up your morning, and an auto-update tool so that makes it easy to keep up with the latest updates from the community.](https://github.com/ohmyzsh/ohmyzsh)


oh-my-bash（没 zsh 好用）
>[GitHub - ohmybash/oh-my-bash: A delightful community-driven framework for managing your bash configuration, and an auto-update tool so that makes it easy to keep up with the latest updates from the community.](https://github.com/ohmybash/oh-my-bash)


windows terminal 以及 vscode 本地设置默认终端为 git bash
>[Windows Terminal添加Git Bash支持 - TruthHell - 博客园](https://www.cnblogs.com/cong-wang/p/15026535.html)
>[在 Windows 中使用 Bash shell | 北辞](https://northword.cn/code/bash-for-windows/)
>[Windows高效开发环境配置（一） | 北鱼扶摇](https://ifuyao.com/blog/install-zsh-and-oh-my-zsh-in-windows-git-bash/)



---

### Windows 端安装配置 zsh

两种方式：WSL+zsh，git bash+zsh
>[Windows高效开发环境配置（一） | 北鱼扶摇](https://ifuyao.com/blog/install-zsh-and-oh-my-zsh-in-windows-git-bash/)


- 下载 zsh 包
```bash
wget https://mirror.msys2.org/msys/x86_64/zsh-5.9-2-x86_64.pkg.tar.zst

tar --zstd -xvf zsh-5.9-2-x86_64.pkg.tar.zst

# 目录结构
├── .BUILDINFO
├── .INSTALL
├── .MTREE
├── .PKGINFO
├── etc
├── usr
```


- 复制 etc、usr 两个文件夹到 Git 安装目录中
- 打开 Git Bash，执行命令 `zsh`
- 配置 zsh 为 Git Bash 的默认 shell，在在 `.bashrc` 添加
```bash
 # Enable zsh
 if [ -t 1 ]; then
    exec zsh
 fi
```

- 安装、配置 oh-my-zsh…
- 修改 windows terminal 的 settings.json
```json
{
    "$help": "https://aka.ms/terminal-documentation",
    "$schema": "https://aka.ms/terminal-profiles-schema",
    // ...
    // 添加项 默认启动为Git Bash
    "defaultProfile": "{5D1F95DF-36E8-56AD-C203-EA75CE06422C}",
    // "defaultProfile": "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",
    // ...
    "profiles": 
    {
        "defaults": 
        {
            "font": 
            {
                "face": "MesloLGM Nerd Font"
            }
        },
        "list": 
        [			
            // 添加项
	        {
                "guid" : "{5D1F95DF-36E8-56AD-C203-EA75CE06422C}",
                "name" : "Git Bash",
                "commandline" : "D:\\Scoop\\apps\\git\\current\\bin\\bash.exe --login -i",
                "icon" : "D:\\Scoop\\apps\\git\\current\\usr\\share\\git\\git-for-windows.ico",
                "startingDirectory": "C:\\Users\\SLY\\Desktop"
            },
            {
                "commandline": "%SystemRoot%\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
                "guid": "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",
                "hidden": false,
                "name": "Windows PowerShell",
                // 添加项
                "startingDirectory": "C:\\Users\\SLY\\Desktop"
            },
			// ...
        ],
    },
}

```



---

### Linux 端安装配置 zsh

```bash
# 安装 zsh
# ubuntu
sudo apt install zsh
# archlinux
sudo pacman -S zsh


# 安装 ohmyzsh
# github 源
# via curl
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
# cia wget
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# gitee 源
sh -c "$(curl -fsSL https://gitee.com/Devkings/oh_my_zsh_install/raw/master/install.sh)"
sh -c "$(wget https://gitee.com/Devkings/oh_my_zsh_install/raw/master/install.sh -O -)"


# 插件下载：自动补全、高亮、建议：zsh-completions、zsh-syntax-highlighting、zsh-autosuggestions
# 主题下载：powerlevel10k
# github 源
git clone https://ghproxy.com/https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM}/plugins/zsh-completions && git clone https://ghproxy.com/https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM}/plugins/zsh-autosuggestions && git clone https://ghproxy.com/https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM}/plugins/zsh-syntax-highlighting && git clone --depth=1 https://ghproxy.com/https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

# gitee 源
git clone https://gitee.com/yuhldr/zsh-syntax-highlighting.git ${ZSH_CUSTOM}/plugins/zsh-syntax-highlighting && git clone https://gitee.com/yuhldr/zsh-autosuggestions ${ZSH_CUSTOM}/plugins/zsh-autosuggestions && git clone https://gitee.com/yuhldr/zsh-completions ${ZSH_CUSTOM}/plugins/zsh-completions && git clone --depth=1 https://gitee.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k


# 备份~/.zshrc（如果有）
cp ~/.zshrc ~/.zshrc.bak

# 更新oh-my-zsh
omz update

# 配置powerlevel10k
p10k configure

```

>[oh\_my\_zsh\_install: oh my zsh 国内Gitee源极速安装](https://gitee.com/Devkings/oh_my_zsh_install)


下载安装好 oh-my-zsh 和 powerlevel10k 后，在 `~/.zshrc` 文件中的 `ZSH_THEME` 改成 `ZSH_THEME="powerlevel10k/powerlevel10k"`，重新登陆，会进入配置 powerlevel10k 的交互，按照指示自定义设置即可。


默认 shell 修改
```bash
# 查看 shell
cat /etc/shells

# 将 zsh 设为默认 shell
chsh -s /bin/zsh

# 重新恢复到 bash
chsh -s /bin/bash
```


oh-my-zsh 有用的内置与外置插件
>[Plugins · ohmyzsh/ohmyzsh Wiki · GitHub](https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins)

```bash
# 内置插件
z  # 强大的目录自动跳转命令，会记忆你曾经进入过的目录，用模糊匹配快速进入你想要的目录
git  # 丰富的git alias
extract  # extract 用于解压任何压缩文件，不必根据压缩文件的后缀名来记忆压缩软件
# x *.gz  使用 x 命令即可解压文件
sublime # 可以使用命令行打开sublime
vi-mode # 开启vi模式
colored-man-pages  # 给你带颜色的 man 命令
safe-paste  # 防止粘贴进终端的多行代码直接执行
web-search  # 可以进行google bing baidu scholar等网页搜索
# 使用 google 关键字 
copypath  # copypath复制当前路径；copypath file/folder 复制文件和文件夹的路径
python  # py 运行python3； ipython 运行ipython
autopep8  # 检查python代码是否符合PEP 8规范；autopep8 file.py 


# 外置
autojump
zsh-syntax-highlighting
zsh-autosuggestions
zsh-completions
```



---

### 源码编译

服务器及超算平台需源码编译 zsh
>[https://jdhao.github.io/2018/10/13/centos_zsh_install_use/](https://jdhao.github.io/2018/10/13/centos_zsh_install_use/)

```bash
# 编译 ncurses
wget https://ftp.gnu.org/pub/gnu/ncurses/ncurses-6.4.tar.gz --no-check-certificate

./configure --prefix=$HOME/yangsl/src/ncurses CXXFLAGS="-fPIC" CFLAGS="-fPIC"

make -j && make install


# 编译zsh
wget https://sourceforge.net/projects/zsh/files/zsh/5.9/zsh-5.9.tar.xz/download -O zsh-5.9.tar.xz --no-check-certificate

./configure --prefix=$HOME/yangsl/src/zsh CPPFLAGS=-I$HOME/yangsl/src/ncurses/include LDFLAGS=-L$HOME/yangsl/src/ncurses/lib

make -j && make install

# 在~/.bashr_profile添加下面的命令，并source（无root权限），登录启用zsh
# 有root权限：chsh -s /bin/zsh 
# 不建议
export PATH=$HOME/yangsl/bin:$PATH
export SHELL=`which zsh`
[ -f "$SHELL" ] && exec "$SHELL" -l
```



---

### 一些问题

- zsh 中的 `[nyae]` 的含义：
>[What does [nyae] mean in Zsh? - Stack Overflow](https://stackoverflow.com/questions/800182/what-does-nyae-mean-in-zsh)


- zsh 安装后，可能会出现 Home / End 失灵问题，虽然可以通过配置解决（并不能完全解决），建议还使用对应的快捷键：Home = Ctrl + A，End = Ctrl + E。




---
---

## rich

>[GitHub - Textualize/rich: Rich is a Python library for rich text and beautiful formatting in the terminal.](https://github.com/Textualize/rich)


```bash
pip install rich
```



---

## ripgrep

>[GitHub - BurntSushi/ripgrep: ripgrep recursively searches directories for a regex pattern while respecting your gitignore](https://github.com/BurntSushi/ripgrep)

```bash
sudo pacman -S ripgrep

sudo apt install ripgrep
```

>可执行文件名为 `rg`



---

## fzf

>[GitHub - junegunn/fzf: :cherry\_blossom: A command-line fuzzy finder](https://github.com/junegunn/fzf)


```bash
sudo pacman -S fzf

sudo apt install fzf
```



---

## exa

>[GitHub - ogham/exa: A modern replacement for 'ls'.](https://github.com/ogham/exa)

替代 ls



---

## lsd

>[GitHub - lsd-rs/lsd: The next gen ls command](https://github.com/lsd-rs/lsd)

替代 ls

二进制文件下载
```bash
wget https://github.com/lsd-rs/lsd/releases/download/v1.0.0/lsd-v1.0.0-x86_64-unknown-linux-gnu.tar.gz
```



---

## lazygit

>[GitHub - jesseduffield/lazygit: simple terminal UI for git commands](https://github.com/jesseduffield/lazygit)




---

## lazyvim

>[GitHub - LazyVim/LazyVim: Neovim config for the lazy](https://github.com/LazyVim/LazyVim)


```bash
# required
mv ~/.config/nvim{,.bak}

# optional but recommended
mv ~/.local/share/nvim{,.bak}
mv ~/.local/state/nvim{,.bak}
mv ~/.cache/nvim{,.bak}

git clone https://ghproxy.com/https://github.com/LazyVim/starter ~/.config/nvim
```

>无法 siyuan 使用



---

## tldr

>[GitHub - tldr-pages/tldr: 📚 Collaborative cheatsheets for console commands](https://github.com/tldr-pages/tldr)

```bash
pip install tldr
```



---

## ncdu

---

## bat

---

## neofetch

>[GitHub - dylanaraps/neofetch: 🖼️ A command-line system information tool written in bash 3.2+](https://github.com/dylanaraps/neofetch)

显示设备信息



---

## frogmouth

>[GitHub - Textualize/frogmouth: A Markdown browser for your terminal](https://github.com/Textualize/frogmouth)

linux 端渲染 markdown 文档



---

## glow

>[GitHub - charmbracelet/glow: Render markdown on the CLI, with pizzazz! 💅🏻](https://github.com/charmbracelet/glow)

linux 端渲染 markdown 文档



---

## thefuck

>[GitHub - nvbn/thefuck: Magnificent app which corrects your previous console command.](https://github.com/nvbn/thefuck)


```bash
sudo pacman -S thefuck

pip install thefuck

# in ~/.zshrc ~/.bashrc
eval $(thefuck --alias)
```



---

## difftastic

文件对比

>[GitHub - Wilfred/difftastic: a structural diff that understands syntax 🟥🟩](https://github.com/Wilfred/difftastic)


```bash
sudo pacman -S difftastic
```



---

## procs

---

## 美化工具

>[40个超有趣的Linux命令行彩蛋和游戏.md](https://github.com/TommyZihao/Zihao-Blog/blob/master/40%E4%B8%AA%E8%B6%85%E6%9C%89%E8%B6%A3%E7%9A%84Linux%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%BD%A9%E8%9B%8B%E5%92%8C%E6%B8%B8%E6%88%8F.md)


- cowsay、sl、fortune（幸运饼干；格言）
- lolcat、figlet、boxes、cmatrix、asciiquarium

```bash
sudo pacman -S which zsh git wget sudo 
sudo pacman -S neofetch glow bat fd 

# 终端美化用 
sudo pacman -S fortune cowsay lolcat figlet boxes cmatrix asciiquarium sl
```


- silicon：将源代码生成美观图片
>[GitHub - Aloxaf/silicon: Create beautiful image of your source code.](https://github.com/Aloxaf/silicon)

- carbon：同上
>[GitHub - carbon-app/carbon: :black\_heart: Create and share beautiful images of your source code](https://github.com/carbon-app/carbon)
