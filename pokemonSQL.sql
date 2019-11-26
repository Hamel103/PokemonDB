
DROP TABLE Account_xref, Customer,  Transaction_log, Account;

CREATE TABLE Customer (
  customer_id VARCHAR(32) PRIMARY KEY,
  ssn INT,
  first_name VARCHAR(50),
  last_name VARCHAR(50)
);

CREATE TABLE Account (
  account_num VARCHAR(32) PRIMARY KEY,
  account_type VARCHAR(50),
  balance DECIMAL(15,2)
);

CREATE TABLE Account_xref (
  customer_id VARCHAR(32) NOT NULL,
  account_num VARCHAR(32) NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
  FOREIGN KEY (account_num) REFERENCES Account(account_num)
  ON UPDATE NO ACTION
  ON DELETE CASCADE
);

CREATE TABLE Transaction_log (
  trans_timestamp VARCHAR(50),
  trans_id VARCHAR(32) PRIMARY KEY,
  account_num VARCHAR(32) NOT NULL,
  trans_type VARCHAR(50),
  trans_amount DECIMAL(15,2),
  FOREIGN KEY (account_num) REFERENCES Account(account_num)
  ON UPDATE NO ACTION
  ON DELETE CASCADE
);
