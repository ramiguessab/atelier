import threading

class Thread(threading.Thread):
  def __init__(self, *args,**kwarg) -> None:
    super().__init__(*args,**kwarg)
    self.__is_stopped=threading.Event()
    
  def stop(self):
    self.__is_stopped.set()
  
  def stopped(self):
    return self.__is_stopped.is_set()
    
  @staticmethod
  def convert_multi_thread(func):
    def threaded_func(*args,**kwargs):
      def _func():
        func(*args,**kwargs)
        
      Thread(target=_func).start()
    
    return threaded_func