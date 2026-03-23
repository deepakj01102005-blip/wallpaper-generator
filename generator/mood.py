def resolve_mood(dreamy, dark):
    if dreamy >= 4 and dark >= 4:
        return "cinematic"
    if dark >= 4:
        return "dark"
    if dreamy >= 4:
        return "dreamy"
    return "calm"
