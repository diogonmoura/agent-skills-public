import unittest

from scripts.build_skill_flow import check


class SkillFlowTests(unittest.TestCase):
    def test_every_skill_is_placed_once_in_the_flow(self):
        _, skills, placed, problems = check()
        self.assertEqual(problems, [], "update documentation/skill-flow.json:\n" + "\n".join(problems))
        self.assertEqual(set(placed), set(skills))


if __name__ == "__main__":
    unittest.main()
