# Developers

## Manage Python Dependencies

```
cd .kit
pipenv install --system SPLAT
pipenv install --system --dev SPLAT
pipenv lock -r > requirements.txt
pip install requirements.txt
```
