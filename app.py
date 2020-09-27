from jinja2 import Environment, PackageLoader, select_autoescape
from gtts import gTTS
from datetime import date

env = Environment(
    loader=PackageLoader('day_starter', 'templates'),
    autoescape=select_autoescape(['html'])
)

template = env.get_template('today.html')
name = 'Ammar'
datetime_today = date.today()
output_text = template.render(
    name=name,
    datetime=datetime_today
)
print(output_text)
language = 'en'
speech = gTTS(
    text=output_text,
    lang=language,
    slow=False
)
speech.save("text.mp3")
