from wtforms import Form
from wtforms.fields import StringField
from wtforms.widgets import TextArea

class FormularioComentario(Form):
    comment = StringField(u'Comment', widget=TextArea())
