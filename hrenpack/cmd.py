import os, ctypes, shutil, getpass
import platform
from datetime import datetime
from hrenpack.listwork import split_list
from typing import Union
from dataclasses import dataclass


# def return_filename(path: str, mode: str) -> Union[str, list]:
#     # fn - возвращает имя файла без расширения
#     # fr - возвращает имя файла с расширением
#     # pl - возвращает полный путь файла как список
#     # rs - возвращает расширение файла
#     if os.path.isfile(path):
#         pass
#     else:
#         raise FileNotFoundError('No such file or directory: ' + path)
#
#     if '/' in path:
#         path_list = path.split('/')
#     elif '\\' in path:
#         path_list = path.split('\\')
#     else:
#         path_list = path
#     filename = path_list[-1]
#     filename_list = filename.split('.')
#     for i in range(len(filename_list) - 2):
#         if i == 0:
#             filename_without_rs = filename_list[0]
#         else:
#             filename_without_rs = filename_without_rs + '.' + filename_list[i]
#
#     if mode == 'fn':
#         return filename_without_rs
#     elif mode == 'fr':
#         return filename
#     elif mode == 'pl':
#         return filename_list
#     elif mode == 'rs':
#         return filename_list[-1]
#     else:
#         raise ValueError('invalid mode: ' + mode)


def get_filename(path: str, raise_error: bool = True) -> str:
    if '/' in path:
        output = path.split('/')[-1]
    elif '\\' in path:
        output = path.split('\\')[-1]
    else:
        output = path

    if not os.path.isfile(path) and raise_error:
        raise FileNotFoundError('No such file: ' + path)
    else:
        return output


def get_extension(path: str, raise_error: bool = True) -> str:
    filename = get_filename(path, raise_error)
    return filename.split('.')[-1] if '.' in filename else ''


def get_path_without_filename(path: str, raise_error: bool = True):
    v85 = True
    if '/' in path:
        path_list = path.split('/')
        path_list.pop()
    elif '\\' in path:
        path_list = path.split('\\')
        path_list.pop()
    else:
        v85 = False
    output = split_list(path_list, '/') if v85 else ''
    if not os.path.isfile(path) and raise_error:
        raise FileNotFoundError('No such file: ' + path)
    else:
        return output


def get_path_and_filename(path: str, raise_error: bool = True):
    if raise_error and not os.path.isfile(path):
        raise FileNotFoundError('No such file: ' + path)
    return get_path_without_filename(path), get_filename(path)


def rename(path: str, new_filename: str):
    pwfn, filename = get_path_and_filename(path)
    if pwfn:
        new_path = f'{pwfn}/{new_filename}'
    else:
        new_path = new_filename
    os.rename(path, new_path)


def create_file(path: str):
    try:
        open(path, 'x').close()
    except FileExistsError:
        raise FileExistsError(f'[WinError 183] Невозможно создать новый файл, так как он уже существует: {path}')


def get_filename_without_extension(path: str, raise_error: bool = True) -> str:
    filename = get_filename(path, raise_error)
    fl = filename.split('.')
    fl.pop()
    return split_list(fl, '.')


def get_path_without_extension(path: str, raise_error: bool = True) -> str:
    filename = get_filename_without_extension(path, raise_error)
    pwfl = get_path_without_filename(path, raise_error)
    return f'{pwfl}/{filename}'


@dataclass
class FileNameInfo:
    path: str
    filename: str = ''
    extension: str = ''
    path_without_extension: str = ''
    path_without_filename: str = ''

    def __post_init__(self):
        self.filename = get_filename(self.path)
        self.extension = get_extension(self.path)
        self.path_without_extension = get_path_without_filename(self.path)
        self.path_without_filename = get_path_without_extension(self.path)


def delete_file(path: str):
    os.remove(path)


def create_file_exist(path: str, space: bool = True, return_filename_and_path: bool = False):
    if not os.path.isfile(path):
        new_path = path
    else:
        counter = 0
        separator = ' ' if space else ''
        pafn = get_path_without_extension(path, False)
        extension = get_extension(path)
        while True:
            new_path = f'{pafn}{separator}({counter}).{extension}'
            if os.path.isfile(new_path):
                counter += 1
            else:
                break

    create_file(new_path)

    if return_filename_and_path:
        return FileNameInfo(new_path)


def edit_time(year: int = -1, month: int = -1, day: int = -1, hour: int = -1, minute: int = -1,
              second: int = -1) -> None:
    now = datetime.now()
    if year < 0:
        year = now.year
    if month < 0:
        month = now.month
    if day < 0:
        day = now.day
    if hour < 0:
        hour = now.hour
    if minute < 0:
        minute = now.minute
    if second < 0:
        second = now.second

    os.system(f'date {year}.{month}.{day}')
    os.system(f'time {hour}:{minute}:{second}')


def is_admin() -> bool:
    return bool(ctypes.windll.shell32.IsUserAnAdmin())


def admin_error() -> None:
    if not is_admin():
        raise OSError("Перезапустите программу с правами администратора")


def admin_pause() -> None:
    if not is_admin():
        print("Перезапустите программу с правами администратора")
        input()


def admin_pause_exit() -> None:
    admin_pause()
    exit(1)


def remove_files_and_folders(*paths):
    for path in paths:
        if os.path.isfile(path):
            try:
                os.remove(path)
            except Exception as e:
                raise OSError(f"Не удалось удалить файл {path}: {e}")
        elif os.path.isdir(path):
            try:
                shutil.rmtree(path)
            except Exception as e:
                raise OSError(f"Не удалось удалить папку {path}: {e}")


def get_username() -> str:
    return getpass.getuser()


def android_path(path: str, domain: str, name: str) -> str:
    if platform.system() == 'Windows':
        return path
    return f'data/data/{domain}.{name}/files/app/{path}'


class AndroidPath:
    def __init__(self, domain: str, name: str):
        self.domain = domain
        self.name = name

    def __call__(self, path: str) -> str:
        if platform.system() == 'Windows':
            return path
        return f'data/data/{self.domain}.{self.name}/files/app/{path}'
