from dataclasses import dataclass, field
from .country import Country

@dataclass
class League:
    id: int = 0 
    country: Country = field(default_factory= Country)
    name: str = ""
