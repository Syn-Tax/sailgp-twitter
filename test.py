import twint

tweets = []
invalid_locations = ["Global", ""]
# dates = {"Sydney": ["201902010000", "201903020000"], "San Francisco": ["201904200000", "201905200000"], "New York": ["201906060000", "201907070000"], "Cowes": ["201907260000", "201908260000"]}
dates = {"Sydney": ["2019-02-01", "2019-03-02"], "San Francisco": ["2019-04-20", "2019-05-20"], "New York": ["2019-06-06", "2019-07-07"], "Cowes": ["2019-07-26", "2019-08-26"]}

c = twint.Config()
c.Since = dates["Cowes"][0]
c.Until = dates["Cowes"][1]
c.Search = "sailgp"
c.Store_json = True
c.Output = "Cowes.json"

twint.run.Search(c)