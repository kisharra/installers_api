from sqlalchemy import MetaData, Table, select
from sqlalchemy import create_engine
import logging



class SelectInfo():
    def __init__(self):
        self.DSN = "mysql+pymysql://root:kisharra@localhost:3306/api_test"
        self.engine = create_engine(self.DSN)
        self.log_file = 'logs.log'
        self.metadata = MetaData()
        self.register_task = Table('register_task', self.metadata, autoload_with=self.engine)
        self.contract = Table('contract', self.metadata, autoload_with=self.engine)
        logging.basicConfig(filename=self.log_file, level=logging.ERROR, format='%(asctime)s:%(message)s')  #logging to file


    def get_fault(self):
        try:
            with self.engine.connect() as conn:
                info_tasks = conn.execute(
                    select(
                        self.contract.c.comment.label('contract_comment'),
                        self.register_task.c.comment 
                    ).join(
                        self.contract, self.register_task.c.cid == self.contract.c.id 
                    ).where(
                        self.register_task.c.status == 0,
                        self.register_task.c.type == 2,
                        self.register_task.c.gr == 1
                    )
                ).fetchall()
                faults = {}

                for row in info_tasks:
                    faults[row.contract_comment] = row.comment

                return faults

        except Exception as e:
            logging.error(e)


    def get_install_without_cable(self):
        try:
            with self.engine.connect() as conn:
                info_tasks = conn.execute(
                    select(
                        self.contract.c.comment.label('contract_comment'),
                        self.register_task.c.comment 
                    ).join(
                        self.contract, self.register_task.c.cid == self.contract.c.id 
                    ).where(
                        self.register_task.c.status == 0,
                        self.register_task.c.type == 1,
                        self.register_task.c.gr == 2
                    )
                ).fetchall()

                install_without_cable = {}

                for row in info_tasks:
                    install_without_cable[row.contract_comment] = row.comment

                return install_without_cable
        except Exception as e:
            logging.error(e)
    
    def get_install_with_cable(self):
        try:
            with self.engine.connect() as conn:
                info_tasks = conn.execute(
                    select(
                        self.contract.c.comment.label('contract_comment'),
                        self.register_task.c.comment 
                    ).join(
                        self.contract, self.register_task.c.cid == self.contract.c.id 
                    ).where(
                        self.register_task.c.status == 0,
                        self.register_task.c.type == 1,
                        self.register_task.c.gr == 1
                    )
                ).fetchall()

                install_with_cable = {}

                for row in info_tasks:
                    install_with_cable[row.contract_comment] = row.comment

                return install_with_cable
        except Exception as e:
            logging.error(e)

if __name__ == '__main__':
    pass
