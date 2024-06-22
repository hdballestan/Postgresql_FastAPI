#!/bin/bash

echo "Seleccione una opción:"
echo "1. Crear la base de datos y el usuario sin Docker."
echo "2. Crear la base de datos y el usuario usando Docker."

read -p "Ingrese su opción (1 o 2): " option

# Función para configurar la base de datos sin Docker
setup_database() {
	DB_NAME="name_db"
	DB_USER="name_user"
	DB_PASSWORD="some"

	# Crear la base de datos
	psql -c "CREATE DATABASE $DB_NAME;"

	# Crear el usuario y asignar privilegios
	psql -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';"
	psql -c "ALTER DATABASE $DB_NAME OWNER TO $DB_USER;"
	psql -c "ALTER USER $DB_USER WITH SUPERUSER;"
	psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"

	echo "Base de datos configurada correctamente."
}

# Usando Docker
setup_database_with_docker() {
	read -p "Ingrese el ID o nombre del contenedor de Docker: " container_name

	export DB_NAME="name_db"
	export DB_USER="name_user"
	export DB_PASSWORD="some"

	docker exec -it "$container_name" bash -c "psql -U postgres -c \"CREATE DATABASE $DB_NAME;\""
	docker exec -it "$container_name" bash -c "psql -U postgres -c \"CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';\""
	docker exec -it "$container_name" bash -c "psql -U postgres -c \"ALTER DATABASE $DB_NAME OWNER TO $DB_USER;\""
	docker exec -it "$container_name" bash -c "psql -U postgres -c \"ALTER USER $DB_USER WITH SUPERUSER;\""
	docker exec -it "$container_name" bash -c "psql -U postgres -c \"GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;\""

	echo "Base de datos configurada correctamente con Docker."
}

if [ "$option" == "1" ]; then
	setup_database
elif [ "$option" == "2" ]; then
	setup_database_with_docker
else
	echo "Opción no válida. Seleccione 1 o 2."
fi
