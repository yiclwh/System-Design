"""
Implement a load balancer for web servers. It provide the following functionality:

    Add a new server to the cluster => add(server_id).
    Remove a bad server from the cluster => remove(server_id).
    Pick a server in the cluster randomly with equal probability => pick().

为网站实现一个负载均衡器，提供如下的 3 个功能：

添加一台新的服务器到整个集群中 => add(server_id)。
从集群中删除一个服务器 => remove(server_id)。
在集群中随机（等概率）选择一个有效的服务器 => pick()。

At beginning, the cluster is empty => {}.

    add(1)
    add(2)
    add(3)
    pick()
    >> 1         // the return value is random, it can be either 1, 2, or 3.
    pick()
    >> 2
    pick()
    >> 1
    pick()
    >> 3
    remove(1)
    pick()
    >> 2
    pick()
    >> 3
    pick()
    >> 3

"""

class LoadBalancer:
    
    def __init__(self):
        self.server_ids = []
        self.id2index = {}

    # @param {int} server_id add a new server to the cluster 
    # @return nothing
    def add(self, server_id):
        if server_id in self.id2index:
            return
        self.server_ids.append(server_id)
        self.id2index[server_id] = len(self.server_ids) - 1

    # @param {int} server_id remove a bad server from the cluster
    # @return nothing
    def remove(self, server_id):
        if server_id not in self.id2index:
            return
        
        # remove the server_id
        index = self.id2index[server_id]
        del self.id2index[server_id]
        
        # overwrite the one to be removed
        last_server_id = self.server_ids[-1]
        self.id2index[last_server_id] = index
        self.server_ids[index] = last_server_id
        self.server_ids.pop()

    # @return {int} pick a server in the cluster randomly with equal probability
    def pick(self):
        import random
        index = random.randint(0, len(self.server_ids) - 1)
        return self.server_ids[index]