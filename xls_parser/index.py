import pandas as pd
import json
import math as m

df = pd.read_excel('data/BD_Docentes.xlsx', header=0)


members = []



def getAreaReference(arg):
    switcher = {
        'SOCIO-HUMANÍSTICA': {
            'label': arg,
            'reference':'academic-areas/socio-humanistica'
        },
        'ADMINISTRATIVA': {
            'label': arg,
            'reference':'academic-areas/administrativa'
        },
        'BIOLÓGICA Y BIOMÉDICA': {
            'label': arg,
            'reference':'academic-areas/biologica-biomedica'
        },
        'TÉCNICA': {
            'label': arg,
            'reference':'academic-areas/tecnica'
        }
    }
    return switcher.get(arg, 'Invalid area')

def getDepartmentReference(arg):
    switcher = {
        'ARQUITECTURA Y ARTES':{
            'label': arg,
            'reference':'departments/arquitectura-artes'
        },
        'CIENCIAS BIOLÓGICAS':{
            'label': arg,
            'reference':'departments/ciencias-biologicas'
        },
        'CIENCIAS DE LA SALUD':{
            'label': arg,
            'reference':'departments/ciencias-salud'
        },
        'CIENCIAS EMPRESARIALES':{
            'label': arg,
            'reference':'departments/ciencias-empresariales'
        },
        'CIENCIAS DE LA COMPUTACIÓN Y ELECTRÓNICA':{
            'label': arg,
            'reference':'departments/ciencias-computacion-electronica'
        },
        'CIENCIAS DE LA COMUNICACIÓN':{
            'label': arg,
            'reference':'departments/ciencias-comunicacion'
        },
        'PSICOLOGÍA':{
            'label': arg,
            'reference':'departments/psicologia'
        },
        'QUÍMICA Y CIENCIAS EXACTAS':{
            'label': arg,
            'reference':'departments/quimica-ciencias-exactas'
        },
        'GEOLOGÍA Y MINAS E INGENIERÍA CIVIL':{
            'label': arg,
            'reference':'departments/geologia-minas-ingenieria-civil'
        },
        'CIENCIAS JURÍDICAS':{
            'label': arg,
            'reference':'departments/ciencias-juridicas'
        },
        'ECONOMÍA':{
            'label': arg,
            'reference':'departments/economia'
        },
        'CIENCIAS DE LA EDUCACIÓN':{
            'label': arg,
            'reference':'departments/ciencias-educacion'
        }
    }
    return switcher.get(arg, 'Invalid dept')

def getSectionReference(arg):
    switcher = {
        'FILOSOFÍA Y TEOLOGÍA':{
            'label': arg,
            'reference':'sections/filosofia-teologia'
        },
        'LENGUAS CONTEMPORÁNEAS':{
            'label': arg,
            'reference':'sections/lenguas-contemporaneas'
        },
        'LENGUAS HISPÁNICAS Y LITERATURA':{
            'label': arg,
            'reference':'sections/lenguas-hispanicas-literatura'
        },
        'PEDAGOGÍA DE LAS CIENCIAS EXPERIMENTALES':{
            'label': arg,
            'reference':'sections/pedagogia-ciencias-experimentales'
        },
        'PSICOPEDAGOGÍA':{
            'label': arg,
            'reference':'sections/psicopedagogia'
        },
        'ARQUITECTURA Y URBANISMO':{
            'label': arg,
            'reference':'sections/arquitectura-urbanismo'
        },
        'ARTE, TEORÍA Y CONSERVACIÓN DEL PATRIMONIO':{
            'label': arg,
            'reference':'sections/arte-teoria-conservacion-patrimonio'
        },
        'BIOLOGÍA Y GENÉTICA':{
            'label': arg,
            'reference':'sections/biologia-genetica'
        },
        'BIOTECNOLOGIA Y PRODUCCION':{
            'label': arg,
            'reference':'sections/biotecnologia-produccion'
        },
        'CIENCIAS DE LA EDUCACIÓN BÁSICA':{
            'label': arg,
            'reference':'sections/ciencias-educacion-basica'
        },
        'CLÍNICO QUIRÚRGICA':{
            'label': arg,
            'reference':'sections/clinico-quirurgica'
        },
        'COMUNICACIÓN ORGANIZACIONAL':{
            'label': arg,
            'reference':'sections/comunicacion-organizacional'
        },
        'COMUNICACIÓN TECNOLOGIAS':{
            'label': arg,
            'reference':'sections/comunicacion-tecnologias'
        },
        'CONTABILIDAD Y AUDITORIA':{
            'label': arg,
            'reference':'sections/contabilidad-auditoria'
        },
        'DERECHO PRIVADO':{
            'label': arg,
            'reference':'sections/derecho-privado'
        },
        'DERECHO PÚBLICO':{
            'label': arg,
            'reference':'sections/derecho-publico'
        },
        'DESARROLLO ECONÓMICO':{
            'label': arg,
            'reference':'sections/desarrollo-economico'
        },
        'DISEÑO Y EXPRESIÓN ARTÍSTICA':{
            'label': arg,
            'reference':'sections/diseno-expresion-artistica'
        },
        'ECOLOGÍA Y SISTEMÁTICA':{
            'label': arg,
            'reference':'sections/ecologia-sistematica'
        },
        "ELECTRONICA Y TELECOMUNICACIONES": {
            'label': arg,
            "reference": "sections/electronica-telecomunicaciones",
        },
        "ESTRUCTURAS, TRANSPORTE Y CONSTRUCCION": {
            'label': arg,
            "reference": "sections/estructuras-transporte-construccion",
        },
        "EVALUACIÓN Y DIAGNÓSTICO PSICOLÓGICO": {
            'label': arg,
            "reference": "sections/evaluacion-diagnostico-psicologico",
        },
        "FILOSOFÍA Y TEOLOGÍA":{
            'label': arg,
            "reference": "sections/filosofia-teologia",
        },
        "FINANZAS Y GESTIÓN BANCARIA":{
            "label": arg,
            "reference": "sections/finanzas-gestion-bancaria"
        },
        "FISICOQUIMÍCA Y MATEMÁTICAS":{
            "label": arg,
            "reference": "sections/fisicoquimica-matematicas"
        },
        "GENÉTICA HUMANA, MICROBIOLOGÍA Y BIOQUÍMICA CLÍNICA":{
            "label": arg,
            "reference": "sections/genetica-humana-microbiologia-bioquimica-clinica"
        },
        "GEODINÁMICA, MINERÍA Y METALURGIA":{
            "label": arg,
            "reference": "sections/geodinamica-mineria-metalurgia"
        },
        "HOTELERÍA Y TURISMO":{
            "label": arg,
            "reference": "sections/hoteleria-turismo",
        },
        "INGENIERÍA AMBIENTAL":{
            "label": arg,
            "reference": "sections/ingenieria-ambiental",
        },
        "INGENIERÍA DE PROCESOS":{
            "label": arg,
            "reference": "sections/ingenieria-procesos"
        },
        "INGENIERÍA DE SOFTWARE Y GTI": {
            "label": arg,
            "reference": "sections/ingenieria-software-gti",
        },
        "INGENIERÍA ARTIFICIAL":{
            "reference": "sections/inteligencia-artificial",
            "label": arg,
        },
        "INTERVENCIÓN PSICOLÓGICA":{
            "reference": "sections/intervencion-psicologica",
            "label": arg,
        },
        "MANEJO Y GESTIÓN DE RECURSOS NATURALES":{
            "reference": "sections/manejo-gestion-recursos-naturales",
            "label": arg
        }, 
        "MÉTODOS CUANTITATIVOS":{
            "reference": "sections/metodos-cuantitativos",
            "label": arg
        },
        "NARRATIVAS AUDIOVISUALES":{
            "reference": "sections/narrativas-audiovisuales",
            "label": arg
        },
        "NUEVAS TENDENCIAS DEL DERECHO":{
            "reference": "sections/nuevas-tendencias-derecho",
            "label": arg
        },
        "ORGANIZACIÓN Y GESTIÓN EMPRESARIAL":{
            "reference": "sections/organizacion-gestion-empresarial",
            "label": arg
        },
        "PEDAGOGÍA DE LAS CIENCIAS EXPERIMENTALES":{
            "reference": "sections/pedagogia-las-ciencias-experimentales",
            "label": arg
        },
        "POLÍTICAS PÚBLICAS":{
            "reference": "sections/politicas-publicas",
            "label": arg
        },
        "PRECLÍNICA":{
            "reference": "sections/preclinica",
            "label": arg
        },
        "PSICOLOGÍA BÁSICA":{   
            "reference": "sections/psicologia-basica",
            "label": arg
        },
        "PSICOLOGÍA EVOLUTIVA":{
            "reference": "sections/psicologia-evolutiva",
            "label": arg
        },
        "PSICOPEDAGOGÍA":{
            "reference": "sections/psicopedagogia",
            "label": arg
        },
        "QUÍMICA BÁSICA Y APLICADA": {
            "reference": "sections/quimica-basica-aplicada",
            "label": arg
        },
        "RECURSOS HÍDRICOS":{
            "reference": "sections/recursos-hidricos",
            "label": arg
        },
        "SOCIOHUMANÍSTICA, SALUD PÚBLICA Y GESTIÓN EN SALUD":{
            "reference": "sections/sociohumanistica-salud-publica-gestion-en-salud",
            "label": arg
        },
        "TECNOLOGIAS AVANZADAS DE LA WEB Y SBC":{
            "reference": "sections/tecnologias-avanzadas-web-sbc",
            "label": arg
        },
        "TEORÍA ECONÓMICA":{
            "reference": "sections/teoria-economica",
            "label": arg
        }
    }
    return switcher.get(arg, 'Invalid section')


for index, row in df.iterrows():
    if(type(row['mail']) is str):
        level_fourth = [row['level_fourth']]
        level_third = [row['level_third']]
        

        temp = {
            "id": row['mail'],
            "ci":row['ci'],
            "mail":row['mail'],
            "area": getAreaReference(row['area']),
            "department":getDepartmentReference(row['department']),
            "displayName":row['displayName'],
            "level_fourth": level_fourth,
            "level_third": level_third,
            "modality": row['modality'],
            "section":getSectionReference(row['section'])
        }
        members.append(temp)

with open('users.json', 'w',encoding='utf8') as outfile:
    json.dump(members, outfile, ensure_ascii=False, indent=4)
