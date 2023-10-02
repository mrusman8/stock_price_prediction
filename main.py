from data_scraper import DataScraping
from database import Database
from get_predictions import final_pipe


name = "ADAMS"
url = "https://dps.psx.com.pk/company/ADAMS"
ds = DataScraping()
db = Database(name)
ds.scrap(url)
db.insert_data_to_db(ds.values)
preds = final_pipe(db.fetch_data_from_db(200))
db.insert_preds_to_db(preds)

