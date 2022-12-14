# Requests to Web Steam API

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