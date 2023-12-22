from __future__ import annotations
from abc import ABC, abstractmethod

class Psql(ABC):
    @abstractmethod
    def __add__(self):...

    @abstractmethod
    def to_querys(self):...

    @abstractmethod
    def set_query(self):...
    
    @abstractmethod
    def commit(self):...
