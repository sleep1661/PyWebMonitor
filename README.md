# PyWebMonitor
## 介绍
  * 一个可以定时监控网页任何数据的monitor
  * 当你所监控的数据达到预期值是就会发邮件给你指定的邮箱地址。

## 场景
  * 你可以用它监控火车余票
  * 你可以用它监控京东上你关注的商品的价格
  * 你可以用它监控股票数据
  * ...

## 使用
  首先，你要在```watchweb.ini```加入你要监控网页的配置数据。需要配置以下几个数据：
* ```url```   监控网页的url地址
* ```regex```   正则表达式，在网页信息中匹配你关注的数据信息，要监控的数据用"()"括起来
* ```condition```   
  * 条件表达式，使用的是python语法，需返回一个布尔值。
  * 如第一个监控数据大于50，则填写```info[0]>50```
  * ```info[n]```是固定写法，```n```是```regex```第几个监控数据，即第几个```()```
  * 当条件表达式为真时，会触发邮件发送
* ```mail_receiver```   收件人邮箱地址
* ```mail_msg```  邮件内容
* ```interval_seconds```  监控间隔时间（单位：秒）

## 环境
* python版本 2.7.9
* 设置环境变量--发送人、邮箱服务、账户以及密码
```
export WM_MAIL_SENDER="pywebmonitor@126.com"
export WM_MAIL_SMTPSERVER="smtp.126.com"
export WM_MAIL_USERNAME="pywebmonitor"
export WM_MAIL_PASSWORD="******"
```
 
## 依赖库
* openSSL
 * [openssl安装说明](http://elliott-shi.iteye.com/blog/1955408) 
* APScheduler
* gevent
 * 安装APScheduler和gevent
 ```
 easy_install APScheduler
 easy_install gevent
 ```

#部署运行
你可以跟我一样把它部署在亚马逊aws上运行，运行命令：```python monitor.py```
   
##有问题反馈
在使用中有任何问题，欢迎反馈给我，可以用以下联系方式跟我交流

* 邮件(sleep1661@126.com)
* QQ: 464915867
