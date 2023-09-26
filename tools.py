import time

def benchmark_it(function, show_info = False):
    """
    wrapper / decorator function
    """
    def time_it(*args, **kwargs):
        st = time.time()

        func = function(*args, *kwargs)

        et = time.time()
        t = et-st
        if show_info: print(f"Čas potřebný k provedení funkce '{function.__name__}' byl {t}s. Výstup: {str(func)}")
        return (t, func)
    
    return time_it
