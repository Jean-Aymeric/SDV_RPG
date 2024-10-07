from abc import ABC
from Named import Named


class Job(Named , ABC):
    def __init__(self, name: str):
        super().__init__(name)
