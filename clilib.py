import os
import platform
from beautifultable import BeautifulTable
from pyfiglet import Figlet
from tqdm import tqdm
import time
from colorama import init, Fore, Back, Style

# Инициализация colorama для Windows
init(autoreset=True)


class SuperHackUI:
    def __init__(self):
        self.clear()


    def clear(self):
        """Очистка экрана"""
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        return self


    def ascii_text(self, text, font="standard", color=Fore.GREEN):
        """КРУТЫЕ ASCII-шрифты через pyfiglet"""
        try:
            f = Figlet(font=font)
            ascii_art = f.renderText(text)
            print(color + ascii_art)
        except:
            # Fallback на простой текст
            print(color + text)
        return self


    def progress_bar(self, iterable, desc="Processing...", color=Fore.CYAN):
        """Красивый прогресс-бар через tqdm"""
        return tqdm(iterable, desc=desc, ncols=80,
                    bar_format="{l_bar}%s{bar}%s{r_bar}" % (color, Style.RESET_ALL))


    def table(self, headers, data, title=None, style="default"):
        """Красивые таблицы через beautifultable"""
        table = BeautifulTable()
        table.columns.header = headers

        for row in data:
            table.rows.append(row)

        if title:
            print(Fore.CYAN + title + Style.RESET_ALL)
        print(table)
        return table


    def choice(self, question, options, color=Fore.YELLOW):
        """ПРОСТОЙ выбор из списка (наша лучшая функция!)"""
        print(color + question + Style.RESET_ALL)
        for i, option in enumerate(options, 1):
            print(f"  {i}. {option}")

        while True:
            try:
                choice = int(input(Fore.CYAN + "\nВведите номер: " + Style.RESET_ALL))
                if 1 <= choice <= len(options):
                    return choice - 1
                print(Fore.RED + f"Введите число от 1 до {len(options)}!")
            except ValueError:
                print(Fore.RED + "Пожалуйста, введите число!")


    def input(self, question, default="", color=Fore.CYAN):
        """Ввод текста"""
        prompt = f"{color}{question}"
        if default:
            prompt += f" [{default}]"
        prompt += ": " + Style.RESET_ALL

        result = input(prompt).strip()
        return result if result else default


    def yesno(self, question, color=Fore.LIGHTYELLOW_EX):
        """Да/Нет вопрос"""
        response = input(f"{color}{question} (y/n): " + Style.RESET_ALL).strip().lower()
        return response in ['y', 'н', 'yes', 'да']


# Глобальный экземпляр
ui = SuperHackUI()


# Короткие алиасы
def p(text, color=Fore.WHITE): print(color + text)


def br(lines=1): [print() for _ in range(lines)]


def choice(q, opts): return ui.choice(q, opts)