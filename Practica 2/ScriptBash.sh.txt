#!/usr/bin/bash

echo "[+] Estos son los archivos ocultos del directorio actual en adelante: "

find . -type f -printf "$f\t%p\t%u\t%g\t%m\n" | column -t