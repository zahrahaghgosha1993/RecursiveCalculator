import redis


def get_redis_client():
    return redis.Redis(host='redis', db=0)