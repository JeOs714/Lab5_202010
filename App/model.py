"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
from ADT import list as lt
from ADT import orderedmap as tree
from ADT import map as map
from ADT import list as lt
from DataStructures import listiterator as it
from datetime import datetime

"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo y retorna el catalogo inicializado.
    """
    catalog = {'booksTitleTree':None,'yearsTree':None,'booksList':None}
    #implementación de Black-Red Tree (brt) por default
    catalog['booksTitleTree'] = tree.newMap ()
    catalog['yearsTree'] = tree.newMap ()
    catalog['booksList'] = lt.newList("ARRAY_LIST")
    catalog['AccidentsTree'] = tree.newMap ()
    catalog['AccidentsList'] = lt.newList("ARRAY_LIST")
    return catalog

def newAccident (row):
    """
    Crea una nueva estructura para almacenar un libro 
    """
    accident = {"id": row['ID'], "Time": {}, "Country":row['Country']}
    accident["Time"]["DateI"]= row['Start_Time'].split(" ")[0]
    accident["Time"]["DateF"]= row['End_Time'].split(" ")[0]
    accident["Time"]["HourI"]= row['Start_Time'].split(" ")[1]
    accident["Time"]["HourF"]= row['End_Time'].split(" ")[1]
    accident["Time"]["DateHI"]= lt.newList("ARRAY_LIST")
    accident["Time"]["DateHF"]= lt.newList("ARRAY_LIST")
    return accident

def newAccidentDate(catalog, row):
    accident = {"id": None, "Date": row["Start_Time"].split(" ")[0], "Severity": None}
    accident["id"]= lt.newList("ARRAY_LIST")
    accident["Severity"]= map.newMap()
    map.put(accident["Severity"], row["Severity"], 1, compareByKey)
    lt.addLast(accident['id'],row['ID'])

    return accident 

def addBookList (catalog, row):
    """
    Adiciona libro a la lista
    """
    books = catalog['booksList']
    book = newBook(row)
    lt.addLast(books, book)
def addAccidentList (catalog, row):
    """
    Adiciona libro a la lista
    """
    accidents = catalog['AccidentsList']
    accident = newAccident(row)
    lt.addLast(accidents, accident)

def addAccidentDate (catalog, row):
    """
    Adiciona libro al map con key=title
    """
    #catalog['booksTree'] = map.put(catalog['booksTree'], int(book['book_id']), book, greater)
    Accidents= catalog['AccidentsTree']
    Exist=tree.get(Accidents,row["Start_Time"].split(" ")[0], greater)
    if Exist:
        lt.addLast(Exist['id'],row['ID'])
        Contador= row["Severity"]
        Nuevovalor= map.get(Exist["Severity"], Contador, compareByKey)
        if Nuevovalor:
            Nuevovalor+=1
            map.put(Exist["Severity"], Contador, Nuevovalor, compareByKey)
        else:
            map.put(Exist["Severity"], Contador, 1, compareByKey)
        tree.put(catalog['AccidentsTree'],row["Start_Time"].split(" ")[0],Exist, greater)    
        #director['sum_average_rating'] += float(row['vote_average'])
    else:
        Accident= newAccidentDate(catalog, row)
        catalog['AccidentsTree']  = tree.put(Accidents , Accident["Date"], Accident, greater)
        #tree.put(Accidents, Accident['Date'], Accident, greater)
        

def addAccidentMap1 (catalog, row):
    """
    Adiciona libro al map con key=title
    """
    accident= newAccident(row)
    #catalog['booksTree'] = map.put(catalog['booksTree'], int(book['book_id']), book, greater)
    catalog['AccidentsTree']  = tree.put(catalog['AccidentsTree'] , accident['Time']["DateHI"] , accident, greater)
def newBook (row):
    """
    Crea una nueva estructura para almacenar un libro 
    """
    book = {"book_id": row['book_id'], "title":row['title'], "average_rating":row['average_rating'], "ratings_count":row['ratings_count']}
    return book

def addBookTree (catalog, row):
    """
    Adiciona libro al tree con key=title
    """
    book = newBook(row)
    #catalog['booksTitleTree'] = tree.put(catalog['booksTitleTree'], int(book['book_id']), book, greater)
    catalog['booksTitleTree']  = tree.put(catalog['booksTitleTree'] , book['title'], book, greater)

def newYear (year, row):
    """
    Crea una nueva estructura para almacenar los libros por año 
    """
    yearNode = {"year": year, "ratingMap":None,}
    yearNode ['ratingMap'] = map.newMap(11,maptype='CHAINING')
    intRating = round(float(row['average_rating']))
    map.put(yearNode['ratingMap'],intRating, 1, compareByKey)
    return yearNode

def addYearTree (catalog, row):
    """
    Adiciona el libro al arbol anual key=original_publication_year
    """
    yearText= row['original_publication_year']
    if row['original_publication_year']:
        yearText=row['original_publication_year'][0:row['original_publication_year'].index('.')]     
    year = strToDate(yearText,'%Y')
    yearNode = tree.get(catalog['yearsTree'] , year, greater)
    if yearNode:
        intRating = round(float(row['average_rating']))
        ratingCount = map.get(yearNode['ratingMap'], intRating, compareByKey)
        if  ratingCount:
            ratingCount+=1
            map.put(yearNode['ratingMap'], intRating, ratingCount, compareByKey)
        else:
            map.put(yearNode['ratingMap'], intRating, 1, compareByKey)
    else:
        yearNode = newYear(year,row)
        catalog['yearsTree']  = tree.put(catalog['yearsTree'] , year, yearNode, greater)

# Funciones de consulta


def getBookTree (catalog, bookTitle):
    """
    Retorna el libro desde el mapa a partir del titulo (key)
    """
    return tree.get(catalog['booksTitleTree'], bookTitle, greater)

def rankBookTree (catalog, bookTitle):
    """
    Retorna la cantidad de llaves menores (titulos) dentro del arbol
    """
    return tree.rank(catalog['booksTitleTree'], bookTitle, greater)

def selectBookTree (catalog, pos):
    """
    Retorna la operación select (titulos) dentro del arbol
    """
    return tree.select(catalog['booksTitleTree'], pos) 

def getBookByYearRating (catalog, year):
    """
    Retorna la cantidad de libros para un año y con un rating dado
    """
    yearElement=tree.get(catalog['yearsTree'], strToDate(year,'%Y'), greater)
    response=''
    if yearElement:
        ratingList = map.keySet(yearElement['ratingMap'])
        iteraRating=it.newIterator(ratingList)
        while it.hasNext(iteraRating):
            ratingKey = it.next(iteraRating)
            response += 'Rating '+str(ratingKey) + ':' + str(map.get(yearElement['ratingMap'],ratingKey,compareByKey)) + '\n'
        return response
    return None
def getSeverityByDate(catalog, date):
    Año= tree.get(catalog["AccidentsTree"], date, greater)
    res=""
    if Año:
        Severidades= map.keySet(Año["Severity"])
        iterator=it.newIterator(Severidades)
        res+= "El total de accidentes la fecha " + str(date) + " fue "+ str(lt.size(Año["id"]))+ "\n"
        while it.hasNext(iterator):
            SevKey = it.next(iterator)
            res += 'Severidad '+str(SevKey) + ' : ' + str(map.get(Año["Severity"],SevKey,compareByKey)) + '\n'
        return res
    return None


# Funciones de comparacion

def compareByKey (key, element):
    return  (key == element['key'] )  

def compareByTitle(bookTitle, element):
    return  (bookTitle == element['title'] )

def greater (key1, key2):
    if ( key1 == key2):
        return 0
    elif (key1 < key2):
        return -1
    else:
        return 1

def strToDate(date_string, format):
    
    try:
        # date_string = '2016/05/18 13:55:26' -> format = '%Y/%m/%d %H:%M:%S')
        return datetime.strptime(date_string,format)
    except:
        return datetime.strptime('1900', '%Y')

