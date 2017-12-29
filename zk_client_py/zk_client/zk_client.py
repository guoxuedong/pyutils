from kazoo.client import KazooClient
from kazoo.retry import KazooRetry

__author__ = 'guoxuedong'

class ZkClient:
    def __init__(self, zk_addresses, zk_timeout_sec):
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

    def set_data(self, path, data):
        print "before ensure path"
        self.__zk_client.ensure_path(path)
        print "set"
        self.__zk_client.set(path, bytes(data))
        print "set done"


if __name__ == "__main__":
    zk_addresses = "localhost:2182"
    zk_timeout_sec = 20
    zk_client = ZkClient(zk_addresses, zk_timeout_sec)
    print "int done"

    zk_root = "/filecache_test/cluster_test"
    data = """
select_offset_max_retry=5
tolerate_one_erased_device_after_retry=3
jedis_pool_max=20
jedis_socket_timeout_ms=200
check_jedis_result_timeout_ms=30
redis_key_expire_sec=3600
redis_access_parallel=false
redis_access_thread_num=14
    """

    zk_client.set_data(zk_root, data)
    print "done"
