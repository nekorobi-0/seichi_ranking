import requests,json
def ranking(duration="daily",ranking_type="break",offset=0,lim=20,unit=False):
    try:
        resp = requests.get(f'https://w4.minecraftserver.jp/api/ranking?type={ranking_type}k&offset={offset}&lim={lim}&duration={duration}')
        data_json = json.loads(resp.text)
        rank_list = list(data_json["ranks"])
        rank = 1
        for mcid_data in rank_list:
            get_mcid = mcid_data["player"]
            get_data = mcid_data["data"]
            seichi_ryo = get_data["raw_data"]
            name = get_mcid["name"]
            if unit == True:
                if len(str(seichi_ryo)) > 8:
                    seichi_ryo_kugiri0 = str(seichi_ryo)[-4:]
                    seichi_ryo_kugiri1 = str(seichi_ryo)[-8:-4]
                    seichi_ryo_kugiri2 = str(seichi_ryo)[:-8]
                    seichi_ryo = f"{seichi_ryo_kugiri2}億{seichi_ryo_kugiri1}万{seichi_ryo_kugiri0}"
                elif len(str(seichi_ryo)) > 4:
                    seichi_ryo_kugiri0 = str(seichi_ryo)[-4:]
                    seichi_ryo_kugiri1 = str(seichi_ryo)[:-4]
                    seichi_ryo = seichi_ryo_kugiri1 + "万" + seichi_ryo_kugiri0
            msg += f"{rank}位 {name} 整地量:{seichi_ryo}\n"
            rank += 1
        return msg
    except:
        text = "引数が無効または整地鯖APIが死んでます"
        return text
def get_data(mcid=None,uuid=None,data_type="break",type_data_type="data"):
    try:
        if mcid != None:
            resp = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{mcid}')
            data_json = json.loads(resp.text)
            uuid_before = data_json["id"]
            uuid = uuid_before[0:8]
            uuid += "-"
            uuid += uuid_before[8:12]
            uuid += "-"
            uuid += uuid_before[12:16]
            uuid += "-"
            uuid += uuid_before[16:20]
            uuid += "-"
            uuid += uuid_before[20:32]
            print(uuid)
            print(f'https://w4.minecraftserver.jp/api/ranking/player/{uuid}?types={data_type}')
            resp = requests.get(f'https://w4.minecraftserver.jp/api/ranking/player/{uuid}?types={data_type}')
            data_json = json.loads(resp.text)
            if type_data_type == "data":
                data = data_json[0]["data"]["raw_data"]
                return data
            if type_data_type == "lastquit":
                return data_json[0]["lastquit"]
        elif uuid != None:
            resp = requests.get(f'https://w4.minecraftserver.jp/api/ranking/player/{uuid}?types={data_type}')
            data_json = json.loads(resp.text)
            if type_data_type == "data":
                return data_json[0]["data"]["raw_data"]
            if type_data_type == "lastquit":
                return data_json[0]["lastquit"]
    except:
        text = "引数が無効または整地鯖APIが死んでます"
        return text
#必須ライブラリ
#json
#reqests
#インストールコマンド
#py -m pip install json
#py -m pip install reqests
#私のdiscord鯖
#https://discord.gg/Gs7VXE
#私のdiscord垢
#neruhito#6113
#672910471279673358