# Task Manager
A simple Django-based task manager for demonstrating use of development tools and CI/CD.

## Local setup

```bash
make setup
```

## Daily automation commands

```bash
make run          # start server on 8080
make test         # run Django tests
make check        # run Django system checks
make ci-local     # run local checks matching CI intent
make health       # call /healthz endpoint
```

You can also change the server port:

```bash
make run PORT=8000
```