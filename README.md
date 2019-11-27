# halo-h2-replace

一键修改halo原生H2数据库中的博客地址

## 前言

使用[halo](https://github.com/halo-dev/halo)部署了个人博客。

租了两台云服务器，一台在香港（[http://lonsty.me](http://lonsty.me)），一台在上海（[http://cn.lonsty.me](http://cn.lonsty.me)），
香港这台国内连接不上，上海这台工作地方（国外网络）连接不上，所以就想两台都搭建上博客，但只更新一个博客，然后通过脚本定时同步到另一台上。

但是因为halo是前后端分离的框架，部分url是以绝对路径保存在数据库中，想要修改域名特别麻烦，当博客内容多了之后，修改起来几乎不可能。

所有写了这个小工具一键替换域名。

## 使用方式

#### 1. 安装依赖

```
git glone https://github.com/lonsty/halo-h2-replace.git
cd halo-h2-replace/
pip3 install --user -r requirements.txt 
```

#### 2. 一键替换

```
python3 h2_replace.py -o http://lonsty.me -n http://cn.lonsty.me --url=/home/allen/workspace/git/halo-h2-replace/halo
```

其中：
- o - 原博客地址
- n - 新博客地址
- url - `halo.mv.db`的路径

## 使用帮助

```
$ python3 h2_replace.py --help

Usage: h2_replace.py [OPTIONS]

  Replace the original host name with the new host name.

Options:
  -o, --ori-str TEXT  original host.
  -n, --new-str TEXT  new host name.
  --url TEXT          H2 JDBC url.  [default: ./halo]
  --h2jar TEXT        location of H2 jar.  [default: ./h2.jar]
  -u, --user TEXT     H2 database username.  [default: admin]
  -p, --passwd TEXT   H2 database password.  [default: 123456]
  --help              Show this message and exit.
```
