---
Title: 如何对某一个模块设置CFLAGS
Tags: gcc
Category: 工具
Date: 2014-10-12 10:32
Slug: how-to-specify-gcc-flags-particularly-for-a-specific-module
Subtitle: 
Summary: 
Keywords:
---

例如，需要对foo模块增加`-Wno-unused`标记

```
CFLAGS_FILE_foo += -Wno-unused
```
