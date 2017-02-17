# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.

from PIL import Image
import numpy

import pprint

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints 
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self,problem):
        pprint.pprint(problem.name)
        pprint.pprint(problem.hasVerbal)

        visualMapHash = {
            'fill' : [],
            'angle' : {
                'count' : 0,
                'total' : 0
            },
            'sizes' : [],
            'shapes' : [],
            'attributes' : 0

        }

        solutions = []


        for attr, value in problem.figures.iteritems():

            if(attr == 'A' or attr == 'B' or attr == 'C'):

                for attributeKey, attributeValue in value.objects.iteritems():
                    for attributeNodeKey, attributeNodeValue in attributeValue.attributes.iteritems():
                        visualMapHash['attributes'] += 1
                        if(attributeNodeKey == 'angle'):
                            visualMapHash['angle']['count'] += 1
                            visualMapHash['angle']['total'] += int(attributeNodeValue)

                        if (attributeNodeKey == 'shape'):
                            visualMapHash['shapes'].append(attributeNodeValue)

                        if (attributeNodeKey == 'fill'):
                            visualMapHash['fill'].append(attributeNodeValue)

                        if (attributeNodeKey == 'size'):
                            visualMapHash['sizes'].append(attributeNodeValue)

            else:

                for attributeKey, attributeValue in value.objects.iteritems():
                    solution = {'shapeFitness' : 0,'angleFitness' : 0,'name' : attr,'shapes' : [], 'sizes' : [] , 'angle' : {'count' : 0,'total' : 0} , 'fill' : []}
                    for attributeNodeKey, attributeNodeValue in attributeValue.attributes.iteritems():

                        if(attributeNodeKey == 'angle'):
                            solution['angle']['count'] += 1
                            solution['angle']['total'] += int(attributeNodeValue)

                        if (attributeNodeKey == 'shape'):
                            solution['shapes'].append(attributeNodeValue)
                            solution['shapeFitness'] = int(solution['shapes'].count(attributeNodeValue) + visualMapHash['shapes'].count(attributeNodeValue)) % 4

                        if (attributeNodeKey == 'fill'):
                            solution['fill'].append(attributeNodeValue)
                            solution['fillFitness'] = int(solution['fill'].count(attributeNodeValue) + visualMapHash['fill'].count(attributeNodeValue)) % 4


                        if (attributeNodeKey == 'size'):
                            solution['sizes'].append(attributeNodeValue)

                    solution['angleFitness'] += (int(solution['angle']['total']) + visualMapHash['angle']['total']) % 4

                    solutions.append(solution)


        print solutions

        print visualMapHash

        return -1

