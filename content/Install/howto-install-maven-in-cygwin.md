---
Title: 在Cygwin中安装Maven
Tags: maven, cygwin
Category: 软件安装
Date: 2014-11-19 16:08
Slug: how-to-install-maven-in-cygwin
Subtitle:
Summary:
Keywords:
---

1\. 从[Maven官方网站][maven]下载二进制版本并解压，例如apache-maven-3.5.0-bin.tar.gz

2\. 链接Maven主程序到PATH下的某个目录，例如：

```
ln -s /cygdrive/*apache-maven-3.5.0/bin/mvn /usr/bin/mvn
```

3\. 从[Oracle官方网站][oracle]下载JDK并安装

有可能遇到安装窗口不显示的情况，那样默认不会安装JDK源代码。可以通过如下的命令行安装源代码：
```
jdk.exe /s ADDLOCAL="ToolsFeature,SourceFeature,PublicjreFeature"
```

4\. 链接JDK目录到/usr/java，例如：
```
ln -s /cygdrive/c/Program\ Files/Java/jdk1.8.0_31 /usr/java
```

5\. 设置JAVA_HOME
```
export JAVA_HOME=/usr/java
```

[maven]: http://maven.apache.org/download.cgi
[oracle]: http://www.oracle.com/technetwork/java/javase/downloads/index.html