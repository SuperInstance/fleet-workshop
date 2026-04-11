"""
Fleet Workshop Board — Central marketplace for fleet ideas and projects.

Generates THE-BOARD.md from active ideas, fence boards, and vessel statuses.
"""
import json
import os
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from typing import List, Optional
from enum import Enum


class IdeaStatus(Enum):
    PROPOSED = "proposed"
    ACCEPTED = "accepted"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ARCHIVED = "archived"


class IdeaPriority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class WorkshopIdea:
    """A fleet workshop idea."""
    id: str
    title: str
    description: str
    author: str
    status: IdeaStatus = IdeaStatus.PROPOSED
    priority: IdeaPriority = IdeaPriority.MEDIUM
    assigned_to: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    votes: int = 0
    voters: List[str] = field(default_factory=list)
    created: str = ""
    updated: str = ""
    
    def __post_init__(self):
        if not self.created:
            self.created = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        if not self.updated:
            self.updated = self.created
    
    def vote(self, vessel: str):
        if vessel not in self.voters:
            self.voters.append(vessel)
            self.votes += 1
            self.updated = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    
    def to_dict(self):
        d = asdict(self)
        d["status"] = self.status.value
        d["priority"] = self.priority.value
        return d


@dataclass
class WorkshopBoard:
    """The fleet workshop board — all ideas in one place."""
    ideas: List[WorkshopIdea] = field(default_factory=list)
    
    def add(self, idea: WorkshopIdea):
        self.ideas.append(idea)
    
    def find(self, idea_id: str) -> Optional[WorkshopIdea]:
        for idea in self.ideas:
            if idea.id == idea_id:
                return idea
        return None
    
    def by_status(self, status: IdeaStatus) -> List[WorkshopIdea]:
        return [i for i in self.ideas if i.status == status]
    
    def by_tag(self, tag: str) -> List[WorkshopIdea]:
        return [i for i in self.ideas if tag in i.tags]
    
    def by_author(self, author: str) -> List[WorkshopIdea]:
        return [i for i in self.ideas if i.author == author]
    
    def top_voted(self, limit: int = 10) -> List[WorkshopIdea]:
        return sorted(self.ideas, key=lambda i: i.votes, reverse=True)[:limit]
    
    def generate_markdown(self) -> str:
        """Generate THE-BOARD.md."""
        now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        lines = [f"# THE BOARD\n"]
        lines.append(f"_Updated: {now}_\n")
        
        # Stats
        lines.append("## Stats\n")
        for status in IdeaStatus:
            count = len(self.by_status(status))
            lines.append(f"- **{status.value}**: {count}")
        lines.append(f"- **Total**: {len(self.ideas)}\n")
        
        # Active ideas
        active = [i for i in self.ideas if i.status in (IdeaStatus.PROPOSED, IdeaStatus.ACCEPTED, IdeaStatus.IN_PROGRESS)]
        if active:
            lines.append("## Active Ideas\n")
            for idea in sorted(active, key=lambda i: i.votes, reverse=True):
                status_icon = {"proposed": "💡", "accepted": "✅", "in_progress": "🔧"}.get(idea.status.value, "❓")
                lines.append(f"### {status_icon} {idea.title}\n")
                lines.append(f"- **ID:** {idea.id}")
                lines.append(f"- **Author:** {idea.author}")
                lines.append(f"- **Status:** {idea.status.value}")
                lines.append(f"- **Priority:** {idea.priority.value}")
                lines.append(f"- **Votes:** {idea.votes} ({', '.join(idea.voters)})")
                if idea.assigned_to:
                    lines.append(f"- **Assigned:** {', '.join(idea.assigned_to)}")
                if idea.tags:
                    lines.append(f"- **Tags:** {', '.join(idea.tags)}")
                lines.append(f"- **Description:** {idea.description}")
                lines.append("")
        
        # Completed
        completed = self.by_status(IdeaStatus.COMPLETED)
        if completed:
            lines.append(f"## Completed ({len(completed)})\n")
            for idea in completed:
                lines.append(f"- ~~{idea.title}~~ ({idea.author})")
            lines.append("")
        
        return "\n".join(lines)
    
    def to_json(self) -> str:
        return json.dumps([i.to_dict() for i in self.ideas], indent=2)


# ── Tests ──────────────────────────────────────────────

import unittest


class TestWorkshopBoard(unittest.TestCase):
    def test_add_idea(self):
        board = WorkshopBoard()
        board.add(WorkshopIdea(id="idea-1", title="Test", description="A test", author="oracle1"))
        self.assertEqual(len(board.ideas), 1)
    
    def test_find_idea(self):
        board = WorkshopBoard()
        board.add(WorkshopIdea(id="idea-1", title="Test", description="A test", author="oracle1"))
        found = board.find("idea-1")
        self.assertIsNotNone(found)
        self.assertEqual(found.title, "Test")
    
    def test_find_missing(self):
        board = WorkshopBoard()
        self.assertIsNone(board.find("nonexistent"))
    
    def test_by_status(self):
        board = WorkshopBoard()
        board.add(WorkshopIdea(id="1", title="A", description="", author="o1", status=IdeaStatus.PROPOSED))
        board.add(WorkshopIdea(id="2", title="B", description="", author="o1", status=IdeaStatus.COMPLETED))
        self.assertEqual(len(board.by_status(IdeaStatus.PROPOSED)), 1)
    
    def test_by_tag(self):
        board = WorkshopBoard()
        board.add(WorkshopIdea(id="1", title="A", description="", author="o1", tags=["cuda", "gpu"]))
        board.add(WorkshopIdea(id="2", title="B", description="", author="o1", tags=["python"]))
        self.assertEqual(len(board.by_tag("cuda")), 1)
    
    def test_vote(self):
        idea = WorkshopIdea(id="1", title="A", description="", author="o1")
        idea.vote("jetsonclaw1")
        self.assertEqual(idea.votes, 1)
        idea.vote("jetsonclaw1")  # duplicate
        self.assertEqual(idea.votes, 1)
        idea.vote("oracle1")
        self.assertEqual(idea.votes, 2)
    
    def test_top_voted(self):
        board = WorkshopBoard()
        for i in range(5):
            idea = WorkshopIdea(id=str(i), title=f"Idea {i}", description="", author="o1")
            for _ in range(i):
                idea.vote(f"voter-{i}-{_}")
            board.add(idea)
        top = board.top_voted(3)
        self.assertEqual(len(top), 3)
        self.assertGreaterEqual(top[0].votes, top[1].votes)
    
    def test_generate_markdown(self):
        board = WorkshopBoard()
        board.add(WorkshopIdea(id="1", title="Test Idea", description="A test", author="oracle1", tags=["test"]))
        md = board.generate_markdown()
        self.assertIn("Test Idea", md)
        self.assertIn("oracle1", md)
        self.assertIn("Stats", md)
    
    def test_to_json(self):
        board = WorkshopBoard()
        board.add(WorkshopIdea(id="1", title="Test", description="", author="o1"))
        j = board.to_json()
        data = json.loads(j)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["status"], "proposed")


if __name__ == "__main__":
    unittest.main(verbosity=2)
