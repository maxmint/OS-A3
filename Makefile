all: assignment3

assignment3: assignment3.py
    chmod +x assignment3.py
    echo -e "#!/bin/bash\npython3 $(CURDIR)/assignment3.py -l \$$1 -p \$$2" > assignment3
    chmod +x assignment3

clean:
    rm -f assignment3
