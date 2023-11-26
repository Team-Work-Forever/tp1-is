import curses


class Console():

    def __init__(self) -> None:
        self.start()

    def input(self, text: str):
        self.clear()
        self.dispose()
        value = input(text)        
        self.start()

        return value

    def start(self):
        self.stdscr = curses.initscr()
        # curses.cbreak()
        curses.noecho()
        self.stdscr.keypad(True)

    def reset(self):
        self.stdscr.clear()
        self.stdscr.refresh()
        curses.curs_set(1)

    def watch_key(self):
        return self.stdscr.getch()

    def clear(self):
        self.stdscr.clear()
    
    def refresh(self):
        self.stdscr.refresh()

    def log(self, text: str):
        self.stdscr.addstr(0, 0, text)

    def set_cursor(self, value: 0|1):
        curses.curs_set(value)

    def log_position(self, text: str, position: (int, int)):
        self.stdscr.addstr(position[0], position[1], text)

    def dispose(self):
        # curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

console = Console()