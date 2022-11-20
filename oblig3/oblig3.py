#Write a Python program that reas inputfiles and builds a graph.

def readMovieFile(): #Oppgave 1.
    """
    Inputs:
        None
    
    Function:
        Open the file, and then extract the data from there. Place the data to dictionaries.
        One of the dictionary has id with movies, other one has movies with ratings.
    
    Returns:
        movieID: dictionary of movies with id
        movieRating: dictionary of movies with ratings
    """
    movieID = {}
    movieRating = {}
    with open("movies.tsv", "r") as file:
        for line in file:
            line = line.strip().split("\t")
            movieID[line[0]] = line[1]
            movieRating[line[0]] = line[2]
        file.close()
    return movieID, movieRating

def readActorFile(): #Oppgave 2.
    """
    Inputs:
        None
    
    Function:
        Open the file, and then extract the data from there. Place the data to dictionaries.
        One of the dictionary has actors with movies, other one has movies with actors.
    
    Returns:
        actorMovie: dictionary of actors, movies and their repective ID
        IDtoName: dictionary of actors with their ID and names
    """
    actorMovie = {}
    IDtoName = {}
    
    with open("actors.tsv", "r") as file:
        for line in file:
            line = line.strip().split("\t")
            movies = []
            for movie in line[2:]:
                movies.append(movie)
            actorMovie[line[0]] = movies
            IDtoName[line[0]] = line[1]
                    
        file.close()
    return actorMovie, IDtoName

def len_Nodes_and_edges(Graph): #Oppgave 1
    """Inputs:
    
    G: All the data from IMDB
    
    Function:
        Calculates total amount of edges and retrieves the length of Nodes
    
    Returns:
        length of the Nodes and total edges
    """
    V, E, w, idToName, movieIdToName, movieRating = Graph
    len_edges = len(V)
    len_nodes = 0
    for nodes in w.keys():
        len_edges += len(w[nodes]) / 2
    return len_nodes, len_edges

def createGraph(): #Oppgave 3.
    """
    Inputs:
        None
    
    Function:
        Create a graph with data from two dictionaries.
    
    Returns:
        V: dictionary of actors with their ID and name
        E: dictionary of movies with their ID and name
        w: dictionary of actors with movies and their repective ID
        idToName: dictionary of actors with their ID and names
        movieIdToName: dictionary of movies with their ID and names
        movieRating: dictionary of movies with ratings
    """
    nodes = {}
    edges = {}
    w = {}
    idToName, movieIdToName, movieRating = readActorFile()[1], readMovieFile()[0], readMovieFile()[1]
    for actor in readActorFile()[0].keys():
        nodes[actor] = idToName[actor]
        for movie in readActorFile()[0][actor]:
            print(edges[movie])
            edges[movie] = movieIdToName[movie]
            if actor in w.keys():
                w[actor][movie] = movieIdToName[movie]
            else:
                w[actor] = {movie: movieIdToName[movie]}
    return nodes, edges, w, idToName, movieIdToName, movieRating

 

if __name__ == "__main__":
    """     id, rate = (readMovieFile())
    print(rate) """
    actorMovie, movieActor = readActorFile()
    #print(readActorFile())
    #print(actorMovie)
    graph = createGraph()
    print(len_Nodes_and_edges(graph))