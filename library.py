import time
from messages import messages


class cleanerVk:
    def __init__(
            self,
            login,
            password,
            conversations_count=1,
            messages_count=1):
        self.offset = 86400
        self.sleep_coef = 1
        self.now_time = int(time.time())
        self.conversations_count = conversations_count
        self.messages_count = messages_count
        self.send_num = 10
        self.messages = messages(login, password)

    def getConversations(self):
        json_conversations = self.messages.method(
            "messages.getConversations", count=self.conversations_count)
        for node in json_conversations['response']['items']:
            yield node['conversation']['peer']['id']

    def getHistory(self, id):
        json_messages = self.messages.method(
            "messages.getHistory", user_id=id, count=self.messages_count)
        for node in json_messages['response']['items']:
            if node['from_id'] == self.messages.id and node['date'] >= self.now_time - self.offset:
                yield node['id']

    def getCandidates(self):
        for node in self.getConversations():
            for msg in self.getHistory(node):
                yield msg
                time.sleep(self.sleep_coef)

    def delete_messages(self, ids):
        ids = list(map(str, ids))
        self.messages.method(
            "messages.delete",
            message_ids=','.join(ids),
            delete_for_all=1)

    def deleteTraces(self):
        to_del = []
        for counter, candidate in enumerate(self.getCandidates()):
            to_del.append(candidate)
            if counter % self.send_num == 0 and counter != 0:
                self.delete_messages(to_del)
                to_del = []
        if to_del != '':
            self.delete_messages(to_del)
