# documake
Simple YAML -> RST converted to be used with Sphinx. Made for documentation generation. Written in simple Python3.

## Usage
doc.yml:
```yml
file: doc.yml
function:
    1:
        id: fib
        name: Fibonacci function
        desc: Generates fibonacci number
        comp:
            1: 
                type: unsigned int
                name: n
```
and then:
```sh
./documake.py doc.yml doc.rst
```

## License:
Copyright 2021 Ayush Bardhan Tripathy  

documake is licensed under MIT License.  
See [LICENSE.md](LICENSE.md) for details.
