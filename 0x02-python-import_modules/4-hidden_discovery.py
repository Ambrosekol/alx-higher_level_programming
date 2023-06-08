#!/usr/bin/python3
if __name__ == "__main__":
    import importlib
    mod = importlib.import_module("hidden_4")
    names = [name for name in dir(mod)
             if not name.startswith("__")]
    for name in sorted(names):
        print(name)

