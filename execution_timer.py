from datetime import datetime

def execution_timer(func):
    """Mide el tiempo de ejecución de una función."""
    def wrapper(*args, **kargs):
        initial_time = datetime.now()
        func(*args, **kargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('Execution time :'+str(time_elapsed.total_seconds())+' seconds.')
    return wrapper



