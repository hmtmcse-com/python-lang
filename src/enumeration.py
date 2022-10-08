# ----------------------------------------------------------------------------------------------------------------------
# Define Status Enum
from enum import Enum


class Status(Enum):
    ACTIVE = "A"
    INACTIVE = "I"
    SUSPEND = "S"
    CANCEL = "C"


# Access Status Enum
print(Status.ACTIVE)


