---
Title: 如何处理SIGKILL信号
Tags: c
Category: 语言
Date: 2014-09-15 13:43
Slug: how-to-handle-sigkill
Subtitle: 
Summary: 
Keywords:
---

# 问题
众所周知（参考[Wikipedia的说明][wiki]），SIGKILL是不能被进程捕获的，既然不能捕获，那么当前进程是无法在收到SIGKILL之后执行指定代码的。
但是在某些时候，我们又需要做一些处理，例如用户通过kill命令直接杀死了进程，我们还是想要一些指定的清理工作被执行。

# 办法
既然被杀死的进程无法处理SIGKILL，那么可以考虑让这些清理工作由别的进程来执行。
所谓的“别的进程”事实上就是一个监控进程。例如，可以在固定的位置创建一个domain socket，监控进程监听此socket， 被监控的进程则打开此socket。
当某个被监控进程退出时，这个socket会被关闭，而监控进程可以监测到此现象，从而执行清理工作。

[wiki]: https://en.wikipedia.org/wiki/Signal_(IPC)
