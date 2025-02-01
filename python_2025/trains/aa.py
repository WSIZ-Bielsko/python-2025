class Train:

    def __init__(self, tid: int, name: str):
        tid: int
        name: str

    def get_wifi(self) -> str:
        return 'N/A'


class ExpressTrain(Train):

    def __init__(self, tid: int, name: str, wifi_ssid: str):
        super().__init__(tid, name)
        self.wifi_ssid = wifi_ssid

    def get_wifi(self) -> str:
        return self.wifi_ssid

    def get_other_wifi(self) -> str:
        return super().get_wifi()

if __name__ == '__main__':
    et = ExpressTrain(11, 'mumbai express', 'mumbai001')
    print(et.get_wifi())
    print(et.get_other_wifi())
