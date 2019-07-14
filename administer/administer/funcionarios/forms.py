from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, SelectField,
					 TextAreaField, RadioField, IntegerField)
from wtforms.validators import DataRequired, Length, Email


class funcionario_form(FlaskForm ):
	
	nome = StringField("Nome", validators=[DataRequired(message="Esse campo e obrigatorio"), Length(min=3, max=120, message="Tamanho minimo de 3 caracteres e maximo de 120!")])
	idade = IntegerField("Idade", validators=[DataRequired(message="Esse campo e obrigatorio")])
	email = StringField("Email", validators=[DataRequired(message="Esse campo e obrigatorio"), Length(min=3, max=120, message="Tamanho minimo de 3 caracteres e maximo de 120!"), Email()])
	setor = SelectField("Setor", validators=[DataRequired(message="Esse campo e obrigatorio")], choices=[("0", "Equipe administrativo"), ("1", "Desenvolvedor"), ("2", "Equipe projetos"), ("3", "Equipe RH"), ("4", "Equipe marketing"), ("5", "Equipe presidencia"), ("6", "Equipe Negocios")])
	submit = SubmitField("Novo Funcionario")

class pesquisa_func_form(FlaskForm):

	pesquisa = StringField("Digite o nome do funcionario")
	submit = SubmitField("Pesquisar")
