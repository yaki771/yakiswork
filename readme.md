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

## 作业二：用Django编写简易云盘系统
