try:
    from game.director import Director


    director = Director()
    director.start_game()
except ModuleNotFoundError:
    #informs user of an error and trys to log it
    print('\nError: Critical files not found or corrupted...\n')
    try:
        from game.error_logger import Error_logger
        ident = 'ModuleNotFoundError @ main.py'
        log_master = Error_logger()
        log_master.scribe(ident)
    except ModuleNotFoundError:
        print('Could not log error: File missing')
except ImportError:
    #informs user of an error and trys to log it
    print('\nError: Class or variable could not be retrieved from director.py...\n')
    try:
        from game.error_logger import Error_logger
        ident = 'ImportError @ main.py'
        log_master = Error_logger()
        log_master.scribe(ident)
    except ModuleNotFoundError:
        print('Could not log error: File missing')
