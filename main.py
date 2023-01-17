import logging
import time

from config import settings

import requests

logger = logging.getLogger(__name__)


def get_player_summaries(user_id: int) -> dict | None:
    """
    Return a list of information about a person.

    :user_id <int>: Player ID.
    """

    url = f'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?' \
          f'key={settings.key}&' \
          f'steamids={user_id}'

    response = requests.get(url)

    if response.status_code >= 400:
        logger.warning(f'User ID - {user_id}. '
                       f'Status code - {response.status_code}.')
        return None

    if not response.json()['response']['players']:
        logger.warning(f'User - {user_id}. '
                       f'There is no such user')
        return None

    try:
        for item in response.json()['response']['players'][0].items():
            print(item)

    except Exception as _ex:
        logger.warning(f'Error is {_ex}. '
                       f'Function - get_player_summaries()')
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

        if response.status_code >= 400:
            logger.warning(f'User ID - {user_id}. '
                           f'Status code - {response.status_code}.')
            continue

        if not response.json()['response']['players']:
            logger.warning(f'User - {user_id}. '
                           f'There is no such user')
            continue

        lst_users.append(response.json())

        for user in response.json()['response']['players'][0].items():
            print(user)
        print()

        time.sleep(0.5)

    return lst_users


def get_global_achievement_percentages_for_app(game_id: int) -> dict | None:
    """
    Returns on global achievements overview of a specific game in percentages.

    :game_id <int>: Game ID.
    """
    url = f'https://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?' \
          f'gameid={game_id}&' \
          f'format=json'

    response = requests.get(url)

    if response.status_code >= 400:
        logger.warning(f'Game ID - {game_id}. '
                       f'Status code - {response.status_code}.')
        return None

    try:
        for achieve in response.json()['achievementpercentages']['achievements']:
            print(achieve)

    except Exception as _ex:
        logger.warning(f'Error is {_ex}. '
                       f'Function - get_global_achievement_percentages_for_app()')
        return None

    return response.json()


def get_news_for_app(app_id: int, count: int, max_length: int) -> dict | None:
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

    if response.status_code >= 400:
        logger.warning(f'App ID - {app_id}. '
                       f'Count - {count}. '
                       f'Max Length - {max_length}. '
                       f'Status code - {response.status_code}.')
        return None

    for news in response.json()['appnews']['newsitems']:
        for article in news.items():
            print(article)

        print()

    return response.json()


def get_friend_list(steam_id: int, relationship: str) -> dict | None:
    """
    Returns the friend list of any Steam user,
    provided their Steam Community profile visibility is set to “Public”.

    :steam_id <int>: User ID.
    :relationship <str>: Relationship filter. Possibles values: all, friend.
    """

    url = f'https://api.steampowered.com/ISteamUser/GetFriendList/v0001/?' \
          f'key={settings.key}&' \
          f'steamid={steam_id}&' \
          f'relationship={relationship}'

    response = requests.get(url)

    if response.status_code >= 400:
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


def get_player_achievements(steam_id: int, app_id: int) -> dict | None:
    """
    Returns a list of achievements for this user by app ID.

    :steam_id <int>: 64 bit Steam ID to return friend list for.
    :app_id <int>: The ID for the game you're requesting.
    """

    url = f'https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?' \
          f'appid={app_id}&' \
          f'key={settings.key}&' \
          f'steamid={steam_id}'

    response = requests.get(url)

    if response.status_code >= 400:
        logger.warning(f'Key - {str(settings.key)[:6]}... '
                       f'Steam ID - {steam_id}. '
                       f'App ID - {app_id}. '
                       f'Status code - {response.status_code}.')
        return None

    print('Name:', response.json()['playerstats']['gameName'])
    print()

    for achievement in response.json()['playerstats']['achievements']:
        print(achievement)

    print()

    return response.json()


def get_user_stats_for_game(steam_id: int, app_id: int) -> dict | None:
    """
    Returns a list of achievements for this user by app ID.

    :steam_id <int>: 64 bit Steam ID to return friend list for.
    :app_id <int>: The ID for the game you're requesting.
    """

    url = f'https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?' \
          f'appid={app_id}&' \
          f'key={settings.key}&' \
          f'steamid={steam_id}'

    response = requests.get(url)

    if response.status_code >= 400:
        logger.warning(f'Key - {str(settings.key)[:6]}... '
                       f'Steam ID - {steam_id}. '
                       f'App ID - {app_id}. '
                       f'Status code - {response.status_code}.')
        return None

    if not response.json()['playerstats'].get('achievements', False):
        logger.warning(f'Key - {str(settings.key)[:6]}... '
                       f'App ID - {app_id}. '
                       f'User ID - {steam_id} doesn\'t have a game {app_id}.')
        return None

    print('Name:', response.json()['playerstats']['gameName'])
    print()

    for achievement in response.json()['playerstats']['achievements']:
        print(achievement)

    print()

    return response.json()


def get_owned_games(steam_id: int) -> dict | None:
    """
    Return a list of games a player owns along with some playtime information,
    if the profile is publicly visible.
    Private, friends-only, and other privacy settings are not supported unless
    you are asking for your own personal details
    (ie the WebAPI key you are using is linked to the steamid you are requesting).

    :steam_id <int>: The SteamID of the account.
    """
    url = f'https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?' \
          f'key={settings.key}&' \
          f'steamid={steam_id}&' \
          f'include_played_free_games=1&' \
          f'include_appinfo=1'

    response = requests.get(url)

    if response.status_code >= 400:
        logger.warning(f'Key - {str(settings.key)[:6]}... '
                       f'Steam ID - {steam_id}. '
                       f'Status code - {response.status_code}.')
        return None

    if not response.json()['response']:
        logger.warning(f'Steam ID - {steam_id}. Response is empty.')
        return None

    print(f'Games count - {response.json()["response"]["game_count"]}')
    print()

    for game in response.json()['response']['games']:
        print(game)

    print()

    return response.json()


def get_recently_played_games(steam_id: int, count: int) -> dict | None:
    """
    Return a list of games a player has played in the last two weeks,
    if the profile is publicly visible.
    Private, friends-only, and other privacy settings are not supported
    unless you are asking for your own personal details
    (ie the WebAPI key you are using is linked to the steamid you are requesting).

    :steam_id <int>: The SteamID of the account.
    :count <int>: Optionally limit to a certain number of games
    (the number of games a person has played in the last 2 weeks is typically very small).
    """

    url = f'https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?' \
          f'key={settings.key}&' \
          f'steamid={steam_id}&' \
          f'count={count}&' \
          f'format=json'

    response = requests.get(url)

    if response.status_code >= 400:
        logger.warning(f'Key - {str(settings.key)[:6]}... '
                       f'Steam ID - {steam_id}. '
                       f'Count - {count}. '
                       f'Status code - {response.status_code}.')
        return None

    if not response.json()['response']['total_count']:
        logger.warning(f'Key - {str(settings.key)[:6]}... '
                       f'Count - {count}. '
                       f'Steam ID - {steam_id} has not played recently')
        return None

    print('Games count -', response.json()['response']['total_count'])
    print()

    for game in response.json()['response']['games']:
        print(game)

    print()

    return response.json()


def main():
    try:
        # get_player_summaries(76561197963562688)
        # get_players_summaries([76561197963562688, 76561197963562688])
        # get_global_achievement_percentages_for_app(440)
        # get_news_for_app(440, 3, 300)
        # get_friend_list(76561197960435530, 'all')
        # get_player_achievements(76561199087475515, 1091500)
        # get_user_stats_for_game(76561199087475515, 1091500)
        # get_owned_games(76561199087475515)
        # get_recently_played_games(76561199087475515, 3)
        pass

    except Exception as _ex:
        logger.critical(f'Error is {_ex}. '
                        f'Function - main()')


if __name__ == '__main__':
    main()
