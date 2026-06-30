# Применение метаклассов: система плагинов

class PluginRegistry(type):
    plugins = {}

    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)
        if name != "BasePlugin":
            cls.plugins[name] = new_cls
        return new_cls

class BasePlugin(metaclass=PluginRegistry):
    """Базовый класс для всех плагинов"""
    def execute(self):
        raise NotImplementedError()

class EmailPlugin(BasePlugin):
    def execute(self):
        print("Отправка email уведомления")

class SMSService(BasePlugin):
    def execute(self):
        print("Отправка SMS сообщения")

def run_plugin(plugin_name):
    plugin_class = PluginRegistry.plugins.get(plugin_name)
    if not plugin_class:
        raise ValueError(f"Плагин '{plugin_name}' не найден")
    return plugin_class().execute()

if __name__ == "__main__":
    print("Доступные плагины:", list(PluginRegistry.plugins.keys()))
    run_plugin("EmailPlugin")
    run_plugin("SMSService")


# Современная альтернатива метаклассам

class Base:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        print(f"Creating subclass {cls.__name__} from {cls.__base__.__name__}")
        # Можно модифицировать класс здесь
        if not hasattr(cls, "default_value"):
            cls.default_value = 0

class Child(Base):
    pass

class AnotherChild(Base):
    default_value = 42

print(Child.default_value)
print(AnotherChild.default_value)


class Base:
    def __init_subclass__(cls, **kwargs):
        """Этот метод автоматически становится classmethod!"""
        print(f"Initializing subclass {cls.__name__}")
        super().__init_subclass__(**kwargs)  # Важно вызывать super(), хотя у нас нет явного родительского класса

class Child(Base):
    pass


# Когда использовать __init_subclass__ вместо метаклассов

class BasePlugin:
    plugins = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.__name__ != "BasePlugin":
            BasePlugin.plugins[cls.__name__] = cls

    def execute(self):
        raise NotImplementedError()

class EmailPlugin(BasePlugin):
    def execute(self):
        return "Email sent"

class SMSService(BasePlugin):
    def execute(self):
        return "SMS sent"

print("Registered plugins:", list(BasePlugin.plugins.keys()))


# Проверка наследования: issubclass() и метаклассы

class Serializable:
    """Маркерный базовый класс: объекты его подклассов можно
    безопасно сериализовать в JSON."""
    def to_dict(self):
        raise NotImplementedError

class User(Serializable):
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name

    def to_dict(self):
        return {"user_id": self.user_id, "name": self.name}

class DatabaseConnection:
    """Небезопасный для сериализации класс — содержит ресурсы."""
    def __init__(self, host: str):
        self.host = host
        self._connection = None  # имитация открытого соединения

def safe_serialize(obj):
    """Сериализует объект, только если его класс унаследован от Serializable.
    Защищает от ошибок и утечек при попытке сериализовать неподходящие объекты."""
    if issubclass(obj.__class__, Serializable):
        return obj.to_dict()
    else:
        raise TypeError(f"Объект типа {type(obj).__name__} нельзя сериализовать")

# Тестовые данные — могут приходить извне (API, конфиг, плагины и т.д.)
objects = [
    User(1, "John"),
    DatabaseConnection("localhost"),
]

for obj in objects:
    try:
        data = safe_serialize(obj)
        print(f"Сериализовано: {data}")
    except TypeError as error:
        print(f"Отклонено: {error}")
