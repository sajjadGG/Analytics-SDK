from Hub import get_client, init

init()
sc = get_client()


class Game:

    with sc:  # capture Exception

        def achivement():
            sc.capture_message("sdasd")
