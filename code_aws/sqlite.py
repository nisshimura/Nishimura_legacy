import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('sqlite:///sample_db.sqlite3',echo=True)

Base = declarative_base()

class Sophia(Base):
    id = Column(Integer)
    name = Column(String, primary_key=True)

    __tablename__ = 'Sophia'

Base.metadata.create_all(bind=engine)
session = sessionmaker(bind=engine)()

#追加
# sakoda, nishimura = Sophia()
# sakoda.id　= , 4 
# sakoda.name = 'sakoda'
# session.add_all(instances=[Sophia(id=4, name='nishimura'),Sophia(id=5, name='okuno')])
# session.commit()

#出力
# query_result = session.query(Sophia)
# for Sophia in query_result:
#     print(Sophia.id, Sophia.name)

#出力条件指定
# sakodas = session.query(Sophia).filter_by(name='sakoda')
# sakodas = session.query(Sophia).filter(Sophia.name != 'nishimura')
# sakodas = session.query(Sophia).filter(Sophia.id > 2)
# sakodas = session.query(Sophia).filter((Sophia.id == 3) | (Sophia.id == 4))
# sakodas = session.query(Sophia).filter((Sophia.id == 3) & (Sophia.id == 4))
# sakodas = session.query(Sophia).filter(Sophia.name.like('%a%'))

## sakoda = session.query(Sophia).filter_by(name='sakoda').one()
# ## sakoda = session.query(Sophia).filter_by(name='sakoda').limit(2)
# sakodas = session.query(Sophia).order_by(Sophia.id.desc()).limit(4) #asc()

# for sakoda in sakodas:
#     print(sakoda.id, sakoda.name)

# nishimura = session.query(Sophia).filter_by(id=4).one()
# nishimura.name = 'nishimuratakayuki'
# session.commit()
## session一回しか使えない ##

nishimura = session.query(Sophia).filter_by(name='nishimuratakayuki').one()
session.delete(nishimura)
session.commit()

session.close()




