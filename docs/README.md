## An example of proper use of dependency injection in fastapi without using third-party DI frameworks

### installation
``` shell
pip install -e .
```

### run web
``` shell
uvicorn app.main.web_api:create_app --factory
```
