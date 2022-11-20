
import time
from collections import defaultdict
from heapq import heappush, heappop
from collections import deque

def readMovieFile(): #Oppgave 1.
    """
    Inputs:
        None
    
    Function:
        Open the file, and then extract the data from there. Place the data to dictionaries.
        One of the dictionary has id with movies, other one has movies with ratings.
    
    Returns:
        movieIdToName: dictionary of movies with id
        movieRating: dictionary of movies with ratings
    """
    filename = open('movies.tsv', encoding="utf8")
    movieIdToName = dict()
    movieRating = dict()
    for lines in filename:
        data = lines.strip().split('\t')
        id = data[0]
        tittel = data[1]
        rating = data[2]
        movieRating[id] = rating
        movieIdToName[id] = tittel
    filename.close()

    return movieIdToName, movieRating

def readActorFile():
    """
    Inputs:
        None
    
    Function:
        Open the file, and then extract the data from there. Place the data to dictionaries.
        One of the dictionary has id with names of actors, other one has movies with actors
        who acted there.
    
    Returns:
        actorToMovies: dictionary with actors with id and movie id.
        idToName: dictionary with actors with id and names of actors.
    """
    filename = open('actors.tsv', encoding="utf8")
    actorToMovies = {}
    idToName = {}
    for lines in filename:
        data = lines.strip().split('\t')
        id = data[0]
        name = data[1]
        movies = set()
        for movie in data[2:]:
            movies.add(movie)
        actorToMovies[id] = movies
        idToName[id] = name
    filename.close()

    return actorToMovies, idToName

def IMDB_GRAPH():
    """
    Inputs:
        None
    
    Function:
        Iterate all actors to a movie, and then add them to the dictionary. Also add all
        movies with id in a dictionary, and also add movie rating to a dictionary. Also 
        create edges, nodes and weights. This will be IMDB graph.
    
    Returns:
        V: Nodes
        E: Edges
        w: Weight
        idToName: dictionary of names with id
        movieIdToName: dictionary of movies with name
        movieRating: dictionary of movies with ratings
    """
    V = set()
    E = defaultdict(set)
    w = defaultdict(list)
    actorToMovies, idToName = readActorFile()
    movieIdToName, movieRating = readMovieFile()
    movieActors = defaultdict(list)
    for actor in actorToMovies.keys():
        V.add(actor)
        for movie in actorToMovies[actor]:
            if not movie in movieRating: #if not weight
                continue
            if movieActors[movie]: #If already exist in dict
                for otherActor in movieActors[movie]:
                    E[actor].add(otherActor)
                    E[otherActor].add(actor)

                    w[(actor, otherActor)].append(
                        (float(movieRating[movie]), movie)
                    )
                    w[(otherActor, actor)].append(
                        (float(movieRating[movie]), movie)
                    )
            movieActors[movie].append(actor)  # add actor

    return V, E, w, idToName, movieIdToName, movieRating

def totalNodes(Graph):
    """
    Inputs:
        G: All the data of the IMDB
    
    Function:
        total nodes
    
    Returns:
        length of the Nodes
    """
    V, E, w, idToName, movieIdToName, movieRating = Graph

    return(len(V))

def totalEdges(Graph):
    """
    Inputs:
        G: All the data of the IMDB
    
    Function:
        Calculate the total edges, by divide the total weight with 2
    
    Returns:
        total edges
    """
    V, E, w, idToName, movieIdToName, movieRating = Graph
    sum = 0
    for nodes in w.keys():
        sum += len(w[nodes]) / 2
    
    return int(sum)

def breadthFirstSearch(Graph, start, end): #Oppgave 2.
    """
    Inputs:
        G: All the data of the IMDB
        start: start point
        end: to end point
    
    Function:
        This will calculate and find the shortest path and return it as a
        dictionary, and then return a print value of the shortest path
        between start and end. Later will print out the values.
        Search: Breadth First Search
    
    Returns:
        strenge: return the print value
    """
    V, E, w, idToName, movieIdToName, movieRating = Graph
    parents = {start: None}
    queue = deque([start])
    result = []
    strings = ""
    while queue:
        v = deque.popleft(queue)
        result.append(v)
        if v == end:
            break
        for child in E[v]:
            if child not in parents:
                movies = w[(v, child)]
                movieRatings = movies[0]
                movieId = movieRatings[1]
                parents[child] = (v, movieId)
                queue.append(child)
    current = parents[end]
    path = []
    if end not in parents:
        return path
    while current and current[0] in parents:
        actorId = current[0]
        path.append([current[0], current[1]])
        current = parents[actorId]
    datas = path[::-1]
    for lines in datas:
        actorId = lines[0]
        movieId = lines[1]
        actorName = idToName[actorId]
        movieName = movieIdToName[movieId]
        strings += actorName + "\n" + \
            "===[" + movieName + \
            " ( " + movieRating[movieId] + " ) " + "]" + "===> "
    strings += str(idToName[end] + "\n")

    print(strings)

def dijkstraAlgorithm(Graph, start, end): #Oppgave 3.
    """
    Inputs:
        G: All the data of the IMDB
        start: from start point
        end: to end point
    
    Function:
        This will calculate the weight and bind parents and weight together, with an
        algorithm called Dijkstra. Afterwards, put parent nodes to a dictionray with
        care of ratings. Print the shortest path from a dictionary parents.
        Algorithm: Dijkstra algorithm
    
    Returns:
        shortest path from dictionary parents, and print them out.
    """
    V, E, w, idToName, movieIdToName, movieRating = Graph
    Q = [(0, start)]
    D = defaultdict(lambda: float('inf'))
    D[start] = 0
    parents = {start: None}
    datas = []
    strings = ""
    weight = 0
    while Q:
        cost, v = heappop(Q)
        if v == end:
            break
        for u in E[v]:
            movies = w[(v, u)] #Tupel: id and then movie id
            minTupel = max(movies)
            minValue = 10 - minTupel[0]
            minId = minTupel[1]
            c = cost + minValue
            if c < D[u]:
                D[u] = c
                heappush(Q, (c, u))
                parents[u] = (v, minId)
    current = parents[end]
    while current and current[0] in parents:
        actorId = current[0]
        datas.append([current[0], current[1]])
        current = parents[actorId]
    datas.reverse()
    for lines in datas:
        actorId = lines[0]
        movieId = lines[1]
        actorName = idToName[actorId]
        movieName = movieIdToName[movieId]
        strings += actorName + "\n" + \
            "===[" + movieName + \
            " ( " + movieRating[movieId] + " ) " + "]" + "===> "
        weight += 10 - float(movieRating[movieId])
    strings += str(idToName[end] + "\n" +
                   "Total weight: " + ("%.1f" % weight) + "\n")
    
    print(strings)

def components(Graph): #Oppgave 4.
    """
    Inputs:
        G: All the data of the IMDB
    
    Function:
        This will first search through all actors. Then add all actors in a list where
        it is reachable with node, and then add them in to a list. Aftewards, check the 
        length of all lists in a list, and map the size of the list until it reached length
        of the list. Save them in a dictionary.
    
    Returns:
        strenge: return the print value
    """
    V, E, w, idToName, movieIdToName, movieRating = Graph
    sizes = defaultdict(int)
    allComponents = []
    visits = set()
    strings = ""
    for x in V:
        if x in visits:
            continue
        visited = set([x])
        stack = [x]
        result = []
        while stack:
            v = stack.pop()
            result.append(v)
            for u in E[v]:
                if u not in visited:
                    visited.add(u)
                    visits.add(u)
                    stack.append(u)
        allComponents.append(result)
    for komponent in allComponents:
        length = len(komponent)
        sizes[length] += 1
    dictionary_items = sizes.items()
    sorted_items = sorted(dictionary_items, reverse=True)
    for total in sorted_items:
        strings += f"There are {total[1]} components of size {total[0]} \n"
    
    print(strings)

if __name__ ==  "__main__":

    """    start_time = time.time()
        Graph = IMDB_GRAPH()
        print("Oppgave 1: \n")
        print("Nodes:",totalNodes(Graph))
        print("Edges:",str(totalEdges(Graph)))
        print("\nOppgave 2: \n")
        breadthFirstSearch(Graph, 'nm2255973', 'nm0000460')
        breadthFirstSearch(Graph, 'nm0424060', 'nm0000243')
        breadthFirstSearch(Graph, 'nm4689420', 'nm0000365')
        breadthFirstSearch(Graph, 'nm0000288', 'nm0001401')
        breadthFirstSearch(Graph, 'nm0031483', 'nm0931324')
        print("Oppgave 3: \n")
        dijkstraAlgorithm(Graph, 'nm2255973', 'nm0000460')
        dijkstraAlgorithm(Graph, 'nm0424060', 'nm0000243')
        dijkstraAlgorithm(Graph, 'nm4689420', 'nm0000365')
        dijkstraAlgorithm(Graph, 'nm0000288', 'nm0001401')
        dijkstraAlgorithm(Graph, 'nm0031483', 'nm0931324')
        print("Oppgave 4: \n")
        components(Graph)
        print("Runtime: ")
        print("--- %s seconds ---" % (time.time() - start_time))"""
    #print(readMovieFile())
    #print(readActorFile())  
    actorMovie, movieActor = readActorFile()
    print(actorMovie)

"""
python innleveringsoppgave3.py >
Oppgave 1:

Nodes: 119205
Edges: 5068918

Oppgave 2:

Donald Glover
===[Lennon or McCartney ( 5.4 ) ]===> David Morrissey
===[Waterland ( 6.6 ) ]===> Jeremy Irons

Scarlett Johansson
===[Don Jon ( 6.5 ) ]===> Cuba Gooding Jr.
===[American Gangster ( 7.8 ) ]===> Denzel Washington

Carrie Coon
===[Avengers: Infinity War ( 8.4 ) ]===> Chris Hemsworth
===[Avengers: Age of Ultron ( 7.3 ) ]===> Julie Delpy

Christian Bale
===[Amsterdam ( 6.2 ) ]===> Leland Orser
===[The Bone Collector ( 6.7 ) ]===> Angelina Jolie

Atle Antonsen
===[In Order of Disappearance ( 7.1 ) ]===> David Sakurai
===[Acts of Vengeance ( 5.7 ) ]===> Paz Vega
===[Kill the Messenger ( 6.9 ) ]===> Michael K. Williams

Oppgave 3:

Donald Glover
===[The Martian ( 8.0 ) ]===> Enzo Cilenti
===[The Man Who Knew Infinity ( 7.2 ) ]===> Jeremy Irons
Total weight: 4.8

Scarlett Johansson
===[Avengers: Endgame ( 8.4 ) ]===> Josh Brolin
===[American Gangster ( 7.8 ) ]===> Denzel Washington
Total weight: 3.8

Carrie Coon
===[Avengers: Infinity War ( 8.4 ) ]===> Samuel L. Jackson
===[Avengers: Age of Ultron ( 7.3 ) ]===> Julie Delpy
Total weight: 4.3

Christian Bale
===[The Dark Knight Rises ( 8.4 ) ]===> Liam Neeson
===[For the Love of Spock ( 7.6 ) ]===> Angelina Jolie
Total weight: 4.0

Atle Antonsen
===[In Order of Disappearance ( 7.1 ) ]===> Stellan Skarsgård
===[Good Will Hunting ( 8.3 ) ]===> Casey Affleck
===[Gone Baby Gone ( 7.6 ) ]===> Michael K. Williams
Total weight: 7.0

Oppgave 4:

There are 1 components of size 113102
There are 1 components of size 11
There are 2 components of size 10
There are 4 components of size 9
There are 2 components of size 8
There are 6 components of size 7
There are 9 components of size 6
There are 19 components of size 5
There are 43 components of size 4
There are 117 components of size 3
There are 320 components of size 2
There are 4666 components of size 1

Runtime:
--- 35.94689702987671 seconds ---
"""