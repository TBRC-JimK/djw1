from enum import Enum

class AuditTestType(Enum):
    """
    Describes the test subject structures
    """
    COMPLETE_TREE = 1
    IMAGE = 2
    IMAGE_GROUP = 3
    STRUCTURE = 4

class AuditTestBase:
    """
    Base class of an auditapp test
    """
    def run(self):
        pass