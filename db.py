from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mysql+pymysql://3fqKJnm2X242V6J.root:<PASSWORD>@gateway01.ap-northeast-1.prod.aws.tidbcloud.com:4000/sys?ssl_ca=<CA_PATH>&ssl_verify_cert=true&ssl_verify_identity=true"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True, 
    connect_args={
        "ssl": {
            "ssl": True
        }
    }
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()