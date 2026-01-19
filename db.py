from sqlalchemy import create_engine, text,inspect
import os
from dotenv import load_dotenv  
load_dotenv()    # 只在本地开发时生效, 容器内无 .env 文件也不会报错
DATABASE_URL = os.getenv("DATABASE_URL") or os.getenv("DATABASE_URL_LOCAL")

# DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(
    DATABASE_URL,
    pool_size=5,           # 连接池大小(个人用够了)
    max_overflow=10, # 连接池溢出大小
    pool_timeout=30,# 连接池超时时间
    pool_pre_ping=True,    # 自动检测无效连接
    echo=False             # 设 True 可看到 SQL 日志, 调试用
)


#🌞打印所有表名, 列名,默认表名为 user_table
def all_table_name(table_name=None):
    print('所有表名:', inspect(engine).get_table_names())
    if table_name is not None:        
        print('默认表列名:', [c['name'] for c in inspect(engine).get_columns(table_name)] )

# all_table_name()


def fetch_sql(sql_command):
    with engine.connect() as conn:
        result = conn.execute(text(sql_command))
        return [dict(row._mapping) for row in result]

# print(fetch_sql("SELECT * FROM taobao_stock_qty"))