import speedtest
import ifcfg
from config import CSV_SEP


class SpeedTest:
    def __init__(self):
        self.results = {}
    
    def test(self):
        speed = speedtest.Speedtest()
        speed.get_best_server()
        speed.download()
        speed.upload(pre_allocate=False)
        self.results = speed.results
        
        connections = []
        for name, interface in ifcfg.interfaces().items():
            if interface["inet"] is not None:
                connections.append(name)
        self.results.connections = connections

    def __str__(self):
        connections = ",".join(self.results.connections)
        return f'{self.results.timestamp}{CSV_SEP}{self.results.ping}{CSV_SEP}{self.results.download}{CSV_SEP}{self.results.upload}{CSV_SEP}{connections}{CSV_SEP}{str(self.results.dict())}\n'
