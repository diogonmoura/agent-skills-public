import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "plugins/development-workflow/skills/project-bootstrap/scripts"


def load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


scaffold = load("scaffold").scaffold
check = load("check_project").check


class ScaffoldTests(unittest.TestCase):
    def test_profiles_pass_and_optional_components_are_explicit(self):
        with tempfile.TemporaryDirectory() as directory:
            for ai in ("none", "adk", "langchain"):
                for mcp in (False, True):
                    with self.subTest(ai=ai, mcp=mcp):
                        root = Path(directory) / f"{ai}-{mcp}"
                        scaffold(root, ai, mcp)
                        self.assertEqual(check(root), [])
                        self.assertEqual((root / "applications/api/src/ai").exists(), ai != "none")
                        self.assertEqual((root / "applications/api/src/mcp").exists(), mcp)

    def test_existing_project_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sentinel = root / "important.txt"
            sentinel.write_text("keep me")
            with self.assertRaises(ValueError):
                scaffold(root)
            self.assertEqual(sentinel.read_text(), "keep me")
            self.assertEqual(list(root.iterdir()), [sentinel])

    def test_missing_doc_invalid_profile_and_broken_link_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            scaffold(root)
            (root / "documentation/product/prd.md").unlink()
            (root / "project-profile.json").write_text("[]")
            with (root / "documentation/README.md").open("a") as document:
                document.write("\n[missing](unknown.md)\n")
            failures = check(root)
            self.assertTrue(any("prd.md" in x for x in failures))
            self.assertTrue(any("Invalid project profile" in x for x in failures))
            self.assertTrue(any("unknown.md" in x for x in failures))

    def test_unapproved_stack_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            scaffold(root)
            path = root / "project-profile.json"
            profile = json.loads(path.read_text())
            profile["stack"]["backend"] = ["sqlite", "sqlmodel"]
            path.write_text(json.dumps(profile))
            self.assertTrue(any("stack.backend" in x for x in check(root)))

    def test_implemented_claim_requires_real_e2e_contract(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            scaffold(root)
            path = root / "project-profile.json"
            profile = json.loads(path.read_text())
            profile["readiness"] = "implemented"
            profile["testing"]["internal_api"] = "mocked"
            path.write_text(json.dumps(profile))
            failures = check(root)
            self.assertTrue(any("testing.internal_api" in x for x in failures))
            self.assertTrue(any("critical E2E journeys" in x for x in failures))
            self.assertTrue(any("e2e-critical" in x for x in failures))

    def test_implemented_metadata_is_not_execution_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            scaffold(root)
            path = root / "project-profile.json"
            profile = json.loads(path.read_text())
            profile["readiness"] = "implemented"
            profile["testing"]["critical_journeys"] = ["REQ-001 primary journey"]
            for name in ["setup", "dev", "e2e-critical", "api-tests", "web-build"]:
                profile["checks"][name] = ["command-not-executed-by-structural-check"]
            path.write_text(json.dumps(profile))
            self.assertEqual(check(root), [])

    def test_escaping_doc_and_destination_symlink_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            scaffold(root)
            outside = Path(directory) / "outside.md"
            outside.write_text("outside")
            doc = root / "documentation/product/prd.md"
            doc.unlink()
            doc.symlink_to(outside)
            self.assertTrue(any("escapes" in x for x in check(root)))
            alias = Path(directory) / "alias"
            alias.symlink_to(root)
            with self.assertRaises(ValueError):
                scaffold(alias)


if __name__ == "__main__":
    unittest.main()
