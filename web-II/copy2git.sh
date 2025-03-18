#!/bin/bash
# filepath: /home/bruno/git/engenharia_de_software/web-II/copy2git.sh

# Diretório de destino
TARGET_DIR="/home/bruno/git/engenharia_de_software/web-II/introducao"

# Verificar se o diretório de destino existe
if [ ! -d "$TARGET_DIR" ]; then
    echo "Criando diretório de destino $TARGET_DIR..."
    mkdir -p "$TARGET_DIR"
fi

# Copiar todos os arquivos e diretórios do diretório atual para o destino
echo "Copiando arquivos do diretório atual para $TARGET_DIR..."
cp -rv ./* "$TARGET_DIR" 2>/dev/null || true

# Verificar se a cópia foi bem-sucedida
if [ $? -eq 0 ]; then
    echo "Cópia concluída com sucesso!"
    echo "Arquivos copiados para: $TARGET_DIR"
    ls -la "$TARGET_DIR"
else
    echo "AVISO: Alguns arquivos podem não ter sido copiados. Verifique os erros acima."
fi