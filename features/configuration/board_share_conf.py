import requests

def share_board(pstr_userId, pstr_user):

    try:

        url = "https://api.miro.com/v2/boards/" + pstr_userId + "/members"

        payload = {
            "emails": [pstr_user],
            "role": "editor"
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": "Bearer eyJtaXJvLm9yaWdpbiI6ImV1MDEifQ_anBLvIHLXPGFLb0a1g1vUNalIaM"
        }

        response = requests.post(url, json=payload, headers=headers)
        return response
    except Exception as e:
        print ("An Exception occurred:" + str(e))
