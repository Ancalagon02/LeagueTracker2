from dataclasses import dataclass, field
from .country import Country

@dataclass
class League:
    id: int = 0 
    name: str = ""
    country: Country = field(default_factory= Country)
