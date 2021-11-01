from sqlalchemy import create_engine

engine = create_engine('postgresql://username:password@hostname/mydatabase')
engine = create_engine('oracle://username:password@127.0.0.1:1521/sidname')
engine = create_engine('oracle://username:password@tnsname') # TNS 名で指定する

from sqlalchemy import *
engine = create_engine('oracle://scott:tiger@127.0.0.1:1521/sidname')

result = engine.execute("select 1, 'hello' from dual")

for row in result:
    print(row)