from saleae.range_measurements import AnalogMeasurer

class VoltageStartAndEnd(AnalogMeasurer):
    supported_measurements = ["v_start", "v_end"]

    def __init__(self, requested_measurements):
        super().__init__(requested_measurements)
        self.start = None
        self.last_batch = None

    def process_data(self, data):
        if self.start is None:
            self.start = data.samples[0]
        self.last_batch = data

    def measure(self):
        return {
            "v_start": self.start,
            "v_end": self.last_batch.samples[-1]
        }
