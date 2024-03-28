from fastapi import FastAPI
from api import adsets, campaigns, groups
from database.database import create_all_tables

app = FastAPI()
create_all_tables()

app.include_router(adsets.router)
app.include_router(campaigns.router)
app.include_router(groups.router)
