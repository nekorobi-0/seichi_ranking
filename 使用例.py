import seichi_ranking
#標準でデイリーランキングの0~20位を取得します
print(seichi_ranking.ranking())
#週間建築ランキングの上位30人を表示そして単位を入れる
print(seichi_ranking.ranking(duration="weekly",ranking_type="build",lim=30,unit=True))
#普通にランキング
print(seichi_ranking.ranking(duration="",lim=150))
#unchamaの整地量
print(seichi_anking.get_data(mcid=unchama))
#unchamaの建築量
print(seichi_ranking.gst_data(mcid=unchama,data_type=build))
