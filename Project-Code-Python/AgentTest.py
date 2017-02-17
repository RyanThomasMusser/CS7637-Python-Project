from __future__ import absolute_import
import unittest
import pprint
from Agent import Agent
from ProblemSet import ProblemSet

agent = Agent()
problemSet = ProblemSet('Basic Problems B')

class AgentTest(unittest.TestCase):

    def testB1(self):

        # objects.attributes
        # {'fill': 'yes', 'shape': 'square', 'size': 'very large'}


        self.assertEqual(agent.Solve(problemSet.problems[5]), 2)

    def testB2(self):
        pprint.pprint(problemSet.problems[1].problemType)
        self.assertEqual(agent.Solve(problemSet.problems[1]), 5)

    def testB3(self):
        pprint.pprint(problemSet.problems[2].problemType)
        self.assertEqual(agent.Solve(problemSet.problems[2]), 1)

    def testB4(self):
        pprint.pprint(problemSet.problems[3].problemType)
        self.assertEqual(agent.Solve(problemSet.problems[3]), 3)

    def testB5(self):
        pprint.pprint(problemSet.problems[4].problemType)
        self.assertEqual(agent.Solve(problemSet.problems[4]), 4)

    def testB6(self):
        pprint.pprint(problemSet.problems[5].problemType)
        self.assertEqual(agent.Solve(problemSet.problems[5]), 5)

    def testB7(self):
        pprint.pprint(problemSet.problems[6].problemType)
        self.assertEqual(agent.Solve(problemSet.problems[6]), 6)

    def testB8(self):
        pprint.pprint(problemSet.problems[7].problemType)
        self.assertEqual(agent.Solve(problemSet.problems[7]), 6)

    def testB9(self):
        pprint.pprint(problemSet.problems[8].problemType)
        self.assertEqual(agent.Solve(problemSet.problems[8]), 5)

    def testB10(self):
        pprint.pprint(problemSet.problems[9].problemType)
        self.assertEqual(agent.Solve(problemSet.problems[9]), 3)

    def testB11(self):
        pprint.pprint(problemSet.problems[10].problemType)
        self.assertEqual(agent.Solve(problemSet.problems[10]), 1)

    def testB12(self):
        pprint.pprint(problemSet.problems[11].problemType)
        self.assertEqual(agent.Solve(problemSet.problems[11]), 1)