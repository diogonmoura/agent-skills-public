import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('evaluation_validator', ROOT / 'scripts/validate_evaluations.py')
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class EvaluationDefinitionsTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'evals/development-workflows.json').read_text())

    def test_complete_definition_graph_is_valid(self):
        self.assertEqual(validator.validate(self.data), [])

    def test_duplicate_and_dangling_scenarios_are_rejected(self):
        self.data['cases'].append(copy.deepcopy(self.data['cases'][0]))
        self.data['flow_matrix'][0]['trial_ids'].append('nonexistent-trial')
        errors = validator.validate(self.data)
        self.assertTrue(any('duplicate id' in e for e in errors))
        self.assertTrue(any('unknown generation_trials reference' in e for e in errors))

    def test_removed_assertions_and_actor_phase_are_rejected(self):
        self.data['cases'][0]['criteria'] = []
        self.data['generation_trials'][0]['phases'][0].pop('prompt')
        errors = validator.validate(self.data)
        self.assertTrue(any('nonempty criteria required' in e for e in errors))
        self.assertTrue(any('task/prompt phases required' in e for e in errors))

    def test_unmapped_case_and_invalid_evidence_are_rejected(self):
        self.data['cases'].append({'id': 'unmapped-case', 'prompt': 'Read supplied artifacts.',
                                   'criteria': ['Report observed state.'], 'evidence': 'not a list'})
        errors = validator.validate(self.data)
        self.assertTrue(any('missing flow mapping' in e for e in errors))
        self.assertTrue(any('evidence must be nonempty strings' in e for e in errors))
