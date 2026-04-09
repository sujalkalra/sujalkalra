#!/usr/bin/env python3
"""Executable developer profile for Sujal Kalra."""

from __future__ import annotations

from dataclasses import dataclass, field
import logging
from typing import Iterable

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
LOGGER = logging.getLogger("developer_profile")


@dataclass(slots=True)
class Developer:
    """Represents a developer profile rendered as executable code."""

    name: str
    headline: str
    summary: str
    skills: dict[str, list[str]]
    projects: list[dict[str, str]]
    experience: list[str]
    achievements: list[str]
    goals: list[str]
    contact: dict[str, str] = field(default_factory=dict)

    def _validate_non_empty(self, label: str, values: Iterable[str]) -> None:
        if not any(str(value).strip() for value in values):
            raise ValueError(f"{label} cannot be empty.")

    def introduce(self) -> None:
        """Print the profile introduction."""
        LOGGER.info("Rendering introduction")
        print(f"\n{self.name}")
        print(self.headline)
        print("-" * len(self.headline))
        print(self.summary)

    def show_skills(self) -> None:
        """Print grouped skills."""
        LOGGER.info("Rendering skills")
        self._validate_non_empty("skills", self.skills.keys())
        print("\nSkills")
        for category, entries in self.skills.items():
            clean_entries = ", ".join(item for item in entries if item.strip())
            print(f"- {category}: {clean_entries}")

    def show_projects(self) -> None:
        """Print featured projects."""
        LOGGER.info("Rendering projects")
        if not self.projects:
            raise ValueError("projects cannot be empty.")

        print("\nFeatured Projects")
        for project in self.projects:
            print(f"- {project['name']}: {project['description']}")

    def show_experience(self) -> None:
        """Print experience highlights."""
        LOGGER.info("Rendering experience")
        self._validate_non_empty("experience", self.experience)
        print("\nExperience")
        for item in self.experience:
            print(f"- {item}")

    def show_achievements(self) -> None:
        """Print achievements and goals."""
        LOGGER.info("Rendering achievements and goals")
        self._validate_non_empty("achievements", self.achievements)
        self._validate_non_empty("goals", self.goals)

        print("\nAchievements")
        for item in self.achievements:
            print(f"- {item}")

        print("\nGoals")
        for goal in self.goals:
            print(f"- {goal}")

    def run(self) -> None:
        """Execute the end-to-end profile rendering flow."""
        LOGGER.info("Developer profile execution started")
        try:
            self.introduce()
            self.show_skills()
            self.show_projects()
            self.show_experience()
            self.show_achievements()

            print("\nContact")
            for key, value in self.contact.items():
                print(f"- {key}: {value}")

            LOGGER.info("Developer profile execution completed successfully")
        except Exception:
            LOGGER.exception("Developer profile execution failed")
            raise


def build_profile() -> Developer:
    """Create the canonical developer profile object."""
    return Developer(
        name="Sujal Kalra",
        headline="Software Engineer | Scalable Systems | Automation-Driven Development",
        summary=(
            "I design and build maintainable backend systems with strong testing, "
            "observability, and performance discipline."
        ),
        skills={
            "Languages": ["Python", "JavaScript/TypeScript", "SQL"],
            "Backend": ["REST APIs", "Service Design", "Data Modeling"],
            "Reliability": ["Logging", "Metrics", "Testing", "Error Handling"],
            "Tooling": ["Git", "pytest", "CI/CD foundations"],
        },
        projects=[
            {
                "name": "Executable Developer Profile",
                "description": "OOP-based resume in code with validation, logging, and modular rendering.",
            },
            {
                "name": "Metrics Dashboard Utility",
                "description": "Tracks latency, throughput, uptime, and error rate from runtime events.",
            },
        ],
        experience=[
            "Designed modular Python systems with clean interfaces and low coupling.",
            "Implemented quality workflows with targeted unit and integration test coverage.",
            "Improved maintainability via documentation, structure standardization, and automation.",
        ],
        achievements=[
            "Built recruiter-ready, production-style portfolio structure from a minimal baseline.",
            "Integrated observability-first patterns with metrics and explicit runtime logging.",
            "Established test strategy including edge, failure, and stress validations.",
        ],
        goals=[
            "Scale into platform and backend architecture leadership responsibilities.",
            "Advance distributed system design and performance engineering depth.",
            "Ship production AI-enabled systems with reliability and safety standards.",
        ],
        contact={
            "Resume": "https://sujalnextweb.vercel.app/sujal_kalra.pdf",
            "GitHub": "https://github.com/sujalkalra",
        },
    )


if __name__ == "__main__":
    build_profile().run()
