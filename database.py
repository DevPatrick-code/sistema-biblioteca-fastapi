from sqlalchemy import create_engine
from configs import DATABASE_URL, POOL_SIZE

engine = create_engine(DATABASE_URL, pool_size=POOL_SIZE)