./backend.sh

cd ../frontend
docker-compose up -d --build

echo "Startup successful... AlgoShell is online."