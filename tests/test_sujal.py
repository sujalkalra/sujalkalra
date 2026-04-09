from __future__ import annotations

import io
from contextlib import redirect_stdout

import pytest

from sujal import Developer, build_profile


def test_build_profile_contains_expected_identity() -> None:
    profile = build_profile()
    assert profile.name == "Sujal Kalra"
    assert "Software Engineer" in profile.headline


def test_run_outputs_core_sections() -> None:
    profile = build_profile()
    output = io.StringIO()

    with redirect_stdout(output):
        profile.run()

    text = output.getvalue()
    assert "Skills" in text
    assert "Featured Projects" in text
    assert "Achievements" in text
    assert "Goals" in text


def test_show_projects_raises_for_empty_projects() -> None:
    profile = build_profile()
    profile.projects = []

    with pytest.raises(ValueError, match="projects cannot be empty"):
        profile.show_projects()


def test_edge_case_empty_skill_category_validation() -> None:
    profile = Developer(
        name="X",
        headline="Y",
        summary="Z",
        skills={},
        projects=[{"name": "A", "description": "B"}],
        experience=["E"],
        achievements=["A"],
        goals=["G"],
    )

    with pytest.raises(ValueError, match="skills cannot be empty"):
        profile.show_skills()
