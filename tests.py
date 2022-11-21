"""
Some tests may fall due to the lack of relevance of the time
or changes to the settings in the account of a certain user.

For example, some tests depend on user settings - these tests will fall.
Either the game's achievements have changed,
or this game is unavailable, etc.
"""

import unittest

from main import get_friend_list, get_players_summaries, \
    get_player_summaries, get_player_achievements, get_owned_games, \
    get_global_achievement_percentages_for_app


class TestGetPlayerSummaries(unittest.TestCase):
    def test_is_none(self):
        user1 = 16561199087475515
        user2 = 66561199087475515

        test1 = get_player_summaries(user1)
        test2 = get_player_summaries(user2)

        self.assertIsNone(test1)
        self.assertIsNone(test2)

    def test_is_not_none(self):
        user1 = 76561199087475515
        user2 = 76561198947093586

        test1 = get_player_summaries(user1)
        test2 = get_player_summaries(user2)

        self.assertIsNotNone(test1['response'])
        self.assertIsNotNone(test2['response'])


class TestGetPlayersSummaries(unittest.TestCase):
    def test_list_is_none(self):
        users = [16561199087475515, 66561199087475515]

        test1 = get_players_summaries(users)

        self.assertEqual([], test1)

    def test_list_is_not_none(self):
        users = [76561199087475515, 76561198947093586]

        test1 = get_players_summaries(users)

        self.assertIsNotNone(test1[0]['response'])


class TestGetFriendList(unittest.TestCase):
    def test_user_is_none(self):
        user1 = 16561199087475515
        user2 = 66561199087475515

        test1 = get_friend_list(user1, 'all')
        test2 = get_friend_list(user2, 'friend')

        self.assertIsNone(test1)
        self.assertIsNone(test2)

    def test_relationship_is_wrong(self):
        user1 = 76561199087475515
        user2 = 76561198947093586

        test1 = get_friend_list(user1, 'no')
        test2 = get_friend_list(user2, 'hello')

        self.assertIsNone(test1)
        self.assertIsNone(test2)

    def test_correct_answer(self):
        user1 = 76561199087475515
        user2 = 76561198947093586

        test1 = get_friend_list(user1, 'all')
        test2 = get_friend_list(user2, 'friend')

        self.assertIsNotNone(test1['friendslist']['friends'])
        self.assertIsNotNone(test2['friendslist']['friends'])


class TestGetPlayerAchievements(unittest.TestCase):
    def test_user_is_wrong(self):
        user1 = 16561199087475515
        user2 = 66561199087475515

        test1 = get_player_achievements(user1, 440)
        test2 = get_player_achievements(user2, 1091500)

        self.assertIsNone(test1)
        self.assertIsNone(test2)

    def test_application_is_wrong(self):
        user1 = 76561199087475515
        user2 = 76561199087475515

        test1 = get_player_achievements(user1, 1)
        test2 = get_player_achievements(user2, 145123413)

        self.assertIsNone(test1)
        self.assertIsNone(test2)

    def test_correct_data(self):
        user1 = 76561199087475515
        user2 = 76561199087475515

        test1 = get_player_achievements(user1, 440)
        test2 = get_player_achievements(user2, 1091500)

        self.assertIsNotNone(test1['playerstats']['achievements'])
        self.assertIsNotNone(test2['playerstats']['achievements'])


class TestGetOwnedGames(unittest.TestCase):
    def test_user_is_wrong(self):
        user1 = 16561199087475515
        user2 = 66561199087475515

        test1 = get_owned_games(user1)
        test2 = get_owned_games(user2)

        self.assertIsNone(test1)
        self.assertIsNone(test2)

    def test_correct_user_id(self):
        user1 = 76561199087475515
        user2 = 76561199087475515

        test1 = get_owned_games(user1)
        test2 = get_owned_games(user2)

        self.assertIsNotNone(test1['response']['games'])
        self.assertIsNotNone(test2['response']['games'])


class TestGetGlobalAchievementPercentagesForApp(unittest.TestCase):
    def test_game_is_wrong(self):
        game1 = 413513
        game2 = 1091501
        game3 = 1

        test1 = get_global_achievement_percentages_for_app(game1)
        test2 = get_global_achievement_percentages_for_app(game2)
        test3 = get_global_achievement_percentages_for_app(game3)

        self.assertIsNone(test1)
        self.assertIsNone(test2)
        self.assertIsNone(test3)

    def test_game_is_correct(self):
        game1 = 440
        game2 = 1091500
        game3 = 292030

        test1 = get_global_achievement_percentages_for_app(game1)
        test2 = get_global_achievement_percentages_for_app(game2)
        test3 = get_global_achievement_percentages_for_app(game3)

        self.assertIsNotNone(test1['achievementpercentages']['achievements'])
        self.assertIsNotNone(test2['achievementpercentages']['achievements'])
        self.assertIsNotNone(test3['achievementpercentages']['achievements'])
