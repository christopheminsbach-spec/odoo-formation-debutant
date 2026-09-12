{
    "name": "Airproof Theme",

    "version": "19.0.1.0.0",

    "author": "Angus Studio Grafix",

    "category": "Website",

    "summary": "Airproof custom website theme",
    "depends": [
        "website"
    ],
    "data": [
        "data/website.xml",
        "data/menu.xml",
        "data/presets.xml",
        "data/images.xml",
        "data/pages/home.xml",
        "views/assets.xml",
    ],
    "assets": {
    "web.assets_frontend": [
        "airproof_theme/static/src/scss/airproof.scss",
        "airproof_theme/static/src/scss/components/hero.scss",
    ],
},
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}