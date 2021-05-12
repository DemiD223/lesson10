from typing import List


class TVController:
    cur_ch = 0

    def __init__(self, channels: List):
        self.chs = channels

    def first_channel(self):
        self.cur_ch = 0
        return self.chs[self.cur_ch]

    def last_channel(self):
        self.cur_ch = len(self.chs) - 1
        return self.chs[self.cur_ch]

    def turn_channel(self, num):
        if num - 1 < len(self.chs):
            self.cur_ch = num - 1
            return self.chs[self.cur_ch]
        return self.last_channel()

    def next_channel(self):
        self.cur_ch += 1
        return self.turn_channel(self.cur_ch)

    def previous_channel(self):
        self.cur_ch -= 1
        if self.cur_ch < 0:
            return self.first_channel()
        return self.turn_channel(self.cur_ch)

    def current_channel(self):
        return self.chs[self.cur_ch]

    def is_exist(self, num: int) -> str:
        if num in range(len(self.chs)):
            return "Yes"
        return "No"

    def is_exist(self, name: str) -> str:
        if name in self.chs:
            return "Yes"
        return "No"
