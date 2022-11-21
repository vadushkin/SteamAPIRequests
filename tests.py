import unittest

from main import get_friend_list, get_players_summaries, \
    get_player_summaries


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
