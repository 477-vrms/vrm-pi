def on_retrieve_position(arm_json) -> None:
    print(arm_json)


class ArmHandler:

    def __init__(self):
        pass

    def add_json(self, item):
        on_retrieve_position(arm_json=item)
