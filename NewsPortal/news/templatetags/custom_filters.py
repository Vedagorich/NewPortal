from django import template

register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def currency(value):
    """
   value: значение, к которому нужно применить фильтр
   """
    # Возвращаемое функцией значение подставится в шаблон.
    return f'{value} Р'


@register.filter()
def censor_text(value: str):
    censored_words = ['блядки', 'блядовать', 'блядство', 'блядь', 'бугор', 'пизду', 'раком', 'хуй']
    for word in censored_words:
        value = value.replace(word, '*' * len(word))
    return value
