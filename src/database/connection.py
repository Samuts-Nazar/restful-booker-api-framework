import logging
from typing import Any
import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Eclipse Adoptium\jdk-17.0.19.10-hotspot"
import jaydebeapi

class DatabaseConnection:
    def __init__(self, jdbc_url: str, driver_class: str, jar_path: str, username: str, password: str):
        self.jdbc_url = jdbc_url
        self.driver_class = driver_class
        self.jar_path = jar_path
        self.username = username
        self.password = password
        self.connection = None
    
    def connect(self) -> Any:
        if self.connection is None:
            try:
                self.connection = jaydebeapi.connect(
                    self.driver_class,
                    self.jdbc_url,
                    [self.username, self.password],
                    self.jar_path
                )
            except Exception as e:
                logging.error(f"Failed to connect to the database: {e}")
                raise
        return self.connection

    def cursor(self):
        if self.connection:
            return self.connection.cursor()
        raise ValueError("No active database connection")