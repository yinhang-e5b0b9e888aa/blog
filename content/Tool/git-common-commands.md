---
Title: Git常用命令
Tags: git
Category: 工具
Date: 2013-04-30 15:32
Slug: git-common-commands
Subtitle: 
Summary: 
Keywords:
---
[TOC]

*除了`checkout`和`clean`命令，基本上不用担心代码丢失，因为有`reflog`，:)*

# 查看提交记录

```
git log --stat
git log -p
git log --decorate
git log --oneline
git log --graph
git log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short'
```

关于格式化输出的详细内容，参考[PRETTY FORMATS](https://git-scm.com/docs/pretty-formats)

# 使用别名简化命令输入

```
git config --global alias.log "log --graph --pretty=format:\
  '%Cred%h%Creset %C(yellow)%d%Creset %Cgreen%ad%Creset %C(bold blue)%an%Creset %n%B' --date=short"
```

# 查看已经add的修改

```
git diff --staged
```

# add的反操作

```
git reset HEAD <文件路径>
```

# 更新所有submodule

```
git submodule update --init --recursive
```

# 提交到远程服务器上的某个branch

```
git push <远端名称> <本地branch名称>:<远端branch名称>
```

# 删除远程服务器上的某个branch

```
git push <远端名称> --delete <远端branch名称>
```

# 修改远程服务器地址

```
git remote set-url <远端名称> <新URL>
```

# 为当前HEAD创建tag

```
git tag -a <tag名称> -m <描述>
```

# 为某个commit创建tag

```
git log -a <tag名称> <commit checksum>
```

# 创建patch

```
git format-patch <起始commit checksum>..<结束commit checksum> --stdout > <patch名称>
git format-patch -10 HEAD --stdout > <patch名称>
git format-patch -1 <commit checksum> --stdout > <patch名称>
git format-patch --relative=<目录名称> <起始commit checksum>..<结束commit checksum> --stdout > <patch名称>
```

# 使用patch

```
git apply <patch名称>
git am <patch名称>
```
