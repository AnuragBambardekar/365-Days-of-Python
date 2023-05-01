import os
import importlib
from typing import Any
from psutil import Process

# Reduces initial startup time - if user doesnt use a package then make it import "lazily"
# Tradeoff is that you need to know about the funictionalities of the package
# so need to know about numpy funtionalities here - no context actions provided by editor
# also increases complexity of the script & gets harder to keep track

def get_memory_usage() -> float:
    process: Process  = Process(os.getpid())
    megabytes: float = process.memory_info().rss / (1024*1024)
    return megabytes

class LazyImport:
    def __init__(self, module_name: str):
        self.module_name = module_name
        self.__module: Any | None = None
    
    def __getattr__(self,attr: str) -> Any:
        if self.__module is None:
            self.__module = importlib.import_module(self.module_name)
        return getattr(self.__module, attr)
    
def main():
    numpy: Any = LazyImport('numpy')

    while True:
        user_input: str = input('You: ')
        message_list: list[str] = user_input.split()

        if 'pi' in message_list:
            message:str = f'Bot: {numpy.pi}'
        else:
            message: str = f'Bot: {user_input}'

        memory_usage: float = get_memory_usage()
        print(f'{message}(Memory: {memory_usage:.2f}MB)')

if __name__ == '__main__':
    main()