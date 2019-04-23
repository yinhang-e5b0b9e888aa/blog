---
Title: 如何使用pdb调试Python程序
Tags: pdb, python
Category: 工具
Date: 2015-01-10 11:23
Slug: howto-use-pdb-to-debug-python-program
Subtitle:
Summary:
Keywords:
---
[TOC]

pdb特别适合在Linux服务器上调试Python程序！

# 启动方法

## 从命令行启动

```
python -m pdb 程序文件名
```

## 从Emacs启动

在打开py文件的Emacs窗口输入`M-x pdb`，然后可通过`C-x 空格`在当前行设置断点

# 命令

*括号表示可选输入，例如输入`l`与输入`list`是相同的功能*

| 命令 | 功能 | 
| --- | --- | 
| `l(ist)` | 显示源代码 | 
| `b(reak) 行号` | 在某一行设置断电 | 
| `s(tep)` | 下一步（如果是函数则进入函数内部） |
| `n(ext)` | 下一步（如果是函数则执行完函数） |
| `c(ont(inue))` | 移动到函数开头 |
| `p 变量名` | 显示变量值 |
| `pp 变量名` | pretty-print变量 |
| `w(here)` | 打印堆栈 |
| `d(own)` | 跳转到堆栈下一帧 |
| `u(p)` | 跳转到堆栈上一帧 |
| `a(rgs)` | 打印当前函数的参数列表 | 