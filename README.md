# Requests to Web Steam API

![Build Status](https://github.com/vadushkin/SteamAPIRequests/actions/workflows/type-checks.yml/badge.svg?branch=main)
![Build Status](https://github.com/vadushkin/SteamAPIRequests/actions/workflows/run-tests.yml/badge.svg?branch=main)

Installation
---------

#### Clone a repository

```
git clone https://github.com/vadushkin/SteamAPIRequests.git
```

#### Change a folder

```
cd SteamAPIRequests
```

#### Venv

```
python -m venv venv
.\venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

#### Poetry

```
poetry install
poetry shell
```

#### Create ```.env``` file

#### Example to fill in

```dotenv
KEY=
```

#### Key - is your steam application key

#### [Documentation](https://steamcommunity.com/dev) from Steam

#### Direct [link](https://steamcommunity.com/dev/apikey) to get the key

#### Poetry run

```shell
poetry run python .\main.py
```
