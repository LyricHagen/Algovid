# Algovid

Group theory app with a Node.js backend and Python CLI.

## Setup

Make sure MongoDB is running on localhost:27017.

Start the backend:
```bash
cd backend
npm install
node index.js
```

Run the CLI:
```bash
cd frontend
python enhanced_cli.py
```

## What it does

- Store groups in MongoDB (name, description, multiplication table)
- Validate groups using group theory axioms
- CLI to add/list/validate groups

## API

- `GET /api/groups` - list all groups
- `POST /api/groups` - create a group

## Math utilities

The `math/group_utils.py` file has functions to check if a multiplication table is a valid group:
- `is_valid_group(table)` - checks closure, associativity, identity, inverses
- `find_identity(table)` - finds the identity element
- `find_inverse(table, element)` - finds an element's inverse
- `get_group_elements(table)` - gets all elements from the table 
