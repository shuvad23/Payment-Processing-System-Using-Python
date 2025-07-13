from rich.progress import Progress
import time

with Progress() as progress:
    task=progress.add_task("Processing...",total=100)
    for i in range(100):
        time.sleep(0.05)
        progress.update(task,advance=1)


