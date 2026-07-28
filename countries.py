import pandas as pd

# Add or remove rows here. Use plain country names — build.py looks each
# one up in iso_codes.py to find its map code. If a lookup fails, the
# build script will tell you exactly which name to fix.

VISITED = pd.DataFrame({
    "country": [
        "Germany",
        "Italy",
        "France",
        "Spain",
        "Portugal",
        "United Kingdom",
        "Netherlands",
        "Belgium",
        "Switzerland",
        "Austria",
        "Czech Rep.",
        "Slovakia",
        "Hungary",
        "Romania",
        "Serbia",
        "Croatia",
        "Slovenia",
        "Greece",
        "Turkey",
        "Lithuania",
        "Latvia",
        "Sweden",
        "Denmark",
        "Iceland",
        "Poland",
        "Belarus",
        "Russia",
        "Ukraine",
        "Azerbaijan",
        "United States",
        "Mexico",
        "Peru",
        "Egypt",
    ]
})
