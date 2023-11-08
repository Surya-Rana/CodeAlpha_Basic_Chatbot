import random

R_EATING = "I don't like eating anything because I'm a chatbot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there! "


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds good.",
                "What does that mean?"]
    [random.randrange(4)]
    return response
