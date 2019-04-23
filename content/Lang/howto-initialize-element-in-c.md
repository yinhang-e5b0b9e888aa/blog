---
Title: 如何初始化C语言结构体或数组的指定元素
Tags: c
Category: 语言
Date: 2014-10-26 14:11
Slug: how-to-initialize-element-in-c
Subtitle: 
Summary: 
Keywords:
---

参考[Designated Initializers](https://gcc.gnu.org/onlinedocs/gcc/Designated-Inits.html)

```C
typedef struct {
    int a;
    char b[10];
} foo;

foo myFoo = {
    .a = 6,
    .b = "Mine"
};

foo myBar[] = {
    [2] = {.a = 2, .b = "2"},
    [6] = {.a = 6, .b = "6"},
};

static const char* error_to_string[] = {
    [0] = "No error",
    [1] = "Internal error",
};
```
