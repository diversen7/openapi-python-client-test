from enum import Enum


class OrderStatus(str, Enum):
    PLACED = "placed"
    APPROVED = "approved"
    DELIVERED = "delivered"

    def __str__(self) -> str:
        return str(self.value)
