#!/bin/sh

#Gerar Arquivo dbml com a conexão com o banco 
dbdocs db2dbml postgres postgresql+psycopg://postgres:postgres@127.0.0.1:5432/fullstack_app -o database.dbml 

