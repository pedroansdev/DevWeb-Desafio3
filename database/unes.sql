create database UNES;
use UNES;

create table contato(
    email varchar(50) not null,
	assunto varchar(60) not null,
	descricao varchar(300) not null
);

select * from contato;