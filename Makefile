PYTHON = python3

SRC = MWST.py

EXEC = MWST

.PHONY: all clean

all: $(EXEC)

$(EXEC): $(SRC)
	echo "#!/bin/bash\n$(PYTHON) $(SRC) \$$1 \$$2" > $(EXEC)
	chmod +x $(EXEC)

clean:
	rm -f $(EXEC)
