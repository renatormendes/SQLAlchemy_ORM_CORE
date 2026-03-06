import sqlalchemy as db

metadata = db.MetaData()

# Definição da tabela como objeto
tabela_cidades = db.Table(
	'cidades_core', metadata,
	db.Column('id', db.Integer, primary_key = True, autoincrement = True),
	db.Column('nome', db.String),
	db.Column('pais', db.String)
)