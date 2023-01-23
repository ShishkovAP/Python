
class Report:

    def __init__(self, user_id, firstname, lastname, login):

        self.user_id    = user_id
        self.firstname  = firstname
        self.lastname   = lastname
        self.login      = login

    def get_user_id(self):
        return self.user_id


if __name__ == '__main__':
    def main():
        report = Report(313, 'Vadim', 'vas', 'vvs')

        return print(report.get_user_id())


main()