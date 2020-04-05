from mycroft import MycroftSkill, intent_file_handler


class GasStationPrice(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('price.station.gas.intent')
    def handle_price_station_gas(self, message):
        self.speak_dialog('price.station.gas')


def create_skill():
    return GasStationPrice()

