---
Title: 配置RHEL 7.3使用CentOS的源
Tags: linux
Category: 软件安装
Date: 2014-11-03 09:39
Slug: how-to-use-centos-repo-in-rhel
Subtitle:
Summary:
Keywords:
---

下面的步骤是配置RHEL 7.3使用网易的CentOS源，其他版本类似

1\. 下载Yum并安装

```
rpm -aq|grep yum|xargs rpm -e --nodeps
rpm -aq|grep python-iniparse|xargs rpm -e --nodeps
curl -o yum-3.4.3-150.el7.centos.noarch.rpm http://mirrors.163.com/centos/7.3.1611/os/x86_64/Packages/yum-3.4.3-150.el7.centos.noarch.rpm
curl -o python-iniparse-0.4-9.el7.noarch.rpm http://mirrors.163.com/centos/7.3.1611/os/x86_64/Packages/python-iniparse-0.4-9.el7.noarch.rpm
curl -o yum-metadata-parser-1.1.4-10.el7.x86_64.rpm http://mirrors.163.com/centos/7.3.1611/os/x86_64/Packages/yum-metadata-parser-1.1.4-10.el7.x86_64.rpm
curl -o yum-plugin-fastestmirror-1.1.31-40.el7.noarch.rpm http://mirrors.163.com/centos/7.3.1611/os/x86_64/Packages/yum-plugin-fastestmirror-1.1.31-40.el7.noarch.rpm
rpm -ivh *.rpm
``` 
    
2\. 编辑文件`/etc/yum.repos.d/rhel-debuginfo.repo`，加入以下内容

```
[base]
name=CentOS-$releasever - Base
baseurl=http://mirrors.163.com/centos/7.3.1611/os/$basearch/
gpgcheck=1
gpgkey=http://mirrors.163.com/centos/7.3.1611/os/x86_64/RPM-GPG-KEY-CentOS-7

[updates]
name=CentOS-$releasever - Updates
baseurl=http://mirrors.163.com/centos/7.3.1611/updates/$basearch/
gpgcheck=1
gpgkey=http://mirrors.163.com/centos/7.3.1611/os/x86_64/RPM-GPG-KEY-CentOS-7

[extras]
name=CentOS-$releasever - Extras
baseurl=http://mirrors.163.com/centos/7.3.1611/extras//$basearch/
gpgcheck=1
gpgkey=http://mirrors.163.com/centos/7.3.1611/os/x86_64/RPM-GPG-KEY-CentOS-7

[centosplus]
name=CentOS-$releasever - Plus
baseurl=http://mirrors.163.com/centos/7.3.1611/centosplus//$basearch/
gpgcheck=1
enabled=0
```

3\. 始设置生效

```
yum clean all
yum update
yum install epel-release
```
