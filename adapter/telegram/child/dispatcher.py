from factory.dispatcher_factory import create_dispatcher



def get_dispatcher(bot_id:int,config:dict):
    return create_dispatcher(bot_id,config)