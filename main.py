#coding: utf-8


from academy.disciplina import Disciplina
from academy.aluno import Aluno
from academy.docente import Docente


jao = Aluno("Jão", "04/02/1934")
maria = Aluno("maria", "07/02/1934")
vantuil = Docente("Vantuil", "07/02/1934")

micro = Disciplina("Microprocessadores I", "Nabo", 48, "ELT005", vantuil)


micro.matricula = [jao, maria]
micro.avaliar([jao, maria])
print "%s nota: %d" % (jao.nome, jao.disciplina['media'])
print "%s nota: %d" % (maria.nome, maria.disciplina['media'])



# print "A disciplina %s sigla (%s) '%s' possui %d vagas" % (micro.nome, micro.sigla, micro.descricao, micro.vagas)

# micro.matricula = [jao, maria]

# print "Agora a disciplina %s sigla (%s) '%s' possui %d vagas" % (micro.nome, micro.sigla, micro.descricao, micro.vagas)

# micro.desmatricula(matricula = [jao.matricula, maria.matricula])

# print "Agora a disciplina %s sigla (%s) '%s' possui %d vagas" % (micro.nome, micro.sigla, micro.descricao, micro.vagas)

# print "E o professor é : %s" % micro.docente.nome
# print vantuil.disciplina