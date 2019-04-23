---
Title: 设置Git
Tags: git
Category: 工具
Date: 2013-03-20 12:35
Slug: git-config
Subtitle: 
Summary: 
Keywords:
---
[TOC]

使用Git的第一步应该进行全局的设置，针对某个别的库可以再进行单独设置（不加--global）

# 查看帮助

```
git config --help
```

# 设置用户信息

```
git config --global user.name "用户名"
git config --global user.email "邮件地址"
```

# 设置编辑器

```
git config --global core.editor "编辑器程序名"
git config --global merge.tool vimdiff
git config --global merge.conflictstyle diff3
git config --global mergetool.prompt false
```

`merge`设置使用vimdiff作为merge工具，熟练使用vimdiff会极大提高效率

## vimdiff的快捷键

| 快捷键 | 功能 | 
| --- | --- | 
| `:set number` | 在当前窗口显示行号 | 
| `:windo set number` | 在所有窗口显示行号 | 
| `ctrl + w,h,j,k,l` | 切换窗口 |
| `[c` | 移动到前一个diff |
| `]c` | 移动到后一个diff |
| `:diffget RE` | 使用远端（REMOTE）的修改 |
| `:diffget LO` | 使用本地（LOCAL）的修改 |
| `:diffget BA` | 使用基准（BASE）的修改 |

# 查看设置

```
git config --list
```