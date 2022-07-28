from flanelinha_veloz.persistence.abstractDAO import DAO


class SendReportDAO(DAO):
    def __init__(self):
        super().__init__('/send_report.pkl')

    def add(self, date):
        super().add(1, date)

    def get(self):
        if isinstance(1, int):
            return super().get(1)

    def remove(self):
        if isinstance(1, int):
            return super().remove(1)
