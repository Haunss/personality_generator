import rich
import sys


rich.print("[bold red]██████╗░███████╗██████╗░░██████╗░█████╗░███╗░░██╗░█████╗░██╗░░░░░██╗████████╗██╗░░░██╗[/bold red]")
rich.print("[bold red]██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗████╗░██║██╔══██╗██║░░░░░██║╚══██╔══╝╚██╗░██╔╝[/bold red]")
rich.print("[bold red]██████╔╝█████╗░░██████╔╝╚█████╗░██║░░██║██╔██╗██║███████║██║░░░░░██║░░░██║░░░░╚████╔╝░[/bold red]")
rich.print("[bold red]██╔═══╝░██╔══╝░░██╔══██╗░╚═══██╗██║░░██║██║╚████║██╔══██║██║░░░░░██║░░░██║░░░░░╚██╔╝░░[/bold red]")
rich.print("[bold red]██║░░░░░███████╗██║░░██║██████╔╝╚█████╔╝██║░╚███║██║░░██║███████╗██║░░░██║░░░░░░██║░░░[/bold red]")
rich.print("[bold red]╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝╚═╝░░░╚═╝░░░░░░╚═╝░░░[/bold red]")
print(" ")
rich.print("[cyan]    ░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░[/cyan]")
rich.print("[cyan]    ██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗[/cyan]")
rich.print("[cyan]    ██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝[/cyan]")
rich.print("[cyan]    ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗[/cyan]")
rich.print("[cyan]    ╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║[/cyan]")
rich.print("[cyan]    ░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝[/cyan]")

__version__=str(open(".version","r").read())

rich.print("[red]                                     By Hauns[/red]")
rich.print("[red]                                     Version: [/red]"+__version__)


rich.print("[bold blue]Choose language[/bold blue]")
rich.print("[bold green][1]Русский\n[2]English\n[3]Deutsch[/bold green]")
lang=input()

if lang=="1":

	try:
		from faker import Faker
		from colorama import Fore, Style
	except ImportError:
		rich.print("[red]Некоторые пакеты не установлены![/red]")
		print(
			"Напишите `pip3 install -r requirements.txt` \nчтобы "
			" установить все необходимые пакеты")
		sys.exit(1)

	rich.print("[red]\nВнимание! Все данные сгенерированы случайным образом, и все совпадения в реальной жизни являются случайными. Скрипт предназначен исключательно в озакомительных целях! Автор не несёт ответственность за ваши действия![/red]")	

	rich.print("\n[green][1]Сгенерировать личность[/green]")
	rich.print("[green][2]Проверка обновлений[/green]")
	rich.print("[green][3]Автор[/green]")
	rich.print("[bold white]\tВведите число[/bold white]")

	option=str(input())

	if option=="1":
		fake=Faker('ru_RU')
		rich.print("[bold blue]Имя: [/bold blue]"+str(fake.name()))
		rich.print("[bold blue]Профессия: [/bold blue]"+str(fake.job()))
		rich.print("[bold blue]Адрес: [/bold blue]"+str(fake.address()))
		rich.print("[bold blue]Дата рождения: [/bold blue]"+str(fake.date_of_birth()))
		rich.print("[bold blue]Цвет волос: [/bold blue]"+str(fake.color_name()))
		rich.print("[bold blue]Банк: [/bold blue]"+str(fake.bank()))
		rich.print("[bold blue]Номер телефона: [/bold blue]"+str(fake.phone_number()))
		rich.print("[bold blue]Компания: [/bold blue]"+str(fake.company()))
	
	elif option=="2":
		rich.print("[cyan]В разработке[/cyan]")

	elif option=="3":
		rich.print("[cyan]Скрипт сделан Hauns[/cyan]")
		rich.print("[cyan]GitHub:https://github.com/Haunss[/cyan]")
		rich.print("[cyan]VK:https://github.com/Haunss[/cyan]")

	else:
		rich.print("[red]Введено неверное число![/red]")

elif lang=="2":
	try:
		from faker import Faker
		from colorama import Fore, Style
	except ImportError:
		rich.print("[red]Some dependencies could not be imported (possibly not installed)![/red]")
		print(
			"Type `pip3 install -r requirements.txt` \nto "
			" install all required packages")
		sys.exit(1)

	rich.print("[red]Attention! All data is randomly generated and all matches in real life are random. The script is intended solely for educational purposes! The author is not responsible for your actions![/red]")	

	rich.print("\n[green][1]Generate personality[/green]")
	rich.print("[green][2]Check for updates[/green]")
	rich.print("[green][3]Autor[/green]")
	rich.print("[bold white]\tEnter the number[/bold white]")

	option=str(input())

	if option=="1":
		fake=Faker()
		rich.print("[bold blue]Name: [/bold blue]"+str(fake.name()))
		rich.print("[bold blue]Job: [/bold blue]"+str(fake.job()))
		rich.print("[bold blue]Addres: [/bold blue]"+str(fake.address()))
		rich.print("[bold blue]Date of birth: [/bold blue]"+str(fake.date_of_birth()))
		rich.print("[bold blue]Hair color: [/bold blue]"+str(fake.color_name()))
		rich.print("[bold blue]Phone: [/bold blue]"+str(fake.phone_number()))
		rich.print("[bold blue]Company: [/bold blue]"+str(fake.company()))
	
	elif option=="2":
		rich.print("[cyan]Coming soon...[/cyan]")

	elif option=="3":
		rich.print("[cyan]Script made by Hauns[/cyan]")
		rich.print("[cyan]GitHub:https://github.com/Haunss[/cyan]")
		rich.print("[cyan]VK:https://github.com/Haunss[/cyan]")

	else:
		rich.print("[red]Invalid number entered![/red]")

elif lang=="3":
	try:
		from faker import Faker
		from colorama import Fore, Style
	except ImportError:
		rich.print("[red]Einige Pakete sind nicht installiert![/red]")
		print(
			"Schreiben `pip3 install -r requirements.txt` \n "
			" um alle benötigten Pakete zu installieren")
		sys.exit(1)

	rich.print("[red]Beachtung! Alle Daten werden zufällig generiert und alle Übereinstimmungen im wirklichen Leben sind zufällig. Das Skript ist ausschließlich für Bildungszwecke bestimmt! Der Autor ist nicht verantwortlich für Ihre Handlungen![/red]")	

	rich.print("\n[green][1]Persönlichkeit generieren[/green]")
	rich.print("[green][2]nach Updates suchen[/green]")
	rich.print("[green][3]Autor[/green]")
	rich.print("[bold white]\tGeben Sie die Nummer ein[/bold white]")

	option=str(input())

	if option=="1":
		fake=Faker("de_DE")
		rich.print("[bold blue]Name: [/bold blue]"+str(fake.name()))
		rich.print("[bold blue]Beruf: [/bold blue]"+str(fake.job()))
		rich.print("[bold blue]Die Anschrift: [/bold blue]"+str(fake.address()))
		rich.print("[bold blue]Geburtsdatum: [/bold blue]"+str(fake.date_of_birth()))
		rich.print("[bold blue]Haarfarbe: [/bold blue]"+str(fake.color_name()))
		rich.print("[bold blue]Telefonnummer: [/bold blue]"+str(fake.phone_number()))
		rich.print("[bold blue]Gesellschaft: [/bold blue]"+str(fake.company()))
	
	elif option=="2":
		rich.print("[cyan]In Bearbeitung[/cyan]")

	elif option=="3":
		rich.print("[cyan]Skript von Hauns[/cyan]")
		rich.print("[cyan]GitHub:https://github.com/Haunss[/cyan]")
		rich.print("[cyan]VK:https://github.com/Haunss[/cyan]")

	else:
		rich.print("[red]Ungültige Nummer eingegeben![/red]")	

else:
	rich.print("[red]Invalid number entered![/red]")




