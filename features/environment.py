import requests


def after_scenario(context, scenario):
    if "library" in scenario.tags:
        delete_response = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={"ID": context.bookID},
                                        headers={"Content-Type": "application/json"}, )

        print("Delete status is {}".format(delete_response.status_code))
        assert delete_response.status_code == 200
        res_json = delete_response.json()

        print(res_json["msg"])
