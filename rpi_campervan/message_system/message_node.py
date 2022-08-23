class Node:
    def __init__(self, sources, destinations, handlers) -> None:
        self.sources = sources
        self.destinations = destinations
        self.handlers = handlers

    def tick(self) -> None:
        for (source_name, source) in self.sources:
            for message in source:
                self._send_to_destinations(self.destinations, source_name, message)
                self._handle_message(self.handlers, message)

    def _send_to_destinations(self, destinations, source_name, message):
        for (destination_name, send_to_destination) in destinations:
            if (destination_name != source_name):
                send_to_destination(message)

    def _handle_message(self, handlers, message):
        for handle_message in handlers:
            handle_message(message)