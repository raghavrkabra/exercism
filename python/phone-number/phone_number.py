class PhoneNumber:
    def __init__(self, number):
        self.number = self._if_valid(self._clean(number))
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.subscriber_number = self.number[6:]
        pass

    def pretty(self):
        return "({})-{}-{}".format(self.area_code,
                self.exchange_code, self.subscriber_number)

    def _clean(self, number):
        clean = ""
        for i in number:
            if i.isdigit():
                clean += i
            elif i in " ()-.+":
                pass
            else:
                raise ValueError("Invalid caractors in number")
        return clean

    def _if_valid(self, number):
        if len(number) == 10 or len(number) == 11 and number.startswith("1"):
            if number[-10] in "01" or number[-7] in "01":
                raise ValueError("Invalid number")
            return number[-10:]
        else:
            raise ValueError("Invalid number")
        pass


