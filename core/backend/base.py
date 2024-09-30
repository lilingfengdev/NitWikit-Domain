from abc import abstractmethod


class DNS:
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def create_record(self, subdomain, record_type, record_value):
        pass

    def delete_record(self, subdomain):
        pass