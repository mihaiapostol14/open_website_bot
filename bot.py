import json
import os

import pyautogui

from helper import (
    Helper,
    browser_info,
    get_html_links
)

pyautogui.PAUSE = 2
pyautogui.FAILSAFE = False

class Bot(Helper):
    def __init__(self, file_source=''):
        self.file_source = file_source

        self.start_browser()

    def open_site(self):
        for url in self.read_json_data(key='links_list'):
            self.random_pause_code(start=1, stop=5)
            pyautogui.write(url)
            pyautogui.press('enter')
            self.random_pause_code(start=1, stop=5)
            pyautogui.hotkey('ctrl','t')



    def start_browser(self):
        try:
            os.startfile(self.read_json_data(key='browser_info'))
            self.open_site()
        except TypeError:
            self.add_data_to_json()


    def read_json_data(self, key=''):

        if os.path.exists('settings/settings.json'):
            with open(file='settings/settings.json', mode='r') as file:
                source = json.load(file)[key]
                return source

        return self.add_data_to_json()

    def read_text_file(self):
        try:
            if os.path.exists(self.file_source):
                with open(file=self.file_source, mode='r') as file:
                    source = file.read().split()
                    return source

        except (FileNotFoundError, FileExistsError):
            print(f'Check path to file {self.file_source}')

    def check_filetype(self):
        match self.file_source.split('.')[1]:
            case 'txt':
                return self.read_text_file()
            case 'html':
                return get_html_links(src=self.file_source)

    def add_data_to_json(self):
        try:
            self.create_directory(name_directory='settings')
            json_dict = {
                'browser_info': browser_info(),
                'links_list': self.check_filetype()
            }

            with open(file='settings/settings.json', mode='w') as file:
                json.dump(json_dict, file, indent=4)
        except KeyError as ex:
            print(ex)


def main():
    return Bot(file_source='')


if __name__ == '__main__':
    main()
