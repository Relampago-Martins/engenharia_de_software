-----------------------------------------------------------------------
-- SISTEMA DE USUARIOS
-----------------------------------------------------------------------

create table usuario (
    id serial not null,
    login varchar(30) not null unique,
    senha varchar(255) not null,
    nome varchar(255) not null,
    marca_nome varchar(40) not null
);


alter table usuario 
add constraint pk_usuario
primary key(id);

insert into usuario(login, senha, nome) values ('joao','123','João da Silva');
insert into usuario(login, senha, nome) values ('maria','123','Maria da Silva');


-----------------------------------------------------------------------
-- SISTEMA DE VEÍCULOS
-----------------------------------------------------------------------

create table marca(
    id serial not null,
    nome varchar(40) not null unique,
    descricao varchar(255) not null,
    primary key (id)
);

create table veiuculo (
    id serial not null,
    nome varchar(40) not null,
    ano integer not null,
    placa varchar(10) not null unique,
    cor varchar(20) not null,
    marca_id integer not null,
    primary KEY (id),
    FOREIGN KEY (marca_id) references marca(id)
);


insert into marca(id, nome, descricao) values (1, 'Fiat', 'Marca de veículos Fiat');
insert into marca(id, nome, descricao) values (2, 'Chevrolet', 'Marca de veículos Chevrolet');

insert into veiuculo(id, nome, ano, placa, cor, marca_id) values (1, 'Palio', 2010, 'ABC-1234', 'Vermelho', 1);
insert into veiuculo(id, nome, ano, placa, cor, marca_id) values (2, 'Celta', 2015, 'XYZ-5678', 'Preto', 2);
insert into veiuculo(id, nome, ano, placa, cor, marca_id) values (3, 'Uno', 2018, 'DEF-9012', 'Branco', 1);
insert into veiuculo(id, nome, ano, placa, cor, marca_id) values (4, 'Onix', 2020, 'GHI-3456', 'Prata', 2);
insert into veiuculo(id, nome, ano, placa, cor, marca_id) values (5, 'Fiorino', 2012, 'JKL-7890', 'Azul', 1);


