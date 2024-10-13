from users.models import User
from .models import Tweet
from rest_framework.test import APITestCase
from . import models

class TestTweets(APITestCase):

    PAYLOAD = "Tweets Des"

    URL = "/api/v1/tweets/"

    def setUp(self):

        self.user = User.objects.create(username="testuser")

        models.Tweet.objects.create(
            user=self.user,
            payload=self.PAYLOAD,
        )

    def test_all_tweets(self):

        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200.",
        )
        self.assertIsInstance(
            data,
            list,
        )
        self.assertEqual(
            len(data),
            1,
        )

        self.assertEqual(
            data[0]["user"],
            self.user.id,
        )
        self.assertEqual(
            data[0]["payload"],
            self.PAYLOAD,
        )

    def test_create_tweet(self):

        PAYLOAD = "Tweets Des"

        response = self.client.post(
            self.URL,
            data={
                "user": self.user.id,
                "payload": PAYLOAD,
            },
        )
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )
        self.assertEqual(
            data["user"],
            self.user.id,
        )
        self.assertEqual(
            data["payload"],
            PAYLOAD,
        )

        response = self.client.post(self.URL)
        data = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertIn("user", data)

class TestTweet(APITestCase):

    PAYLOAD = "This is a test tweet"

    def setUp(self):

        self.user = User.objects.create(username="testuser")

        Tweet.objects.create(
            payload=self.PAYLOAD,
            user=self.user,
        )

    def test_tweet_not_found(self):

        response = self.client.get("/api/v1/tweets/2")
        self.assertEqual(response.status_code, 404)

    def test_get_tweet(self):

        response = self.client.get("/api/v1/tweets/1")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["payload"], self.PAYLOAD)
        self.assertEqual(data["user"], self.user.id)

    def test_update_tweet(self):

        self.client.force_authenticate(user=self.user)

        response = self.client.put(
            "/api/v1/tweets/1",
            data={
                "payload": self.PAYLOAD,
                "user": self.user.id, 
            },
        )
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["payload"], self.PAYLOAD)
        self.assertEqual(data["user"], self.user.id)

    def test_delete_tweet(self):

        response = self.client.delete("/api/v1/tweets/1")

        self.assertEqual(response.status_code, 204)