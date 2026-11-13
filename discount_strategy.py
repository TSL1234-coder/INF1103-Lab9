from abc import ABC, abstractmethod

class DiscountStrategy(ABC):

    @abstractmethod
    def apply(self, total: float) -> float:
        pass


# Returns original total
class NoDiscount(DiscountStrategy):

    def apply(self, total: float) -> float:
        return total



# Deducts a percentage
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float) -> None:
        self.__percent = percent

    def apply(self, total: float) -> float:
        return total * (1 - self.__percent / 100)


# Deducts a fixed amount when total reaches a threshold
class BulkDiscount(DiscountStrategy):

    def __init__(self, threshold: float, amount: float) -> None:
       self.__threshold = threshold
       self.__amount = amount


    def apply(self, total: float) -> float:
        if total >= self.__threshold:
            return total - self.__amount

        return total

# Student Discount (12% Discount)
class StudentDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.90