# Autor: Christopher Gabriel Pedraza Pohlenz

# Libreria necesaria para hacer peticiones a paginas web
import requests

# Libreria que se usara para permitir los colores en la terminal
import os
os.system("color")

# Version actual del programa
VERSION = "3.0"

# Enlaces a los repositorios
UPDATER_REPO = "https://api.github.com/repos/christopher-pedraza/NAEVYS-updater/releases/latest"
NAEVYS_REPO = "https://api.github.com/repos/christopher-pedraza/NAEVYS/releases/latest"

# Colores para el texto
# Referencia:
# https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\x1b[1;32;40m'
NORMAL = '\033[0m'
RED = '\033[91m'
TITLE = '\x1b[6;36;40m'

# Aplica color que alterna brillo (brilla..deja de brillar..brilla) al titulo
print(TITLE)

# Texto creado con ayuda de https://www.messletters.com/en/big-text/
# usando el estilo alligator2
print("===============================================================================")
print(":::    ::: :::::::::  :::::::::      :::     ::::::::::: :::::::::: :::::::::  ")
print(":+:    :+: :+:    :+: :+:    :+:   :+: :+:       :+:     :+:        :+:    :+: ")
print("+:+    +:+ +:+    +:+ +:+    +:+  +:+   +:+      +:+     +:+        +:+    +:+ ")
print("+#+    +:+ +#++:++#+  +#+    +:+ +#++:++#++:     +#+     +#++:++#   +#++:++#:  ")
print("+#+    +#+ +#+        +#+    +#+ +#+     +#+     +#+     +#+        +#+    +#+ ")
print("#+#    #+# #+#        #+#    #+# #+#     #+#     #+#     #+#        #+#    #+# ")
print(" ########  ###        #########  ###     ###     ###     ########## ###    ### ")
print("===============================================================================")

# Aplica el estilo normal para quitar el brillo al resto de los textos
print(NORMAL)

# Obtiene el nombre (numero de version) del release mas reciente
current_version = requests.get(UPDATER_REPO).json()["name"]

# Si concuerdan las versiones, se procede a descargar los archivos de NAEVYS
if (current_version==VERSION):
	# Obtener el archivo JSON del ultimo release del repositorio
	response = requests.get(NAEVYS_REPO).json()

	# Se pregunta si se quiere descargar la nueva version
	print(RED + "\nThe latest version available of NAEVYS is '" +
		response["name"] + "'. Do you want to download it (y/n)? " +
		NORMAL, end="")
	ans = input()

	# Si el usuario desea descargar la nueva version
	if (ans == "y"):

		# Crea una lista con los datos de los assets (archivos del release)
		list = response["assets"]

		# Especifica al usuario la version que se esta actualizando
		print(CYAN + "\n\n   ~~~ NAEVYS Version '" + response["name"] + "' ~~~\n" + NORMAL)

		# Recorre la lista de los assets
		for asset in list:
			# Despliega el nombre del archivo
			print("Downloading '" + BLUE + asset["name"] + NORMAL + "'" + NORMAL, end=" .")
			# Obtiene el archivo a partir del enlace del asset
			file_dir = requests.get(asset["browser_download_url"])
			print(".", end="")
			# Crea el archivo
			open(asset["name"], "wb").write(file_dir.content)
			print(". ", end="")
			print(GREEN + "Finished." + NORMAL)

		# Espera un input para que no se cierre la terminal
		input(NORMAL + "\nPress <Enter> to continue...")

# Si las versiones no concuerda, ofrecer descargar el updater
else:
	# Se pregunta si se quiere descargar la nueva version
	print(RED + "\nA new version of the updater is available. " +
	 "Do you want to download it (y/n)? " + NORMAL, end="")
	ans = input()

	# Si el usuario desea descargar la nueva version
	if (ans == "y"):
		# Obtener el archivo JSON del ultimo release del repositorio
		response = requests.get(UPDATER_REPO).json()

		# Especifica al usuario la version que se esta actualizando
		print(CYAN + "\n\n   ~~~ Updater Version '" + response["name"] + "' ~~~\n" + NORMAL)

		# Crea una lista con los datos de los assets (archivos del release)
		list = response["assets"]

		# Recorre la lista de los assets
		for asset in list:
			# Al nombre del ejecutable le agrega la version del release
			file_name = asset["name"].replace(".exe", "_v" + response["name"] + ".exe")

			# Despliega el nombre del archivo
			print("Downloading '" + BLUE + file_name + NORMAL + "'" + NORMAL, end=" .")
			# Obtiene el archivo a partir del enlace del asset
			file_dir = requests.get(asset["browser_download_url"])
			print(".", end="")
			# Crea el archivo
			open(file_name, "wb").write(file_dir.content)
			print(". ", end="")
			print(GREEN + "Finished." + NORMAL)

		# Espera un input para que no se cierre la terminal
		input(NORMAL + "\nPress <Enter> to continue...")