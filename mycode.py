from Hub import get_client, init
from Client import SimpleClinet, ExceptionClient

init()
sc = SimpleClinet()
ec = ExceptionClient()


class Game:

    with ec:  # capture Exception

        def achivement():
            sc.capture_message("sdasd")
