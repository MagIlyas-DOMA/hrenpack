from setuptools import setup

desc = '\n'.join(("Универсальная библиотека python для большинства задач", 'A universal python library for most tasks'))
req = '''soundfile==0.13.0
SpeechRecognition==3.14.0
requests>=2.32.3
screeninfo>=0.8.1
psutil>=6.1.1
bs4==0.0.2
beautifulsoup4==4.12.3
pyodbc==5.2.0'''.split('\n')

setup(
    name='hrenpack',  # Название вашей библиотеки
    version='0.1.0',  # Версия
    author_email='hrenpack@mail.ru',
    author='Маг Ильяс DOMA (MagIlyas_DOMA)',  # Авторы
    description=desc,  # Описание
    long_description=open('README.md').read(),  # Долгое описание (обычно из README)
    long_description_content_type='text/markdown',  # Формат долгого описания
    url='https://github.com/MagIlyas-DOMA/hrenpack',  # URL репозитория
    packages=['hrenpack'],  # Найдите пакеты автоматически
    license=open('LICENSE.md').read(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',  # Минимальная версия Python
    install_requires=req  # Зависимости
)
