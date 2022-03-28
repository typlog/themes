.PHONY: build update clean

update:
	@python3 build/update.py
	@python3 build/generate.py

build:
	@npm run build
	@cp -r data dist
	@cp names.json dist

clean:
	@rm -fr dist
