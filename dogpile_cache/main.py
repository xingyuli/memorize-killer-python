from dogpile.cache import make_region

region = make_region().configure(
    'dogpile.cache.redis',
    # in seconds
    expiration_time=30,

    # for more options, see: dogpile.cache.backends.redis RedisBackend
    arguments={
        # 
        'redis_expiration_time': 40
    }
)

@region.cache_on_arguments()
def load_user_info(user_id):
    return f'{user_id}: data to be continued ...'
