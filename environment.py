from decouple import config, Csv

DB_NAME_ = config('DB_NAME')
DB_USER_ = config('DB_USER')
DB_PASSWORD_ = config('DB_PASSWORD')
DB_HOST_ = config('DB_HOST')
DB_PORT_ = config('DB_PORT', default='5432')
