import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('marketplace', Path(__file__).resolve().parents[1] / 'scripts/build_claude_marketplace.py')
marketplace = importlib.util.module_from_spec(spec)
spec.loader.exec_module(marketplace)


class ClaudeMarketplaceTests(unittest.TestCase):
    def test_lists_each_built_bundle_with_its_manifest_version(self):
        with tempfile.TemporaryDirectory() as tmp:
            built = Path(tmp)
            for name, version in (('strategy', '1.2.0'), ('development', '3.0.0')):
                (built / name).mkdir()
                (built / name / 'plugin.json').write_text(json.dumps(
                    {'name': name, 'version': version, 'description': f'{name} bundle'}))
            (built / 'notes').mkdir()

            count = marketplace.write_marketplace(built, 'agent-skills-public', 'Owner')

            data = json.loads((built / '.claude-plugin' / 'marketplace.json').read_text())
            self.assertEqual(count, 2)
            self.assertEqual(data['name'], 'agent-skills-public')
            self.assertEqual(data['owner'], {'name': 'Owner'})
            self.assertEqual(data['plugins'], [
                {'name': 'development', 'source': './development', 'description': 'development bundle', 'version': '3.0.0'},
                {'name': 'strategy', 'source': './strategy', 'description': 'strategy bundle', 'version': '1.2.0'},
            ])

    def test_refuses_to_overwrite_an_existing_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            built = Path(tmp)
            (built / '.claude-plugin').mkdir()
            with self.assertRaises(FileExistsError):
                marketplace.write_marketplace(built, 'agent-skills-public', 'Owner')


if __name__ == '__main__':
    unittest.main()
