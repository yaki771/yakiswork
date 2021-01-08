作业
# 分布式系统与云计算课程报告
------------
[toc]
## 作业一：虚拟机相关操作
### 1.安装Ubuntu20.04服务器版
### 2.配置虚拟机网络为桥接

![Alt text](./1606896833837.png)
### 3.使用ifconfig命令查看虚拟主机地址
> **NAT**为虚拟机内部独立的网络（网关），为内网
> **桥接网络**虚拟机和主机在同一个网络中，在局域网中使用虚拟机，并且虚拟机对其他pc提供服务

基本命令：cd/sudo/apt/ifconfig等
![Alt text](./1606897289652.png)
### 4.host主机与guest主机的ping通
### 5.在guest主机中开通http server服务
#### （1）git clone对应仓库
以 https://github.com/zxuqian/html-css-examples 80 示例仓库为例
- **问题** 克隆失败
- **解决方法** 网络转换为NAT模式，并将服务开通在自己的目录下
#### （2）host主机网络服务接通
- **问题** host主机无法显示网址：未ping通
- **解决方法** 改变网络连接方式为“桥接网卡”，并更新一下,检查是否ping通
```  python
#更新网络# sudo ifconfig enp0s3 down up
sudo python3 -m http.server --directory html-css-examples 80
```
- **html页面展示** 
![Alt text](./1607072875144.png)
###6.阿里云服务器操作
####（1）访问到云主机http服务
####（2）申请域名


## 作业二：用Django编写简易云盘系统
### 1.环境搭建基础
（1）git下载、在github上建立仓库
产生密钥证书 ,并将公钥信息告诉服务器
```python
ssh-keygen
cat ~/.ssh/id_rsa.pub
```
![Alt text](./1608024052115.png)
（2）建立本地目录repos，将git仓库地址clone到文件中
```python
git clone  git@github.com:yaki771/yakiswork.git
#将内容提交到仓库中# 
git add.
#显示当前目录（更改）状态#
git status
#将本次修改提交到本地仓库中#
git commit -m "注释"
#将本次操作提交到远程仓库#
git push
```
(3)Django程序编写
```python
#django初始化#
django-admin startproject mysite
#查看初始化是否成功#
python3 manage.py runserver
#创建app：业务开发#
python manage.py startapp polls

```
开发应用程序：
i.创建数据模型model：确定数据库表的结构
无需提交的代码：*pyc
							   *.sqlit3(数据库)
								添加到.gitignore
	44'50
	打开mysite-settings，将app加入INSTALL_APP中
```python
#查看数据库#
sqlite3 
.open db.sqlit3
.tables
#数据库迁移，生成改变数据库结构的文件#
python3 manage.py makemigrations
```
ii.     