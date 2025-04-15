# PHP proj

# Requisitos

- Servidor apache2
- Banco de dados MySQL

## Scripts

- `copy2www.sh` copia um arquivo para a pasta `/var/www/html/`
    - `./copy2www.sh -f <arquivo>`
    - `./copy2www.sh -d <diretório>`
- `copyservice.sh` faz o copy2www.sh todo vez que o arquivo é modificado
    - `./copyservice.sh -d <diretório>`

## Logs

O servidor apache logga os erros do servidor php em um arquivo.
Para ficar escutando os erros do server php: `sudo tail -f /var/log/apache2/error.log`. 