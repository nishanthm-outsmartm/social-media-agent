VALID_STYLES = ["persuasive", "humorous", "professional"]
VALID_PLATFORMS = ["Instagram", "X", "Facebook", "LinkedIn"]

def validate_style(style: str):
    if style not in VALID_STYLES:
        raise ValueError(f"Invalid style. Choose from {VALID_STYLES}")

def validate_platform(platform: str):
    if platform not in VALID_PLATFORMS:
        raise ValueError(f"Invalid platform. Choose from {VALID_PLATFORMS}")