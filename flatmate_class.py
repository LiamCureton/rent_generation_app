from bill_class import Bill

class Flatmate:
    """
    Object that contains details os the Person that lives in the flat and pays a share of the bill
    """

    def __init__(self, name: str, days_in_flat: int):
        self.name = name
        self.days_in_flat = days_in_flat

    def pays(self, bill: Bill) -> int:
        weight = self.days_in_flat / bill.time_period
        return round(bill.total * weight, 2)
