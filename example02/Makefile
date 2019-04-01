default: start

service:=ms-python-hello

.PHONY: start
start: 
	docker-compose up -d

.PHONY: stop
stop: 
	docker-compose down

.PHONY: restart
restart: stop start

.PHONY: ps
ps: 
	docker-compose ps

.PHONY: logs
logs:
	docker-compose logs -f

.PHONY: build
build:
	docker-compose build --no-cache

.PHONY: clean
clean: stop build start

.PHONY: install-package-in-container
install-package-in-container:
	docker-compose exec ${service} pip install -S ${package}
	docker-compose exec ${service} pip freeze > requirements.txt

.PHONY: add
add: install-package-in-container build	

.PHONY: deps
deps:
	docker-compose exec ${service} pip install -r requirements.txt	