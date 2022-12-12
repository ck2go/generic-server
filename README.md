# MockServer

Python generic server implementation, with predefined request-answer pairs and different answering modes (e.g, 'normal', 'no response', 'fail test1').

**Status:**  Pre-Alpha (early development)
**Authors:** Carsten König

## Purpose

In order to test different network components in a lab environment, some components might not be available. In order to simulate their presence, MockServer answers requests with pre-defined answers. 

## Installation

```bash
pip install generic-server # not yet published
```

## How to use
In order to start a MockServer, start the server with the desired config:

```bash
generic-server <config-file>
```
The config-file is a simple yaml file that contains the modes and request-answer pairs.


## License
[MIT License](https://choosealicense.com/licenses/mit/)

## Author
**Carsten König**

- [GitLab](https://gitlab.com/ck2go "Carsten König")
- [GitHub](https://github.com/ck2go "Carsten König")
- [LinkedIn](https://www.linkedin.com/in/ck2go/ "Carsten König")
- [Website](https://www.carsten-koenig.de "Carsten König")

