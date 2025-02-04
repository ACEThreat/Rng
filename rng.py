import rumps
import random
import sys

class RandomNumberApp(rumps.App):
    def __init__(self):
        try:
            print("Initializing app...")
            super(RandomNumberApp, self).__init__("RNG")
            self.timer = rumps.Timer(self.update_number, 2)
            print("Starting timer...")
            self.timer.start()
        except Exception as e:
            print(f"Error during initialization: {e}", file=sys.stderr)
            raise

    def update_number(self, _):
        try:
            new_number = str(random.randint(1, 100))
            print(f"Updating number to: {new_number}")
            self.title = new_number
        except Exception as e:
            print(f"Error updating number: {e}", file=sys.stderr)

if __name__ == "__main__":
    try:
        print("Starting app...")
        RandomNumberApp().run()
    except Exception as e:
        print(f"Failed to start app: {e}", file=sys.stderr)
