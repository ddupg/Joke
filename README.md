# Joke #
利用一个百度的api获取笑话，并定时发送邮件。

- 运行之前需要更改settings.yaml文件中的个人邮箱信息。
- 发件人和收件人的邮箱都需要开启smtp服务，并需要发件人的smtp服务的口令，具体邮箱的开启方法请自行搜索。
- 收件人收到的邮件可能在垃圾箱里。

## settings.yaml ##
在settings文件中，记录程序运行所需要的配置信息。

注意：发件人邮箱密码并不是邮箱的登录密码，应该是邮箱的smtp服务的口令。

## utils.py ##
该文件中包含一些可能在其他类中需要使用的简单的工具函数。

- get_settings()：负责解析settings.yaml文件，将文件内容处理成字典格式返回。

## JokeGetter.py ##
JokeGetter类负责从api获取json格式的笑话，并处理成列表格式的数据返回。

## MailSender.py ##
MailSender类负责发送邮件。在1.0版本中，邮件内容只是纯文本内容。

