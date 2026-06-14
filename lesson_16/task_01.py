# Объявление и инстанцирование класса

class Dummy:
    pass

obj = Dummy()


class SimpleExample:
    """
    Demonstrates the basic capabilites of classes.
    """

    def __init__(self, a, b):
        self._a = a
        self.b = b

    def update_a(self, new_a):
        self._a = new_a
        return self._a

    def print_b(self):
        print(f"b value: {self.b}")

obj = SimpleExample(4, 1)

print(obj.update_a(8))

obj.print_b()
obj.b = 10
obj.print_b()


# Статистика HTTP кодов ответов сервиса

class ResponseStats:
    def __init__(self):
        self.responses = {}

    def add_response(self, http_code):
        self.responses[http_code] = self.responses.get(http_code, 0) + 1

    def response_count(self, http_code):
        return self.responses.get(http_code, 0)

    def http_err_pct(self):
        error_count = 0
        all_count = 0

        for code, number in self.responses.items():
            all_count += number
            if code >= 400:
                error_count += number

        if all_count == 0:
            return 0

        error_percentage = round(error_count / all_count * 100)

        return error_percentage

stats = ResponseStats()
http_codes = [200, 200, 200, 300, 300, 400, 404, 500]

for code in http_codes:
    stats.add_response(code)

print(stats.response_count(200))
print(stats.response_count(300))
print(stats.response_count(400))
print(stats.http_err_pct())
