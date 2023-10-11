import rich.traceback
import rich
from rich.progress import track
import time

#rich.traceback.install()
#3 / 0

rich.get_console().clear()
rich.get_console().rule('My Script')
rich.get_console().print('Hello :smiley:, [bold magenta]World[/bold magenta]!')

for i in track(range(100)):
    time.sleep(0.1)

