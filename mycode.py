from Hub import get_client, init
from Client import SimpleClinet

init()
sc = SimpleClinet()


class Game:

    with sc:  # capture Exception

        def achivement():
            sc.capture_message("sdasd")
