import curses

from utils.console import Console
from utils.menu.menu import Menu

class UnixMenu(Menu):

    DISTANCE_OFFSET = 2

    ENTER_KEY = 10
    ARROW_UP_KEY = 65
    ARROW_DOWN_KEY = 66
    SPACE_KEY = 32

    def __init__(self, title: str, options: list[str]) -> None:
        super().__init__(title, options)

        self.console = Console()

    def run(self) -> int:
        self.console.start()
        self.console.set_cursor(0)
        key = 0

        while key != ord(' '):
            self.console.clear()
            self.console.log(self.title)
            self.console.log_position("Press 'q' to quit. Press 'SPACE' to do something.", (4 + self.DISTANCE_OFFSET + len(self._options), 0))

            self.draw_another()

            key = self.console.watch_key()

            if key == curses.KEY_UP:
                self._selected_index -= 1
                if self._selected_index < 0:
                    self._selected_index = len(self._options) - 1
            elif key == curses.KEY_DOWN:
                self._selected_index += 1
                if self._selected_index > len(self._options) - 1:
                    self._selected_index = 0
            elif key == ord('q'):
                self.console.reset()
                return -1

        self.console.dispose()
        return self._selected_index

    def draw_another(self):
        for i in range(len(self._options)):
            if i == self._selected_index:
                self.console.log_position(f"{self._options[i]} <-", (i + self.DISTANCE_OFFSET, 10))
            else:
                self.console.log_position(f"{self._options[i]}", (i + self.DISTANCE_OFFSET, 10))