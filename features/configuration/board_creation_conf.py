import requests



def boadr_creation(pstr_board):

    try:
        url = "https://api.miro.com/v2/boards"

        payload = {
            "name": pstr_board,
            "policy": {
                "permissionsPolicy": {
                    "collaborationToolsStartAccess": "all_editors",
                    "copyAccess": "anyone",
                    "sharingAccess": "team_members_with_editing_rights"
                },
                "sharingPolicy": {
                    "access": "private",
                    "inviteToAccountAndBoardLinkAccess": "no_access",
                    "organizationAccess": "private",
                    "teamAccess": "private"
                }
            }
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": "Bearer eyJtaXJvLm9yaWdpbiI6ImV1MDEifQ_anBLvIHLXPGFLb0a1g1vUNalIaM"
        }

        response = requests.post(url, json=payload, headers=headers)
        return response
        print(response.text)
    except Exception as e:
        print("An Exception occurred:" + str(e))