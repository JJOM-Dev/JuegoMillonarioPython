"""Juego de Historia Universal (interfaz gráfica en Python).

Esta versión ofrece una interfaz moderna con Tkinter, gestor de partidas,
confeti al acertar y categorías completas.
"""

from __future__ import annotations

import json
import random
import tkinter as tk
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from tkinter import messagebox, ttk

ARCHIVO_GUARDADO = Path("partidas_guardadas.json")


@dataclass
class Pregunta:
    enunciado: str
    opciones: list[str]
    respuesta: str
    retroalimentacion: str


@dataclass
class Categoria:
    nombre: str
    descripcion: str
    preguntas: list[Pregunta]


def cargar_categorias() -> list[Categoria]:
    return [
        Categoria(
            nombre="Antigüedad",
            descripcion="Civilizaciones iniciales, ciencia y cultura.",
            preguntas=[
                Pregunta(
                    "¿Cuál de estas civilizaciones se desarrolló junto al río Nilo?",
                    ["Mesopotamia", "Egipto", "China", "Grecia"],
                    "Egipto",
                    "Egipto creció gracias a las crecidas del Nilo.",
                ),
                Pregunta(
                    "¿Qué invento permitió registrar leyes y comercio?",
                    ["La escritura", "La brújula", "La pólvora", "La rueda"],
                    "La escritura",
                    "La escritura organizó la vida urbana.",
                ),
                Pregunta(
                    "¿En qué región surgió Mesopotamia?",
                    [
                        "Entre los ríos Tigris y Éufrates",
                        "En los Andes",
                        "En el Sahara",
                        "En la península Ibérica",
                    ],
                    "Entre los ríos Tigris y Éufrates",
                    "Mesopotamia significa 'entre ríos'.",
                ),
                Pregunta(
                    "¿Qué pueblo destacó por su comercio marítimo?",
                    ["Fenicios", "Mayas", "Aztecas", "Incas"],
                    "Fenicios",
                    "Los fenicios dominaron rutas comerciales.",
                ),
                Pregunta(
                    "¿Qué sistema político se consolidó en Atenas?",
                    ["Democracia", "Feudalismo", "Teocracia", "Monarquía absoluta"],
                    "Democracia",
                    "Atenas impulsó la democracia directa.",
                ),
                Pregunta(
                    "¿Qué imperio construyó la Vía Apia?",
                    ["Imperio Romano", "Imperio Persa", "Imperio Chino", "Imperio Otomano"],
                    "Imperio Romano",
                    "Roma expandió su red de calzadas.",
                ),
                Pregunta(
                    "¿Cuál fue un aporte científico de los griegos?",
                    ["Geometría", "Imprenta", "Electricidad", "Motor de combustión"],
                    "Geometría",
                    "Euclides destacó en geometría.",
                ),
                Pregunta(
                    "¿Qué río fue clave para la civilización del Indo?",
                    ["Indo", "Amazonas", "Danubio", "Nilo"],
                    "Indo",
                    "El Indo dio origen a esa civilización.",
                ),
                Pregunta(
                    "¿Qué imperio inició la Gran Muralla?",
                    ["China", "Roma", "Persia", "Egipto"],
                    "China",
                    "La Gran Muralla fue obra china.",
                ),
                Pregunta(
                    "¿Cuál fue la capital del Imperio Bizantino?",
                    ["Constantinopla", "Roma", "Atenas", "Alejandría"],
                    "Constantinopla",
                    "Constantinopla fue su centro político.",
                ),
                Pregunta(
                    "¿Qué estructura monumental eran tumbas reales en Egipto?",
                    ["Pirámides", "Zigurats", "Anfiteatros", "Catedrales"],
                    "Pirámides",
                    "Las pirámides guardaban a los faraones.",
                ),
                Pregunta(
                    "¿Qué código legal es uno de los más antiguos?",
                    ["Código de Hammurabi", "Código Napoleónico", "Leyes de Indias", "Fuero Juzgo"],
                    "Código de Hammurabi",
                    "Hammurabi dejó un código famoso.",
                ),
                Pregunta(
                    "¿Qué invento chino revolucionó la navegación?",
                    ["Brújula", "Telescopio", "Imprenta", "Motor a vapor"],
                    "Brújula",
                    "La brújula facilitó los viajes marítimos.",
                ),
                Pregunta(
                    "¿Qué civilización construyó Machu Picchu?",
                    ["Inca", "Maya", "Azteca", "Olmeca"],
                    "Inca",
                    "Machu Picchu es un legado inca.",
                ),
                Pregunta(
                    "¿Qué río permitió el desarrollo de la India antigua?",
                    ["Ganges", "Nilo", "Tigris", "Éufrates"],
                    "Ganges",
                    "El Ganges es sagrado y vital en India.",
                ),
                Pregunta(
                    "¿Qué ciudad fue enterrada por el Vesubio?",
                    ["Pompeya", "Roma", "Cartago", "Atenas"],
                    "Pompeya",
                    "Pompeya quedó sepultada en el año 79.",
                ),
                Pregunta(
                    "¿Cuál era el lenguaje de la antigua Roma?",
                    ["Latín", "Griego", "Hebreo", "Árabe"],
                    "Latín",
                    "El latín fue la lengua del Imperio Romano.",
                ),
                Pregunta(
                    "¿Qué dios era principal en la mitología egipcia?",
                    ["Ra", "Zeus", "Odín", "Anubis"],
                    "Ra",
                    "Ra era el dios del sol.",
                ),
                Pregunta(
                    "¿Qué civilización levantó Stonehenge?",
                    ["Britanos antiguos", "Mayas", "Persas", "Chinos"],
                    "Britanos antiguos",
                    "Stonehenge es una construcción megalítica.",
                ),
                Pregunta(
                    "¿Cuál fue uno de los primeros alfabetos?",
                    ["Fenicio", "Latino", "Cirílico", "Hebreo"],
                    "Fenicio",
                    "El alfabeto fenicio inspiró otros alfabetos.",
                ),
            ],
        ),
        Categoria(
            nombre="Edad Media",
            descripcion="Feudos, religiones y expansión cultural.",
            preguntas=[
                Pregunta(
                    "¿Qué sistema social dominó Europa medieval?",
                    ["Feudalismo", "Capitalismo", "Socialismo", "Democracia"],
                    "Feudalismo",
                    "El feudalismo estructuró la sociedad medieval.",
                ),
                Pregunta(
                    "¿Qué ruta comercial conectaba Europa con Asia?",
                    ["Ruta de la Seda", "Ruta del Ámbar", "Ruta del Inca", "Ruta del Oro"],
                    "Ruta de la Seda",
                    "La Ruta de la Seda unía Oriente y Occidente.",
                ),
                Pregunta(
                    "¿Qué ciudad fue capital del Imperio Carolingio?",
                    ["Aquisgrán", "París", "Roma", "Londres"],
                    "Aquisgrán",
                    "Carlomagno gobernó desde Aquisgrán.",
                ),
                Pregunta(
                    "¿Qué institución religiosa tuvo gran poder en la Edad Media?",
                    ["Iglesia", "Senado", "Parlamento", "Gremios"],
                    "Iglesia",
                    "La Iglesia fue central en la vida medieval.",
                ),
                Pregunta(
                    "¿Cómo se llamaban las comunidades de artesanos?",
                    ["Gremios", "Tribus", "Senados", "Ligas"],
                    "Gremios",
                    "Los gremios organizaban oficios urbanos.",
                ),
                Pregunta(
                    "¿Qué conflicto enfrentó a cristianos y musulmanes en Tierra Santa?",
                    ["Cruzadas", "Reconquista", "Guerra de los Cien Años", "Guerra Fría"],
                    "Cruzadas",
                    "Las cruzadas buscaron controlar Jerusalén.",
                ),
                Pregunta(
                    "¿Qué imperio se expandió desde Constantinopla?",
                    ["Bizantino", "Mongol", "Inca", "Azteca"],
                    "Bizantino",
                    "El Imperio Bizantino continuó a Roma.",
                ),
                Pregunta(
                    "¿Qué civilización construyó la Alhambra?",
                    ["Musulmanes", "Visigodos", "Francos", "Vikingos"],
                    "Musulmanes",
                    "La Alhambra es una joya andalusí.",
                ),
                Pregunta(
                    "¿Qué pandemia asoló Europa en el siglo XIV?",
                    ["Peste Negra", "Gripe Española", "Viruela", "Cólera"],
                    "Peste Negra",
                    "La Peste Negra redujo la población europea.",
                ),
                Pregunta(
                    "¿Quién fue un líder vikingo famoso?",
                    ["Erik el Rojo", "Julio César", "Napoleón", "Alejandro"],
                    "Erik el Rojo",
                    "Erik el Rojo exploró Groenlandia.",
                ),
                Pregunta(
                    "¿Qué ciudad italiana fue un centro comercial medieval?",
                    ["Venecia", "Madrid", "Berlín", "Lisboa"],
                    "Venecia",
                    "Venecia dominó rutas marítimas.",
                ),
                Pregunta(
                    "¿Qué imperio se originó en la península arábiga?",
                    ["Islámico", "Inca", "Romano", "Chino"],
                    "Islámico",
                    "El Islam se expandió rápidamente.",
                ),
                Pregunta(
                    "¿Qué rey inglés firmó la Carta Magna?",
                    ["Juan Sin Tierra", "Enrique VIII", "Ricardo III", "Eduardo I"],
                    "Juan Sin Tierra",
                    "La Carta Magna limitó al rey.",
                ),
                Pregunta(
                    "¿Qué estilo arquitectónico se usó en catedrales medievales?",
                    ["Gótico", "Barroco", "Neoclásico", "Moderno"],
                    "Gótico",
                    "El gótico destaca por sus vitrales.",
                ),
                Pregunta(
                    "¿Qué territorio recuperaron los reinos cristianos en España?",
                    ["Al-Ándalus", "Borgoña", "Sicilia", "Baviera"],
                    "Al-Ándalus",
                    "La Reconquista buscó recuperar Al-Ándalus.",
                ),
                Pregunta(
                    "¿Qué documento definió leyes en el reino visigodo?",
                    ["Fuero Juzgo", "Código Napoleónico", "Doce Tablas", "Código Hammurabi"],
                    "Fuero Juzgo",
                    "El Fuero Juzgo fue un código visigodo.",
                ),
                Pregunta(
                    "¿Qué orden militar protegía peregrinos?",
                    ["Templarios", "Espartanos", "Samuráis", "Legionarios"],
                    "Templarios",
                    "Los templarios fueron una orden militar.",
                ),
                Pregunta(
                    "¿Qué ciudad fue arrasada por los mongoles en 1258?",
                    ["Bagdad", "Roma", "París", "El Cairo"],
                    "Bagdad",
                    "Bagdad cayó ante los mongoles.",
                ),
                Pregunta(
                    "¿Qué país vivió la Guerra de los Cien Años?",
                    ["Francia e Inglaterra", "España y Portugal", "Rusia y Suecia", "Alemania y Italia"],
                    "Francia e Inglaterra",
                    "La guerra duró más de un siglo.",
                ),
                Pregunta(
                    "¿Qué universidad medieval es una de las más antiguas?",
                    ["Bolonia", "Harvard", "Oxford", "Salamanca"],
                    "Bolonia",
                    "Bolonia se fundó en el siglo XI.",
                ),
            ],
        ),
        Categoria(
            nombre="Renacimiento",
            descripcion="Arte, ciencia y exploraciones globales.",
            preguntas=[
                Pregunta(
                    "¿Qué artista pintó la Mona Lisa?",
                    ["Leonardo da Vinci", "Miguel Ángel", "Rafael", "Donatello"],
                    "Leonardo da Vinci",
                    "Da Vinci creó la Mona Lisa.",
                ),
                Pregunta(
                    "¿Qué invento permitió difundir libros masivamente?",
                    ["Imprenta", "Telescopio", "Brújula", "Motor"],
                    "Imprenta",
                    "Gutenberg impulsó la imprenta.",
                ),
                Pregunta(
                    "¿Qué ciudad italiana fue cuna del Renacimiento?",
                    ["Florencia", "Roma", "Venecia", "Milán"],
                    "Florencia",
                    "Florencia fue epicentro cultural.",
                ),
                Pregunta(
                    "¿Quién esculpió el David?",
                    ["Miguel Ángel", "Leonardo", "Botticelli", "Bernini"],
                    "Miguel Ángel",
                    "El David es una obra de Miguel Ángel.",
                ),
                Pregunta(
                    "¿Qué monarquía financió el viaje de Colón?",
                    ["España", "Portugal", "Francia", "Inglaterra"],
                    "España",
                    "Los Reyes Católicos apoyaron a Colón.",
                ),
                Pregunta(
                    "¿Qué océano cruzó Colón en 1492?",
                    ["Atlántico", "Índico", "Pacífico", "Ártico"],
                    "Atlántico",
                    "Colón cruzó el Atlántico.",
                ),
                Pregunta(
                    "¿Qué científico defendió el heliocentrismo?",
                    ["Copérnico", "Ptolomeo", "Galeno", "Aristóteles"],
                    "Copérnico",
                    "Copérnico propuso el Sol al centro.",
                ),
                Pregunta(
                    "¿Qué navegante dio la primera vuelta al mundo?",
                    ["Magallanes-Elcano", "Marco Polo", "Vespucci", "Da Gama"],
                    "Magallanes-Elcano",
                    "La expedición completó la circunnavegación.",
                ),
                Pregunta(
                    "¿Qué obra escribió Maquiavelo?",
                    ["El Príncipe", "Utopía", "La República", "Hamlet"],
                    "El Príncipe",
                    "Maquiavelo analizó el poder político.",
                ),
                Pregunta(
                    "¿Qué explorador llegó a la India rodeando África?",
                    ["Vasco da Gama", "Colón", "Caboto", "Pizarro"],
                    "Vasco da Gama",
                    "Da Gama abrió la ruta a Asia.",
                ),
                Pregunta(
                    "¿Qué civilización conquistó Hernán Cortés?",
                    ["Azteca", "Inca", "Maya", "Olmeca"],
                    "Azteca",
                    "Cortés conquistó Tenochtitlán.",
                ),
                Pregunta(
                    "¿Quién conquistó el Imperio Inca?",
                    ["Francisco Pizarro", "Colón", "Balboa", "Almagro"],
                    "Francisco Pizarro",
                    "Pizarro capturó a Atahualpa.",
                ),
                Pregunta(
                    "¿Qué pintor creó la Capilla Sixtina?",
                    ["Miguel Ángel", "Rafael", "Botticelli", "Tiziano"],
                    "Miguel Ángel",
                    "Miguel Ángel pintó la bóveda.",
                ),
                Pregunta(
                    "¿Qué movimiento religioso inició Lutero?",
                    ["Reforma", "Contrarreforma", "Humanismo", "Ilustración"],
                    "Reforma",
                    "Lutero inició la Reforma protestante.",
                ),
                Pregunta(
                    "¿Qué obra literaria escribió Dante?",
                    ["Divina Comedia", "Quijote", "Fausto", "Beowulf"],
                    "Divina Comedia",
                    "Dante escribió la Divina Comedia.",
                ),
                Pregunta(
                    "¿Qué artista pintó El nacimiento de Venus?",
                    ["Botticelli", "Caravaggio", "Da Vinci", "Giotto"],
                    "Botticelli",
                    "Botticelli pintó Venus.",
                ),
                Pregunta(
                    "¿Qué monarca impulsó la Contrarreforma?",
                    ["Carlos V", "Luis XIV", "Isabel I", "Pedro I"],
                    "Carlos V",
                    "Carlos V apoyó la Contrarreforma.",
                ),
                Pregunta(
                    "¿Qué instrumento mejoró Galileo?",
                    ["Telescopio", "Microscopio", "Brújula", "Reloj"],
                    "Telescopio",
                    "Galileo perfeccionó el telescopio.",
                ),
                Pregunta(
                    "¿Qué país lideró la exploración del Atlántico?",
                    ["Portugal", "Rusia", "Suecia", "Polonia"],
                    "Portugal",
                    "Portugal exploró rutas atlánticas.",
                ),
                Pregunta(
                    "¿Qué obra pintó Rafael en el Vaticano?",
                    ["La Escuela de Atenas", "Guernica", "Las Meninas", "La Última Cena"],
                    "La Escuela de Atenas",
                    "Rafael pintó La Escuela de Atenas.",
                ),
            ],
        ),
        Categoria(
            nombre="Revoluciones",
            descripcion="Cambios políticos, industriales y sociales.",
            preguntas=[
                Pregunta(
                    "¿Qué documento proclamó los derechos del hombre en 1789?",
                    ["Declaración de los Derechos del Hombre", "Carta Magna", "Constitución de Cádiz", "Bill of Rights"],
                    "Declaración de los Derechos del Hombre",
                    "La declaración fue clave en la Revolución Francesa.",
                ),
                Pregunta(
                    "¿Qué país lideró la Revolución Industrial?",
                    ["Inglaterra", "España", "Portugal", "Rusia"],
                    "Inglaterra",
                    "Inglaterra fue pionera industrial.",
                ),
                Pregunta(
                    "¿Qué máquina impulsó la industria textil?",
                    ["Spinning Jenny", "Telégrafo", "Imprenta", "Locomotora"],
                    "Spinning Jenny",
                    "La Spinning Jenny aumentó la producción.",
                ),
                Pregunta(
                    "¿Qué líder encabezó la independencia de Haití?",
                    ["Toussaint Louverture", "Bolívar", "San Martín", "Sucre"],
                    "Toussaint Louverture",
                    "Louverture lideró la revolución haitiana.",
                ),
                Pregunta(
                    "¿Qué evento inició la Revolución Francesa?",
                    ["Toma de la Bastilla", "Congreso de Viena", "Paz de Westfalia", "Tratado de Versalles"],
                    "Toma de la Bastilla",
                    "La toma de la Bastilla fue simbólica.",
                ),
                Pregunta(
                    "¿Quién lideró la independencia de EE.UU.?",
                    ["George Washington", "Abraham Lincoln", "Thomas Jefferson", "Benjamin Franklin"],
                    "George Washington",
                    "Washington comandó al ejército continental.",
                ),
                Pregunta(
                    "¿Qué imperio fue derrotado en la Revolución Americana?",
                    ["Británico", "Español", "Francés", "Portugués"],
                    "Británico",
                    "Las colonias vencieron al Imperio Británico.",
                ),
                Pregunta(
                    "¿Qué líder consolidó el poder tras la Revolución Francesa?",
                    ["Napoleón", "Robespierre", "Luis XVI", "Marat"],
                    "Napoleón",
                    "Napoleón se proclamó emperador.",
                ),
                Pregunta(
                    "¿Qué revolución ocurrió en 1917 en Rusia?",
                    ["Revolución Bolchevique", "Revolución Gloriosa", "Revolución Industrial", "Revolución Cultural"],
                    "Revolución Bolchevique",
                    "Los bolcheviques tomaron el poder.",
                ),
                Pregunta(
                    "¿Qué sistema económico defendía Karl Marx?",
                    ["Socialismo", "Mercantilismo", "Liberalismo", "Feudalismo"],
                    "Socialismo",
                    "Marx propuso el socialismo científico.",
                ),
                Pregunta(
                    "¿Qué fue la Comuna de París?",
                    ["Gobierno obrero", "Tratado", "Reforma agraria", "Movimiento religioso"],
                    "Gobierno obrero",
                    "La Comuna fue un gobierno popular.",
                ),
                Pregunta(
                    "¿Qué revolución inició en 1910 en México?",
                    ["Revolución Mexicana", "Revolución Cubana", "Revolución Gloriosa", "Revolución Verde"],
                    "Revolución Mexicana",
                    "La Revolución Mexicana cambió el país.",
                ),
                Pregunta(
                    "¿Qué líder mexicano impulsó la reforma agraria?",
                    ["Emiliano Zapata", "Porfirio Díaz", "Villa", "Madero"],
                    "Emiliano Zapata",
                    "Zapata defendió 'Tierra y libertad'.",
                ),
                Pregunta(
                    "¿Qué evento marcó el inicio de la independencia de Venezuela?",
                    ["19 de abril de 1810", "5 de julio de 1811", "Batalla de Carabobo", "Congreso de Angostura"],
                    "19 de abril de 1810",
                    "Fue el inicio del proceso independentista.",
                ),
                Pregunta(
                    "¿Qué batalla selló la independencia de Venezuela?",
                    ["Carabobo", "Boyacá", "Pichincha", "Junín"],
                    "Carabobo",
                    "Carabobo fue decisiva en 1821.",
                ),
                Pregunta(
                    "¿Qué documento firmó la independencia de Venezuela?",
                    ["Acta de 1811", "Constitución de 1830", "Grito de Dolores", "Tratado de Tordesillas"],
                    "Acta de 1811",
                    "El 5 de julio se firmó el Acta.",
                ),
                Pregunta(
                    "¿Qué revolución terminó en 1959 en Cuba?",
                    ["Revolución Cubana", "Revolución Gloriosa", "Revolución Industrial", "Revolución Cultural"],
                    "Revolución Cubana",
                    "Fidel Castro lideró la Revolución Cubana.",
                ),
                Pregunta(
                    "¿Qué líder cubano encabezó la revolución?",
                    ["Fidel Castro", "Che Guevara", "Batista", "Allende"],
                    "Fidel Castro",
                    "Fidel Castro lideró el movimiento.",
                ),
                Pregunta(
                    "¿Qué movimiento buscó abolir la esclavitud en el siglo XIX?",
                    ["Abolicionismo", "Mercantilismo", "Colonialismo", "Nacionalismo"],
                    "Abolicionismo",
                    "El abolicionismo luchó contra la esclavitud.",
                ),
                Pregunta(
                    "¿Qué tratado terminó la Primera Guerra Mundial?",
                    ["Tratado de Versalles", "Tratado de Utrecht", "Tratado de París", "Tratado de Viena"],
                    "Tratado de Versalles",
                    "Versalles se firmó en 1919.",
                ),
            ],
        ),
        Categoria(
            nombre="Siglo XX",
            descripcion="Guerras mundiales, tecnología y geopolítica.",
            preguntas=[
                Pregunta(
                    "¿Qué conflicto inició en 1914?",
                    ["Primera Guerra Mundial", "Guerra Fría", "Guerra de Crimea", "Guerra de los Cien Años"],
                    "Primera Guerra Mundial",
                    "La Primera Guerra Mundial inició en 1914.",
                ),
                Pregunta(
                    "¿Qué evento desencadenó la Primera Guerra Mundial?",
                    ["Asesinato de Sarajevo", "Revolución Rusa", "Tratado de Versalles", "Ataque a Pearl Harbor"],
                    "Asesinato de Sarajevo",
                    "El asesinato del archiduque fue la chispa.",
                ),
                Pregunta(
                    "¿Qué organización surgió tras la Segunda Guerra Mundial?",
                    ["ONU", "OTAN", "Unión Europea", "Liga Hanseática"],
                    "ONU",
                    "La ONU se fundó en 1945.",
                ),
                Pregunta(
                    "¿Qué país lanzó la bomba atómica en 1945?",
                    ["Estados Unidos", "Alemania", "Japón", "URSS"],
                    "Estados Unidos",
                    "EE.UU. lanzó bombas en Hiroshima y Nagasaki.",
                ),
                Pregunta(
                    "¿Qué alianza se formó en 1949?",
                    ["OTAN", "Pacto de Varsovia", "ASEAN", "OEA"],
                    "OTAN",
                    "La OTAN nació en 1949.",
                ),
                Pregunta(
                    "¿Qué muro cayó en 1989?",
                    ["Muro de Berlín", "Muralla China", "Muro de Adriano", "Muro de Varsovia"],
                    "Muro de Berlín",
                    "La caída del muro simbolizó el fin de la Guerra Fría.",
                ),
                Pregunta(
                    "¿Qué conflicto enfrentó a EE.UU. y la URSS?",
                    ["Guerra Fría", "Guerra de Corea", "Guerra de Vietnam", "Guerra del Golfo"],
                    "Guerra Fría",
                    "Fue un conflicto ideológico y geopolítico.",
                ),
                Pregunta(
                    "¿Qué carrera tecnológica marcó la Guerra Fría?",
                    ["Carrera espacial", "Carrera naval", "Carrera armamentista", "Carrera comercial"],
                    "Carrera espacial",
                    "La carrera espacial impulsó la tecnología.",
                ),
                Pregunta(
                    "¿Quién fue el primer humano en la Luna?",
                    ["Neil Armstrong", "Yuri Gagarin", "Buzz Aldrin", "John Glenn"],
                    "Neil Armstrong",
                    "Armstrong llegó a la Luna en 1969.",
                ),
                Pregunta(
                    "¿Qué país fue potencia del bloque oriental?",
                    ["URSS", "Reino Unido", "Francia", "Italia"],
                    "URSS",
                    "La URSS lideró el bloque oriental.",
                ),
                Pregunta(
                    "¿Qué conflicto se libró en Vietnam?",
                    ["Guerra de Vietnam", "Guerra de Corea", "Guerra del Golfo", "Guerra Civil Española"],
                    "Guerra de Vietnam",
                    "Vietnam fue un conflicto de la Guerra Fría.",
                ),
                Pregunta(
                    "¿Qué país fue dividido en dos después de 1945?",
                    ["Alemania", "España", "Brasil", "Canadá"],
                    "Alemania",
                    "Alemania se dividió en RFA y RDA.",
                ),
                Pregunta(
                    "¿Qué evento inició la Segunda Guerra Mundial?",
                    ["Invasión de Polonia", "Ataque a Pearl Harbor", "Revolución China", "Guerra Civil Española"],
                    "Invasión de Polonia",
                    "Alemania invadió Polonia en 1939.",
                ),
                Pregunta(
                    "¿Qué líder encabezó la India independiente?",
                    ["Mahatma Gandhi", "Churchill", "Mandela", "Nehru"],
                    "Mahatma Gandhi",
                    "Gandhi lideró la independencia con no violencia.",
                ),
                Pregunta(
                    "¿Qué líder sudafricano luchó contra el apartheid?",
                    ["Nelson Mandela", "Desmond Tutu", "De Klerk", "Mbeki"],
                    "Nelson Mandela",
                    "Mandela fue símbolo de la lucha antiapartheid.",
                ),
                Pregunta(
                    "¿Qué organización busca la cooperación económica en Europa?",
                    ["Unión Europea", "OTAN", "ONU", "OEA"],
                    "Unión Europea",
                    "La UE integra economías europeas.",
                ),
                Pregunta(
                    "¿Qué revolución tecnológica marcó finales del siglo XX?",
                    ["Internet", "Imprenta", "Máquina de vapor", "Telégrafo"],
                    "Internet",
                    "Internet cambió la comunicación global.",
                ),
                Pregunta(
                    "¿Qué conflicto ocurrió en 1991 en el Golfo?",
                    ["Guerra del Golfo", "Guerra de Corea", "Guerra Civil Española", "Guerra de los Balcanes"],
                    "Guerra del Golfo",
                    "La Guerra del Golfo inició en 1991.",
                ),
                Pregunta(
                    "¿Qué país lanzó el primer satélite artificial?",
                    ["URSS", "Estados Unidos", "China", "Francia"],
                    "URSS",
                    "La URSS lanzó el Sputnik en 1957.",
                ),
                Pregunta(
                    "¿Qué líder fue primer ministro del Reino Unido en la Segunda Guerra Mundial?",
                    ["Winston Churchill", "Thatcher", "Chamberlain", "Attlee"],
                    "Winston Churchill",
                    "Churchill lideró al Reino Unido durante la guerra.",
                ),
            ],
        ),
    ]


def leer_guardados() -> list[dict]:
    if not ARCHIVO_GUARDADO.exists():
        return []
    with ARCHIVO_GUARDADO.open("r", encoding="utf-8") as archivo:
        return json.load(archivo)


def escribir_guardados(guardados: list[dict]) -> None:
    with ARCHIVO_GUARDADO.open("w", encoding="utf-8") as archivo:
        json.dump(guardados, archivo, ensure_ascii=False, indent=2)


class AplicacionJuego:
    def __init__(self, raiz: tk.Tk) -> None:
        self.raiz = raiz
        self.raiz.title("Juego de Historia Universal")
        self.raiz.geometry("1200x720")
        self.raiz.configure(bg="#edf2f9")

        self.categorias = cargar_categorias()
        self.indice_categoria = 0
        self.indice_pregunta = 0
        self.vidas = 3
        self.puntaje = 0
        self.orden_preguntas: list[int] = []
        self.tiempo_limite = 30
        self.tiempo_restante = 30
        self.pregunta_especial = False
        self.pregunta_actual: Pregunta | None = None
        self.temporizador_id: str | None = None
        self.comodines = {"pista": True, "saltar": True, "investigar": True}
        self.permitir_salida_hasta: float = 0.0

        self.particulas_confeti: list[tuple[int, int, int, int, str]] = []

        self._configurar_estilos()
        self._construir_interfaz()
        self._actualizar_panel()
        self._renderizar_guardados()
        self.raiz.bind("<FocusOut>", self._gestionar_salida)
        self.raiz.bind("<Unmap>", self._gestionar_salida)

    def _configurar_estilos(self) -> None:
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("TFrame", background="#edf2f9")
        estilo.configure("Tarjeta.TFrame", background="#ffffff", relief="flat")
        estilo.configure("Titulo.TLabel", background="#ffffff", foreground="#111827", font=("Montserrat", 20, "bold"))
        estilo.configure("Subtitulo.TLabel", background="#ffffff", foreground="#6b7280", font=("Montserrat", 10, "bold"))
        estilo.configure("Texto.TLabel", background="#ffffff", foreground="#4b5563", font=("Montserrat", 11))
        estilo.configure(
            "BotonPrincipal.TButton",
            font=("Montserrat", 11, "bold"),
            padding=10,
            foreground="#ffffff",
            background="#4f46e5",
        )
        estilo.map("BotonPrincipal.TButton", background=[("active", "#6366f1")])
        estilo.configure(
            "BotonSecundario.TButton",
            font=("Montserrat", 10, "bold"),
            padding=8,
            foreground="#1f2937",
            background="#f3f4f6",
        )
        estilo.map("BotonSecundario.TButton", background=[("active", "#e5e7eb")])

    def _construir_interfaz(self) -> None:
        self.contenedor = ttk.Frame(self.raiz)
        self.contenedor.pack(fill="both", expand=True, padx=20, pady=20)

        self.cabecera = ttk.Frame(self.contenedor, style="Tarjeta.TFrame")
        self.cabecera.pack(fill="x", pady=(0, 16))

        ttk.Label(self.cabecera, text="Juego Educativo", style="Subtitulo.TLabel").pack(anchor="w", padx=20, pady=(16, 0))
        ttk.Label(self.cabecera, text="Historia Universal", style="Titulo.TLabel").pack(anchor="w", padx=20)
        ttk.Label(
            self.cabecera,
            text="Vive los períodos históricos con retos dinámicos y progreso guardado.",
            style="Texto.TLabel",
        ).pack(anchor="w", padx=20, pady=(4, 16))

        self.zona_principal = ttk.Frame(self.contenedor)
        self.zona_principal.pack(fill="both", expand=True)

        self.columna_menu = ttk.Frame(self.zona_principal, style="Tarjeta.TFrame")
        self.columna_menu.pack(side="left", fill="y", padx=(0, 16))

        ttk.Label(self.columna_menu, text="Menú Principal", style="Subtitulo.TLabel").pack(anchor="w", padx=16, pady=(16, 8))

        ttk.Button(self.columna_menu, text="Nueva partida", style="BotonPrincipal.TButton", command=self.nueva_partida).pack(
            fill="x", padx=16, pady=4
        )
        ttk.Button(self.columna_menu, text="Cargar partida", style="BotonSecundario.TButton", command=self.cargar_partida).pack(
            fill="x", padx=16, pady=4
        )

        ttk.Label(self.columna_menu, text="Nombre de la partida", style="Texto.TLabel").pack(anchor="w", padx=16, pady=(12, 4))
        self.entrada_nombre = ttk.Entry(self.columna_menu)
        self.entrada_nombre.pack(fill="x", padx=16)

        ttk.Button(self.columna_menu, text="Guardar partida", style="BotonSecundario.TButton", command=self.guardar_partida).pack(
            fill="x", padx=16, pady=8
        )

        self.estado_guardado = ttk.Label(self.columna_menu, text="No hay partida guardada.", style="Texto.TLabel")
        self.estado_guardado.pack(anchor="w", padx=16, pady=(4, 8))

        ttk.Label(self.columna_menu, text="Partidas guardadas", style="Subtitulo.TLabel").pack(anchor="w", padx=16)
        self.lista_guardados = tk.Listbox(self.columna_menu, height=10)
        self.lista_guardados.pack(fill="x", padx=16, pady=6)
        self.lista_guardados.bind("<<ListboxSelect>>", self._seleccionar_guardado)

        self.columna_juego = ttk.Frame(self.zona_principal, style="Tarjeta.TFrame")
        self.columna_juego.pack(side="left", fill="both", expand=True)

        self.etiqueta_categoria = ttk.Label(self.columna_juego, text="Selecciona una categoría", style="Subtitulo.TLabel")
        self.etiqueta_categoria.pack(anchor="w", padx=20, pady=(16, 0))
        self.etiqueta_nivel = ttk.Label(self.columna_juego, text="Reto actual", style="Titulo.TLabel")
        self.etiqueta_nivel.pack(anchor="w", padx=20, pady=(0, 12))

        self.panel_estadisticas = ttk.Frame(self.columna_juego, style="Tarjeta.TFrame")
        self.panel_estadisticas.pack(fill="x", padx=20)

        self.etiqueta_vidas = ttk.Label(self.panel_estadisticas, text="Vidas: 3", style="Texto.TLabel")
        self.etiqueta_vidas.pack(side="left", padx=10, pady=8)
        self.etiqueta_puntaje = ttk.Label(self.panel_estadisticas, text="Puntaje: 0", style="Texto.TLabel")
        self.etiqueta_puntaje.pack(side="left", padx=10, pady=8)
        self.etiqueta_tiempo = ttk.Label(self.panel_estadisticas, text="Tiempo: 30s", style="Texto.TLabel")
        self.etiqueta_tiempo.pack(side="left", padx=10, pady=8)

        self.tarjeta_pregunta = ttk.Frame(self.columna_juego, style="Tarjeta.TFrame")
        self.tarjeta_pregunta.pack(fill="x", padx=20, pady=16)

        self.texto_pregunta = ttk.Label(self.tarjeta_pregunta, text="", style="Texto.TLabel", wraplength=600)
        self.texto_pregunta.pack(anchor="w", padx=16, pady=(12, 8))

        self.marco_opciones = ttk.Frame(self.tarjeta_pregunta)
        self.marco_opciones.pack(fill="x", padx=16, pady=(0, 12))

        self.retroalimentacion = ttk.Label(self.columna_juego, text="", style="Texto.TLabel")
        self.retroalimentacion.pack(anchor="w", padx=20)

        self.panel_comodines = ttk.Frame(self.columna_juego, style="Tarjeta.TFrame")
        self.panel_comodines.pack(fill="x", padx=20, pady=(8, 0))
        ttk.Button(
            self.panel_comodines,
            text="Comodín: Pista",
            style="BotonSecundario.TButton",
            command=self.usar_comodin_pista,
        ).pack(side="left", padx=4, pady=6)
        ttk.Button(
            self.panel_comodines,
            text="Comodín: Saltar",
            style="BotonSecundario.TButton",
            command=self.usar_comodin_saltar,
        ).pack(side="left", padx=4, pady=6)
        ttk.Button(
            self.panel_comodines,
            text="Comodín: Investigar 10s",
            style="BotonSecundario.TButton",
            command=self.usar_comodin_investigar,
        ).pack(side="left", padx=4, pady=6)

        self.lienzo_confeti = tk.Canvas(self.columna_juego, height=120, bg="#ffffff", highlightthickness=0)
        self.lienzo_confeti.pack(fill="x", padx=20, pady=(12, 16))

        self.panel_categorias = ttk.Frame(self.contenedor, style="Tarjeta.TFrame")
        self.panel_categorias.pack(fill="x")
        ttk.Label(self.panel_categorias, text="Categorías disponibles", style="Subtitulo.TLabel").pack(anchor="w", padx=20, pady=(16, 8))

        self.lista_categorias = ttk.Frame(self.panel_categorias)
        self.lista_categorias.pack(fill="x", padx=20, pady=(0, 16))

        for indice, categoria in enumerate(self.categorias):
            boton = ttk.Button(
                self.lista_categorias,
                text=f"{categoria.nombre} ({len(categoria.preguntas)} preguntas)",
                style="BotonSecundario.TButton",
                command=lambda i=indice: self.seleccionar_categoria(i),
            )
            boton.pack(side="left", padx=4, pady=4)

    def _actualizar_panel(self) -> None:
        categoria = self.categorias[self.indice_categoria]
        if not self.orden_preguntas:
            self.orden_preguntas = list(range(len(categoria.preguntas)))
            random.shuffle(self.orden_preguntas)
        self.etiqueta_categoria.config(text=categoria.nombre)
        self.etiqueta_nivel.config(text="Reto activo")
        self.etiqueta_vidas.config(text=f"Vidas: {self.vidas}")
        self.etiqueta_puntaje.config(text=f"Puntaje: {self.puntaje}")
        self.etiqueta_tiempo.config(text=f"Tiempo: {self.tiempo_restante}s")

        if self.indice_pregunta >= len(categoria.preguntas):
            self.texto_pregunta.config(text="¡Categoría completada!")
            self.retroalimentacion.config(text="Excelente trabajo. Puedes elegir otra categoría.")
            for widget in self.marco_opciones.winfo_children():
                widget.destroy()
            self._detener_temporizador()
            return

        indice_real = self.orden_preguntas[self.indice_pregunta]
        pregunta = self._seleccionar_pregunta(categoria, indice_real)
        self.pregunta_actual = pregunta
        self.texto_pregunta.config(text=pregunta.enunciado)
        self.retroalimentacion.config(text="Selecciona la opción correcta.")
        self._iniciar_temporizador()

        for widget in self.marco_opciones.winfo_children():
            widget.destroy()

        for opcion in pregunta.opciones:
            ttk.Button(
                self.marco_opciones,
                text=opcion,
                style="BotonSecundario.TButton",
                command=lambda op=opcion: self.responder(op),
            ).pack(side="left", padx=4, pady=4)
        self._actualizar_comodines()

    def _seleccionar_pregunta(self, categoria: Categoria, indice_real: int) -> Pregunta:
        es_especial = random.randint(1, 10) == 1
        self.pregunta_especial = es_especial
        if es_especial:
            self.tiempo_limite = 10
            self.tiempo_restante = 10
            return self._obtener_pregunta_especial(categoria.nombre)
        self.tiempo_limite = 30
        self.tiempo_restante = 30
        return categoria.preguntas[indice_real]

    def _obtener_pregunta_especial(self, categoria: str) -> Pregunta:
        banco = {
            "Antigüedad": [
                Pregunta(
                    "¿Qué mito habla de una isla avanzada que desapareció en el mar?",
                    ["Atlántida", "Lemuria", "Pangea", "Hiperbórea"],
                    "Atlántida",
                    "Atlántida es una leyenda antigua.",
                )
            ],
            "Edad Media": [
                Pregunta(
                    "¿Qué objeto sagrado se buscaba en leyendas medievales?",
                    ["Santo Grial", "Piedra Filosofal", "Arca de Noé", "Cáliz de Oro"],
                    "Santo Grial",
                    "El Santo Grial es un mito medieval.",
                )
            ],
            "Renacimiento": [
                Pregunta(
                    "¿Qué personaje es famoso por el misterio de su sonrisa en una pintura?",
                    ["Mona Lisa", "David", "Venus", "Dama del Armiño"],
                    "Mona Lisa",
                    "La sonrisa de la Mona Lisa es enigmática.",
                )
            ],
            "Revoluciones": [
                Pregunta(
                    "¿Qué consigna se asocia con la Revolución Francesa?",
                    ["Libertad, igualdad, fraternidad", "Orden y progreso", "Paz y trabajo", "Fe y patria"],
                    "Libertad, igualdad, fraternidad",
                    "Es una consigna histórica de la época.",
                )
            ],
            "Siglo XX": [
                Pregunta(
                    "¿Qué fenómeno se relaciona con teorías del siglo XX sobre objetos voladores?",
                    ["OVNIs", "Hiperbórea", "Atlántida", "Roswell es mito"],
                    "OVNIs",
                    "Los OVNIs protagonizan teorías modernas.",
                )
            ],
        }
        return random.choice(banco.get(categoria, banco["Antigüedad"]))

    def _iniciar_temporizador(self) -> None:
        self._detener_temporizador()
        self.etiqueta_tiempo.config(text=f"Tiempo: {self.tiempo_restante}s")
        self.temporizador_id = self.raiz.after(1000, self._actualizar_temporizador)

    def _actualizar_temporizador(self) -> None:
        self.tiempo_restante -= 1
        self.etiqueta_tiempo.config(text=f"Tiempo: {self.tiempo_restante}s")
        if self.tiempo_restante <= 0:
            self._tiempo_agotado()
            return
        self.temporizador_id = self.raiz.after(1000, self._actualizar_temporizador)

    def _detener_temporizador(self) -> None:
        if self.temporizador_id:
            self.raiz.after_cancel(self.temporizador_id)
            self.temporizador_id = None

    def _tiempo_agotado(self) -> None:
        self._detener_temporizador()
        self._perder_partida("Se acabó el tiempo.")

    def _perder_partida(self, mensaje: str) -> None:
        self.vidas = 0
        self.puntaje = 0
        self.indice_pregunta = 0
        self.orden_preguntas = list(range(len(self.categorias[self.indice_categoria].preguntas)))
        random.shuffle(self.orden_preguntas)
        self.comodines = {"pista": True, "saltar": True, "investigar": True}
        self.retroalimentacion.config(text=f"{mensaje} Debes empezar de cero.")
        self._actualizar_comodines()
        self._detener_temporizador()
        self._guardar_automatico()
        self._actualizar_panel()

    def _actualizar_comodines(self) -> None:
        for boton, disponible in zip(self.panel_comodines.winfo_children(), self.comodines.values()):
            boton.configure(state="normal" if disponible else "disabled")

    def usar_comodin_pista(self) -> None:
        if not self.comodines["pista"] or not self.pregunta_actual:
            return
        pista = f"Pista: la respuesta inicia con \"{self.pregunta_actual.respuesta[0]}\"."
        self.retroalimentacion.config(text=pista)
        self.comodines["pista"] = False
        self._actualizar_comodines()
        self._guardar_automatico()

    def usar_comodin_saltar(self) -> None:
        if not self.comodines["saltar"]:
            return
        self.comodines["saltar"] = False
        self.indice_pregunta += 1
        self._actualizar_comodines()
        self._actualizar_panel()
        self._guardar_automatico()

    def usar_comodin_investigar(self) -> None:
        if not self.comodines["investigar"]:
            return
        self.comodines["investigar"] = False
        self.permitir_salida_hasta = datetime.now().timestamp() + 10
        self.estado_guardado.config(text="Puedes salir 10 segundos para investigar.")
        self._actualizar_comodines()
        self._guardar_automatico()

    def _gestionar_salida(self, _evento: tk.Event) -> None:
        ahora = datetime.now().timestamp()
        if ahora > self.permitir_salida_hasta:
            self._perder_partida("Saliste de la ventana sin comodín.")
        else:
            self.raiz.after(11000, self._comprobar_regreso)

    def _comprobar_regreso(self) -> None:
        if not self.raiz.focus_displayof():
            self._perder_partida("No regresaste a tiempo.")

    def responder(self, opcion: str) -> None:
        if not self.pregunta_actual:
            return
        self._detener_temporizador()
        if opcion == self.pregunta_actual.respuesta:
            self.puntaje += 10
            self.retroalimentacion.config(text=f"✅ {self.pregunta_actual.retroalimentacion}")
            self._lanzar_confeti()
            if self.pregunta_especial:
                self.vidas += 1
                self.retroalimentacion.config(text=f"✅ {self.pregunta_actual.retroalimentacion} ¡Ganaste una vida!")
        else:
            self.vidas -= 1
            self.retroalimentacion.config(
                text=f"❌ {self.pregunta_actual.retroalimentacion} Te quedan {self.vidas} vidas."
            )

        self.indice_pregunta += 1
        if self.vidas <= 0:
            self._perder_partida("Has perdido todas las vidas.")
            return
        self._guardar_automatico()
        self._actualizar_panel()

    def seleccionar_categoria(self, indice: int) -> None:
        self.indice_categoria = indice
        self.indice_pregunta = 0
        self.vidas = 3
        self.puntaje = 0
        self.orden_preguntas = list(range(len(self.categorias[indice].preguntas)))
        random.shuffle(self.orden_preguntas)
        self.comodines = {"pista": True, "saltar": True, "investigar": True}
        self._actualizar_panel()
        self._guardar_automatico()

    def nueva_partida(self) -> None:
        self.indice_categoria = 0
        self.indice_pregunta = 0
        self.vidas = 3
        self.puntaje = 0
        self.orden_preguntas = list(range(len(self.categorias[0].preguntas)))
        random.shuffle(self.orden_preguntas)
        self.comodines = {"pista": True, "saltar": True, "investigar": True}
        self._actualizar_panel()
        self._guardar_automatico()

    def _guardar_automatico(self) -> None:
        nombre = self.entrada_nombre.get().strip()
        if nombre:
            self._guardar_con_nombre(nombre)

    def guardar_partida(self) -> None:
        nombre = self.entrada_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Nombre requerido", "Escribe un nombre para guardar la partida.")
            return
        self._guardar_con_nombre(nombre)

    def _guardar_con_nombre(self, nombre: str) -> None:
        guardados = leer_guardados()
        existente = next((g for g in guardados if g["nombre"] == nombre), None)
        maximo = max(existente["maximo_puntaje"] if existente else 0, self.puntaje)
        registro = {
            "id": existente["id"] if existente else str(random.randint(1000, 9999)),
            "nombre": nombre,
            "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "maximo_puntaje": maximo,
            "estado": {
                "indice_categoria": self.indice_categoria,
                "indice_pregunta": self.indice_pregunta,
                "vidas": self.vidas,
                "puntaje": self.puntaje,
                "orden_preguntas": self.orden_preguntas,
                "tiempo_limite": self.tiempo_limite,
                "tiempo_restante": self.tiempo_restante,
                "pregunta_especial": self.pregunta_especial,
                "comodines": self.comodines,
            },
        }
        guardados = [g for g in guardados if g["nombre"] != nombre]
        guardados.insert(0, registro)
        escribir_guardados(guardados)
        self.estado_guardado.config(text="Partida guardada correctamente.")
        self._renderizar_guardados()

    def cargar_partida(self) -> None:
        seleccion = self.lista_guardados.curselection()
        if not seleccion:
            messagebox.showwarning("Selecciona una partida", "Selecciona una partida en la lista.")
            return
        registro = leer_guardados()[seleccion[0]]
        self._cargar_registro(registro)

    def _seleccionar_guardado(self, _evento: tk.Event) -> None:
        seleccion = self.lista_guardados.curselection()
        if not seleccion:
            return
        registro = leer_guardados()[seleccion[0]]
        self._cargar_registro(registro)

    def _cargar_registro(self, registro: dict) -> None:
        estado = registro["estado"]
        self.indice_categoria = estado["indice_categoria"]
        self.indice_pregunta = estado["indice_pregunta"]
        self.vidas = estado["vidas"]
        self.puntaje = estado["puntaje"]
        self.orden_preguntas = estado.get(
            "orden_preguntas", list(range(len(self.categorias[self.indice_categoria].preguntas)))
        )
        self.tiempo_limite = estado.get("tiempo_limite", 30)
        self.tiempo_restante = estado.get("tiempo_restante", 30)
        self.pregunta_especial = estado.get("pregunta_especial", False)
        self.comodines = estado.get("comodines", {"pista": True, "saltar": True, "investigar": True})
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_nombre.insert(0, registro["nombre"])
        self.estado_guardado.config(text=f"Partida cargada: {registro['nombre']}")
        self._actualizar_panel()

    def _renderizar_guardados(self) -> None:
        self.lista_guardados.delete(0, tk.END)
        guardados = leer_guardados()
        if not guardados:
            self.lista_guardados.insert(tk.END, "Sin partidas guardadas")
            return
        for guardado in guardados:
            texto = f"{guardado['nombre']} | Máx {guardado['maximo_puntaje']} | {guardado['fecha']}"
            self.lista_guardados.insert(tk.END, texto)

    def _lanzar_confeti(self) -> None:
        self.lienzo_confeti.delete("all")
        ancho = self.lienzo_confeti.winfo_width() or 800
        for _ in range(40):
            x = random.randint(0, ancho)
            y = random.randint(0, 20)
            dx = random.randint(-3, 3)
            dy = random.randint(2, 6)
            color = random.choice(["#6366f1", "#38bdf8", "#f472b6", "#22c55e"])
            self.particulas_confeti.append((x, y, dx, dy, color))
        self._animar_confeti()

    def _animar_confeti(self) -> None:
        self.lienzo_confeti.delete("all")
        nuevas = []
        for x, y, dx, dy, color in self.particulas_confeti:
            nx, ny = x + dx, y + dy
            if ny < 120:
                nuevas.append((nx, ny, dx, dy, color))
                self.lienzo_confeti.create_oval(nx, ny, nx + 6, ny + 6, fill=color, outline="")
        self.particulas_confeti = nuevas
        if nuevas:
            self.raiz.after(30, self._animar_confeti)


def main() -> None:
    raiz = tk.Tk()
    AplicacionJuego(raiz)
    raiz.mainloop()


if __name__ == "__main__":
    main()
