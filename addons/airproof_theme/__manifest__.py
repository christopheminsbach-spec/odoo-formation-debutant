{
    "name": "Airproof Theme",
    "description": """
        Custom Website Theme inspired by Airproof
    """,
    "category": "Theme/Website",
    "version": "19.0.1.0.0",
    "author": "Christophe Minsbach",
    "license": "LGPL-3",
    
    "depends": [
        "website",
    ],

    "data": [
        "data/website.xml",
    ],

    "assets": {
        "web._assets_primary_variables": [
            "airproof_theme/static/src/scss/primary_variables.scss",
        ],

        "web.assets_frontend": [
            "airproof_theme/static/src/scss/**/*.scss",
        ],
    },

    "application": True,
}