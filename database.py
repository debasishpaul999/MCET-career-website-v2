from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:root@localhost/mcet_career?charset=utf8mb4")

def load_jobs_from_db():
        with engine.connect() as conn:
            result=conn.execute(text("select * from jobs"))
            jobs=[]
            for row in result.all():
                jobs.append(row._mapping)
            return jobs




    # print("type(result): ",type(result))
    # result_all = result.all()
    # print("type(result_all): ",type(result_all))
    # first_result = result_all[0]
    # print("type(first_result): ",type(result_all[0]))
    # first_result_dict = result_all[0]._asdict()
    # print("type(first_result_dict): ",type(first_result_dict))
    # print(first_result_dict)