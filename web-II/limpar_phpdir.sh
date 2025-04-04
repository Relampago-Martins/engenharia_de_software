#!/bin/bash
# Limpar o diretório PHP

PHP_DIR="/var/www/html"


# Verifica se o diretório existe
if [ -d "$PHP_DIR" ]; then
    # Remove todos os arquivos e subdiretórios dentro do diretório
    echo "Limpando o diretório $PHP_DIR..."
    sudo rm -rf "$PHP_DIR"/*
    echo "Diretório limpo com sucesso."
else
    echo "O diretório $PHP_DIR não existe."
fi
