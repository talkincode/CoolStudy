import redis
import json
from datetime import datetime


class WordLearning:
    def __init__(self, redis_host='localhost', redis_port=6379, redis_db=0):
        self.client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

    def _get_word_key(self, word):
        return f"word:{word}"

    def add_word(self, word, meaning):
        word_key = self._get_word_key(word)
        word_data = {
            "word": word,
            "meaning": meaning,
            "study_count": 0,
            "test_success": 0,
            "test_failure": 0,
            "last_test_time": None
        }
        self.client.json().set(word_key, '$', word_data)

    def update_word(self, word, study_count=None, test_success=None, test_failure=None):
        word_key = self._get_word_key(word)
        if study_count is not None:
            self.client.json().set(word_key, '$.study_count', study_count)
        if test_success is not None:
            self.client.json().set(word_key, '$.test_success', test_success)
        if test_failure is not None:
            self.client.json().set(word_key, '$.test_failure', test_failure)
            self.client.json().set(word_key, '$.last_test_time', datetime.now().isoformat())

    def get_word(self, word):
        word_key = self._get_word_key(word)
        return self.client.json().get(word_key)

    def update_score_ranking(self, word):
        word_data = self.get_word(word)
        if word_data:
            # Calculate score based on study_count, test_success, test_failure, and time since last test
            score = self._calculate_score(word_data)
            self.client.zadd('word_scores', {word: score})

    def _calculate_score(self, word_data):
        """
        Calculate score based on study_count, test_success, test_failure, and time since last test.
        This method implements a simple scoring algorithm based on these factors.
        """
        study_count = word_data.get('study_count', 0)
        test_success = word_data.get('test_success', 0)
        test_failure = word_data.get('test_failure', 0)
        last_test_time = word_data.get('last_test_time')

        # Calculate time decay factor
        time_decay = 1
        if last_test_time:
            last_test_datetime = datetime.fromisoformat(last_test_time)
            time_since_last_test = (datetime.now() - last_test_datetime).total_seconds()
            # Assuming time decay is inversely proportional to the time since the last test
            # This is just a placeholder calculation and should be adjusted according to the memory curve
            time_decay = 1 / (1 + time_since_last_test / (24 * 3600))  # Example: decay over days

        # Example scoring formula
        score = (study_count + test_success - test_failure) * time_decay
        return score

    def get_highest_score_word(self):
        highest_score_words = self.client.zrevrange('word_scores', 0, 0)
        return highest_score_words[0].decode('utf-8') if highest_score_words else None
