from dataclasses import dataclass, field
from enum import Enum
from typing import List

class RiskLevel(Enum):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    CATASTROPHIC = 'Catastrophic'

@dataclass
class Artifact:
    name: str
    risk_level: RiskLevel
    tags: List[str] = field(default_factory=list)