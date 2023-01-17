"""
Some tests may fall due to the lack of relevance of the time
or changes to the settings in the account of a certain user.

For example, some tests depend on user settings - these tests will fall.
Either the game's achievements have changed,
or this game is unavailable, etc.
"""
import unittest

import main


class TestGetPlayerSummaries(unittest.TestCase):
    def test_is_none(self):
        user1 = 16561199087475515
        user2 = 66561199087475515

        test1 = main.get_player_summaries(user1)
        test2 = main.get_player_summaries(user2)

        self.assertIsNone(test1)
        self.assertIsNone(test2)

    def test_is_not_none(self):
        user1 = 76561199087475515
        user2 = 76561198947093586

        test1 = main.get_player_summaries(user1)
        test2 = main.get_player_summaries(user2)

        self.assertIsNotNone(test1['response'])
        self.assertIsNotNone(test2['response'])


class TestGetPlayersSummaries(unittest.TestCase):
    def test_list_is_none(self):
        users = [16561199087475515, 66561199087475515]

        test1 = main.get_players_summaries(users)

        self.assertEqual([], test1)

    def test_list_is_not_none(self):
        users = [76561199087475515, 76561198947093586]

        test1 = main.get_players_summaries(users)

        self.assertIsNotNone(test1[0]['response'])


class TestGetFriendList(unittest.TestCase):
    def test_user_is_none(self):
        user1 = 16561199087475515
        user2 = 66561199087475515

        test1 = main.get_friend_list(user1, 'all')
        test2 = main.get_friend_list(user2, 'friend')

        self.assertIsNone(test1)
        self.assertIsNone(test2)

    def test_relationship_is_wrong(self):
        user1 = 76561199087475515
        user2 = 76561198947093586

        test1 = main.get_friend_list(user1, 'no')
        test2 = main.get_friend_list(user2, 'hello')

        self.assertIsNone(test1)
        self.assertIsNone(test2)

    def test_correct_answer(self):
        user1 = 76561199087475515
        user2 = 76561198947093586

        test1 = main.get_friend_list(user1, 'all')
        test2 = main.get_friend_list(user2, 'friend')

        self.assertIsNotNone(test1['friendslist']['friends'])
        self.assertIsNotNone(test2['friendslist']['friends'])


class TestGetPlayerAchievements(unittest.TestCase):
    def test_user_is_wrong(self):
        user1 = 16561199087475515
        user2 = 66561199087475515

        test1 = main.get_player_achievements(user1, 440)
        test2 = main.get_player_achievements(user2, 1091500)

        self.assertIsNone(test1)
        self.assertIsNone(test2)

    def test_application_is_wrong(self):
        user1 = 76561199087475515
        user2 = 76561198947093586

        test1 = main.get_player_achievements(user1, 1)
        test2 = main.get_player_achievements(user2, 145123413)

        self.assertIsNone(test1)
        self.assertIsNone(test2)

    def test_correct_data(self):
        user1 = 76561199087475515
        user2 = 76561198947093586

        test1 = main.get_player_achievements(user1, 440)
        test2 = main.get_player_achievements(user2, 440)

        self.assertIsNotNone(test1['playerstats']['achievements'])
        self.assertIsNotNone(test2['playerstats']['achievements'])


class TestGetOwnedGames(unittest.TestCase):
    def test_user_is_wrong(self):
        user1 = 16561199087475515
        user2 = 66561199087475515

        test1 = main.get_owned_games(user1)
        test2 = main.get_owned_games(user2)

        self.assertIsNone(test1)
        self.assertIsNone(test2)

    def test_correct_user_id(self):
        user1 = 76561199087475515
        user2 = 76561198947093586

        test1 = main.get_owned_games(user1)
        test2 = main.get_owned_games(user2)

        self.assertIsNotNone(test1['response']['games'])
        self.assertIsNotNone(test2['response']['games'])


class TestGetGlobalAchievementPercentagesForApp(unittest.TestCase):
    def test_game_is_wrong(self):
        game1 = 413513
        game2 = 1091501
        game3 = 1

        test1 = main.get_global_achievement_percentages_for_app(game1)
        test2 = main.get_global_achievement_percentages_for_app(game2)
        test3 = main.get_global_achievement_percentages_for_app(game3)

        self.assertIsNone(test1)
        self.assertIsNone(test2)
        self.assertIsNone(test3)

    def test_game_is_correct(self):
        game1 = 440
        game2 = 1091500
        game3 = 292030

        test1 = main.get_global_achievement_percentages_for_app(game1)
        test2 = main.get_global_achievement_percentages_for_app(game2)
        test3 = main.get_global_achievement_percentages_for_app(game3)

        self.assertIsNotNone(test1['achievementpercentages']['achievements'])
        self.assertIsNotNone(test2['achievementpercentages']['achievements'])
        self.assertIsNotNone(test3['achievementpercentages']['achievements'])


class TestGetNewsForApp(unittest.TestCase):
    def test_game_is_wrong(self):
        game1 = 413513
        game2 = 1091501
        game3 = 1

        test1 = main.get_news_for_app(game1, 4, 100)
        test2 = main.get_news_for_app(game2, 2, 4)
        test3 = main.get_news_for_app(game3, 5, 20)

        self.assertIsNone(test1)
        self.assertIsNone(test2)
        self.assertIsNone(test3)

    def test_count_is_correct(self):
        game1 = 292030
        game2 = 1091500
        game3 = 440

        test1 = main.get_news_for_app(game1, 1, 100)
        test2 = main.get_news_for_app(game2, 2, 4)
        test3 = main.get_news_for_app(game3, 3, 20)

        print(test3)

        self.assertEqual(1, len(test1['appnews']['newsitems']))
        self.assertEqual(2, len(test2['appnews']['newsitems']))
        self.assertEqual(3, len(test3['appnews']['newsitems']))

    def test_game_is_correct(self):
        game1 = 292030
        game2 = 1091500
        game3 = 440

        test1 = main.get_news_for_app(game1, 4, 100)
        test2 = main.get_news_for_app(game2, 2, 4)
        test3 = main.get_news_for_app(game3, 5, 20)

        self.assertIsNotNone(test1['appnews']['newsitems'])
        self.assertIsNotNone(test2['appnews']['newsitems'])
        self.assertIsNotNone(test3['appnews']['newsitems'])

    def test_count_of_symbols_is_correct(self):
        game1 = 1091500
        game2 = 440
        game3 = 292030

        test1 = main.get_news_for_app(game1, 3, 6)
        test2 = main.get_news_for_app(game2, 5, 35)
        test3 = main.get_news_for_app(game3, 3, 2)

        print(test1)
        print(test2)
        print(test3)

        # 9, 38 and 5, because an ellipsis is added to the lines.

        self.assertEqual(9, len(test1['appnews']['newsitems'][0]['contents']))
        self.assertEqual(38, len(test2['appnews']['newsitems'][0]['contents']))
        self.assertEqual(5, len(test3['appnews']['newsitems'][0]['contents']))


class TestGetRecentlyPlayedGames(unittest.TestCase):
    def test_user_is_wrong(self):
        user1 = 16561199087475515
        user2 = 66561199087475515

        test1 = main.get_recently_played_games(user1, 4)
        test2 = main.get_recently_played_games(user2, 2)

        self.assertIsNone(test1)
        self.assertIsNone(test2)

    def test_user_has_not_played_recently(self):
        user1 = 76561198947093586

        test1 = main.get_recently_played_games(user1, 4)

        self.assertIsNone(test1)

    def test_data_is_correct(self):
        user1 = 76561199087475515

        test1 = main.get_recently_played_games(user1, 4)

        # I don't check for the presence of a specific amount games,
        # since the Steam API returns the last games that the user played and
        # if there are none, it will be 0, and if less than you specified,
        # then the amount how many the user played.

        self.assertIsNone(test1)


class TestGetUserStatsForGame(unittest.TestCase):
    def test_user_is_wrong(self):
        user1 = 16561199087475515
        user2 = 66561199087475515

        game1 = 1091500
        game2 = 440

        test1 = main.get_user_stats_for_game(user1, game1)
        test2 = main.get_user_stats_for_game(user2, game2)

        self.assertIsNone(test1)
        self.assertIsNone(test2)

    def test_game_is_wrong(self):
        user1 = 76561199087475515
        user2 = 76561198947093586

        game1 = 1091504
        game2 = 444

        test1 = main.get_user_stats_for_game(user1, game1)
        test2 = main.get_user_stats_for_game(user2, game2)

        self.assertIsNone(test1)
        self.assertIsNone(test2)

    def test_user_doesnt_have_game(self):
        user1 = 76561198947093586

        game1 = 1091500
        game2 = 440

        test1 = main.get_user_stats_for_game(user1, game1)
        test2 = main.get_user_stats_for_game(user1, game2)

        self.assertIsNone(test1)
        self.assertIsNone(test2)

    def test_data_is_correct(self):
        user1 = 76561199087475515

        game1 = 1091500

        test1 = main.get_user_stats_for_game(user1, game1)

        self.assertIsNotNone(test1['playerstats']['achievements'])


if __name__ == "__main__":
    unittest.main()
