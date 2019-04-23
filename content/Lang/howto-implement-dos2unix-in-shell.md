---
Title: 如何通过shell实现dos2unix的功能
Tags: dos2unix, shell
Category: 语言
Date: 2014-11-03 14:35
Slug: how-to-implement-dos2unix-in-shell
Subtitle: 
Summary: 
Keywords:
---

有些服务器上没有安装dos2unix，但是又没有权限去安装。实际上可以通过sed命令实现dos2unix的功能。

- dos2unix即

  ```bash
  sed -i 's/^M//g' 文件名
  ```
  
- unix2dos即

  ```bash
  sed -i 's/$/^M/g' 文件名
  ```
  
*注意：`^M`的输入方式是先输入Ctrl+v，然后输入Ctrl+m*