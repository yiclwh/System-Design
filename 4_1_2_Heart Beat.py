"""
在Master-Slave结构模式中，slave端会每隔k秒向master端发送ping请求表示自己还在运行。
如果master端在 2 * k 秒内没有接收到任何来自slave的ping请求，那么master端会向管理员发送一个警告(比如发送一个电子邮件)。

现在让我们来模拟master端，你需要实现以下三个功能：
1.initialize(slaves_ip_list, k)，slaves_ip_list是所有slaves的ip地址列表，k为一个定值。
2.ping(timestamp, slave_ip)，这个方法在master端从slave端收到ping请求时执行，
  timestamp指当前的时间戳，slave_ip代表当前发送请求的slave端的ip地址
3.getDiedSlaves(timestamp)，这个方法会定期的(两次执行之间的时间间隔不确定)执行，
  timestamp代表当前的时间戳，此方法需要返回不再运行的slave端的所有ip地址列表，如果没有发现则返回空集合。

你可以假设当master端开始运行的时候时间戳为0，所有的方法都会根据全局的增长的时间戳来运行。


In the Master-Slave architecture, slave server will ping master in every k seconds to 
tell master server he is alive. If a master server didn't receive any ping request from 
a slave server in 2 * k seconds, the master will trigger an alarm (for example send an email) to administrator.

Let's mock the master server, you need to implement the following three methods:

    1. initialize(slaves_ip_list, k). salves_ip_list is a list of slaves' ip addresses. k is define above.
    2. ping(timestamp, slave_ip). This method will be called every time master received a ping request from 
    one of the slave server. timestamp is the current timestamp in seconds. 
    slave_ip is the ip address of the slave server who pinged master.
    3. getDiedSlaves(timestamp). This method will be called periodically 
    (it's not guaranteed how long between two calls). timestamp is the current 
    timestamp in seconds, and you need to return a list of slaves' ip addresses that died. 
    Return an empty list if no died slaves found.

You can assume that when the master started, the timestamp is 0, 
and every method will be called with an global increasing timestamp.

Example
    initialize(["10.173.0.2", "10.173.0.3"], 10)
    ping(1, "10.173.0.2")
    getDiedSlaves(20)
    >> ["10.173.0.3"]
    getDiedSlaves(21)
    >> ["10.173.0.2", "10.173.0.3"]
    ping(22, "10.173.0.2")
    ping(23, "10.173.0.3")
    getDiedSlaves(24)
    >> []
    getDiedSlaves(42)
    >> ["10.173.0.2"]

"""

class HeartBeat:

    def __init__(self):
        # initialize your data structure here
        self.slaves_ip_list = dict()


    # @param {str[]} slaves_ip_list a list of slaves'ip addresses
    # @param {int} k an integer
    # @return nothing
    def initialize(self, slaves_ip_list, k):
        # Write your code here
        self.k = k
        for ip in slaves_ip_list:
            self.slaves_ip_list[ip] = 0


    # @param {int} timestamp current timestamp in seconds
    # @param {str} slave_ip the ip address of the slave server
    # @return nothing
    def ping(self, timestamp, slave_ip):
        # Write your code here
        if slave_ip not in self.slaves_ip_list:
            return

        self.slaves_ip_list[slave_ip] = timestamp


    # @param {int} timestamp current timestamp in seconds
    # @return {str[]} a list of slaves'ip addresses that died
    def getDiedSlaves(self, timestamp):
        # Write your code here
        results = []
        for ip, time in self.slaves_ip_list.items():
            if time <= timestamp - 2 * self.k:
                results.append(ip)
        return results