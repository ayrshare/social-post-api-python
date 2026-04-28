import unittest

from ayrshare import SocialPost


KEY_HEADER = 'X-Twitter-OAuth1-Api-Key'
SECRET_HEADER = 'X-Twitter-OAuth1-Api-Secret'


class TwitterBYOHeadersTest(unittest.TestCase):
    def test_headers_absent_when_byo_never_set(self):
        social = SocialPost('API_KEY')
        self.assertNotIn(KEY_HEADER, social.headers)
        self.assertNotIn(SECRET_HEADER, social.headers)

    def test_set_twitter_byo_injects_both_headers(self):
        social = SocialPost('API_KEY')
        social.set_twitter_byo('ck_123', 'cs_456')
        self.assertEqual(social.headers[KEY_HEADER], 'ck_123')
        self.assertEqual(social.headers[SECRET_HEADER], 'cs_456')

    def test_clear_twitter_byo_removes_both_headers(self):
        social = SocialPost('API_KEY')
        social.set_twitter_byo('ck_123', 'cs_456')
        social.clear_twitter_byo()
        self.assertNotIn(KEY_HEADER, social.headers)
        self.assertNotIn(SECRET_HEADER, social.headers)

    def test_clear_twitter_byo_is_noop_when_nothing_set(self):
        social = SocialPost('API_KEY')
        # Should not raise even when nothing is set.
        social.clear_twitter_byo()
        self.assertNotIn(KEY_HEADER, social.headers)

    def test_setters_are_chainable(self):
        social = SocialPost('API_KEY')
        self.assertIs(social.set_twitter_byo('a', 'b'), social)
        self.assertIs(social.clear_twitter_byo(), social)

    def test_byo_coexists_with_profile_key(self):
        social = SocialPost('API_KEY')
        social.setProfileKey('PK').set_twitter_byo('ck', 'cs')
        self.assertEqual(social.headers['Profile-Key'], 'PK')
        self.assertEqual(social.headers[KEY_HEADER], 'ck')
        self.assertEqual(social.headers[SECRET_HEADER], 'cs')

    def test_instances_have_independent_byo_state(self):
        a = SocialPost('A').set_twitter_byo('a_k', 'a_s')
        b = SocialPost('B')
        self.assertNotIn(KEY_HEADER, b.headers)
        self.assertEqual(a.headers[KEY_HEADER], 'a_k')


if __name__ == '__main__':
    unittest.main()
