.PHONY:build
build:
	docker build -t pollme:latest .
.PHONY:nc
nc:
	docker build --no-cache -t pollme:latest .

.PHONY:run
run:
	docker kill pm || true 2>/dev/null
	docker rm pm || true 2>/dev/null
	docker run --name pm -p 80:5000 pollme:latest
