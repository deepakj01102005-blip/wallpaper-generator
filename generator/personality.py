def personality_to_colors(dreamy, dark):
    """
    Maps mood values to cinematic color palettes
    """

    if dark:
        # Dark / moody palette
        base = (18, 18, 30)
        accent = (
            int(100 + dreamy * 60),
            int(80 + dreamy * 40),
            int(160 + dreamy * 40)
        )
    else:
        # Dreamy / ethereal palette
        base = (235, 235, 245)
        accent = (
            int(180 + dreamy * 40),
            int(150 + dreamy * 30),
            int(200 + dreamy * 30)
        )

    return base, accent
