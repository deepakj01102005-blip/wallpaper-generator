import random

FALLBACK_QUOTES = {
    "calm": [
        "Stillness feels like home.",
        "Quiet moments hold the truth.",
        "Peace arrives without sound."
    ],
    "dark": [
        "Even the dark learns to glow.",
        "Night teaches patience.",
        "Shadows are honest."
    ],
    "dreamy": [
        "Dreams wander softly.",
        "The mind drifts where it feels safe.",
        "Reality loosens its grip."
    ],
    "cinematic": [
        "Every moment feels larger here.",
        "Time slows when meaning appears.",
        "Some scenes stay forever."
    ]
}

def generate_quote(mood):
    # later this can call OpenAI / local LLM
    # for now, this is intelligent + reliable
    return random.choice(FALLBACK_QUOTES[mood])
