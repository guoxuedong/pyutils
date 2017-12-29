from kazoo.client import KazooClient
from kazoo.retry import KazooRetry

class ZkClient:
    def __init__(self, zk_addresses, zk_timeout_sec=20):
        """
        :type zk_addresses: str
        :type zk_timeout_sec: int
        """
        self.__zk_addresses = zk_addresses
        self.__zk_timeout = zk_timeout_sec

        zk_retry = KazooRetry(max_tries=3, delay=1.0, ignore_expire=False)
        self.__zk_client = KazooClient(hosts=self.__zk_addresses, timeout=self.__zk_timeout,
                                       connection_retry=zk_retry)

        self.__zk_client.start(zk_timeout_sec)

    def list_redis_nodes(self, pool_path):
        if not self.__zk_client.exists(pool_path):
            print "path not exist:", pool_path

        redis_address = []
        redis_pool = self.__zk_client.get_children(path=pool_path)
        for redis_node in redis_pool:
            zk_redis_path = "%s/%s" % (pool_path, redis_node)
            zk_redis_address = self.__zk_client.get(zk_redis_path)
            redis_address.append("%s:%s" % (zk_redis_address[0], redis_node))
        redis_address.sort()
        return redis_address

    def close(self):
        self.__zk_client.stop()
        self.__zk_client.close()

if __name__ == "__main__":
    zk_addresses = "zk1.srv:2222,zk2.srv:2222"
    zk_pool_path = "/filecache_test/pool"

    print "zk:", zk_addresses
    print "path:", zk_pool_path

    zk_client = ZkClient(zk_addresses)
    redis_hosts = zk_client.list_redis_nodes(zk_pool_path)
    zk_client.close()

    for host in redis_hosts:
        print host


