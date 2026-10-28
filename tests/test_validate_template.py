"""Regression checks for invalid template configurations, not application tests."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("template_validator", ROOT / "scripts/validate_template.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "template"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def edit_json(self, path, edit):
        target = self.root / path
        value = json.loads(target.read_text(encoding="utf-8"))
        edit(value)
        target.write_text(json.dumps(value), encoding="utf-8")

    def assert_rejected(self, phrase):
        self.assertTrue(any(phrase in error for error in MODULE.validate(self.root)),
                        MODULE.validate(self.root))

    def test_valid_template(self):
        self.assertEqual(MODULE.validate(self.root), [])

    def test_duplicate_skill_is_rejected(self):
        self.edit_json("skills.registry.json", lambda v: v["skills"].append(v["skills"][0].copy()))
        self.assert_rejected("duplicate skill")

    def test_broken_local_link_is_rejected(self):
        with (self.root / "README.md").open("a", encoding="utf-8") as output:
            output.write("\n[broken](docs/does-not-exist.md)\n")
        self.assert_rejected("broken local link")

    def test_mutable_source_is_rejected(self):
        self.edit_json("sources.lock.json", lambda v: v["sources"][0].update(commit="main"))
        self.assert_rejected("immutable commit")

    def test_missing_license_is_rejected(self):
        (self.root / "licenses/ECC-MIT.txt").unlink()
        self.assert_rejected("missing license file")

    def test_reference_only_import_is_rejected(self):
        self.edit_json("skills.registry.json",
                       lambda v: v["skills"][0].update(source_ids=["awesome-code"]))
        self.assert_rejected("reference-only source")

    def test_missing_description_is_rejected(self):
        path = self.root / ".agents/skills/coding-standards/SKILL.md"
        lines = path.read_text(encoding="utf-8").splitlines()
        path.write_text("\n".join(line for line in lines if not line.startswith("description:")) + "\n",
                        encoding="utf-8")
        self.assert_rejected("invalid name or description")

    def test_unregistered_skill_is_rejected(self):
        path = self.root / ".agents/skills/orphan/SKILL.md"
        path.parent.mkdir()
        path.write_text("# Not registered\n", encoding="utf-8")
        self.assert_rejected("unregistered skill")

    def test_conflicting_scenario_is_rejected(self):
        self.edit_json("evals/scenarios.json",
                       lambda v: v["cases"][0]["not_primary"].append(v["cases"][0]["primary_skill"]))
        self.assert_rejected("contradictory scenario routing")

    def test_path_escape_is_rejected(self):
        self.edit_json("skills.registry.json",
                       lambda v: v["skills"][0].update(path="../outside.md"))
        self.assert_rejected("unexpected skill path")


if __name__ == "__main__":
    unittest.main()
