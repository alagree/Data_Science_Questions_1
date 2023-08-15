'''
Question #1: Count symbols
In this question, you are given a string s which represents a DNA string. The string s consists of symbols 'A', 'C', 'G', and 'T'. An example of a length 21 DNA string is "ATGCTTCAGAAAGGTCTTACG."
Your task is to write a code which will count the number of times each of the symbols 'A', 'C', 'G', and 'T' occur in s. Your code should generate a list of 4 integers and print it out.
'''
s = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

#List the abbreviation of the chemicals that make of the nucleotide bases of DNA
Nucleotide_bases = ['A', 'C', 'G', 'T']

#Iterate over the chemicals counting the number of apperiences 
count_list = [Nucleotide_bases.count(chemical) for chemical in Nucleotide_bases]

#Print the number of apperiences
_ = [print(f"{Nucleotide_bases[i]} appered {f} times in the seqence") for i,f in enumerate(count_list)]

'''
Question #2: Find a substring
You are given a dictionary of the US states and their capitals. The keys in the dictionary are states and the values are capital names.
Write a code to return a list of all capitals that contain the name of a state in their name as a substring.
HINT: For example, Indianapolis as a capital name and Indiana as a state name is one of the key/value pairs that your code would find. Your code should add Indianapolis to the list. After you found all capitals and added them to the list, print out the list.
'''
capitals={
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'  
}

#Create and empty list to store the results
new_capitals = []

#Iterate over the items in the dct
for key, value in capitals.items():
    #If the statename appears in the capital name, append the capital name to the list
    if key in value:
        new_capitals.append(value)



'''
Question #3: Is a data point within a rectangle?
Write a function isIn() which returns boolean True if a point is within a rectangle specified by two sets of coordinates and boolean False if the point is outside the rectangle. The function should accept three parameters:
the first parameter is a set of coordinates which defines one of the corners of the rectangle,
the second parameter is also a set of coordinates that defines the second corner,
the third set of coordinates defines a single point which is being tested.
For example,
isIn((1,2), (3,4), (1.5, 3.2)) should return True,
isIn((4,3.5), (2,1), (3, 2)) should return True,
isIn((-1,0), (5,5), (6,0)) should return False,
isIn((4,1), (2,4), (2.5,4.5)) should return False.
Test your function with at least 2 different sets of data points in addition to the examples above.
NOTES:
If the point being tested is on the side of the rectangle, consider it to be within the rectangle. For example, if the rectangle is defined as (1,2), (3,4) and the point is (2,2), the function should return True.
In this assignment, we assume that the edges of the rectangle are parallel to coordinate axes.
We also assume that the first parameter does not always represent the left corner of the rectangle and the second parameter is not always the right corner. The function should work correctly either way. Please note the second test condition above where the first parameter, (4,3.5), represents the top-right corner and the second parameter, (2,1), represents left-bottom corner.
'''

def isIn(firstCorner=(0,0), secondCorner=(0,0), point=(0,0)):
    '''
    Parameters
    ----------
    firstCorner : Tuple
        Takes as input a single of the rectangle. Default is (0,0).
    secondCorner : Tuple
        Takes as input a single of the rectangle. Default is (0,0).
    point : Tuple
        Takes as input a single point. Default is (0,0).
        
    Raises
    ------
    Exception
        Raises exception if input variable is not TYPE Tuple.

    Returns
    -------
    bool
        Returns True if the point lies within or on the edge of the rectangle.

    '''
    
    #Throw exception if input variable is not a Tuple
    for in_var in [firstCorner,secondCorner,point]:
        if isinstance(in_var, tuple) == False:    
            raise Exception(f"Input variable must be type Tuple. Input variable is identified as {type(in_var)}")
    
    #Create a list of all the x vertices
    x_points = list((firstCorner[0], secondCorner[0]))
    #Create a list of all the y vertices
    y_points = list((firstCorner[1], secondCorner[1]))

    #Determine whether the point is within the rectangle
    if min(x_points) <= point[0] <= max(x_points) and min(y_points) <= point[1] <= max(y_points):
        return True
    else:
        return False

isIn(firstCorner=(0,0), secondCorner=(0,0), point=(0,0))    

'''
Question #4: Are all points within a rectangle?
Modify your function from the previous question so it takes a list of points rather than a single point and returns boolean True only if all points in the list are in the rectangle.
For example,
allIn((0,0), (5,5), [(1,1), (0,0), (5,5)]) should return True
but allIn((0,0), (5,5), [(1,1), (0,0), (5,6)]) should return False
empty list of points allIn((0,0), (5,5), []) should return False
Use the same assumptions as above about the placement of the points and how rectangle is defined. Make sure that your function returns False for empty list of points (no values).
Test your function with at least 3 different sets of data points.
'''

def allIn(firstCorner=(0,0), secondCorner=(0,0), pointList=[]):
    '''
    Parameters
    ----------
    firstCorner : Tuple
        Takes as input a single of the rectangle. Default is (0,0).
    secondCorner : Tuple
        Takes as input a single of the rectangle. Default is (0,0).
    point_List : List
        Takes as input a List of points. Default is None.
        
    Raises
    ------
    Exception
        Raises exception if input variable is not TYPE Tuple or list.

    Returns
    -------
    TYPE
        Returns True if all points lie within or on the edge of the rectangle..

    '''
    
    #Throw exception if input variable is not a Tuple
    for in_var in [firstCorner,secondCorner]:
        if isinstance(in_var, tuple) == False:    
            raise Exception(f"Input variable must be type Tuple. Input variable is identified as {type(in_var)}")
            
    #Throw exception if input variable is not a Tuple        
    if isinstance(pointList, list) == False:    
        raise Exception(f"Input variable must be type List. point_List is identified as {type(pointList)}")
    
    #Create a list of all the x vertices
    x_points = list((firstCorner[0], secondCorner[0]))
    #Create a list of all the y vertices
    y_points = list((firstCorner[1], secondCorner[1]))

    #Determine whether the point is within the rectangle
    point_results = [True if min(x_points) <= point[0] <= max(x_points) and min(y_points) <= point[1] <= max(y_points) else False for point in pointList]

    if not pointList:
        return False
    else:
        return all(point_results)


allIn(firstCorner=(0,0), secondCorner=(0,0), pointList=[])




















































