all: assignment3

assignment3: assignment3.py
    echo -e "#!/bin/bash\npython3 $(CURDIR)/assignment3.py \$$1 \$$2" > assignment3
    chmod +x assignment3

clean:
    rm -f assignment3
