import logging
import time

import requests

from config import settings

logger = logging.getLogger(__name__)


def get_player_summaries(user_id: int) -> [dict, None]:
    """
    Return a list of information about a person.

    :user_id <int>: Player ID.
    """

    url = f'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?' \
          f'key={settings.key}&' \
          f'steamids={user_id}'

    response = requests.get(url)

    if response.status_code > 400:
        logger.warning(f'User ID - {user_id}. Status code - {response.status_code}.')
        return None

    if not response.json()['response']['players']:
        logger.warning(f'User - {user_id}. There is no such user')
        return None

    try:
        for item in response.json()['response']['players'][0].items():
            print(item)

    except Exception as _ex:
        logger.warning(f'Error is {_ex}. Function - get_player_summaries()')
        return None

    return response.json()


def get_players_summaries(user_ids: list[int]) -> list[dict]:
    """
    Return a list of information about people.

    :user_ids <list[int]>: List of players IDs.
    """

    lst_users = []

    for user_id in user_ids:
        url = f'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?' \
              f'key={settings.key}&' \
              f'steamids={user_id}'

        response = requests.get(url)

        if response.status_code > 400:
            logger.warning(f'User ID - {user_id}. Status code - {response.status_code}.')
            continue

        if not response.json()['response']['players']:
            logger.warning(f'User - {user_id}. There is no such user')
            continue

        lst_users.append(response.json())

        for user in response.json()['response']['players'][0].items():
            print(user)
        print()

        time.sleep(0.5)

    return lst_users


def get_global_achievement_percentages_for_app(game_id: int) -> [dict, None]:
    """
    Returns on global achievements overview of a specific game in percentages.

    :game_id <int>: Game ID.
    """
    url = f'https://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?' \
          f'gameid={game_id}&' \
          f'format=json'

    response = requests.get(url)

    if response.status_code > 400:
        logger.warning(f'Game ID - {game_id}. Status code - {response.status_code}.')
        return None

    try:
        for achieve in response.json()['achievementpercentages']['achievements']:
            print(achieve)

    except Exception as _ex:
        logger.warning(f'Error is {_ex}. Function - get_global_achievement_percentages_for_app()')
        return None

    return response.json()


def get_news_for_app(app_id: int, count: int, max_length: int) -> [dict, None]:
    """
    Return the latest of a game specified by its appID.

    :app_id <int>: AppID of the game you want the news of.
    :count <int>: How much news entries you want to get returned.
    :max_length <int>: Maximum length of each news entry.
    """

    url = f'https://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?' \
          f'appid={app_id}&' \
          f'count={count}&' \
          f'maxlength={max_length}&' \
          f'format=json'

    response = requests.get(url)

    if response.status_code > 400:
        logger.warning(
            f'App ID - {app_id}, Count - {count}, Max Length - {max_length}. Status code - {response.status_code}.')
        return None

    for news in response.json()['appnews']['newsitems']:
        for article in news.items():
            print(article)

        print()

    return response.json()


def get_friend_list(steam_id: int, relationship: str) -> None:
    """
    Returns the friend list of any Steam user, provided their Steam Community profile visibility is set to “Public”.

    :steam_id <int>: User ID.
    :relationship <str>: Relationship filter. Possibles values: all, friend.
    """

    url = f'https://api.steampowered.com/ISteamUser/GetFriendList/v0001/?' \
          f'key={settings.key}&' \
          f'steamid={steam_id}&' \
          f'relationship={relationship}'

    response = requests.get(url)

    if response.status_code > 400:
        logger.warning(f'Key - {str(settings.key)[:6]}... '
                       f'Steam ID - {steam_id}. '
                       f'Relationship - {relationship}. '
                       f'Status code - {response.status_code}.')
        return None

    for friends in response.json()['friendslist']['friends']:
        for friend in friends.items():
            print(friend)

        print()

    return response.json()


def main():
    try:
        # get_player_summaries(76561197963562688)
        # get_players_summaries([76561197963562688, 76561197963562688])
        # get_global_achievement_percentages_for_app(440)
        # get_news_for_app(440, 3, 300)
        # get_friend_list(76561197960435530, 'all')
        pass

    except Exception as _ex:
        logger.critical(f'Error is {_ex}. Function - main()')


if __name__ == '__main__':
    main()
