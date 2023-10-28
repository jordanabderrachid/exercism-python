from typing import Any


class InputCell:
    def __init__(self, initial_value):
        self.callbacks = []
        self.value = initial_value

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def __setattr__(self, __name: str, __value: Any) -> None:
        super.__setattr__(self, __name, __value)

        if __name == "value":
            for c in self.callbacks:
                c(__value)


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.callbacks = []
        self.inputs = inputs
        self.compute_function = compute_function
        self.memoized_cb_value = self.value
        for input in inputs:
            input.add_callback(self._on_input_change)

    def __getattr__(self, __name: str) -> Any:
        if __name == "value":
            return self.compute_function([input.value for input in self.inputs])

    def _on_input_change(self, value):
        new_value = self.value
        if new_value != self.memoized_cb_value:
            for c in self.callbacks:
                c(new_value)

        self.memoized_cb_value = new_value

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        if callback in self.callbacks:
            self.callbacks.remove(callback)
