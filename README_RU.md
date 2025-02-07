# hrenpack
#### [README in English](https://github.com/MagIlyas-DOMA/hrenpack/blob/main/README.md)
#### Универсальная библиотека python для большинства задач.

## Библиотека делится на несколько пакетов:  
`__init__` - основные функции и функции, которые не могут быть отнесены ни к одной категории  
`boolwork` - работа с булевыми значениями  
`classes` - классы  
`clipboard_work` - работа с буфером обмена  
`cmd` - работа с инструментам ОС  
`constants` - разные полезные константы
`date_and_time_work` - работа со значениями даты и времени  
`decorators` - декораторы  
`functionwork` - работа с функциями  
`gpswork` - работа с GPS  
`hashwork` - работа с хешированием  
`encapsulation` - полноценная инкапсуляция  
`kwargswork` - работа с **kwargs  
`listwork` - работа со списками, кортежами и словарями   
`network` - работа с интернетом  
`numwork` - работа с числами  
`print_color` - цветная консоль. Может работать не во всех консолях  
`resolution` - определение разрешения экрана  
`slugwork` - работа со slug, т. е. с строками, которые соответствуют правилам   
`strwork` - работа со строками  
`taskmgr` - работа с задачами  
`type_define` - определение, относятся ли данные к определнному типу, или нет  
`windows_registry` - работа с реестром Windows 

### Помимо пакетов, в hrenpack есть несколько подбиблиотек:  
`custom_methods` - дополнительные методы для уже существующих объектов   
`filework` - работа с файлами  
`framework` - дополнительные функции для уже существующих библиотек и фреймворков  

### Ресурсы:
В папке ресурсов находятся файлы ресурсов для корректной работы hrenpack

## Использование:
Данная библиотека распостраняется по 3-пунктной лицензии BSD

## Обновления
#### 1.1.x
###### 1.1.0
1. Удалены модули `dec_to_hex`, `dbwork`, `office` из-за их нестабильности
2. Удалена зависимости `pyodbc`
3. Добавлены зависимости `gps`, `bcrypt`
4. Удалены некоторые функции из модуля `__init__`  
Удалена из-за наличия ошибок 
###### 1.1.1
Исправлены ошибки версии 1.1.0 
